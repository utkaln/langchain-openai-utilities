# Build an Agent
- Agent is a way to allow LLMs to take actions by invoking external APIs and chaining actions
- Building an agent can be possible by using Langchain - Langgraph that allows building stateful, multi-actor applications with LLMs. [More details ...](https://langchain-ai.github.io/langgraph/)
- This example is referred from [Langchain Tutorial - Build an Agent](https://python.langchain.com/docs/tutorials/agents/)
- This example agent interacts with Tavily search engine. A separate implementation of the just the search using Tavily bound to Open AI is [here](./src/search/tavily-search.ipynb)
- By using Memory, the agent can be used as a chatbot
- Trace activities at [Langsmith](https://smith.langchain.com/). This requires one time setup. 

## Prerequisites
- Install Tavily library : `pip install -qU "langchain-community>=0.2.11" tavily-python`

## Steps to embed realtime Search within LLM
1. Define Search API 
2. Define search parameters and limits
3. Create search as an available tool for LLM
4. Bind search tool to LLM (This is an intermittent step for testing, not required for final step)
5. Interact with LLM. LLM can decide when to invoke search. If not required LLM answers on its own
  - However, point to note LLM decides to use the tool, actually does not perform the search at this point
  - To actually perform a search using the bound search tool from LLM, define an agent to perform the action
6. Create an agent using [Langgraph](https://langchain-ai.github.io/langgraph/)
  - Agent automatically binds the search tool to LLM, hence step 4 is NOT needed
7. Add memory to make the agent stateful




