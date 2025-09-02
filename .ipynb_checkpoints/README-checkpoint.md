# 📚 LLM + RAG con LangChain, Chroma y HuggingFace

Este proyecto implementa un **sistema de Recuperación Aumentada por Generación (RAG)** usando **LangChain**, **ChromaDB** y modelos de **HuggingFace**.  
La idea principal es:  
1. **Dividir documentos** en chunks manejables.  
2. **Crear embeddings** con un modelo de sentence-transformers.  
3. **Almacenar y consultar** en una base vectorial (Chroma).  
4. **Usar un modelo LLM** para responder preguntas basado en contexto relevante.  

## 🚀 Instalación

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/tu_usuario/tu_repo.git
   cd tu_repo

2.  conda create -n llm-env python=3.11 -y
    conda activate llm-env

3. pip install -r requirements.txt

4. Diagramas utiles para entender el proyecto

   ![ Embedding + chroma ](1.png)
   ![ Ejemplo de consulta ](2.png)
