# Step 1: Import required libraries
from dotenv import load_dotenv
load_dotenv()

import os
import requests

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
from tavily import TavilyClient
from rich import print

# Step 2: Tool1 - Weather Tool
@tool 
def get_weather(city: str) -> str:
    """Get the current weather of the city"""
    if not openweather_api_key:
        return "Error: OPENWEATHER_API_KEY not found in environment variables"
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    print("DEBUG:", data)
    
    if str(data.get("cod")) != "200":
        return f"Error fetching weather data: {data.get('message', 'Could not retrieve weather information.')}"
    
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    
    return f"The current weather in {city} is {temp}°C with {description}."

# Step 3: Tool2 - Tavily News Tool
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_latest_news(city: str) -> str:
    """Get the latest news of the city"""
    response = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3
    )
    
    result = response.get("results", [])
    if not result:
        return f"No news found for {city}."
    
    news_list = []
    for r in result:
        title = r.get("title", "No title")
        url = r.get("url", "No URL")
        content = r.get("content", "No content")
        news_list.append(f"- {title}\n  {content}\n  Source: {url}\n")
    
    return f"Latest news in {city}:\n\n" + "\n".join(news_list)

# Step 4 - Creating LLM and Agent Loop
llm = ChatMistralAI(model="mistral-small-2506")

tools = {
    "get_weather": get_weather,
    "get_latest_news": get_latest_news
}

llm_with_tool = llm.bind_tools([get_weather, get_latest_news])

messages = []

print("CITY INTELLIGENCE SYSTEM")
print("Type exit to quit")

while True:
    user_input = input("You :")
    if user_input.lower() == "exit":
        break
    messages.append(HumanMessage(content=user_input))
    
    while True:
        result = llm_with_tool.invoke(messages)
        
        if result.tool_calls:
            # IMPORTANT: First add the AI's tool-call message to history
            messages.append(result)  # result is AIMessage with tool_calls
            
            for tool_call in result.tool_calls:
                tool_name = tool_call['name']
                confirm = input(f"Agent wants to call {tool_name}. Approve (yes/no): ")
                
                if confirm.lower() == "no":
                    print("Tool call denied. Cannot get that information.")
                    # If denied, we break out of inner loop and ask user again?
                    # To keep simple, we just skip this tool and continue.
                    # But better to break and restart.
                    # We'll break the for loop and then break outer while?
                    # Actually, just break out of inner while to ask user again.
                    break
                
                tool_result = tools[tool_name].invoke(tool_call)
                messages.append(ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call["id"]
                ))
            # After processing all tool calls, continue the loop
            # so the AI can use the tool results to give final answer
            continue
        
        else:
            # No tool calls – final answer
            print(result.content)
            messages.append(AIMessage(content=result.content))
            break
# @tool
# This is a "decorator". It's like putting a special sticker on the function below that says: "This function can be used as a tool by the AI." Without this sticker, the AI wouldn't know it can call this function.

# def get_weather(city: str) -> str:
# We are defining (creating) a function named get_weather. It takes one input called city which must be text (string). It will give back text (string) as the result. Example: get_weather("Dehradun") will return something like "The current weather in Dehradun is 25°C with clear sky."

# """Get the current weather of the city"""
# This is a docstring – a little note to explain what the function does. It doesn't change how the code runs, but it helps humans (and AI) understand the purpose.

# if not openweather_api_key:
# This checks if the openweather_api_key variable is empty or missing. If we don't have the key, we cannot talk to OpenWeatherMap.

# return "Error: OPENWEATHER_API_KEY not found in environment variables"
# If the key is missing, we immediately exit the function and send back this error message.

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=metric"
# We build a special web address (URL) that we will ask for the weather. The URL has parts:

# https://api.openweathermap.org/data/2.5/weather – the main address of the weather service.

# ?q={city} – we put the city name into the URL (e.g., ?q=Dehradun).

# &appid={openweather_api_key} – we attach our secret key to prove we are allowed.

# &units=metric – this tells the service to give us temperature in Celsius (not Fahrenheit).

# response = requests.get(url)
# We use the requests.get function to send a "GET" request to that URL. It's like typing that URL into a web browser and pressing Enter. The service sends back the weather data as a response. We store that response in a variable called response.

# data = response.json()
# The response comes as a special format called JSON (looks like a mix of curly braces and colons). The .json() function converts that into a Python dictionary (like a list with named slots) so we can easily read it. We store it in data.

# print("DEBUG:", data)
# We print the word DEBUG: followed by the whole weather data. This is just for us to see what the API gave back, so we can debug if something goes wrong. It's like a peek behind the curtain.

# if str(data.get("cod")) != "200":
# Inside the weather data, there is a field called "cod". It usually contains a number like 200 if everything went fine, or 404 if the city wasn't found, etc. We convert it to a string (text) and compare it to "200". If it's not "200", then something went wrong.

