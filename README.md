# chatbot-pdf

Este chatbot consiste del modelo LLM de OpenAI, que utiliza una base vectorial de Milvus para procesar documentos 
PDF. Además, utiliza un sistema CSBM para mantener memoria en la conversación.

## Configuración

1. Crear archivo `.env` utilizando el archivo `.env.example` y adjuntar la OpenAI API Key
2. En la carpeta `assets` modificar el archivo `prompt.txt` para el uso que se quiera utilizar.
3. Copiar tus documentos PDF en la carpeta `docs`

## Ejecución

1. Instalar dependencias

```bash
pip install -r requirements.txt
```

2. Correr docker con BDD Milvus

```bash
docker compose up -d
```

3. Correr main.py

```bash
streamlit run main.py
```