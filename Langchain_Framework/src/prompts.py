'''
===========================================
        Module: Prompts collection
===========================================
'''
# Note: Precise formatting of spacing and indentation of the prompt template is important for Llama-2-7B-Chat,
# as it is highly sensitive to whitespace changes. For example, it could have problems generating
# a summary from the pieces of context if the spacing is not done correctly

qa_template = """Use the entirety of the Harry Potter Book 1 file to answer the user's question. Imagine that you are a reader and you are taking notes about the book, keeping in mind the very important details as well as the overall ideas to summarize the whole book. If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else. Make sure to obtain the answer specifically and directly from the file. Relate to the story as best as you can. Answer in complete and detailed thoughts.
Answer:
"""
