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

# Input
topic = "Deep Learning"

# # Without RUNNABLES for short prompt response
# formatted_short = short_prompt.format_messages(topic=topic)
# response_short = model.invoke(formatted_short)
# str_output = parser.parse(response_short.content)

# print(str_output)


#WITH RUNNABLES(PIPELINE)

from langchain_core.runnables import RunnableParallel
#IT allows us to run multiple chains in parallel and get their results together.

# ✅ FIX: Ensure each pipeline is a Runnable (prompt | model | parser)
chain = RunnableParallel({
    "short": short_prompt | model | parser,
    "detailed": detailed_prompt | model | parser
})

#We are creating chains inside a dictionary because we want to run them in parallel. Each key represents a different chain with its own prompt, model, and parser.

result = chain.invoke({"topic": topic})
#It will run both the short and detailed explanations in parallel and return a dictionary with the results. The keys "short" and "detailed" will contain the respective explanations.


print("Short Explanation:", result["short"])
print("Detailed Explanation:", result["detailed"])




