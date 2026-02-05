from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv

load_dotenv()

def get_search_tool():
   # A professional researcher brings you the top 5 results from the internet
    return TavilySearch(k=5)