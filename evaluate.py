import time
import argparse
from utils.loader import load_json
from utils.scoring import (
    score_relevance,
    score_completeness,
    score_hellucination
)

def evaluate(chat_json_path, context_json_path):
    chat = load_json(chat_json_path)
    ctx = load_json(context_json_path)

    user_query = chat["conversation_turns"][-1]["message"]

    ai_response_list = ctx["data"]["sources"]["final_response"]
    ai_response = " ".join(ai_response_list)

    context_chunks = [
    entry.get("text", "")
    for entry in ctx["data"]["vector_data"]
    if entry.get("text")
]

    start = time.time()

    relevance = score_relevance(user_query, ai_response)
    completeness = score_completeness(ai_response, context_chunks)
    hallucination = score_hellucination(ai_response, context_chunks)

    end = time.time()

    return {
        "relevance": relevance,
        "completeness": completeness,
        "hallucination": hallucination,
        "latency_ms": round((end - start) * 1000, 3),
        "cost_estimate_usd": 0.00001
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chat", type=str, required=True)
    parser.add_argument("--context", type=str, required=True)

    args = parser.parse_args()

    report = evaluate(args.chat, args.context)

    print("\n=== Evaluation Report ===")
    for k, v in report.items():
        print(f"{k}: {v}")
