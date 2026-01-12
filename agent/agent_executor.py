from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import destination_tool, hotel_tool, itinerary_tool
from agent.memory import get_memory
from prompts.system_prompt import SYSTEM_PROMPT

def create_agent():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3
    )

    agent = initialize_agent(
        tools=[destination_tool, hotel_tool, itinerary_tool],
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=get_memory(),
        system_message=SYSTEM_PROMPT,
        verbose=True
    )

    return agent
