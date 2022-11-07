import requests
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

results = requests.get('http://localhost:8983/solr/books/select?fl=title%2C%20authors%2C%20rating%2C%20published_date%2C%20description&indent=true&q.op=OR&q=description%3A%22dragons%22%0Atitle%3A%22dragons%22%0Acategories%3A%22fantasy%22&rows=25&sort=rating%20desc').json()['response']['docs']

relevant = list(map(lambda el: el.strip(), open("evaluation/q2rels.txt").readlines()))

for doc in results:
    print(doc['title'][0])

"""
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

precision_values = [
    len([
        doc
        for doc in results[:idx]
        if doc['title'][0] in relevant
    ]) / idx
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([
        doc for doc in results[:idx]
        if doc['title'][0] in relevant
    ]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

@metric
def ap():
    return sum(precision_values) / len(precision_values)

@metric
def ar():
    return sum(recall_values) / len(recall_values)

@metric
def acc():
    sum = 0.0
    for i in range(len(results)):
        if (i == len(relevant)):
            return sum / len(results)
        if (results[i]['title'][0] == relevant[i]):
            sum += 1.0
    return sum / len(results)

def calculate_metric(key):
    return metrics[key]()

evaluation_metrics = {
    'ap' : 'Average Precision',
    'ar' : 'Average Recall',
    'acc' : 'Accuracy'
}

df = pd.DataFrame([['Metric', 'Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m)]
        for m in evaluation_metrics
    ]
)

with open('evaluation/results_Q2.tex', 'w') as tf:
    tf.write(df.to_latex())

precision_recall_match = {k: v for k, v in zip(recall_values, precision_values)}
recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
recall_values = sorted(set(recall_values))

for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if recall_values[idx-1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
        else:
            precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()
plt.savefig('images/precision_recall_Q2.png')
"""