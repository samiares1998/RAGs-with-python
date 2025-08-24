{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0be3a5ff-9544-4efd-89b2-a98bffd37d91",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_huggingface import HuggingFaceEmbeddings\n",
    "from langchain.vectorstores import Chroma\n",
    "from langchain.document_loaders import TextLoader\n",
    "#from sentence_transformers import SentenceTransformer\n",
    "\n",
    "from langchain_huggingface import HuggingFaceEmbeddings\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18308172-7ac5-43e1-9741-675535b662ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Cargar dataset\n",
    "loader = TextLoader(\"dataset.jsonl\")\n",
    "documents = loader.load()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "822e6a80-5505-4bc3-8dcf-ad792691e268",
   "metadata": {},
   "outputs": [],
   "source": [
    "#model_name = \"paraphrase-multilingual-MiniLM-L12-v2\"\n",
    "#model = SentenceTransformer(model_name)\n",
    "\n",
    "# 2. Crear embeddings con Hugging Face\n",
    "embedding_model = HuggingFaceEmbeddings(model_name=\"sentence-transformers/all-MiniLM-L6-v2\")\n",
    "vector_db = Chroma.from_documents(documents, model, persist_directory=\"./chroma_db\")\n",
    "vector_db.persist()\n",
    "print(\"✅ Base de conocimiento creada\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e94f11af-85ab-49a2-a3b6-1db60a967211",
   "metadata": {},
   "outputs": [],
   "source": [
    "def query_db(question: str, k: int = 2):\n",
    "    docs = vector_db.similarity_search(question, k=k)\n",
    "    print(f\"\\n🔎 Pregunta: {question}\\n\")\n",
    "    for i, d in enumerate(docs, 1):\n",
    "        print(f\"👉 Respuesta {i}: {d.page_content}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "115c1b41-424c-4b4c-825f-60f0888c035d",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    query_db(\"Circular Basica Juridica de la SFC?\")\n",
    "    query_db(\"¿Para qué se usa Python?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce8a7e86-2ec1-4bb8-882f-887e9df97b6b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (llm-env)",
   "language": "python",
   "name": "llm-env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
