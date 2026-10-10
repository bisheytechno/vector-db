# Vector DB Practice

Learning vector databases using ChromaDB — foundation for RAG in AI engineering.

---

## What This Covers

- Basic ChromaDB — store and search documents
- Persistent storage — data survives restarts
- Metadata — extra info with documents
- Full pipeline — embed, store, search

---

## Tech Stack

- Python 3.x
- ChromaDB
- sentence-transformers
- VS Code

---

## Project Structure

```
vector-db-practice/
│
├── myvenv/
├── chroma_db/              → Auto-generated (persistent)
├── chroma_db_pipeline/     → Auto-generated (pipeline)
├── 01_basic.py             → Basic ChromaDB
├── 02_persistent.py        → Persistent storage
├── 03_full_pipeline.py     → Full pipeline
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

**1. Clone:**
```bash
git clone https://github.com/bisheytechno/vector-db.git
cd vector-db
```

**2. Virtual Environment:**
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install:**
```bash
pip install -r requirements.txt
```

**4. Run:**
```bash
python 01_basic.py
python 02_persistent.py
python 03_full_pipeline.py
```

---

## Key Concepts

| Concept | What it does |
|---------|-------------|
| chromadb.Client() | In-memory — temporary |
| PersistentClient() | Disk — data saved! |
| create_collection() | New collection |
| get_or_create_collection() | Smart — get or create |
| collection.add() | Store documents |
| collection.query() | Search documents |
| metadatas | Extra info per document |

---

## ChromaDB vs Normal DB

```
Normal DB  → Exact word match
ChromaDB   → Meaning based search

"AI learning" query:
Normal DB  → Finds "AI learning" only
ChromaDB   → Finds "machine learning",
              "deep learning" too!
```

---

## Why Vector DB Matters

```
Vector DB = Foundation of RAG

Documents → Embed → Store in ChromaDB
Query     → Embed → Search ChromaDB
Results   → Send to LLM → Answer! 
```

---

## Requirements

```
chromadb
sentence-transformers
```

---

## Author

**Bishal KC** — Aspiring AI Engineer

---

## License

MIT License