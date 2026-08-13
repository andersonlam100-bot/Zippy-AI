import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
db = chromadb.PersistentClient(path="./chroma_db")
memories = db.get_or_create_collection("memories")
question = "What food do I like the most?"
# RETRIEVE
hits = memories.query(query_texts=[question], n_results=2)
notes = "\n".join(hits["documents"][0])
# AUGMENT
prompt = f"""Answer using ONLY these notes.
{notes}
Question: {question}"""
print("--- the prompt we're about to send ---")
print(prompt)
