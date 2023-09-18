from decouple import config
from griptape import utils
from griptape.structures import Agent
from griptape.tools import WebScraper, WebSearch


# Get Google Custom Search credentials on
# https://developers.google.com/custom-search/v1/introduction
web_search = WebSearch(
    google_api_key=config("GOOGLE_API_KEY"),
    google_api_search_id=config("GOOGLE_API_SEARCH_ID"),
)

web_scraper = WebScraper()

agent = Agent(
    tools=[
        web_search, web_scraper
    ]
)

utils.Chat(agent).start()
