from decouple import config
from griptape.structures import Agent
from griptape.tools import FileManager, WebSearch, WebScraper, ToolOutputProcessor


# Get Google Custom Search credentials on
# https://developers.google.com/custom-search/v1/introduction
web_search = WebSearch(
    google_api_key=config("GOOGLE_API_KEY"),
    google_api_search_id=config("GOOGLE_API_SEARCH_ID"),
)

web_scraper = WebScraper()

file_manager = FileManager()

tool_output_processor = ToolOutputProcessor()

agent = Agent(
    tools=[
        web_scraper, file_manager, tool_output_processor
    ]
)

# Dynamically summarize file content
# agent.run("me a summary of the file attention_abstract.txt in the files directory")

# Dynamically summarize file content and avoid the main prompt entirely
agent.tool_memory.disable_activities()
agent.run("summarize www.griptape.ai and store the summary in files/griptape.txt")
