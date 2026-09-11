# 🌿 ClimaVerify — Bot de Discord para la Detección del Greenwashing

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Discord.py](https://img.shields.io/badge/Discord.py-v2.3.0-5865F2?style=for-the-badge&logo=discord)
![Database](https://img.shields.io/badge/Database-SQLite3-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Proyecto:** Proyecto Final Python Pro  
> **Autor:** [Tu Nombre / Usuario de GitHub] =)  

---

## 📋 Tabla de Contenidos
- [📖 Descripción del Proyecto](#-descripción-del-proyecto)
- [🎯 Problema que Resuelve y Público Objetivo](#-problema-que-resuelve-y-público-objetivo)
- [✨ Funciones y Características](#-funciones-y-características)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [🎬 Demostración del Funcionamiento](#-demostración-del-funcionamiento)
- [⚙️ Instalación y Configuración](#️-instalación-y-configuración)
- [💻 Guía de Uso y Comandos](#-guía-de-uso-y-comandos)
- [💬 Comentarios y Contribuciones](#-comentarios-y-contribuciones)
- [💡 Conclusión](#-conclusión)

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

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** `Python 3.10+` (Uso de entorno virtual `venv`)
* **Librería del Bot:** `discord.py`
* **Scraping y Procesamiento:** `BeautifulSoup4` / `requests` / `WordCloud`
* **Persistencia:** `SQLite3` (Base de datos relacional)
* **Estándar de Código:** `PEP8`

---

## 🎬 Demostración del Funcionamiento

### Capturas de Pantalla

| Comando `$analizar` | Comando `$nube` |
| :---: | :---: |
| ![Demo Analizar](docs/screenshots/demo_analizar.png) | ![Demo Nube](docs/screenshots/demo_nube.png) |

---

### 🎥 Vídeo Demostrativo
Puedes ver una demostración completa del funcionamiento en YouTube:  
▶️ [Ver Demostración de ClimaVerify en YouTube](https://youtube.com) *(Reemplazar con enlace real)*

---

## ⚙️ Instalación y Configuración

### Pre-requisitos
* Python 3.10 o superior instalado.
* Cuenta de desarrollador en Discord con un Bot creado.

### Pasos para la instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/ClimaVerify.git](https://github.com/tu-usuario/ClimaVerify.git)
   cd ClimaVerify
