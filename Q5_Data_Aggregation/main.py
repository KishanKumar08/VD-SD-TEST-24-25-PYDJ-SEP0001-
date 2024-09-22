from collections import defaultdict

class DataAggregator:
    """Class for aggregating dictionary data."""
    
    def aggregate_data(self, data, key, aggregator):
        """Aggregates data based on the key and applies the aggregator function."""
        grouped_data = defaultdict(list)
        
        for item in data:
            grouped_data[item[key]].append(item)
        
        return {k: aggregator(v) for k, v in grouped_data.items()}

if __name__ == "__main__":
    data = [
        {'category': 'fruits', 'value': 10},
        {'category': 'fruits', 'value': 20},
        {'category': 'vegetables', 'value': 15}
    ]
    aggregator = lambda x: sum(item['value'] for item in x)
    da = DataAggregator()
    print(da.aggregate_data(data, 'category', aggregator))  # {'fruits': 30, 'vegetables': 15}
