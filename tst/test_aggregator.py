import unittest
from diting.aggregator import Aggregator

class TestAggregator(unittest.TestCase):

    def setUp(self):
        self.aggregator = Aggregator()

    def test_aggregate_news(self):
        # Test the aggregation of news from various sources
        sources = ['source1', 'source2']
        aggregated_news = self.aggregator.aggregate(sources)
        self.assertIsInstance(aggregated_news, list)
        self.assertGreater(len(aggregated_news), 0)

    def test_filter_news(self):
        # Test filtering functionality
        news_items = [
            {'title': 'Tech News', 'category': 'Technology'},
            {'title': 'Sports Update', 'category': 'Sports'}
        ]
        filtered_news = self.aggregator.filter(news_items, category='Technology')
        self.assertEqual(len(filtered_news), 1)
        self.assertEqual(filtered_news[0]['title'], 'Tech News')

if __name__ == '__main__':
    unittest.main()