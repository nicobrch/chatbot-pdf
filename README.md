# Chatbot PDF

<p align="center">
  <img src="https://www.svgrepo.com/show/306500/openai.svg" alt="OpenAI Logo" style="height: 100px;"/> <img src="https://artwork.lfaidata.foundation/projects/milvus/icon/color/milvus-icon-color.png" alt="Milvus Logo" style="height: 100px;"/>
</p>

## Descripción

Este chatbot consiste del modelo LLM y embeddings de OpenAI, que utiliza una base vectorial de Milvus para almacenar documentos PDF. Además, utiliza un sistema CSBM para mantener memoria en la conversación. Para conectar todos los componentes, utiliza el framework de LangChain, y para crear una interfaz gráfica utiliza Streamlit.

## Configuración

1. Crear archivo `.env` utilizando el archivo `.env.example` y adjuntar la OpenAI API Key
2. En la carpeta `assets` modificar el archivo `prompt.txt` para el uso que se quiera utilizar.
3. Copiar tus documentos PDF en la carpeta `docs`

## Ejecución

Opcionalmente, puedes crear un entorno virtual:
* Crear entorno con `python -m venv venv`
* Activar entorno con `source venv/bin/activate` en Linux o `.\venv\Scripts\Activate` en Windows

1. Instalar dependencias (se puede demorar)

```bash
pip install -r requirements.txt
```

2. Ejecutar docker que contiene la base de datos de Milvus

```bash
docker compose up -d
```

3. Ejecutar aplicación

```bash
streamlit run main.py
```
