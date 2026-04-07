from .llm import llm

def rewrite_agent(topic, blog):

    prompt = f"""
You are an expert editor.

TOPIC:
{topic}

BLOG:
{blog}

TASK:
- REMOVE any unrelated sections completely
- DELETE content about military, politics, alliances, etc.
- Keep ONLY education-related content
- Fix grammar and structure

IMPORTANT:
Do NOT rewrite everything — just CLEAN it.

OUTPUT:
Return a clean blog.
"""

    response = llm.invoke(prompt)

    return response.content