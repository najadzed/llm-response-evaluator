📘 BeyondChats AI Response Evaluator

A lightweight but complete evaluation engine built for the BeyondChats AI Evaluation Intern Task.
This project scores chatbot outputs based on:

Relevance → How closely the AI’s answer matches the user’s query

Completeness → How well the answer aligns with available context

Hallucination → Whether the model invents information not found in context

Latency → Total evaluation time

Cost Estimate → Approximate (mock) inference cost

The evaluator uses semantic similarity (Sentence Transformers) to generate real-time scoring.

🚀 Features
✅ Relevance Scoring

Measures semantic similarity between the latest user query and the AI response.

✅ Completeness Scoring

Checks how much of the AI response is grounded in the provided context chunks.

✅ Hallucination Detection

Detects mismatches or fabricated information by measuring similarity against context.

✅ Latency Measurement

Computes total evaluation time in milliseconds.

✅ Plug-and-Play JSON Loader

Accepts:

chat.json

context.json (BeyondChats format)

📁 Project Structure
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

🔧 Installation

Clone the repo:

git clone https://github.com/<your-username>/beyondchats-ai-evaluator
cd beyondchats-ai-evaluator


Install dependencies:

pip install -r requirements.txt

📌 Usage

Run the evaluator with:

python evaluate.py --chat data/chat.json --context data/context.json


Example output:

=== Evaluation Report ===
relevance: 0.25
completeness: 0.67
hallucination: 0.51
latency_ms: 687.456
cost_estimate_usd: 0.00001

🧠 How the Evaluation Works
1️⃣ Extract User Query

Pulls the latest user message from:

"conversation_turns"

2️⃣ Extract AI Response

BeyondChats returns:

final_response: [ "sentence1", "sentence2" ]


Evaluator merges it into one string.

3️⃣ Load Context Chunks

Extracts all "text" fields from vector_data.

Missing texts are safely skipped to avoid errors.

4️⃣ Compute Semantic Scores

Uses all-MiniLM-L6-v2:

Cosine similarity for relevance

Cosine similarity vs context for completeness

1 - similarity for hallucination

5️⃣ Output JSON-like metrics

Human-readable + easily parseable.

📊 Why This Approach?

Fast execution (<1 second)

Cheap (local inference)

No external API dependency

Deterministic results

Clean code for easy extension

🧪 Example: Detecting a Hallucination

If the model claims:

"We offer subsidized rooms inside the clinic."

…but this does not exist in the context vectors, the hallucination score rises (0.5+).
This is exactly what your sample evaluation output showed.

👨‍💻 Intern Task Requirements — Covered
Requirement	Status
Load chat + context JSON	✅
Extract user query	✅
Extract AI response	✅
Parse vector context	✅
Compute relevance	✅
Compute completeness	✅
Detect hallucinations	✅
Measure latency	✅
Produce final clean score object	✅
Easy to run	✅
Clean code	✅

📬 Author

Built by --Najad
As part of the BeyondChats Intern Task.

⭐ If you found this helpful, star the repository!
