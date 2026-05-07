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

seq= code_prompt | model | parser | explain_prompt | model | parser
#Now in above pipeline, first in 
# code_prompt: we are asking the model to generate code based on the input topic. The output of this step will be the generated code.
# model: This step takes the prompt from the previous step and generates a response, which in this case will be the code related to the topic.
# parser: This step takes the output from the model and parses it into a string format that we can easily understand and use. The output of this step will be the generated code in a string format.
# explain_prompt: This step takes the generated code from the previous step and creates a new prompt asking the model to explain that code in simple terms. The output of this step will be a prompt that includes the code and asks for an explanation.
# model: This step takes the explanation prompt from the previous step and generates a response, which will be the explanation of the code in simple terms.
# parser: This step takes the output from the model and parses it into a string format that we can easily understand and use. The output of this step will be the explanation of the code in simple terms in a string format.


result= seq.invoke({"topic": "Write a Python function to calculate the factorial of a number."})

print(result)
#In output I will get a explanation of the code, but i will not get a code even though I crated prompt temlate for both code generation and explanation
#But still i got only code explanation , not the code itself
#Because we did not save the output of the code generation step anywhere, so when we try to explain the code in the next step, we don't have access to it. The RunnablePassthrough allows us to pass the generated code from the code generation step to the explanation step without modifying it, ensuring that we can use it in the explanation prompt.
#To fix this issue, we can use RunnablePassthrough to pass the generated code from the code generation step to the explanation step. This way, we can ensure that the generated code is available for the explanation prompt, and we can get both the code and its explanation in the output.


#SOLUTION IS IN NEXT PYTHON FILE 4_runnable_Passthrough_2.py