<div align="center">

# 🤖 GenAI Agents Hub — Runnables • Tools • AI Agents

### *Master LangChain's Execution Paradigm: Build, Chain, and Deploy AI Agents*

**Production-Grade Patterns for LangChain Runnables • Tool Integration • Autonomous Agents**

---

<div align="center">
  <p>
    <a href="#-quickstart">
      <img src="https://img.shields.io/badge/🚀_Get_Started-v2.0-111?style=for-the-badge&labelColor=000&logo=github">
    </a>
    <a href="#-core-modules">
      <img src="https://img.shields.io/badge/🎯_Modules-3%2B-22C55E?style=for-the-badge">
    </a>
    <a href="#-examples">
      <img src="https://img.shields.io/badge/💡_Examples-10%2B-FF6B6B?style=for-the-badge">
    </a>
    <a href="https://github.com/gaurav-singh-tech">
      <img src="https://img.shields.io/badge/👤_Author-gaurav--singh--tech-0EA5E9?style=for-the-badge&logo=github">
    </a>
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
    </a>
    <a href="https://langchain.com/">
      <img src="https://img.shields.io/badge/LangChain-0.1%2B-1C3A5E?style=for-the-badge&logo=databricks">
    </a>
    <a href="https://mistral.ai/">
      <img src="https://img.shields.io/badge/Mistral-AI-FFA500?style=for-the-badge">
    </a>
    <a href="https://tavily.com/">
      <img src="https://img.shields.io/badge/Tavily-News_API-FF6B6B?style=for-the-badge">
    </a>
    <a href="https://openweathermap.org/">
      <img src="https://img.shields.io/badge/OpenWeather-API-4285F4?style=for-the-badge">
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
    <img src="https://img.shields.io/badge/Status-Active_Development-blue?style=flat-square">
    <img src="https://img.shields.io/github/stars/gaurav-singh-tech/GenAIAgentsHub--RUNNABLES-TOOLS-AI-AGENTS?style=flat-square">
  </p>

</div>

---

## 🎯 Overview

A **comprehensive hands-on laboratory** for mastering LangChain's **Runnable** architecture and building **autonomous AI agents**. Learn how to:

- ✅ Chain operations sequentially and in parallel
- ✅ Create custom tools with automatic binding
- ✅ Build weather/news agents with real external APIs
- ✅ Master message history and tool execution flow
- ✅ Deploy production-ready multi-tool agents

**Perfect for:**
- 🚀 LangChain developers mastering Runnables
- 🧪 AI engineers building autonomous agents
- 🏢 Teams deploying multi-tool LLM applications
- 📚 Learners understanding agent architecture

</div>

---

## 🌟 What Makes This Hub Special?

| Feature | Why It Matters |
|---------|----------------|
| **Runnables Pattern** | Learn LangChain 0.1+ paradigm for composable AI pipelines |
| **Tool Integration** | Understand automatic tool binding & execution |
| **Real Agents** | Build weather + news agents with live API integration |
| **Message History** | Master conversational AI with proper context management |
| **Production Patterns** | Copy-paste code ready for enterprise deployments |

---

## 📁 Repository Structure

```
📦 GenAIAgentsHub--RUNNABLES-TOOLS-AI-AGENTS/
│
├── 📂 RUNNABLES/                          # Core LangChain Runnables Patterns
│   ├── 1_sequence_runnable.py             # Basic pipeline: Prompt → Model → Parser
│   ├── 2_parallel_runnable_one_input.py   # Parallel execution of multiple chains
│   ├── 3_lambda_runnable_many_inputs.py   # Lambda functions in pipelines
│   └── 4_runnable_passthrough_2.py        # Pass data through without modification
│
├── 📂 Tools/                              # Custom Tool Creation & Binding
│   ├── own_tool.py                        # Custom @tool decorator example
│   ├── tool_binding.py                    # Binding tools to LLM
│   ├── tool_execution                     # Tool execution workflow
│   └── tool_messages & history.py         # Tool calls with message history
│
├── 📂 AI Agents/                          # Autonomous Multi-Tool Agents
│   └── agents.py                          # Weather + News agent with external APIs
│
└── 📄 README.md                           # This file
```

---

## 🚀 Quick Start

### 1️⃣ Installation

```bash
git clone https://github.com/gaurav-singh-tech/GenAIAgentsHub--RUNNABLES-TOOLS-AI-AGENTS.git
cd GenAIAgentsHub--RUNNABLES-TOOLS-AI-AGENTS

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install langchain langchain-mistralai python-dotenv tavily-py requests rich
```

### 2️⃣ Configure API Keys

Create `.env` file in project root:

```dotenv
# Core LLM
MISTRAL_API_KEY=sk_...

# External APIs
TAVILY_API_KEY=tvly_...
OPENWEATHER_API_KEY=...
```

### 3️⃣ Run Your First Example

```bash
# Try a simple Runnable chain
python RUNNABLES/1_sequence_runnable.py

# Expected output:
# Deep Learning is a subset of machine learning that uses neural networks...
```

