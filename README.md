# Doc 411

## Introduction
This is a simple project that utilizes Langchain to have a large language model ingest your documents and be able to answer questions about them.

## Installation

1. Clone this repository and cd into it.
1. Create and activate a virtual environment with `python -m venv .venv && .venv/scripts/activate` (Windows) or `python -m venv .venv && source .venv/bin/activate` (Mac/Linux)
1. Install the requirements with `pip install -r requirements.txt`
1. The above command may fail with the error message:
```bash
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```
If this happens you will need to install the Microsoft C++ Build Tools. You can get them [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Then try installing the requirements again.


NOTE: I had to downgrade the version of the clickhouse-connect package (required by chromadb) from 0.6.4 to 0.5.22 because of the issue described [here](https://github.com/imartinez/privateGPT/issues/723). This may be fixed in the future, so you can try installing the latest version of clickhouse-connect if you want.
1. Copy the `.env.example` file to `.env` and fill in the values. 