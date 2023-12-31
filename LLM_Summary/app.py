from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader

# from transformers import T5Tokenizer, T5ForConditionalGeneration
import transformers
from transformers import pipeline
import torch
import base64
# from huggingface_hub import login

# Model and tokenizer 
# model_checkpoint = "google/flan-t5-large"
# model_tokenizer = T5Tokenizer.from_pretrained(model_checkpoint)
# model = T5ForConditionalGeneration.from_pretrained(model_checkpoint)
# model = transformers.AutoModelForCausalLM.from_pretrained("microsoft/Orca-2-7b")
# model_tokenizer = transformers.AutoTokenizer.from_pretrained(
#         "microsoft/Orca-2-7b"
#         # use_fast=False,
#     )

# File loader and preprocessing
def preprocess_pdf(file):
    loader =  PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=170, chunk_overlap=70)
    texts = text_splitter.split_documents(pages)
    final_text = ""
    for text in texts:
        final_text = final_text + text.page_content
    return final_text

# Language Model pipeline
def language_model_pipeline(filepath):
    summarization_pipeline = pipeline(
        'summarization',
        model="pszemraj/led-large-book-summary",
        device=0 if torch.cuda.is_available() else -1)
    input_text = preprocess_pdf(filepath)
    summary_result = summarization_pipeline(input_text, min_length=8,
    max_length = 1024,
    num_beams=4,
    do_sample=False)
    summarized_text = summary_result[0]['summary_text']
    return summarized_text

def main():
    summarized_result = language_model_pipeline("pdf/llama.pdf")
    print("\nSummarized Result: \n")
    print(summarized_result)

if __name__ == "__main__":
    main()
