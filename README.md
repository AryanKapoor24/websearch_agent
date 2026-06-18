# websearch_agent


A LangGraph-based AI agent that answers questions 
by searching the web in real time using Tavily.

So, it started as a basic pipeline i have created for a system which to be a multi modal agent in future. Right now, I have tools like Tavily search to fetch the data from the browser. It basically is search engine for LLM or agents(for now). LLM can use this tool to fetch information from the browser without using their limited database on their own. 

Current project includes of tav.py files, where i have establish all the libraries and code in it.

Libraries Used- 
langchain_groq
langchain_tavily
langchain.graph
langgraph.prebuilt
dotenv

Before coming to the code, let me briefly explain the architecture of the of the project i have created/used.


User Query -> LLM -> Decision(Web Search-Y/N)-> Tool Calling(if yes)-> Result-> LLM-> Action(Read,Write etc)

I have used langgraph for the orchestration, but due to its excessive abstraction and over complexity, i aim to change the frameworks in future or rather build my own. 

Meanwhile, brief info about how langgraph agents work,
they consist of of Nodes,Edges and State
Node- Functions which calls a tool(tavily, llm calling etc)
Edge- Defines how application moves from one node to another, like llm answer is yes, it will use a tool to websearch, if no, it will directly give the response to user
State- it holds messages and data, that is provided or changed by the nodes.


Ways to run it-
1. Clone the repo
2. Install dependencies
   pip install langchain-groq langchain-tavily langgraph python-dotenv
3. Create a .env file
   GROQ_API_KEY=your_key
   TAVILY_API_KEY=your_key
4. Run
   python tav.py