from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1 Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "What is {input}?")
    ]
)

# 2 Model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.5)

# 3 Output Parser
parser = StrOutputParser()

# 4 Two different prompts (fixed)
short_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Explain {topic} in one sentence.")
    ]
)

detailed_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Explain {topic} in detail.")
    ]
)



#WITH RUNNABLES(PIPELINE)

from langchain_core.runnables import RunnableParallel#IT allows us to run multiple chains in parallel and get their results together.
from langchain_core.runnables import RunnableLambda #In very simple words RunnableLambda allows us to create a simple function that can be run as part of a pipeline. It takes a Python function and makes it runnable within the LangChain framework.

# ✅ FIX: Ensure each pipeline is a Runnable (prompt | model | parser)
chain = RunnableParallel({
    "short": RunnableLambda(lambda x: x['short']) | short_prompt | model | parser,
    "detailed": RunnableLambda(lambda x: x['detailed']) |detailed_prompt | model | parser
})

#Now in above dictionary , in very simple language we are saying that for the "short" chain, take the input from the "short" key of the input dictionary, pass it through the short_prompt, then to the model, and finally to the parser.
# Similarly for the "detailed" chain, take the input from the "detailed" key, pass it through the detailed_prompt, then to the model, and finally to the parser.
#We are using Runnable Lamda to extract the specific input for each chain from the overall input dictionary that we will pass when invoking the chain.


result = chain.invoke({
    "short": {"topic": "AI & Machine Learning"},
    "detailed": {"topic":  "Natural Language Processing"}
})

print(result["short"])
print(result["detailed"])