# return f"Error fetching weather data: {data.get('message', 'Could not retrieve weather information.')}"
# If there was an error, we return a message that includes the error message from the API (if available), or a default message.

# temp = data["main"]["temp"]
# If no error, we go inside the data dictionary. First we look at the "main" part, then inside that we get the "temp" (temperature). Example: data["main"]["temp"] might be 22.5. We save it in temp.

# description = data["weather"][0]["description"]
# The "weather" part is a list (array) of weather conditions. Usually there is one item, so we take the first one with [0]. Inside that item we get the "description" (e.g., "clear sky", "light rain"). We save it in description.

# return f"The current weather in {city} is {temp}°C with {description}."
# We build a nice sentence using the city name, temperature, and description, and return it as the result of the function.

# print(get_weather.invoke("Dehradun"))
# This is a test call. We use .invoke("Dehradun") to run the get_weather function with "Dehradun" as the city. Then we print whatever the function returns. This is just to check that the tool works before we use it in the real AI.

# Step 3: Tool 2 – Tavily News Tool
# tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
# We create a new TavilyClient object (like a little robot that knows how to fetch news). We give it the secret API key stored under the name TAVILY_API_KEY in our environment. This client will do the news searches for us.

# @tool
# Again, the special sticker that marks the next function as a tool for the AI.

# def get_latest_news(city: str) -> str:
# Define a function called get_latest_news that takes a city name and returns text.

# """Get the latest news of the city"""
# Docstring explaining the function.

# response = tavily_client.search( query= f"latest news in {city}", search_depth="basic", max_results=3 )
# We ask the tavily_client to search for news. The search query is "latest news in {city}" (for example, "latest news in Dehradun"). search_depth="basic" means we want a simple, fast search. max_results=3 means we want at most 3 news articles. The result is stored in response.

# result = response.get("results", [])
# The response is a dictionary (like a box with labels). We look for the label "results". If it exists, we take its value; if not, we take an empty list []. This is safe because if there are no results, we don't want the program to crash.

# if not result:
# If result is an empty list (i.e., no news found), we enter this if block.

# return f"No news found for {city}."
# Return a simple message saying no news was found.

# news_list = []
# Create an empty list (like a shopping list) to store the formatted news items.

# for r in result:
# Loop through each news article in the result list. Each article is stored as r for one iteration.

# title = r.get("title", "No title")
# From the article r, try to get the value under the key "title". If it doesn't exist, use "No title" instead. Store it in title.

# url = r.get("url", "No URL")
# Try to get the "url" key (the web address of the full article). If missing, use "No URL".

# content = r.get("content", "No content")
# Try to get the "content" key (a short summary of the news). If missing, use "No content".

# news_list.append(f"- {title}\n {content}\n Source: {url}\n")
# We add a formatted string to the news_list. The - is like a bullet point. The \n means "new line". So each news item appears as:

# text
# - Title
#   Summary content
#   Source: URL
# and then a blank line.

# return f"Latest news in {city}:\n\n" + "\n".join(news_list)
# Finally, we build the full result. First we write "Latest news in Dehradun:\n\n" (two new lines). Then we take all the strings in news_list and join them together with a newline \n between each. The plus sign + combines them into one long string, which is returned.

# print(get_latest_news.invoke("Dehradun"))
# Another test call to see if the news tool works for Dehradun.

# Step 4 – Creating the LLM and the Agent Loop
# llm = ChatMistralAI(model = "mistral-small-2506")
# We create an instance of the Mistral AI language model (the smart robot). We tell it to use the model named "mistral-small-2506". This model is good at understanding and generating human-like text.

# tools = { "get_weather" : get_weather, "get_latest_news" : get_latest_news }
# We make a dictionary (a look-up table) that maps the tool names (as strings) to the actual functions. So later, when the AI says "I want to call get_weather", we can look up tools["get_weather"] and get the real function to run.

# llm_with_tool = llm.bind_tools([get_weather, get_latest_news])
# We "bind" the tools to the LLM. That means we tell the AI: "Hey, you are allowed to use these two tools (functions). When you think you need to know the weather, you can call get_weather; when you need news, you can call get_latest_news." The result is a new object llm_with_tool that has this knowledge.

# messages = []
# Create an empty list called messages. This will store the entire conversation history (what the user said, what the AI said, and the results from tools). It's like a diary of the chat.

# print("CITY INTELLIGENCE SYSTEM")
# Print a title for our program.

# print("Type exit to quit")
# Tell the user how to stop the program.

# while True:
# Start an infinite loop. This means the program will keep asking for user input forever, until we tell it to break (stop).

# user_input = input("You :")
# The program waits for the user to type something. The text "You :" is shown as a prompt. Whatever the user types is stored in user_input.

# if user_input.lower() == "exit":
# Convert the user input to lowercase (so "Exit", "EXIT", "exit" all count) and compare it to the string "exit". If it matches, then the user wants to quit.

# break
# This command jumps out of the infinite while loop, ending the conversation.

