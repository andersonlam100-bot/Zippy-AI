import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
import chromadb.utils.embedding_functions as ef

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GITHUB_TOKEN"),
)

db = chromadb.PersistentClient(path="../chroma_db")
memories = db.get_or_create_collection("my_facts")

memories.upsert(
    documents=[
        "Test memory",
        "Cool Market",
        "Class"
    ],
    ids=["fact4", "fact5", "fact6"],
)

print("\nstored:", memories.count(), "facts")

question = input("Ask a question: ")

results = memories.query(query_texts=[question], n_results=4)

memory_text = "\n".join(results["documents"][0])

r = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": f"Using these notes:{memory_text}, answer to the question: {question}",
        },
        {
            "role": "user",
            "content": question
        }
    ],
)

print(r.choices[0].message.content)