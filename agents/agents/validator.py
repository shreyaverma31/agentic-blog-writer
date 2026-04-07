from .llm import llm

def validator_agent(topic, blog):

    prompt = f"""
You are a STRICT content validator.

TOPIC:
{topic}

BLOG:
{blog}

TASK:
Check if the blog contains ANY irrelevant content.

STRICT RULES:
- Blog must ONLY be about the topic
- If ANY unrelated topic appears (military, war, alliances, policies, etc.) → INVALID
- Even ONE unrelated section = INVALID

Examples of INVALID content:
- Military agreements
- Political treaties
- Anything not related to education

OUTPUT:
Return ONLY one word:
VALID or INVALID
"""

    response = llm.invoke(prompt)

    return response.content.strip().upper()