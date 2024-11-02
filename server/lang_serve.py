# pip install "langserve[all]"
#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Create Prompt Template
system_template = "Translate the following text into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('user', '{text}')
])
# 2. Create LLM
model = ChatOpenAI()

# 3. Create Parser
parser = StrOutputParser()

# 4. Create Chain
chain = prompt_template | model | parser

# 5. Define REST API
translate_app = FastAPI(
    title="Langchain based Translation Server",
    version="1.0",
    description="A FastAPI from Langchain that translates user input",
)

# 6. Add Chain Route
add_routes(
    translate_app,
    chain,
    path="/trans",
)

# Steps to run the server, do not change
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(translate_app,host="localhost",port=8000)