# Doc 411

## Introduction
This is a simple project that utilizes Langchain to have a large language model ingest your documents and be able to answer questions about them.

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
95% of the time for creating this project was spent on figuring out a way to install the requirements. There are some conflicts in the current versions, but if you are reading this far enough in the future, you can try to simply run:
```bash
pip install langchain openai chromadb tiktoken unstructured
```
If that doesn't work (for a reason other than the one described in step 4 below), then let's proceed with the workaround:
- run `pip install unstructured==0.7.12`
- upgrade numpy: `pip install numpy==1.24.3`
    - you will likely get a warning about a conflict, ignore it
    - if this fails, try from the beginning with pip version 22.3.1
- install the rest of the requirements: `pip install langchain==0.0.222 openai==0.27.8 chromadb==0.3.26 tiktoken==0.4.0`
- downgrade clickhouse-connect: `pip install clickhouse-connect==0.5.22`
    - the reason for this is the issue described [here](https://github.com/imartinez/privateGPT/issues/723)
    
#### 4. The above command may fail with the error message:
```bash
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```
If this happens you will need to install the Microsoft C++ Build Tools. You can get them [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Then try installing the requirements again.

#### 5. Copy the `.env.example` file to `.env` and fill in the values. 


### Installation Notes
 I had to downgrade the version of the clickhouse-connect package (required by chromadb) from 0.6.4 to 0.5.22 because of the issue described [here](https://github.com/imartinez/privateGPT/issues/723). This may be fixed in the future, so you can try installing the latest version of clickhouse-connect if you want.
