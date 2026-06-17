from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode

llm = ChatGroq(model="llama-3.1-8b-instant")
tools = [TavilySearch(max_results=3)]
llm_with_tools = llm.bind_tools(tools)

# NODE 1 — LLM thinks and decides
def call_llm(state: MessagesState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

# NODE 2 — Tavily runs if LLM decided to search
tool_node = ToolNode(tools)

# EDGE — should we search or are we done?
def should_search(state: MessagesState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "search"   # LLM wants to use a tool
    return END            # LLM has final answer

# BUILD THE GRAPH
graph = StateGraph(MessagesState)

graph.add_node("llm", call_llm)
graph.add_node("search", tool_node)

graph.add_edge(START, "llm")
graph.add_conditional_edges("llm", should_search)
graph.add_edge("search", "llm")  # after search, go back to LLM

agent = graph.compile()

result = agent.invoke({"messages": [{"role": "user", "content": "Who is Messi?"}]})
print(result["messages"][-1].content)