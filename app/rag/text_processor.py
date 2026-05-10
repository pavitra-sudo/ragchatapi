def read_text_file(file_path: str) -> str:

    with open(file_path, "r", encoding="utf-8") as file:

        return file.read()
    
def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks