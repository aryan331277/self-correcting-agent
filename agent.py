# agent.py

from utils import call_model
from prompts import THINKER_PROMPT, VERIFIER_PROMPT, REFINER_PROMPT
from config import MODEL_THINKER, MODEL_VERIFIER, MAX_ITERATIONS

def thinker(question):
    prompt = THINKER_PROMPT.format(question=question)
    return call_model(MODEL_THINKER, prompt)

def verifier(question, reasoning):
    prompt = VERIFIER_PROMPT.format(question=question, reasoning=reasoning)
    return call_model(MODEL_VERIFIER, prompt)

def refine_reasoning(question, reasoning, feedback):
    prompt = REFINER_PROMPT.format(
        question=question,
        reasoning=reasoning,
        feedback=feedback
    )
    return call_model(MODEL_THINKER, prompt)

def self_correcting_agent(question):
    current_reasoning = thinker(question)
    steps = [{"step": "Initial Reasoning", "content": current_reasoning}]

    for i in range(MAX_ITERATIONS):
        feedback = verifier(question, current_reasoning)
        steps.append({"step": f"Iteration {i+1} Feedback", "content": feedback})

        current_reasoning = refine_reasoning(question, current_reasoning, feedback)
        steps.append({"step": f"Iteration {i+1} Updated Reasoning", "content": current_reasoning})

    return current_reasoning, steps
