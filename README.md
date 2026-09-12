# 🌿 ClimaVerify — Bot de Discord para la Detección del Greenwashing

> **Proyecto:** Proyecto Final Python Pro  
> **Autor:** Guillermo Fraile García

---

## 📖 Descripción del Proyecto

**ClimaVerify** es un bot de Discord inteligente concebido para combatir la desinformación ambiental y el *greenwashing* (publicidad ecológica engañosa) en medios digitales. 

Mediante el procesamiento de texto y técnicas de *web scraping* (técnica automatizada para extraer datos de páginas web y transformarlos en formatos estructurados) **ClimaVerify** analiza noticias, comunicados o declaraciones corporativas para evaluar su grado de credibilidad, extrayendo métricas de frecuencia de palabras y generando representaciones visuales para el usuario.

---

## 🎯 Problema que Resuelve y Público Objetivo

### 🛑 El Problema
En la actualidad, proliferan las afirmaciones de sostenibilidad falsas o sesgadas en internet. La falta de herramientas accesibles dificulta que las personas verifiquen si una iniciativa ambiental cuenta con respaldo real o si es meramente un truco publicitario.

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
| 🧱 **Arquitectura** | Código estructurado en clases y métodos cumpliendo las directrices **PEP8**. |

---

💻 Guía de Uso y de Comandos
$analizar: Extrae el texto, analiza patrones y devuelve un diagnóstico de credibilidad.
$nube: Genera y envía una imagen con la nube de palabras de las consultas recientes.

💡 Conclusión
ClimaVerify demuestra el potencial de combinar herramientas de código abierto como Python, discord.py y SQLite para abordar un problema social y ecológico crítico: la desinformación climática. Al proporcionar un mecanismo transparente y automatizado para examinar el discurso ecológico, el proyecto empodera a los usuarios para detectar el greenwashing y promover una conciencia ambiental basada en datos reales.
