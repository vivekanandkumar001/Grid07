from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from personas import PERSONAS

texts = [p["persona"] for p in PERSONAS]
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

KEYWORDS = {
    "A": ["ai", "crypto", "elon", "space", "openai", "technology"],
    "B": ["privacy", "capitalism", "monopoly", "billionaire", "nature", "society"],
    "C": ["market", "rates", "trading", "roi", "finance", "money", "stock"],
}

def route_post_to_bots(post_content, threshold=0.02):
    post = post_content.lower()
    q = vectorizer.transform([post])
    sims = cosine_similarity(q, X)[0]

    results = []
    for i, bot in enumerate(PERSONAS):
        score = float(sims[i])

        for kw in KEYWORDS[bot["bot_id"]]:
            if kw in post:
                score += 0.25

        if score >= threshold:
            results.append({
                "bot_id": bot["bot_id"],
                "score": round(score, 3)
            })

    return results