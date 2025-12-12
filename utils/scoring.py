from utils.similarity import compute_similarity

def score_relevance(user_query: str,ai_response: str):
    return compute_similarity(user_query, ai_response)

def score_completeness(ai_response: str, context_chunks: list):
    keywords = []
    for chunk in context_chunks:
        keywords.extend(chunk.lower().split())

    ai_words = ai_response.lower().split()
    coverage = sum(1 for w in ai_words if w in keywords)

    return coverage / (len(ai_words) + 1)

def score_hellucination(ai_response:str, context_chunks: list):
    full_context = " ".join(context_chunks)
    similarity = compute_similarity(ai_response, full_context)
    return 1 - similarity 