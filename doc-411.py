import sys
import os
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI

# from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

if __name__ == "__main__":
    # check that the necessary environment variables are set
    load_dotenv()
    DOCS_TO_INGEST_DIR_OR_FILE = os.getenv("DOCS_TO_INGEST_DIR_OR_FILE")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    if DOCS_TO_INGEST_DIR_OR_FILE is None or os.getenv("OPENAI_API_KEY") is None:
        print("Please set the environment variables in .env, as shown in .env.example.")
        sys.exit()

    # find documents to ingest
    if not os.path.exists(DOCS_TO_INGEST_DIR_OR_FILE):
        print(
            "The path set in the DOCS_TO_INGEST_DIR_OR_FILE .env variable is not a valid directory or file."
        )
        sys.exit()

    # load documents to ingest
    if os.path.isfile(DOCS_TO_INGEST_DIR_OR_FILE):
        loader = TextLoader(DOCS_TO_INGEST_DIR_OR_FILE)
    else:
        loader = DirectoryLoader(DOCS_TO_INGEST_DIR_OR_FILE)
    docs = loader.load()

    # create vectorstore
    try:
        # index = VectorstoreIndexCreator().from_loaders([loader])
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(docs, embeddings)

        llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
        bot = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
    except Exception as e:
        # print authentication errors etc.
        print(e)
        sys.exit()

    # start chat
    print("Replies may take a few seconds.")
    print("Doc-411 remembers the conversation but, not very accurately.")
    print('To exit, type "exit" or "quit".')
    chat_history = []
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

        # get response from model
        # reply = index.query(query, llm=ChatOpenAI() if USE_GENERAL_KNOWLEDGE else None)
        result = bot({"question": query, "chat_history": chat_history})
        reply = result["answer"]

        # update chat history
        chat_history.append((query, reply))

        # print reply
        print("DOC-411: ", reply)
        print("-" * 40 + "\n")
