from langchain.tools import tool

@tool# decorator to define a tool, decorator  simply means that we are using a special syntax to define a function as a tool that can be used in our language model chains. It allows us to easily integrate custom functions into our pipelines and make them available for use in our language model interactions.

def get_greeting(name: str) -> str: #pointer argument is string, also in return i want string output
    """Generate a greeting message for the given name.""" #Its a docstring that provides a brief description of what the function does. In this case, it explains that the function generates a greeting message for the given name.
    return f"Hello, {name}!, Welcome to the AI world" 

#Tools are also runnables
result= get_greeting.invoke("Alice") #Here we are invoking the get_greeting tool with the input "Alice". The invoke method is used to call the tool and pass the necessary arguments to it. In this case, we are passing the name "Alice" to the get_greeting function, which will generate a greeting message for that name.   

print(result)


#Tools Features:
print(get_greeting.name) #This will print the name of the get_greeting function, which is "get_greeting". The __name__ attribute is a built-in attribute in Python that holds the name of the function as a string. 

print(get_greeting.description) #This will print the description of the get_greeting tool, which is a brief explanation of what the tool does. In this case, it will print "Generate a greeting message for the given name.", which is the same as the docstring of the function. The description attribute is often used to provide a more user-friendly explanation of the tool's functionality.

print(get_greeting.args)