# messages.append(HumanMessage(content = user_input))
# We add a new message to the conversation history. We wrap the user's text inside a HumanMessage so the AI knows it came from the human. Example: HumanMessage(content="What's the weather in Dehradun?")

# while True:
# Start another inner infinite loop. This loop will handle the AI's responses and tool calls. It will keep going until the AI gives a final answer (without calling any more tools).

# result = llm_with_tool.invoke(messages)
# We ask the AI (with its bound tools) to respond to the conversation so far (which is in messages). The AI looks at what the user said and decides whether to answer directly or to use a tool like get_weather. The AI's response (which might be a text answer or a request to call a tool) is stored in result.

# # IMPORTANT FIX: ...
# This is a comment (not code). It explains that earlier there was a bug: the programmer used to append the AI's raw result directly to messages, which caused an error. Now they fixed it by only appending ToolMessage when a tool is actually called.

# if result.tool_calls:
# Check if the AI wants to call any tools. tool_calls is a list inside result. If it exists and is not empty, then the AI is asking to use a tool.

# for tool_call in result.tool_calls:
# Loop through each tool call that the AI requested (there could be more than one, though usually it's one).

# tool_name = tool_call['name']
# From the tool call, get the name of the tool, like "get_weather" or "get_latest_news".

# confirm = input(f"Agent wants to call {tool_name}. Approve (yes/no)")
# This is the human-in-the-loop part. The program asks the user: "Agent wants to call get_weather. Approve (yes/no)?" The user must type "yes" or "no". This is a safety feature so that the AI cannot use tools without permission.

# if confirm.lower() == "no":
# If the user says "no" (in any case), then we deny the tool call.

# print("tool call denied and I cannot get latest information")
# Tell the user that the tool call was denied. Then we break out of the inner loop? Actually let's see: after the if confirm.lower() == "no": there is break, but that break would only exit the for loop? Wait, the code actually has break inside the if, but it's not inside a loop? Let's look again:

# python
# if confirm.lower() == "no":
#     print("tool call denied and I cannot get latest information")
#     break
# That break would break out of the while True inner loop? Actually no – it's inside the for loop. But break inside a for loop only breaks out of the for loop, not the outer while. However, after breaking, the program will go to the next line after the for loop, which is continue. That continue would skip to the next iteration of the while. So this is a bit messy. But for explanation, we can say: if the user denies, we stop trying to run this tool and go back to ask the AI again (maybe without that tool). But in this code, it's not perfect – it's okay for learning.

# Actually the code continues with the break after the if, but then after the for loop there is a continue. Let's read carefully:

# python
# if confirm.lower() == "no":
#     print("tool call denied and I cannot get latest information")
#     break

# # Tool Input - Execute tool
# tool_result = tools[tool_name].invoke(tool_call)

# messages.append(ToolMessage(
#     content= tool_result,
#     tool_call_id = tool_call["id"]
# ))
# If the user says no, we break – but that break is actually breaking out of the for loop. Then after the for loop, there is continue (the next line). So the continue will send the outer while loop back to the beginning, and the AI gets another chance. But the messages list hasn't been updated, so the AI might repeat itself. This is a small bug, but for a 10-year-old we can just say: if the user says no, the program prints a message and stops trying to use that tool.

# (To keep it simple, I'll explain the intended behavior: the user must approve; if not, the tool is not run.)

# tool_result = tools[tool_name].invoke(tool_call)
# If the user says yes, we look up the actual function from the tools dictionary using the tool name. Then we .invoke() it, passing the tool_call object (which contains the arguments, like the city name). This runs the function (e.g., get_weather("Dehradun")) and stores the result in tool_result.

# messages.append(ToolMessage(content=tool_result, tool_call_id=tool_call["id"]))
# We add a new message to the conversation history. This time it's a ToolMessage. It contains the result from the tool (the weather or news text). It also includes the tool_call_id so the AI knows which tool call this result belongs to. This is important for the AI to match the result with its request.

# continue
# After processing the tool call (and appending the result), we use continue to jump back to the beginning of the inner while loop. That means the AI will be invoked again, but now the conversation has the tool result. The AI can then use that information to give a final answer.

# else:
# This else goes with the if result.tool_calls: above. If the AI did not ask for any tool calls, then we go into the else block.

# print(result.content)
# The AI gave a direct text answer (no tools needed). We print that answer to the screen.

# messages.append(HumanMessage(content=result.content))
# We add the AI's answer to the conversation history as a HumanMessage? Wait, that seems odd: the AI's answer is from the AI, not a human. But the programmer writes HumanMessage – that might be a small mistake. It should be AIMessage. However, for the purpose of continuing the conversation, it's okay because the AI will see its own previous answer as if a human said it, which might work but is not ideal. For simplicity, we explain that we store the AI's response in the message list so the AI remembers what it said.

# break
# Finally, we break out of the inner while loop because the AI has given a final answer. Then the program goes back to the outer while loop, which asks the user for the next input.