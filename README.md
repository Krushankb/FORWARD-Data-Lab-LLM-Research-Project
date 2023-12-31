# Next-Generation Search

## Overview

This module is responsible for generating answers to questions based on documents provided in a human-like thought process manner, with models such as Llama2 and BART-Large.

## Setup

List the steps needed to install your module's dependencies: 

1. Python version needed: Python 3.8.12

```
pip install -r requirements.txt 
```

2. Running tests/model:

For testing with Langchain

```
python3.8 db_build.py
python3.8 main.py
```

For testing with Huggingface Pipeline:
```
python3.8 app.py
```

Text description for files: 
* `LLM_Summary/app.py`: Executes Huggingface Pipeline with BART-Large model for step-by-step summarization
* `Langchain_Framework/data`: Contains source documents for model reference
* `Langchain_Framework/db_build.py`: Builds the vectordatabase to store the new tokenized documents for the model to read
* `Langchain_Framework/main.py`: Executes the Langchain framework with the Llama2 model for question-answering model chain

## Demo video

Link to video: 

https://drive.google.com/file/d/13-ju8MgIVA2rVBsGspb64wU_IES88eRq/view?usp=sharing

## Issues and Future Work
- Need to move away from stuff approach for Langchain framework
- Try to use a better model for summarization of larger files
- Need to combine the two frameworks to have model operate like a human-thought process agent

## References
For Document QA chain: https://towardsdatascience.com/running-llama-2-on-cpu-inference-for-document-q-a-3d636037a3d8

For Huggingface Pipeline: https://huggingface.co/docs/transformers/pipeline_tutorial
