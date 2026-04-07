from .llm import llm

def research_agent(outline):

    prompt = f"""
    Research the following outline and provide useful points:

    {outline}
    """

    response = llm.invoke(prompt)

    return response.content