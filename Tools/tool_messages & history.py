from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
#WE are importing human messages to main a history to get proper generated result

from rich import print

@tool
def get_text_length(text : str)-> int:
    """Calculate the length of the given text"""
    return len(text)

tools = {
    "get_text_length": get_text_length
}

llm = ChatMistralAI(model="mistral-small-2506")

#tool binding
llm_with_tool=llm.bind_tools([get_text_length])


messages=[]

prompt= input("You: ")
query =HumanMessage(content=prompt) #Here we are creating a human message with the content of the user's input prompt. The HumanMessage is a specific type of message that represents the user's input in a format that can be processed by the language model. By creating a HumanMessage, we can maintain a history of the conversation and provide

messages.append(query)

result=llm_with_tool.invoke(messages)

messages.append(result)

print(messages)


if result.tool_calls:
    tool_name= result.tool_calls[0]["name"]
    tool_message= tools[tool_name].invoke(result.tool_calls[0])
    messages.append(tool_message)
    print(messages)

llm_with_tool.invoke(messages)
print(result.content)

# Tool Flow (Simple)
# User asks something
# → Example: “What is the length of hello?”
# Model reads the question
# → Instead of answering, it may say:
# “I need to use get_text_length tool”
# Your code checks this
# → if result.tool_calls:
# → Means: “Did the model ask for a tool?”
# Get tool name
# → "get_text_length"
# Use dictionary to find function
# → tools["get_text_length"] → get_text_length function
# Manually run the tool
# → Tool calculates length → returns 5
# Add tool result to messages
# → So model can see the answer
# Send everything back to model again
# → Now model uses tool result
# Model gives final answer
# → “The length is 5”
# 🔑 One-line core idea

# 👉 Model decides,
# 👉 Your code executes,
# 👉 Tool returns result,
# 👉 Model finalizes answer.
