https://bluelight.co/blog/diagrams-as-code

# How to Install Diagrams
Requirement: Python 3.6 or higher

Depending on your environment, run one of those commands below:
  
    # using Homebrew for macOS users$
    brew install graphviz

    # using pip (pip3)
    $ pip install diagrams
    # pip3 install graphviz 

    # using pipenv
    $ pipenv install diagrams

    # using poetry
    $ poetry add diagrams

# How to Use Diagrams
You must import the necessary modules you want to add to your diagrams. 

They are called Nodes. They represent a node or system component. 

Nodes are composed of three parts: Provider, Resource type, Name.

Diagram represents a global diagram context.

Clusters allows you to group the nodes in an isolated group. You can create a cluster context with Cluster class. And you can also connect the nodes in a cluster to other nodes outside a cluster. There is no depth limit of nesting so that you can imagine the possibilities.

Edges represent a link between Nodes. It contains three attributes: label, color, and style.

Custom node: We usually import icons externally hosted so they can be accessed when we generate the diagrams.

## Data Flow and how to connect nodes together:

‍>> Connect nodes in the left to the right direction.

<< Connect nodes in right to left direction.

- Connect nodes in no direction. Undirected.

You can change the data flow direction with the direction parameter. Default is LR. (Left to Right)

# Generate the diagram

Once you're happy with the code, generate the diagram by running the command bellow which will create a .png version of your diagram.

            python my_diagram.py