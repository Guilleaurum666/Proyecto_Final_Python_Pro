import re
import sqlite3
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud


class AnalizadorClima:
    def __init__(self, db_path='clima_verify.db'):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS analisis 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT, sospecha INTEGER)''')

        self.vagas = ['verde', 'eco', 'sostenible', 'consciente', 'planeta', 'natural', 'bio', 'salvar', 'limpio', 'comprometidos', 'potencial', 'estimado', 'teorica', 'preliminar', 'compensacion', 'creditos', 'neutralizacion', 'transicion', 'proyectando']
        self.vanidad = ['region', 'región', 'regional', 'norte', 'sur', 'sede', 'administrativo', 'personal', 'vasos', 'poliestireno', 'patrocinio', 'catedra', 'cátedra', 'virtual', 'capacitacion', 'capacitación', 'módulo', 'litros', 'polímeros']
        self.concretas = ['certificacion', 'certificación', 'iso', 'emisiones', 'porcentaje', 'auditoria', 'auditoría', 'informe', 'toneladas', 'kwh', 'medicion', 'medición', 'reduccion', 'reducción', 'datos', 'alcance 1', 'alcance 2', 'alcance 3', 'co2', 'global']

    def _extraer_texto_web(self, url):
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                return ' '.join([p.get_text().strip() for p in soup.find_all(['p', 'li'])])
        except Exception:
            pass
        return "No se pudo extraer el contenido del enlace."

    def _analizar_contexto_numeros(self, texto):
        texto_lower = texto.lower()
        numeros = list(re.finditer(r'\b(?!19\d\d|20\d\d)\d+[\d\.,]*%?\b', texto_lower))
        reales, vanidad = 0, 0

        kw_impacto = ['toneladas', 'co2', 'emisiones', 'kwh', 'iso', 'alcance', 'global', 'reduccion', 'reducción']
        kw_vanidad = ['región', 'region', 'norte', 'sur', 'vasos', 'litros', 'personal', 'capacitación', 'cátedra']

        for m in numeros:
            ctx = texto_lower[max(0, m.start() - 50):min(len(texto_lower), m.end() + 50)]
            if any(k in ctx for k in kw_vanidad):
                vanidad += 1
            elif any(k in ctx for k in kw_impacto):
                reales += 1
            else:
                reales += 0.5

        return int(reales), vanidad

    def procesar_entrada(self, contenido):
        texto = self._extraer_texto_web(contenido) if contenido.startswith(('http://', 'https://')) else contenido
        t_limpio = texto.lower()

        c_vagas = sum(len(re.findall(r'\b' + p + r'\b', t_limpio)) for p in self.vagas)
        c_vanidad = sum(len(re.findall(r'\b' + p + r'\b', t_limpio)) for p in self.vanidad)
        c_concretas = sum(len(re.findall(r'\b' + p + r'\b', t_limpio)) for p in self.concretas)

        num_reales, num_vanidad = self._analizar_contexto_numeros(texto)

        total_sospechosas = c_vagas + c_vanidad + num_vanidad
        total_concretas = c_concretas + num_reales
        total = total_sospechosas + total_concretas

        if total == 0:
            pct, cred, riesgo = 30, "Media 🟡", "Moderado ⚡"
            detalle = "No se detectaron suficientes datos clave."
        else:
            pct = int((total_sospechosas / total) * 100)
            if pct > 50:
                cred, riesgo = "Baja 🔴", "Alto ⚠️"
                detalle = f"Predomina la jerga comercial o de alcance limitado ({total_sospechosas}) sobre datos reales ({total_concretas})."
            elif pct > 25:
                cred, riesgo = "Media 🟡", "Moderado ⚡"
                detalle = f"Texto equilibrado entre adjetivos/alcance acotado ({total_sospechosas}) y datos reales ({total_concretas})."
            else:
                cred, riesgo = "Alta 🟢", "Bajo ✅"
                detalle = f"Texto respaldado por {total_concretas} datos o cifras de impacto real."

        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO analisis (texto, sospecha) VALUES (?, ?)", (texto, pct))

        return {
            'credibilidad': cred,
            'riesgo': riesgo,
            'porcentaje': pct,
            'detalle': detalle,
            'vagas': total_sospechosas,
            'concretas': total_concretas
        }

    def generar_nube_palabras(self):
        with sqlite3.connect(self.db_path) as conn:
            filas = conn.execute('SELECT texto FROM analisis').fetchall()

        texto_completo = ' '.join([f[0] for f in filas]) if filas else ''
        if len(texto_completo.strip()) < 10:
            return None

        ruta = 'nube.png'
        WordCloud(width=800, height=400, background_color='white', max_words=50).generate(texto_completo).to_file(ruta)
        return ruta