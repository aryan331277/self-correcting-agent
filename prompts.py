# prompts.py

THINKER_PROMPT = """
You are a logical thinker agent.
Answer the following question step by step.

Question: {question}

Reasoning:
"""

VERIFIER_PROMPT = """
You are a verifier agent.
Review the following reasoning for correctness.

Question: {question}
Reasoning: {reasoning}

Provide feedback and corrections if any:
"""

REFINER_PROMPT = """
Original Question: {question}
Current Reasoning: {reasoning}
Feedback: {feedback}

Refine your reasoning based on the feedback:
"""
