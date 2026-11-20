from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch




llm=ChatGroq(model='openai/gpt-oss-120b',temperature=0)
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)

def main():
    print("Hello from the langchain-course")
    result=agent.invoke({'messages':HumanMessage(content='search for 3 job postings for an ai engineer using langchain in the chennai area on linkedin and list their details')})
    print(result)
if __name__=="__main__":
    main()