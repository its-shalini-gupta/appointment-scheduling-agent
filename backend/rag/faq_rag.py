import json
from pathlib import Path
from backend.rag.embeddings import get_embedding
from backend.rag.vector_store import add_faq, search_faq

FAQ_FILE = Path(__file__).resolve().parents[2] / "data" / "clinic_info.json"

loaded = False

def load_faqs():
    global loaded
    if loaded:
        return

    data = json.load(open(FAQ_FILE))
    for item in data["faqs"]:
        emb = get_embedding(item["q"])
        add_faq(item["q"], item["a"], emb)

    loaded = True

def answer_faq(message: str):
    load_faqs()

    q_emb = get_embedding(message)
    results = search_faq(q_emb, k=1)

    if not results["metadatas"]:
        return ""

    return results["metadatas"][0][0]["answer"]
