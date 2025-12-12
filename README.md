BeyondChats AI Response Evaluator

This project implements an AI response evaluation engine for the BeyondChats Internship Task.
It analyzes chatbot responses using semantic similarity to compute the following metrics:

Relevance

Completeness

Hallucination

Latency

Cost Estimate

The evaluator loads a chat transcript and backend context vectors and scores the latest AI response.

Features

Extracts latest user query from conversation_turns

Extracts final_response from BeyondChats formatted context

Computes semantic similarity scores

Detects hallucinations by comparing response against context

Measures evaluation latency

Works fully offline using sentence-transformers

Project Structure
beyondchats-ai-evaluator/
│
├── evaluate.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── chat.json
│   ├── context.json
│
└── utils/
    ├── loader.py
    ├── similarity.py
    └── scoring.py

Installation

git clone https://github.com/<your-username>/beyondchats-ai-evaluator
cd beyondchats-ai-evaluator

Install dependencies:

pip install -r requirements.txt

Usage

Run evaluation:
python evaluate.py --chat data/chat.json --context data/context.json

Example output:

=== Evaluation Report ===
relevance: 0.25
completeness: 0.67
hallucination: 0.51
latency_ms: 687.456
cost_estimate_usd: 0.00001


How Evaluation Works

Extract the most recent user message from chat.json.

Merge the AI final_response list from context.json.

Gather all context chunk texts from vector_data.

Compute:

Relevance: similarity(user_query, ai_response)

Completeness: similarity(ai_response, context)

Hallucination: 1 - similarity(ai_response, context)

Measure latency using timestamps.

The scoring model used is:

all-MiniLM-L6-v2

Requirements
sentence-transformers
torch
numpy

Notes

Missing text fields in context vectors are skipped safely.

Cost estimate is a placeholder value.

The evaluator is modular and extendable.

Author

Najad
BeyondChats Evaluation Intern Task Submission
