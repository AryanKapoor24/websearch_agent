from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
import os
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Tool only 1 as of now
search_tool = TavilySearchResults(max_results=3)
tools = [search_tool]

# tells LLM how to think and decide
prompt = hub.pull("hwchase17/react")

# Create agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run with user input
query = input("Ask me anything: ")
result = agent_executor.invoke({"input": query})
print(result["output"])