---

## 🔗 RUNNABLES Module: The Foundation

Runnables are the core execution unit in LangChain 0.1+. Master 4 essential patterns:

### 📌 Pattern 1: Sequential Runnable

**What:** Chain operations one after another  
**When:** Prompt → Model → Parse Output

```bash
python RUNNABLES/1_sequence_runnable.py
```

**Under the hood:**
```python
from langchain_core.runnables import RunnableSequence

chain = prompt | model | parser
# "|" operator chains operations sequentially
result = chain.invoke({"input": "Deep Learning"})
```

---

### 📌 Pattern 2: Parallel Runnable

**What:** Run multiple chains concurrently on same input  
**When:** Get short + detailed explanations simultaneously

```bash
python RUNNABLES/2_parallel_runnable_one_input.py
```

**Under the hood:**
```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel({
    "short": short_prompt | model | parser,
    "detailed": detailed_prompt | model | parser
})

result = chain.invoke({"topic": "Deep Learning"})
# Returns: {"short": "...", "detailed": "..."}
```

---

### 📌 Pattern 3: Lambda Runnable

**What:** Transform data mid-pipeline with custom functions  
**When:** Extract, filter, or map data between stages

```bash
python RUNNABLES/3_lambda_runnable_many_inputs.py
```

**Under the hood:**
```python
from langchain_core.runnables import RunnableLambda

chain = RunnableParallel({
    "short": RunnableLambda(lambda x: x['short']) | short_prompt | model,
    "detailed": RunnableLambda(lambda x: x['detailed']) | detailed_prompt | model
})
```

---

### 📌 Pattern 4: Passthrough Runnable

**What:** Pass data through without modification  
**When:** Forward intermediate results to next stage

```bash
python RUNNABLES/4_runnable_passthrough_2.py
```

**Under the hood:**
```python
from langchain_core.runnables import RunnablePassthrough

chain = code_generator | RunnableParallel({
    "code": RunnablePassthrough(),  # Keep generated code
    "explanation": explain_prompt | model | parser  # Also explain it
})
```

---

## 🛠️ Tools Module: Create & Execute Custom Functions

### 🎯 Step 1: Define a Tool

```bash
python Tools/own_tool.py
```

```python
from langchain.tools import tool

@tool
def get_greeting(name: str) -> str:
    """Generate a greeting message for the given name."""
    return f"Hello, {name}!"

# Tools are Runnables
result = get_greeting.invoke("Alice")
print(result)  # Hello, Alice!
```

---

### 🎯 Step 2: Bind Tools to LLM

```bash
python Tools/tool_binding.py
```

```python
llm = ChatMistralAI(model="mistral-small-2506")

@tool
def get_text_length(text: str) -> int:
    """Calculate the length of the given text."""
    return len(text)

# Bind tool to LLM
llm_with_tool = llm.bind_tools([get_text_length])

# LLM can now decide to use the tool
result = llm_with_tool.invoke("Count chars in 'Hello'")
```

---

### 🎯 Step 3: Execute Tool Calls

```bash
python Tools/tool_execution
```

**Flow:**
1. LLM decides to call a tool → `result.tool_calls`
2. Extract tool name & args
3. Execute the tool manually
4. Send result back to LLM

```python
if result.tool_calls:
    tool_call = result.tool_calls[0]
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    
    # Execute
    tool_result = tools[tool_name].invoke(tool_args)
    
    # Send back to LLM for final answer
```

---

### 🎯 Step 4: Message History & Multi-Turn

```bash
python Tools/tool_messages\ \&\ history.py
```

**Key concept:** Maintain conversation history so LLM remembers context

```python
messages = []

# User input
messages.append(HumanMessage(content="What is the length of 'hello'?"))

# LLM response (may request tool)
result = llm_with_tool.invoke(messages)
messages.append(result)  # Add AI response

# Tool execution
if result.tool_calls:
    tool_result = tools[tool_name].invoke(tool_args)
    messages.append(tool_result)  # Add tool result

# Final LLM answer
final = llm_with_tool.invoke(messages)
```

---

## 🤖 AI Agents Module: Build Autonomous Systems

### 🌦️ City Intelligence Agent

Real-world example: Build an agent that answers questions about any city.

```bash
python "AI Agents/agents.py"
```

**Capabilities:**
- 🌤️ Get real-time weather via OpenWeather API
- 📰 Fetch latest news via Tavily Search
- 💬 Ask in natural language: "What's the weather in New York and latest news?"
- ✅ Human-in-the-loop approval for tool calls

**Example Interaction:**
```
You: What's the weather in San Francisco?
Agent wants to call get_weather. Approve (yes/no): yes
→ The current weather in San Francisco is 72°F with partly cloudy.

You: Tell me about the latest news there
Agent wants to call get_latest_news. Approve (yes/no): yes
→ Latest news in San Francisco:
   - Article 1: ...
   - Article 2: ...
```

**Code Walkthrough:**

