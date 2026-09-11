# 🌿 ClimaVerify — Bot de Discord para la Detección del Greenwashing

> **Proyecto:** Proyecto Final Python Pro  
> **Autor:** Guillermo Fraile García

---

## 📖 Descripción del Proyecto

**ClimaVerify** es un bot de Discord inteligente concebido para combatir la desinformación ambiental y el *greenwashing* (publicidad ecológica engañosa) en medios digitales. 

Mediante el procesamiento de texto y técnicas de *web scraping*, **ClimaVerify** analiza noticias, comunicados o declaraciones corporativas para evaluar su grado de credibilidad, extrayendo métricas de frecuencia de palabras y generando representaciones visuales para la comunidad.

---

## 🎯 Problema que Resuelve y Público Objetivo

### 🛑 El Problema
En la actualidad, proliferan las afirmaciones de sostenibilidad falsas o sesgadas en internet. La falta de herramientas accesibles dificulta que las personas verifiquen si una iniciativa ambiental cuenta con respaldo real o si es meramente un ardid publicitario.

### 👥 ¿A quién beneficia?
* **Comunidades ambientales:** Servidores de Discord enfocados en la ecología y la sostenibilidad.
* **Usuarios e Investigadores:** Personas que buscan contrastar titulares e información climática rápidamente.
* **Debates informados:** Canales de debate que requieren verificar fuentes antes de compartir noticias.

---

## ✨ Funciones y Características

| Función | Descripción |
| :--- | :--- |
| 🔍 **Análisis de Credibilidad** | Evalúa textos o enlaces de noticias mediante *scraping* y algoritmos de frecuencia de palabras clave. |
| ☁️ **Generación de Nubes de Palabras** | Sintetiza visualmente las temáticas climáticas más consultadas de la semana. |
| 🗄️ **Historial en Base de Datos** | Almacena el registro de consultas en SQLite3 para el seguimiento de tendencias. |
| 🧱 **Arquitectura Modular (OOP)** | Código estructurado en clases y métodos cumpliendo las directrices **PEP8**. |

---

💻 Guía de Uso y ComandosComandoParámetrosDescripción$analizar<URL o Texto>Extrae el texto, analiza patrones y devuelve un diagnóstico de credibilidad.$nubeNingunoGenera y envía una imagen con la nube de palabras de las consultas recientes.$historialNingunoMuestra las últimas noticias o textos guardados en la base de datos.

---

💬 Comentarios y Contribuciones
¡Las sugerencias y contribuciones son siempre bienvenidas!

🐛 ¿Especialmente un error? Abre un reporte en la pestaña de Issues.

💡 ¿Quieres proponer una mejora? Revisa las discusiones o crea un nuevo Issue.

🔀 ¿Deseas aportar código?

Haz un Fork del proyecto.

Crea tu rama de características (git checkout -b feature/NuevaCaracteristica).

Haz un Commit de tus cambios (git commit -m 'Añadir NuevaCaracteristica').

Realiza un Push a la rama (git push origin feature/NuevaCaracteristica).

Abre un Pull Request.

---

💡 Conclusión
ClimaVerify demuestra el potencial de combinar herramientas de código abierto como Python, discord.py y SQLite para abordar un problema social y ecológico crítico: la desinformación climática. Al proporcionar un mecanismo transparente y automatizado para examinar el discurso ecológico, el proyecto empodera a los usuarios para detectar el greenwashing y promover una conciencia ambiental basada en datos reales.
