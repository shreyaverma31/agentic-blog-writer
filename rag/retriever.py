def retrieve_context(db, query):

    docs = db.similarity_search(query, k=3)

    context = ""

    for d in docs:
        context += d.page_content + "\n"

    return context