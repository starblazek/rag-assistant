from rag.retriever import retrieve


def format_source(result):
    metadata = result.get("metadata", {})
    location = ""

    if "page" in metadata:
        location = f", page {metadata['page']}"
    elif "slide" in metadata:
        location = f", slide {metadata['slide']}"
    elif "paragraph" in metadata:
        location = f", paragraph {metadata['paragraph']}"
    elif "table" in metadata:
        location = f", table {metadata['table']}"

    return f"{result['source']}{location}"


def get_context(question):
    results = retrieve(question)

    if not results:
        return ""

    context_parts = []
    for result in results:
        context_parts.append(
            f"Source: {format_source(result)}\n{result['text']}"
        )

    return "\n\n".join(context_parts)
