
# LLM endpoint chat

Load a PDF file and ask questions via llama_index, LangChain and a LLM endpoint hosted on OctoAI

## Instructions

- Install the requirements

```bash
pip install -r requirements.txt -U
```
### Environment setup

To run our example app, there are four simple steps to take:

-  Paste the Endpoint URL in a file called `.env` in the root directory of the project.

```bash
ENDPOINT_URL="https://text.octoai.run/v1/chat/completions"
```

- Get an API Token from [your OctoAI account page](https://octoai.cloud/settings).
- Paste your API key in a file called `.env` in the root directory of the project.

```bash
OCTOAI_API_TOKEN=<your key here>
```

- Run `chat_main.py` script to chat with the LLM hosted endpoint.
```bash
python3 chat_main.py
```

or 
- Select a file from the menu or replace the default file `file.pdf` with the PDF you want to use.
- Run `pdf_qa_main.py` script to ask questions about your pdf file via llama_index, LangChain and the hosted endpoint.
```
python3 pdf_qa_main.py
```
- Ask any questions about the content of the PDF. 
<br>


For detailed setup steps, please see https://docs.octoai.cloud/docs/setup-steps-for-the-qa-app
<br>
<br>
