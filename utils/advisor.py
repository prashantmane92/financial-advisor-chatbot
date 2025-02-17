from langchain_openai import ChatOpenAI
from langchain.agents import Tool, AgentExecutor
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.agents.openai_functions_agent.agent_token_buffer_memory import AgentTokenBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, List
from utils.api import StockAPI

class FinancialAdvisor:
    def __init__(self, openai_api_key: str):
        """Initialize the FinancialAdvisor with necessary components"""
        self.llm = ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
            openai_api_key=openai_api_key
        )
        self.stock_api = StockAPI()
        self.tools = self._create_tools()
        self.agent = self._create_agent()

    def _create_tools(self) -> List[Tool]:
        """Create tools for the agent to use"""
        return [
            Tool(
                name="StockInfo",
                func=self.stock_api.get_stock_info,
                description="Get current stock information for a given symbol"
            )
        ]

    def _create_agent(self) -> AgentExecutor:
        """Create the financial advisor agent"""
        prompt = PromptTemplate(
            template="""You are a professional financial advisor. Use your knowledge and the tools available to provide 
            sound financial advice. Always consider the user's risk tolerance and financial goals.

            Current question: {input}
            {agent_scratchpad}""",
            input_variables=["input", "agent_scratchpad"]
        )

        agent = OpenAIFunctionsAgent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )

        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )

    def get_advice(self, query: str) -> str:
        """Get financial advice based on user query"""
        try:
            response = self.agent.run(query)
            return response
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}" 