# Doc 411

## Introduction
Doc 411 is a chatbot that utilizes Langchain, OpenAi's LLMs (or other language models of your choice), and ChromaDB to ingest your documents and utilize information contained in them in its responses. Roughly speaking, it is like ChatGPT that can additionally pull information from your documents.

## Installation

#### 1. Clone this repository and cd into it.

#### 2. Create and activate a virtual environment.
On Windows:
```bash
python -m venv .venv && .venv\scripts\activate
```

On Mac/Linux:
```bash
python -m venv .venv && source .venv/bin/activate
```

#### 3. Install the requirements.
Figuring out a way to install the requirements without running into errors turned out to be quite a challenge. There are some conflicts in the current versions, but if you are reading this far enough in the future, you can try to simply run:
```bash
pip install langchain openai chromadb tiktoken unstructured
```
If that doesn't work (for a reason other than the one described in step 4 below), then let's proceed with the workaround:
- run `pip install unstructured==0.7.12`
- upgrade numpy: `pip install numpy==1.24.3`
    - you will likely get a warning about a conflict, ignore it
- install the rest of the requirements: `pip install langchain==0.0.222 openai==0.27.8 chromadb==0.3.26 tiktoken==0.4.0`
- downgrade clickhouse-connect: `pip install clickhouse-connect==0.5.22`
    - the reason for this is the issue described [here](https://github.com/imartinez/privateGPT/issues/723)

If one of the above steps fails, try them again from the beginning using pip version 22.3.1: `pip install pip==22.3.1`. If that also fails, additionally switch to python version 3.11.3 (remember to double-check the pip version after switching).

#### 4. Installing requirements may fail with the error message:
```bash
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```
If this happens you will need to install the Microsoft C++ Build Tools. You can get them [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Then try installing the requirements again.

#### 5. Copy the `.env.example` file to `.env` and fill in the values. 

#### 6. Run the project.
```bash
python doc-411.py
```

## Resources
[Conversational retrieval QA: memory, condensing history](https://python.langchain.com/docs/modules/chains/popular/chat_vector_db)<br>
[Conversation memory, streaming, answering with sources](https://python.langchain.com/docs/ecosystem/integrations/vectara/vectara_chat)<br>
[Use case: understanding an entire Github repo](https://python.langchain.com/docs/use_cases/code/)

