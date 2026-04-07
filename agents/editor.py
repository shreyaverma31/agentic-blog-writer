from .llm import llm

def editor_agent(blog):
    print("✏️ Editing blog...")
    import time
    start = time.time()
    prompt = f"""
    Improve the following blog:
    - grammar
    - readability
    - structure

    Blog:
    {blog}
    """

    response = llm.invoke(prompt)
    print(f"✅ Edited in {time.time() - start:.1f}s")
    return response.content
