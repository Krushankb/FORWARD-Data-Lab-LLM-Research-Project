# Integrate custom prompt templates into different chain types

Sure, I can explain how to use prompt templates with different chain types. A prompt template is a way of generating a text input for a language model based on some input variables. A prompt template has a template string and a list of input variables that can be formatted to produce a prompt. For example, if you have a prompt template like this:

```python
template = "Answer the following question based on the retrieved documents: {question}\n\n{summaries}"
prompt_template = PromptTemplate(template=template, input_variables=["question", "summaries"])
```

Then you can format it with different values for the input variables, such as:

```python
prompt_template.format(question="What is the capital of Germany?", summaries="Berlin is the capital and largest city of Germany by both area and population. ...")
```

This will produce a prompt like this:

```python
Answer the following question based on the retrieved documents: What is the capital of Germany?

Berlin is the capital and largest city of Germany by both area and population. ...
```
You can use prompt templates with different chain types in Langchain, such as **stuff**, **refine**, **map_reduce**, and **map_rerank**. Each chain type has its own expected input variables and output format. You can pass the prompt template to the **load_qa_chain** function or the **from_chain_type** method of the **RetrievalQA** chain. You can also specify additional arguments for the chain type, such as **document_variable_name**, **existing_answer**, or **context_str**. Here are some examples of how to use prompt templates with different chain types:

## stuff*
- **Stuff**: This chain type returns a list of retrieved documents as the output. The expected input variable for the prompt template is **document_variable_name**, which is the name of the variable that holds the list of documents. For example, if your prompt template is:

```python
template = "Answer the following question based on the retrieved documents: {question}\n\n{summaries}"
prompt_template = PromptTemplate(template=template, input_variables=["question", "summaries"])
```

Then you should pass **document_variable_name="summaries"** as an argument to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(OpenAI(), chain_type="stuff", prompt_template=prompt_template, document_variable_name="summaries")
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(), chain_type_kwargs={"prompt": prompt_template, "document_variable_name": "summaries"})
```
## Refine
- **Refine**: This chain type returns a single retrieved document as the output. The expected input variables for the prompt template are **question**, **existing_answer**, and **context_str**. For example, if your prompt template is:

```python
template = "Answer the following question based on the retrieved document: {question}\n\n{context_str}"
prompt_template = PromptTemplate(template=template, input_variables=["question", "context_str"])
```

Then you should pass **existing_answer=""** as an argument to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(OpenAI(), chain_type="refine", prompt_template=prompt_template, existing_answer="")
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(), chain_type_kwargs={"prompt": prompt_template, "existing_answer": ""})
```
### workig 


To create a custom refine template, you can use the **PromptTemplate** class or the **from_template** class method. You can specify the template string and the input variables that you want to use. For example, if you want to create a refine template that has a different wording, you can do something like this:

```python
refine_template = "You asked: {question}\nWe answered: {existing_answer}\nWe found some more information that might be relevant:\n{context_str}\nCan you improve the answer based on this information? If not, just repeat the original answer."
refine_prompt_template = PromptTemplate(template=refine_template, input_variables=["question", "existing_answer", "context_str"])
```

To integrate it with your retrievalqa chain, you can pass it as the value of **refine_prompt** to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(llm=llm, chain_type="refine", refine_prompt=refine_prompt_template)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="refine", retriever=docsearch.as_retriever(), chain_type_kwargs={"refine_prompt": refine_prompt_template})
```

I hope this helps you create and use a custom refine template.😊

## Map_reduce
- **Map_reduce**: This chain type applies a map function to each retrieved document and then combines them using a reduce function. The expected input variable for the map prompt template is **text**, which is the text content of each document. The expected input variable for the combine prompt template is **texts**, which is a list of texts returned by the map function. For example, if your map prompt template is:

```python
map_template = "Write a summary of the following text:\n\n{text}"
map_prompt_template = PromptTemplate(template=map_template, input_variables=["text"])
```

And your combine prompt template is:

```python
combine_template = "Write an answer to the following question based on these summaries:\n\n{question}\n\n{texts}"
combine_prompt_template = PromptTemplate(template=combine_template, input_variables=["question", "texts"])
```

Then you should pass them as arguments to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(OpenAI(), chain_type="map_reduce", map_prompt=map_prompt_template, combine_prompt=combine_prompt_template)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=docsearch.as_retriever(), chain_type_kwargs={"map_prompt": map_prompt_template, "combine_prompt": combine_prompt_template})
```

### testing 1
Sure, I can create a custom map reduce prompt template for you. Here is an example of how to do it:

