from langgraph.graph import StateGraph
from typing import TypedDict, Any

from agents.planner import planner_agent
from agents.search_agent import web_search_agent
from agents.writer import writer_agent
from agents.editor import editor_agent
from agents.validator import validator_agent
from agents.rewrite import rewrite_agent

from rag.vector_store import create_vector_store
from rag.retriever import retrieve_context


# -------------------
# State
# -------------------
class BlogState(TypedDict):
    topic: str
    outline: str
    search_data: str
    db: Any
    context: str
    blog: str
    final_blog: str
    is_valid: str


# -------------------
# Planner
# -------------------
def planner(state: BlogState):
    print("🤔 Starting planner...")
    outline = planner_agent(state["topic"])
    print("✅ Planner complete")
    return {"outline": outline}


# -------------------
# Search
# -------------------
def search(state: BlogState):
    print("🔍 Starting search...")
    search_data = web_search_agent(state["topic"])
    print("✅ Search complete")
    return {"search_data": search_data}


# -------------------
# Build RAG
# -------------------
def build_rag(state: BlogState):
    print("📦 Building RAG vector store...")
    db = create_vector_store(state["search_data"])
    print("✅ RAG built")
    return {"db": db}


# -------------------
# Retrieve
# -------------------
def retrieve(state: BlogState):
    print("📖 Retrieving context...")
    context = retrieve_context(state["db"], state["topic"])
    print("✅ Context retrieved")
    return {"context": context}


# -------------------
# Filter Context
# -------------------
def filter_context(state: BlogState):
    print("🧹 Filtering context...")

    topic = state["topic"].lower()
    context = state["context"]

    filtered_lines = []

    for line in context.split("\n"):
        line_lower = line.lower()

        # 🚫 Remove unwanted domains
        if any(word in line_lower for word in [
            "military", "alliance", "war", "defense", "accord"
        ]):
            continue

        # ✅ Keep relevant lines
        if (
            "education" in line_lower or
            "learning" in line_lower or
            "student" in line_lower or
            "teaching" in line_lower or
            topic in line_lower
        ):
            filtered_lines.append(line)

    if not filtered_lines:
        filtered_lines = context.split("\n")[:5]

    filtered_context = "\n".join(filtered_lines)

    print("✅ Context filtered")

    return {"context": filtered_context}


# -------------------
# Writer
# -------------------
def writer(state: BlogState):
    print("✍️ Starting writer...")
    blog = writer_agent(state["outline"], state["context"])
    print("✅ Writer complete")
    return {"blog": blog}


# -------------------
# Validator
# -------------------
def validator(state: BlogState):
    print("🔍 Validating blog...")

    result = validator_agent(state["topic"], state["blog"]).strip().upper()

    print(f"Validator result: {result}")

    return {"is_valid": result}


# -------------------
# Rewrite
# -------------------
def rewrite(state: BlogState):
    print("♻️ Rewriting blog...")
    new_blog = rewrite_agent(state["topic"], state["blog"])
    return {"blog": new_blog}


# -------------------
# Editor
# -------------------
def editor(state: BlogState):
    print("✏️ Starting editor...")
    final_blog = editor_agent(state["blog"])
    print("✅ Final blog ready!")
    return {"final_blog": final_blog}


# -------------------
# Final Cleaner (LAST DEFENSE)
# -------------------
def final_cleaner(state: BlogState):
    print("🧼 Final cleaning...")

    blog = state["final_blog"]

    # 🔥 HARD REMOVE entire Blue Sky section
    if "Blue Sky Accord" in blog:
        print("⚠️ Removing unwanted section...")

        start = blog.find("### International Alliances")
        if start != -1:
            blog = blog[:start]

    # 🔥 Extra safety
    bad_keywords = ["military", "alliance", "war", "defense", "coalition"]

    cleaned_lines = []
    for line in blog.split("\n"):
        if not any(word in line.lower() for word in bad_keywords):
            cleaned_lines.append(line)

    cleaned_blog = "\n".join(cleaned_lines)

    print("✅ Final blog cleaned")

    return {"final_blog": cleaned_blog}


# -------------------
# Routing Logic
# -------------------
def route_validation(state: BlogState):
    if state["is_valid"] == "VALID":
        return "editor"
    else:
        return "rewrite"


# -------------------
# Build Graph
# -------------------
def build_graph():

    builder = StateGraph(BlogState)

    # Nodes
    builder.add_node("planner", planner)
    builder.add_node("search", search)
    builder.add_node("build_rag", build_rag)
    builder.add_node("retrieve", retrieve)
    builder.add_node("filter", filter_context)
    builder.add_node("writer", writer)
    builder.add_node("validator", validator)
    builder.add_node("rewrite", rewrite)
    builder.add_node("editor", editor)
    builder.add_node("cleaner", final_cleaner)

    # Entry
    builder.set_entry_point("planner")

    # Flow
    builder.add_edge("planner", "search")
    builder.add_edge("search", "build_rag")
    builder.add_edge("build_rag", "retrieve")
    builder.add_edge("retrieve", "filter")
    builder.add_edge("filter", "writer")

    builder.add_edge("writer", "validator")

    builder.add_conditional_edges(
        "validator",
        route_validation,
        {
            "editor": "editor",
            "rewrite": "rewrite"
        }
    )

    builder.add_edge("rewrite", "validator")

    # Final step
    builder.add_edge("editor", "cleaner")
    builder.set_finish_point("cleaner")

    return builder.compile()