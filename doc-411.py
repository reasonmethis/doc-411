import sys
import os
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

if __name__ == "__main__":
    # check that the necessary environment variables are set
    load_dotenv()
    try:
        _ = os.getenv("OPENAI_API_KEY")
        DOCS_TO_INGEST_DIR_OR_FILE = os.getenv("DOCS_TO_INGEST_DIR_OR_FILE")
    except Exception as e:
        print(
            "Please set the DOCS_TO_INGEST_DIR_OR_FILE and OPENAI_API_KEY environment variables in .env."
        )
        sys.exit()

    # find documents to ingest
    if not os.path.exists(DOCS_TO_INGEST_DIR_OR_FILE):
        print(
            "The path set in the DOCS_TO_INGEST_DIR_OR_FILE environment variable is not a valid directory or file."
        )
        sys.exit()

    # load documents and create index
    if os.path.isfile(DOCS_TO_INGEST_DIR_OR_FILE):
        loader = TextLoader(DOCS_TO_INGEST_DIR_OR_FILE)
    else:
        loader = DirectoryLoader(DOCS_TO_INGEST_DIR_OR_FILE)

    try:
        index = VectorstoreIndexCreator().from_loaders([loader])
    except Exception as e:
        # print authentication errors etc.
        print(e)
        sys.exit()

    print('Please submit your questions. Replies may take a few seconds.')
    print('NOTE: Doc-411 only remembers your current question, not the entire conversation.')
    print('To exit, type "exit" or "quit".')
    while True:
        # get query from user
        query = input("YOU: ")
        if query == "exit" or query == "quit":
            break   

        # get response from index
        response = index.query(query)

        # print response
        print("DOC-411: ", response)