```python
# Define tools
@tool 
def get_weather(city: str) -> str:
    """Get the current weather of the city"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}..."
    data = requests.get(url).json()
    return f"Weather in {city}: {data['main']['temp']}°C..."

@tool
def get_latest_news(city: str) -> str:
    """Get the latest news of the city"""
    response = tavily_client.search(query=f"latest news in {city}")
    return format_news(response)

# Create agent
llm_with_tools = llm.bind_tools([get_weather, get_latest_news])

# Agent loop
while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))
    
    while True:
        result = llm_with_tool.invoke(messages)
        
        if result.tool_calls:
            for tool_call in result.tool_calls:
                tool_name = tool_call['name']
                confirm = input(f"Approve {tool_name}? (yes/no): ")
                
                if confirm == "yes":
                    result = tools[tool_name].invoke(tool_call['args'])
                    messages.append(result)
        else:
            break  # No more tool calls, LLM gave final answer
```

---

## 📊 Comparison: Runnables vs Traditional LangChain

| Aspect | Traditional | Runnables |
|--------|-------------|-----------|
| **Chaining** | `.chain()` method | `\|` operator (pipe) |
| **Parallelism** | Complex setup | `RunnableParallel()` |
| **Transparency** | Black box | Full execution visibility |
| **Error Handling** | Limited | Built-in retry mechanisms |
| **Production Ready** | Partial | ✅ Full support |

---

## 🎓 Learning Flashcards

**Q1: What's the difference between Sequence and Parallel Runnable?**  
A: Sequence runs operations one-after-another (A→B→C). Parallel runs multiple chains on same input simultaneously ({X→A, X→B}).

**Q2: Why use `@tool` decorator?**  
A: It automatically converts Python functions into LangChain tools with `.invoke()`, tool binding, and LLM integration.

**Q3: What's tool binding?**  
A: It connects tools to an LLM so the model can decide when to use them. `llm.bind_tools([tool1, tool2])` makes tools available.

**Q4: Why maintain message history?**  
A: LLMs have no memory. History ensures the model knows previous context, tool results, and user questions for coherent responses.

**Q5: What's the agent loop?**  
A: User input → LLM decides tools → Execute tools → Add results to history → LLM generates answer → Repeat if needed.

**Q6: When should I use RunnableLambda?**  
A: When you need to transform data between pipeline stages (filter, map, reshape) without a full chain.

**Q7: What's RunnablePassthrough?**  
A: It forwards input unchanged. Useful when you want to keep intermediate results for multiple downstream operations.

---

## 🧯 Troubleshooting

| Issue | Solution |
|-------|----------|
| `MISTRAL_API_KEY not found` | Add to `.env` and run `load_dotenv()` |
| `Tavily API errors` | Verify `TAVILY_API_KEY` in `.env` and check rate limits |
| `Weather API returns 401` | Ensure `OPENWEATHER_API_KEY` is valid and active |
| `Tool not executed` | Check `if result.tool_calls:` and manually invoke the tool |
| `Message history empty` | Initialize `messages = []` and append `HumanMessage` first |

---

## 📚 Real-World Use Cases

### 1. **Multi-Source Data Aggregator**
Combine weather, news, stock prices into one unified response.

### 2. **Customer Support Bot**
Route queries to different tools: FAQ lookup, live agent, knowledge base search.

### 3. **Research Assistant**
Parallelize web search, arXiv papers, and database queries for comprehensive results.

### 4. **Smart Home Controller**
Tools: turn lights on/off, adjust temperature, play music. Agent decides based on user intent.

### 5. **Financial Advisor**
Tools: fetch stock prices, economic news, portfolio data. Agent synthesizes insights.

---

## 🤝 Contributing

Contributions welcome!

**To contribute:**
1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Add your Runnable pattern or Agent example
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

---

## 👤 About the Author

**Gaurav Singh**  
*LangChain Expert | AI Systems Architect | GenAI Builder*

- 🔗 **LinkedIn:** [contact-gauravsingh](https://www.linkedin.com/in/contact-gauravsingh/)
- 🐙 **GitHub:** [@gaurav-singh-tech](https://github.com/gaurav-singh-tech)
- 🌐 **Portfolio:** [gaurav-singh-portfolio.me](https://www.gaurav-singh-portfolio.me/)

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🎯 Next Steps

1. **Start with Runnables:** Try `RUNNABLES/1_sequence_runnable.py`
2. **Create Tools:** Build your custom tool in `Tools/`
3. **Build an Agent:** Extend `AI Agents/agents.py` with new tools
4. **Deploy:** Use with FastAPI, LangServe, or cloud platforms

---

<div align="center">

### ⭐ Found this useful? Star the repo!

It helps other developers discover LangChain Runnables and AI Agent patterns.

**[⭐ Star on GitHub](https://github.com/gaurav-singh-tech/GenAIAgentsHub--RUNNABLES-TOOLS-AI-AGENTS/stargazers)**

<br>

**Built with ❤️ for the GenAI community**

*Master Runnables. Build Agents. Ship Products.*

</div>