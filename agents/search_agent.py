from tavily import TavilyClient

# Replace with your Tavily API key
client = TavilyClient(api_key="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")

def web_search_agent(topic):
    print("🔍 Web searching...")
    import time
    start = time.time()
    result = client.search(
        query=topic,
        max_results=5
    )

    content = ""

    for r in result["results"]:
        content += r["content"] + "\n"

    print(f"✅ Search complete in {time.time() - start:.1f}s")
    return content
