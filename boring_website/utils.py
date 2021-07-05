import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = buffer.getvalue()
    graph = base64.b64encode(image)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(title, scores, labels, colors):
    x = np.array(labels)
    y = np.array(scores)
    plt.bar(x, y, color=colors)
    plt.title(title)
    graph = get_graph()
    return graph