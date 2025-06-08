# filters.py

# This file defines the filtering mechanisms to customize the news feed based on user preferences.

class Filter:
    def __init__(self, criteria):
        self.criteria = criteria

    def apply(self, articles):
        """Apply the filter criteria to a list of articles."""
        filtered_articles = []
        for article in articles:
            if self.matches_criteria(article):
                filtered_articles.append(article)
        return filtered_articles

    def matches_criteria(self, article):
        """Check if the article matches the filter criteria."""
        # Implement the logic to check if the article meets the criteria
        return all(criterion in article for criterion in self.criteria)

def create_filter(criteria):
    """Factory function to create a new filter."""
    return Filter(criteria)