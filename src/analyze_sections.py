# src/analyze_sections.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_relevant_sections(text_blocks, persona_description, job_description):
    combined_context = persona_description + " " + job_description
    docs = [combined_context] + [block["text"] for block in text_blocks]

    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform(docs)

    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Attach similarity to each block
    for idx, sim in enumerate(similarities):
        text_blocks[idx]["similarity"] = sim

    # Sort by similarity score
    ranked_blocks = sorted(text_blocks, key=lambda x: x["similarity"], reverse=True)
    return ranked_blocks
