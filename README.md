# Tipología y ciclo de vida del dato. Web Scrapping

## Descripción

Este repositorio de código se ha generado para llevar a cabo la **Práctica 1** de la asignatura *Tipología y ciclo de vida del dato* del máster universitario en Ciencia de Datos (Data Science) de la Universitat Oberta de Catalunya (UOC). El código sirve de ejemplo de cómo realizar web scrapping de una página web pública y crea un dataset con la información de registro de terremotos publicados en la página [Earthquake Hazard Program](https://earthquake.usgs.gov/)

## Miembros participantes

La práctica ha sido realizada individualmente por **Miguel Tablado León**

## Contenido

El repositorio se encuentran los siguientes ficheros:

```
.
├── csv
│   └── dataset.csv                   # Dataset generado
├── environment.yml                   # Fichero de entorno para Anaconda
├── notebook
│   ├── earthquakes_notebook.ipynb    # Notebook para presentar las respuestas solicitadas
│   └── terremoto-lorca.png           # Imagen de terremoto en Lorca para representación
├── README.md                         # Este fichero
└── src
    ├── main.py                       # Fichero main que tiene el proceso iterativo y guardado de csv
    ├── scrap.py                      # Contiene los procesos de parseado con BeautifulSoup
    ├── technologies.py               # Comandos para comprobar el sitio donde hacer web scrapping
    └── web_download.py               # Utilidades de descarga de HTML con Selenium

```