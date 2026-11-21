from dotenv import load_dotenv
load_dotenv()

from typing import List
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain.agents.structured_output import ToolStrategy

class Source(BaseModel):
    '''Scheme for a source used by the agent '''
    url:str=Field(description='The url of the source')

class AgentResponse(BaseModel):
    '''Schema for agent response with answer and sources'''
    answer:str=Field(description='The agents answer to the query')
    Sources:List[Source]=Field(default_factory=list,description='List of sources used to generate the answers ')

llm=ChatGroq(model='openai/gpt-oss-120b',temperature=0)
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)
structured_llm=llm.with_structured_output(AgentResponse,method='json_mode')

def main():
    print("Hello from the langchain-course")
    result=agent.invoke({'messages':HumanMessage(content='find a job for ai engineer in chennai')})
    result=structured_llm.invoke(f"Return a JSON object with keys 'answer' and 'Sources' (list of objects with 'url') from:\n{result['messages'][-1].content}")
    print(result.Sources)
if __name__=="__main__":
    main()