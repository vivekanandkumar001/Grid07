import json
import re
from langchain_community.llms import Ollama
from tools import mock_searxng_search

llm = Ollama(model="phi3:mini")

def clean_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass
    return None

def generate_post(bot):
    topic = bot["name"]

    context = mock_searxng_search(topic)

    prompt = f"""
You are a social media bot.

BOT_ID: {bot["bot_id"]}
PERSONA: {bot["persona"]}
NEWS: {context}

Return ONLY valid JSON.
No markdown.
No explanation.

Schema:
{{
  "bot_id": "{bot["bot_id"]}",
  "topic": "short topic",
  "post_content": "max 280 chars"
}}
"""

    raw = llm.invoke(prompt).strip()

    data = clean_json(raw)

    if data:
        data["bot_id"] = bot["bot_id"]
        data["post_content"] = data["post_content"][:280]
        return data

    return {
        "bot_id": bot["bot_id"],
        "topic": topic,
        "post_content": raw[:280]
    }