# Step 1: Import required libraries
from textwrap import wrap

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



#WRAP TOOL CALL

@wrap_tool_call




            
            
