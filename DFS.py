TIME = 0 # Global time variable for DFS

def DFS(G):
    for u in G.V:
        u.color = 'white'
        u.predecessor = None
    for u in G.vertList:
        if u.color == 'white':
            DFS_Visit(G, u)

def DFS_Visit(G, u):
    global TIME
    TIME += 1
    u.discovery = TIME
    u.color = 'grey'
    for v in u.getConnections():
        if v.color == 'white':
           v.predecessor = u
           DFS_Visit(G, v)
    u.color = 'black'
    TIME += 1
    u.finish = TIME
    L = u.finish - u.discovery
    G.fput(u, L)


class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = 'id', 'connectedTo', 'color', 'predecessor', 'discovery', 'finish'

    def __init__(self, key, color='white'):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :return: None
        """
        self.id = key
        self.connectedTo = {}
        self.color = color
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self, nbr, weight=0):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.id) + ' connectedTo: ' + str([str(x.id) for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]


class Graph:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
        object
    :slot: numVertices (int):  The total number of vertices in the graph
    """

    __slots__ = 'vertList', 'numVertices', 'f'

    def __init__(self):
        """
        Initialize the graph
        :return: None
        """
        self.vertList = {}
        self.f = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Add a new vertex to the graph.
        :param key: The identifier for the vertex (typically a string)
        :return: Vertex
        """
        # count this vertex if not already present
        if self.getVertex(key) == None:
            self.numVertices += 1
            vertex = Vertex(key)
            self.vertList[key] = vertex
        return vertex

    def fput(self, u, length):
        """
        Update the finish time dictionary for the specified vertex if not already added
        :param u: Vertex
        :param length: Length of time from discovery to finish
        """
        if u not in self.f.keys():
            self.f[u] = length

    def getVertex(self, key):
        """
        Retrieve the vertex from the graph.
        :param key: The vertex identifier
        :return: Vertex if it is present, otherwise None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        """
        Returns whether the vertex is in the graph or not.
        :param key: The vertex identifier
        :return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def addEdge(self, src, dest, cost=0):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :param cost: The edge cost (defaults to 0)
        :return: None
        """
        if src not in self.vertList:
            self.addVertex(src)
        if dest not in self.vertList:
            self.addVertex(dest)
        self.vertList[src].addNeighbor(self.vertList[dest], cost)

    def getVertices(self):
        """
        Return the collection of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Return an iterator over the vertices in the graph.
        :return: A list iterator over Vertex objects
        """
        return iter(self.vertList.values())

if __name__ == '__main__':
    pass