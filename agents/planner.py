from .llm import llm

def planner_agent(topic):
    print("🤔 Planning blog outline...")
    import time
    start = time.time()
    prompt = f"""
    Create a structured blog outline for the topic: {topic}

    Include:
    - Title
    - 5 sections
    """
    response = llm.invoke(prompt)
    print(f"✅ Outline planned in {time.time() - start:.1f}s")
    return response.content
