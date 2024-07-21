import dash
from dash import html, dcc
import dash_cytoscape as cyto
import networkx as nx
import ast
from django_plotly_dash import DjangoDash

app = DjangoDash('Test')

app.layout = html.Div([
    html.H1('Введите список смежности:'),
    dcc.Input(id='adjacency-list', type='text', value="{'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}", placeholder='Список смежности'),
    html.Button('Построить граф', id='submit-val', n_clicks=0),
    cyto.Cytoscape(id='graph')
])

def create_graph(adjacency_list):
    G = nx.from_dict_of_lists(adjacency_list)
    pos = nx.spring_layout(G)

    nodes = [{'data': {'id': node, 'label': node}, 'position': {'x': 20 * pos[node][0], 'y': -20 * pos[node][1]}} for node in G.nodes()]
    edges = [{'data': {'source': edge[0], 'target': edge[1]}} for edge in G.edges()]

    elements = nodes + edges
    return elements

@app.callback(
    dash.dependencies.Output('graph', 'elements'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('adjacency-list', 'value')]
)
def update_graph(n_clicks, adjacency_list):
    adjacency_list = ast.literal_eval(adjacency_list)
    elements = create_graph(adjacency_list)
    return elements
