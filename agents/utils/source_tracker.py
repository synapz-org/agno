"""Custom tool for tracking and formatting sources from web searches."""

from typing import List, Dict
from agno.tools.duckduckgo import DuckDuckGoTools


class SourceTracker(DuckDuckGoTools):
    def __init__(self):
        super().__init__()
        self.sources: List[Dict[str, str]] = []

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Perform a search and track the sources."""
        results = super().search(query, max_results)
        self._add_sources(results)
        return results

    def news(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Perform a news search and track the sources."""
        results = super().news(query, max_results)
        self._add_sources(results)
        return results

    def _add_sources(self, results: List[Dict[str, str]]):
        """Add sources while avoiding duplicates."""
        for result in results:
            if result["link"] not in [s["link"] for s in self.sources]:
                self.sources.append(result)

    def format_sources(self) -> str:
        """Format the tracked sources with detailed information."""
        if not self.sources:
            return ""

        footnotes = "\n\n## Sources & References\n\n"
        footnotes += "_The following sources were consulted for this article:_\n\n"

        for i, source in enumerate(self.sources, 1):
            # Format the title as a clickable link
            footnotes += f"{i}. **[{source['title']}]({source['link']})**\n"

            # Add source details
            if "snippet" in source and source["snippet"]:
                snippet = source["snippet"].replace("\n", " ")
                footnotes += f"   - Summary: {snippet}\n"
            if "published" in source and source["published"]:
                footnotes += f"   - Published: {source['published']}\n"
            footnotes += "\n"

        footnotes += "_Note: Sources are retrieved via DuckDuckGo search. "
        footnotes += "Please verify information independently._\n"

        return footnotes
