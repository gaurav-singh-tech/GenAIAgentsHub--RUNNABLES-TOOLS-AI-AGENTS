from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
#Runnable passthrough in very simple words is a tool that allows us to pass data through a pipeline without any modification. It acts as a transparent layer that simply takes the input and forwards it to the next step in the pipeline without changing it in any way. This can be useful when we want to include certain data in our pipeline that doesn't require any processing or transformation, but we still want it to be available for later steps in the chain.
#In a very simple language whatever input we give to the RunnablePassthrough it will just pass that input to the next step in the pipeline without doing anything to it. It is like a middleman that takes the input and hands it over to the next part of the process without changing it at all.

model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
])

seq1= code_prompt | model | parser

seq2= RunnableParallel( #Using runnable paraller as we are creating more than one chain/sequence
    {
        "code": RunnablePassthrough(), #This will pass the generated code from seq1 to seq2 without any modification.
        "explanation": explain_prompt | model | parser #It will explain the code as input for explain_prompt then go to mode and finally parser
    }
)

chain = seq1 | seq2
#In above code we are creating two separate sequences, seq1 and seq2. The first

result= chain.invoke({"topic": "Write a Python function to calculate the factorial of a number."})

print(result['code']) #This will print the generated code for calculating the factorial of a number.
print(result["explanation"]) #This will explain the code

#Now this time we will get both code & its explanation also 