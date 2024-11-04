## Agent for interaction with SQL DB
1. Fetch all the available tables from a database
2. Decide whether tables are relevant to the question asked to LLM
3. Fetch DDL for the relevant tables
4. Generate a query based on question asked, and information from DDL
5. Double check query for common mistakes
6. Execute query and return results
7. Correct mistakes until query is successful
8. Formulate response based on the results
- Reference Documentation : https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#setup 

## Implementation Steps
1. Configure Database
  - Used Chinook DB. [Reference Document](https://langchain-ai.github.io/langgraph/tutorials/sql-agent/#setup)
2. Import required packages and setup LLM configuration
3. Error handling and utility methods
4. Define tools available for agent
5. Define workflow
6. Run the agent
7. Evaluate Response
- Full implementation : [agent_sql](./src/agent_sql/agent_sql.ipynb)

