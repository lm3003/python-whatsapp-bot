from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import AIMessage
import logging

checkpointer = InMemorySaver()
ai_prompt = """
You are a helpful health assitant agent. 
A user may ask you anything about health, food or exercise, please guide them to the best of your ability.
Also, help them to generate their daily calorie needs as per their height or weight, track their daily calorie intake, generate a tasty but healthy weekly meal plan as per their requirement.
If the question is not about health, just say that you don't know anything about that domain.
"""
agent = create_react_agent(
    model="gpt-4o-mini",
    tools=[],
    checkpointer=checkpointer,
    prompt=ai_prompt
)

def generate_response(message_body):
    config = {"configurable": {"thread_id": "1"}}
    agent_response = agent.invoke(
        {"messages": [{"role": "user", "content": message_body}]},
        config=config)
    for message in reversed(agent_response["messages"]):
        if isinstance(message, AIMessage):
            return message.content


