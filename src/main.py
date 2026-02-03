"""
Analytics Copilot - Day 1 Starter

This is the entry point for the project.
Later, this file will connect:
- user question input
- prompt building
- LLM call
- SQL generation
- query execution
- insight summary
"""

from datetime import datetime


def clean_question(question: str) -> str:
    """Basic input cleaning."""
    return question.strip()


def main() -> None:
    print("🚀 Analytics Copilot - Day 1 Starter")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    question = "   Top 10 customers by ACH volume last month   "
    cleaned = clean_question(question)

    print("\nOriginal question:", repr(question))
    print("Cleaned question:", repr(cleaned))

    # Placeholder output (simulating AI response)
    output = {
        "question": cleaned,
        "sql": "SELECT customer_id, SUM(amount) AS total_amount FROM transactions GROUP BY customer_id ORDER BY total_amount DESC LIMIT 10;",
        "summary": "Top 10 customers by transaction volume.",
        "confidence": 0.75,
    }

    print("\nSimulated AI Output:")
    for k, v in output.items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
