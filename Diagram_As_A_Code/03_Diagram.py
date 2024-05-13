from graphviz import Digraph

# Create a new Digraph object
dot = Digraph()

# Define nodes
dot.node('Storage', 'Cloud Storage')
dot.node('Function', 'Cloud Function')
dot.node('Dataflow', 'Cloud Dataflow')
dot.node('BigQuery', 'BigQuery')

# Define edges
dot.edges(['Storage->Function', 'Function->Dataflow', 'Dataflow->BigQuery'])

# Add labels to edges
dot.edge('Storage', 'Function', label='Upload File')
dot.edge('Function', 'Dataflow', label='Trigger')
dot.edge('Dataflow', 'BigQuery', label='Process Data')

# Render the graph to a file
dot.render('gcp_workflow', format='png', cleanup=True)