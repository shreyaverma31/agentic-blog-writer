from .llm import llm

def rewrite_agent(topic, blog):

    prompt = f"""
You are an expert editor.

TOPIC:
{topic}

BLOG:
{blog}

TASK:
- Remove ALL irrelevant content
- Keep only topic-related content
- Improve clarity and structure

Return a clean, corrected blog.
"""

    response = llm.invoke(prompt)

    return response.content