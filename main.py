from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from tools import search_tool, wiki_tool, save_tool


load_dotenv()


# =========================================================
# LLM
# =========================================================

llm = ChatOllama(
    model="mistral:7b",
    temperature=0,
    num_predict=3000
)


# =========================================================
# TOOLS
# =========================================================

tools = [
    wiki_tool,
    search_tool
]


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are an expert AI research assistant.

Your job is to research the user's topic and produce a detailed,
accurate and well-structured research report.

RESEARCH RULES:

1. Use Wikipedia for:
   - definitions
   - background
   - history
   - established information
   - important concepts

2. Use web search for:
   - additional information
   - recent developments
   - applications
   - examples
   - information not sufficiently covered by Wikipedia

3. For broad topics, use multiple research sources when useful.

4. Do not invent facts.

5. Do not repeat information simply to increase the length.

FINAL ANSWER:

Produce a detailed research report of approximately 800-1500 words
when sufficient information is available.

Use appropriate sections such as:

1. Introduction
2. Definition / Overview
3. Background
4. History and Development
5. Key Features
6. Important Concepts
7. Types / Categories
8. How It Works
9. Applications / Use Cases
10. Real-World Examples
11. Advantages
12. Limitations
13. Current Developments
14. Future Scope
15. Conclusion

Do not force sections that are irrelevant to the topic.

Use headings, subheadings, bullet points and numbered lists where
appropriate.

Explain technical concepts in understandable language.

At the end, include:

Sources:

Then list the sources used during research.

Do not create fake sources or URLs.
"""


# =========================================================
# CREATE AGENT
# =========================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)


# =========================================================
# USER INPUT
# =========================================================

print("\n" + "=" * 60)
print("             AI RESEARCH ASSISTANT")
print("=" * 60)

query = input("\nWhat do you want to research? ").strip()

if not query:
    print("\nPlease enter a research topic.")
    raise SystemExit


# =========================================================
# RUN AGENT
# =========================================================

print("\nResearching:", query)
print("-" * 60)

try:

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    })

except Exception as error:

    print("\nAn error occurred:")
    print(error)
    raise SystemExit


# =========================================================
# GET FINAL RESPONSE
# =========================================================

messages = result.get("messages", [])

output_text = ""

for message in reversed(messages):

    if getattr(message, "type", None) == "ai":

        content = message.content

        if isinstance(content, str):
            output_text = content
        else:
            output_text = str(content)

        break


# =========================================================
# DISPLAY FINAL ANSWER
# =========================================================

print("\n\n" + "=" * 60)
print("                    FINAL ANSWER")
print("=" * 60 + "\n")

print(output_text)


# =========================================================
# EXTRACT SOURCES
# =========================================================

sources = []

if "Sources:" in output_text:

    sources_block = output_text.rsplit("Sources:", 1)[1]

    for source in sources_block.split("\n"):

        source = source.strip()
        source = source.lstrip("-* ").strip()

        if source:
            sources.append(source)


# =========================================================
# DISPLAY SOURCES
# =========================================================

if sources:

    print("\n" + "=" * 60)
    print("                 EXTRACTED SOURCES")
    print("=" * 60)

    for index, source in enumerate(sources, start=1):

        print(f"{index}. {source}")


# =========================================================
# SAVE REPORT
# =========================================================

save = input("\nSave this research report? (y/n): ").strip().lower()

if save in ["y", "yes"]:

    try:

        result = save_tool.invoke(output_text)

        print("\n" + result)

    except Exception as error:

        print("\nUnable to save report:")
        print(error)

else:

    print("\nReport was not saved.")


print("\nResearch completed.")