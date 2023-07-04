import sys
import os
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

if __name__ == "__main__":
    # check that the necessary environment variables are set
    load_dotenv()
    DOCS_TO_INGEST_DIR_OR_FILE = os.getenv("DOCS_TO_INGEST_DIR_OR_FILE")
    USE_GENERAL_KNOWLEDGE = os.getenv("USE_GENERAL_KNOWLEDGE")
    USE_GENERAL_KNOWLEDGE = (
        bool(USE_GENERAL_KNOWLEDGE) and USE_GENERAL_KNOWLEDGE.lower() != "false"
    )
    if DOCS_TO_INGEST_DIR_OR_FILE is None or os.getenv("OPENAI_API_KEY") is None:
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

    # start chat
    print("Please submit your queries. Replies may take a few seconds.")
    print(
        "NOTE: Doc-411 only remembers your current question, not the entire conversation."
    )
    print('To exit, type "exit" or "quit".')
    while True:
        # get query from user
        query = input("YOU: ")
        if query == "exit" or query == "quit":
            break
        if query == "":
            print("Please enter your query or press Enter to exit.")
            query = input("YOU: ")
            if query == "":
                break
        print()

        # get response from model/index
        reply = index.query(query, llm=ChatOpenAI() if USE_GENERAL_KNOWLEDGE else None)

        # print reply
        print("DOC-411: ", reply)
        print('-' * 40 + '\n')
