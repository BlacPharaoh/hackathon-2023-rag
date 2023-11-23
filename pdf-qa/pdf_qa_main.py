import logging
import os
import sys

from dotenv import load_dotenv

from langchain.llms.octoai_endpoint import OctoAIEndpoint
from langchain.embeddings.octoai_embeddings import OctoAIEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index import (
    LLMPredictor,
    ServiceContext,
    GPTVectorStoreIndex,
    SimpleDirectoryReader
)

import time

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory
os.chdir(current_dir)
# Set logging level to CRITICAL
logging.basicConfig(level=logging.CRITICAL)

# Load environment variables
load_dotenv()

# Set the file storage directory
FILES = "./files"


def init():
    """
    Initialize the files directory.
    """
    if not os.path.exists(FILES):
        os.mkdir(FILES)


def handle_exit():
    """
    Handle exit gracefully.
    """
    print("\nGoodbye!\n")
    sys.exit(1)


def ask(file):
    """
    Load the file, create the query engine and interactively answer user questions about the document.
    """
    print("Loading...")
    documents = SimpleDirectoryReader(
        input_files=[os.path.abspath(file)]
    ).load_data()

    # Set up the language model and predictor
    llm = OctoAIEndpoint(
        endpoint_url="https://text.octoai.run/v1/chat/completions",
        model_kwargs={
            "model": "llama-2-70b-chat-fp16",
            "messages": [
                {
                    "role": "system",
                    "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request.",
                }
            ],
            "stream": False,
            "max_tokens": 256,
        },
    )

    llm_predictor = LLMPredictor(llm=llm)

    # Create the LangchainEmbedding
    embeddings = LangchainEmbedding(
        OctoAIEmbeddings(
            endpoint_url="https://instructor-large-f1kzsig6xes9.octoai.run/predict"
        )
    )

    # Create the ServiceContext
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor, chunk_size_limit=512, embed_model=embeddings
    )

    # Create the index from documents
    index = GPTVectorStoreIndex.from_documents(
        documents, service_context=service_context
    )

    # Create the query engine
    query_engine = index.as_query_engine(verbose=True, llm_predictor=llm_predictor)

    # Clear the screen
    os.system("clear")

    print("Ready! Ask anything about the document")
    print("")
    print("Press Ctrl+C to exit")

    try:
        from termios import tcflush, TCIFLUSH
        tcflush(sys.stdin, TCIFLUSH)
        while True:
            prompt = input("\nPrompt: ")
            if prompt is None:
                continue
            if prompt == "exit":
                handle_exit()

            start_time = time.time()
            response = query_engine.query(prompt)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print()

            # Transform response to string and remove leading newline character if present
            response = str(response).lstrip("\n")

            print(f"Response({round(elapsed_time, 1)} sec): {response}")
    except KeyboardInterrupt:
        handle_exit()


if __name__ == "__main__":
    # Initialize the file directory
    init()
    ask("file.pdf")
