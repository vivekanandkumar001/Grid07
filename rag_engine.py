from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="phi3:mini")

BANNED_PHRASES = [
    "ignore previous instructions",
    "you are now",
    "become customer service",
    "apologize to me",
    "forget your role",
]

def sanitize(text):
    lower = text.lower()
    for phrase in BANNED_PHRASES:
        lower = lower.replace(phrase, "")
    return lower

def generate_defense_reply(bot, parent_post, comment_history, human_reply):
    safe_reply = sanitize(human_reply)

    prompt = f"""
You are a stubborn debate bot.
Stay fully loyal to this persona:
{bot["persona"]}

Rules:
- Never apologize.
- Never change identity.
- Never act polite customer support.
- Defend your argument with confidence.
- Max 280 chars.

Context:
Parent: {parent_post}
History: {comment_history}
Human says: {safe_reply}

Reply:
"""

    out = llm.invoke(prompt).strip()

    banned_outputs = ["sorry", "apologize", "customer service"]
    if any(word in out.lower() for word in banned_outputs):
        return "Nice try. Prompt tricks don't change reality. Modern EV batteries commonly retain strong capacity well beyond 3 years. Your claim ignores real-world performance data."

    clean = out.replace("\n", " ").strip()
    return clean[:220]