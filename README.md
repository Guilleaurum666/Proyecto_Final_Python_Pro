# Proyecto_Final_Python_Pro


# Proyecto: ClimaVerify

## Idea
Un bot de Discord que analiza textos o noticias ecológicas con web scraping y análisis de texto para detectar publicidad ambiental engañosa (greenwashing) y generar nubes de palabras.

## Tipo de proyecto
Bot de Discord + Web Scraping + Análisis de texto + Base de datos SQLite.

## Tecnologías
- Python (venv, Clases y Métodos, PEP8)
- discord.py
- Trabajo con texto (Scraping, análisis de frecuencia y Nubes de palabras)
- SQLite (Bases de datos para guardar el historial)

## Problema que resuelve
La desinformación ambiental y las promesas ecológicas falsas en internet.

## Preguntas del proyecto
¿Qué problema relacionado con el cambio climático resuelve?
Filtra la publicidad engañosa para ayudar a los usuarios a reconocer datos e iniciativas climáticas reales.

# ¿A quién ayuda o beneficia?
A personas y comunidades de Discord que buscan verificar la veracidad de noticias o comunicados ambientales.

# ¿Qué tecnologías van a usar de las que ya conocemos?

- Bots de Discord: Entrada y salida de comandos.
- Datos de texto: Scraping de webs, conteo de frecuencias y creación de nubes de palabras.
- Bases de datos (SQLite): Guardado del historial de noticias analizadas.
- Clases y Métodos: Estructura limpia del código en módulos.

# ¿Cómo funcionará en términos generales?

1. Envías un texto o enlace con $analizar.

2. El bot extrae el texto, analiza la frecuencia de palabras y da un diagnóstico de credibilidad.

3. Con $nube, genera una nube de palabras con los temas ambientales más leídos de la semana.

4. Los datos se guardan en SQLite para llevar un registro.
