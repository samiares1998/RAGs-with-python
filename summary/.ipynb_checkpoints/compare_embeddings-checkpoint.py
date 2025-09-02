from langchain_huggingface import HuggingFaceEmbeddings
from langchain.evaluation import load_evaluator


def main():
    # Get embedding for a word
    emb_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = emb_model.embed_query("apple")
    print(f"Vector for 'apple': {vector[:5]}...")  # print only first 5 values
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("embedding_distance", embeddings=emb_model)
    result = evaluator.evaluate_strings(
        prediction="apple",
        reference="iphone"
    )
    print(f"Embedding distance (apple vs iphone): {result['score']}")


if __name__ == "__main__":
    main()
