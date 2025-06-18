# src/main.py
from config import get_llm
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import FileManagementToolkit

llm = get_llm()
tools = FileManagementToolkit(root_dir="./data").get_tools()

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("List all files and summarize their contents.")
