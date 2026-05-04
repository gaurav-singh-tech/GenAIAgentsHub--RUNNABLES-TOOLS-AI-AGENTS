from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#1 Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "What is {input}?")
    ]
)

#2 Model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.5)

#3 Output Parser
parser = StrOutputParser() #In very simple worrd we can say that it is a tool that takes the output from the model and converts it into a format that we can easily understand and use. In this case, it takes the response from the model and turns it into a simple string that we can work with.

#4 Chain
chain = prompt | model | parser

response=chain.invoke("Deep Learning")
print(response)