```python
# Create a custom map prompt template that asks the language model to extract the main idea of each document
map_template = "Write the main idea of the following document in one sentence:\n\n{text}"
map_prompt_template = PromptTemplate(template=map_template, input_variables=["text"])

# Create a custom combine prompt template that asks the language model to use the main ideas to answer the question
combine_template = "Use the main ideas of the retrieved documents to answer the question: {question}\n\n{texts}"
combine_prompt_template = PromptTemplate(template=combine_template, input_variables=["question", "texts"])

# Pass the custom prompt templates to the load_qa_chain function or the from_chain_type method
qa_chain = load_qa_chain(llm=llm, chain_type="map_reduce", map_prompt=map_prompt_template, combine_prompt=combine_prompt_template)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=docsearch.as_retriever(), chain_type_kwargs={"map_prompt": map_prompt_template, "combine_prompt": combine_prompt_template})
```

This will create a retrievalqa chain that uses the map_reduce chain type, which applies the custom map prompt template to each retrieved document and then combines them using the custom combine prompt template. I hope this helps you create and use a custom map reduce prompt template.😊

### testing 2
It seems that you are getting a validation error for the **StuffDocumentsChain**. This might be because you are not passing the **document_variable_name** argument to the **load_qa_chain** function or the **from_chain_type** method. According to the Langchain documentation¹, the **document_variable_name** argument is the name of the variable in the llm_chain to put the documents in. For example, if your prompt template is:

```python
template = "Answer the following question based on the retrieved documents: {question}\n\n{summaries}"
prompt_template = PromptTemplate(template=template, input_variables=["question", "summaries"])
```

Then you should pass **document_variable_name="summaries"** as an argument to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(llm=llm, chain_type="map_reduce", map_prompt=map_prompt_template, combine_prompt=combine_prompt_template, document_variable_name="summaries")
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=docsearch.as_retriever(), chain_type_kwargs={"map_prompt": map_prompt_template, "combine_prompt": combine_prompt_template, "document_variable_name": "summaries"})
```

I found a similar question on Stack Overflow² that might be helpful. I hope this solves your problem.😊

Quelle: Unterhaltung mit Bing, 3.8.2023
(1) langchain custom prompts & input parameters not clear. https://stackoverflow.com/questions/76093852/langchain-custom-prompts-input-parameters-not-clear.
(2) How to use StuffDocumentsChain / Error when using third input variable .... https://github.com/langchain-ai/langchain/issues/504.
(3) StuffDocumentsChain | ️ Langchain. https://js.langchain.com/docs/api/chains/classes/StuffDocumentsChain.

## Map_rerank
- **Map_rerank**: This chain type applies a map function to each retrieved document and then reranks them based on a score function. The expected input variable for the map prompt template is **text**, which is the text content of each document. The expected input variable for the score prompt template is **text**, which is the text returned by the map function. For example, if your map prompt template is:

```python
map_template = "Write a summary of the following text:\n\n{text}"
map_prompt_template = PromptTemplate(template=map_template, input_variables=["text"])
```

And your score prompt template is:

```python
score_template = "Rate the relevance of this summary to the question {question} on a scale of 1 to 5:\n\n{text}"
score_prompt_template = PromptTemplate(template=score_template, input_variables=["question", "text"])
```

Then you should pass them as arguments to the **load_qa_chain** function or the **from_chain_type** method. For example:

```python
qa_chain = load_qa_chain(OpenAI(), chain_type="map_rerank", map_prompt=map_prompt_template, score_prompt=score_prompt_template)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_rerank", retriever=docsearch.as_retriever(), chain_type_kwargs={"map_prompt": map_prompt_template, "score_prompt": score_prompt_template})
```

### testing 1
To create a custom template for the map_rerank chain type, you need to create two prompt templates: one for the map function and one for the score function. The map function applies a transformation to each retrieved document, such as summarization or extraction. The score function assigns a relevance score to each transformed document based on the question. For example, if you want to create a map_rerank chain that summarizes each document and then rates them on a scale of 1 to 5, you can do something like this:

```python
# Create a custom map prompt template that asks the language model to write a summary of each document
map_template = "Write a summary of the following document in one sentence:\n\n{text}"
map_prompt_template = PromptTemplate(template=map_template, input_variables=["text"])

# Create a custom score prompt template that asks the language model to rate the relevance of each summary to the question on a scale of 1 to 5
score_template = "Rate the relevance of this summary to the question {question} on a scale of 1 to 5:\n\n{text}"
score_prompt_template = PromptTemplate(template=score_template, input_variables=["question", "text"])

# Pass the custom prompt templates to the load_qa_chain function or the from_chain_type method
qa_chain = load_qa_chain(llm=llm, chain_type="map_rerank", map_prompt=map_prompt_template, score_prompt=score_prompt_template)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_rerank", retriever=docsearch.as_retriever(), chain_type_kwargs={"map_prompt": map_prompt_template, "score_prompt": score_prompt_template})
```

This will create a retrievalqa chain that uses the map_rerank chain type, which applies the custom map prompt template to each retrieved document and then reranks them using the custom score prompt template. I hope this helps you create and use a custom template for the map_rerank chain type.😊

I hope this helps you understand how to use prompt templates with different chain types. For more information, you can check the Langchain documentation¹²³ or the Langchain examples. Happy learning!😊



