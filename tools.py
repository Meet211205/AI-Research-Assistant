from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

from datetime import datetime
import wikipedia


# =========================================================
# SAVE TOOL
# =========================================================

@tool
def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Save the final research report to a text file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = f"""
============================================================
                    RESEARCH REPORT
============================================================

Generated: {timestamp}

{data}

============================================================
                    END OF REPORT
============================================================

"""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Research successfully saved to {filename}"


# Keep the same name used by main.py
save_tool = save_to_txt


# =========================================================
# WEB SEARCH TOOL
# =========================================================

search = DuckDuckGoSearchRun()

search_tool = search


# =========================================================
# WIKIPEDIA TOOL
# =========================================================

api_wrapper = WikipediaAPIWrapper(
    wiki_client=wikipedia,
    top_k_results=3,
    doc_content_chars_max=6000
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)