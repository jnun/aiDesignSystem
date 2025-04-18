# Python Data Processing Pipelines

## Pipeline Architecture Patterns

### Function-Based Pipeline
```python
def process_data(data):
    data = load_data(data)
    data = clean_data(data)
    data = transform_data(data)
    data = analyze_data(data)
    return data
```

### Class-Based Pipeline
```python
class DataPipeline:
    def __init__(self, config):
        self.config = config
        
    def process(self, data):
        data = self.load(data)
        data = self.clean(data)
        data = self.transform(data)
        return self.analyze(data)
        
    def load(self, data): ...
    def clean(self, data): ...
    def transform(self, data): ...
    def analyze(self, data): ...
```

### Generator-Based Pipeline
```python
def pipeline(data):
    for item in data:
        item = clean(item)
        item = transform(item)
        yield item

results = list(pipeline(source_data))
```

## Data Transformation Patterns

### Map-Reduce Pattern
```python
# Map phase
transformed_data = map(transform_function, data)

# Reduce phase
result = reduce(combine_function, transformed_data, initial_value)
```

### Filter-Map Pattern
```python
# Filter phase
filtered_data = filter(filter_predicate, data)

# Map phase
results = map(transform_function, filtered_data)
```

### Batch Processing
```python
def process_in_batches(data, batch_size=100):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        process_batch(batch)
```

## Error Handling Strategies

### Try-Except with Logging
```python
def safe_process(item):
    try:
        return process_item(item)
    except Exception as e:
        logging.error(f"Error processing {item}: {e}")
        return None
        
results = [r for r in map(safe_process, data) if r is not None]
```

### Error Collection
```python
def process_with_errors(data):
    results = []
    errors = []
    
    for item in data:
        try:
            results.append(process_item(item))
        except Exception as e:
            errors.append((item, str(e)))
            
    return results, errors
```

## Optimization Techniques

### Parallel Processing
```python
from concurrent.futures import ProcessPoolExecutor

def parallel_process(data, max_workers=4):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(process_function, data))
```

### Lazy Evaluation
```python
def lazy_pipeline(data):
    # Create generators instead of materializing intermediate results
    step1 = (transform1(x) for x in data)
    step2 = (transform2(x) for x in step1)
    step3 = (transform3(x) for x in step2)
    
    # Data only processes when consumed
    for result in step3:
        yield result
```

### Caching Results
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_transformation(data_key):
    # Expensive operation here
    return transformed_data
```

## Integration with Data Libraries

### Pandas Pipelines
```python
import pandas as pd

def pandas_pipeline(df):
    return (
        df
        .dropna()
        .assign(new_col=lambda x: x['col1'] + x['col2'])
        .query('value > 0')
        .groupby('category')
        .agg({'value': 'sum'})
    )
```

### NumPy Vectorization
```python
import numpy as np

def vectorized_process(data_array):
    # Instead of loops
    return np.where(
        data_array > 0,
        np.sqrt(data_array),
        data_array
    )
```