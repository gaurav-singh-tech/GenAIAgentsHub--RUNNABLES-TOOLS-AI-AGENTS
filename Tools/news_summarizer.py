from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults # Search tool to fetch news articles
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

search_tool= TavilySearchResults(max_result =5) # Fetches the latest 5 news articles related to AI & Tech in 2026

llm= ChatMistralAI(model= "mistral-small-2506")

prompt= ChatPromptTemplate.from_template(
    """You are a helpful assistant that summarizes news articles.
    Given a news article, provide a concise summary of the main points and key information.
    The summary should be clear and easy to understand, capturing the essence of the article without unnecessary details.
    
    {news}"""# The {news} variable will be replaced with the news articles fetched by the search tool
)

chain = prompt | llm | StrOutputParser()

news_result= search_tool.run("latest AI & Tech news of 2026")

result= chain.invoke({"news": news_result})

print(result)

# The very simple explantion of above code step by step is
# 1. We import necessary libraries and load environment variables.
# 2. We initialize a search tool to fetch the latest news articles related to AI & Tech in 2026.
# 3. We set up a language model (Mistral) to process the news articles.
# 4. We create a prompt template that instructs the model to summarize the news articles.
# 5. We chain the prompt and the language model together, specifying that the output should be a string.
# 6. We run the search tool to get the latest news articles and then invoke the chain to generate a summary of those articles.


print(search_tool.args) #This will print the arguments that the search tool accepts, which in this case is "query". The args attribute is a list of the parameters that the tool can take as input. In this case, it indicates that the search tool requires a query string to perform the search and fetch relevant news articles.

print(search_tool.description) #This will print the description of the search tool, which provides a brief explanation of what the tool does. In this case, it will describe the functionality of the TavilySearchResults tool, which is to fetch news articles based on a given query. The description attribute is often used to provide users with an understanding of the tool's purpose and how it can be used effectively.    

print(search_tool.name) #This will print the name of the search tool, which is "TavilySearchResults". The name attribute is a string that represents the name of the tool, and it can be used to identify the tool when working with multiple tools in a language model pipeline.   