from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

#model names
model_1 = "llama-3.2-1b-preview"
model_2 = "gemma2-9b-it"
model_3 = "llama3-70b-8192"


load_dotenv()
#web search agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the Information",
    model = Groq(id=model_3),
    tools = [(DuckDuckGo())],
    isinstance =["Always include sources"],
    news = True,
    show_tool_calls = True,
    markdown =  True,
)

#Financial Agent
Financial_agent = Agent(
    name = "Financial Agent",
    model = Groq(id=model_3),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news = True,historical_prices = True,)],
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown =  True,
)

#combine Agent

multi_ai_agent = Agent(
    team=[web_search_agent,Financial_agent],
    model=Groq(id=model_3),
    instructions=["Use the web search agent to find information about the company and the financial agent to find information about the stock.",
                  "Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)
#Display in Terminal
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for SpaceX",stream=True)

#Display the Phidata Playground Terminal
#app = Playground(agents = [web_search_agent,Financial_agent]).get_app()

#if __name__ == "__main__":
    #serve_playground_app("playground:app", reload=True)