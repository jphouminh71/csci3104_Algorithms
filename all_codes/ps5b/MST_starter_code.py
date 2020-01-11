# Author: Aric Hagberg (hagberg@lanl.gov)

#    Copyright (C) 2004-2019 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.
#    Modified by Shivendra Agrawal
#   student: Jonathan Phouminh 
import random
import re
import matplotlib.pyplot as plt
import networkx as nx

## DO NOT MODIFY THE CODE WITHIN THIS BLOCK ########################################

def miles_graph():
    """ Return the cites example graph in miles_dat.txt
        from the Stanford GraphBase.
    """
    # open file miles_dat.txt.gz (or miles_dat.txt)
    import gzip
    fh = gzip.open('miles_dat.txt.gz', 'r')

    G = nx.Graph()
    G.position = {}
    G.population = {}

    cities = []
    for line in fh.readlines():
        line = line.decode()
        if line.startswith("*"):  # skip comments
            continue

        numfind = re.compile("^\d+")

        if numfind.match(line):  # this line is distances
            dist = line.split()
            for d in dist:
                G.add_edge(city, cities[i], weight=int(d))
                i = i + 1
        else:  # this line is a city, position, population
            i = 1
            (city, coordpop) = line.split("[")
            cities.insert(0, city)
            (coord, pop) = coordpop.split("]")
            (y, x) = coord.split(",")

            G.add_node(city)
            # assign position - flip x axis for matplotlib, shift origin
            G.position[city] = (-int(x) + 7500, int(y) - 3000)
            G.population[city] = float(pop) / 1000.0
    return G


def draw_graph(G, kruskal_selected_edges, sorted_edges):
    '''
    Plots the networkx graph with MST selected by Kruskal's as overlay

    :param G: Networkx graph
    :param kruskal_selected_edges: List of edge tuple
    :return: None
    '''
    pos = G.position  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=10)
    title = ""

    if len(kruskal_selected_edges) > 0:
        non_MST_edges = [edge for edge in sorted_edges if edge not in kruskal_selected_edges]
        nx.draw_networkx_edges(G, pos,
                               edgelist=kruskal_selected_edges, width=0.5, edge_color='g')
        print("\nNumber of edges selected by Kruskal's = ", len(kruskal_selected_edges))

        nx.draw_networkx_edges(G, pos, edgelist=non_MST_edges,
                                width=1, alpha=0.5, edge_color='b')
        title = ", Edges in the MST = " + str(len(kruskal_selected_edges))
    else:
        nx.draw_networkx_edges(G, pos, edgelist=sorted_edges,
                               width=1, alpha=0.5, edge_color='b')
    plt.title("Threshold = " + str(EDGE_SELECTION_CRITERIA) + title)
    plt.savefig('MST.png')
    plt.show()


def find(vertex):
    '''
    Function that returns the leader vertex for any 'vertex'
    '''
    return leader_dict[vertex]

####################################################################################

''' take in two diffent vertexs, then make the smallers compenents become the leaders of the larger '''
def union(v1, v2):
    
    v1_leader = find(v1)
    v2_leader = find(v2)
    
    '''
    # at this point we have fused all of v2's components into v1's leader 
    components[v1_leader] = components[v1_leader] + components[v2_leader]
    for i in components[v2_leader]:
        leader_dict[i] = v1_leader
    '''
    

    #fuse based on size 
    if len(components[v1_leader]) >=  len(components[v2_leader]):
        # this will happen if we know that v1 has more components than v2 
        components[v1_leader] = components[v1_leader] + components[v2_leader]
        for i in components[v2_leader]:
            leader_dict[i] = v1_leader
            
            
    else:
        # this will happen if we know that v2 has more components than v1 
        components[v2_leader] = components[v2_leader] + components[v1_leader]
        for i in components[v1_leader]:
            leader_dict[i] = v2_leader

    
    
            

if __name__ == '__main__':
    ########## DO NOT MODIFY THE CODE IN THIS BLOCK ################################

    EDGE_SELECTION_CRITERIA = random.choice([500 + (i+1)*20 for i in range(4)])

    G = miles_graph()

    print("Loaded miles_dat.txt containing 128 cities.")
    print("digraph has %d nodes with %d edges"
          % (nx.number_of_nodes(G), nx.number_of_edges(G)))


    edges_to_consider = [(u, v, d) for (u, v, d) in G.edges(data=True)
                          if d['weight'] <= EDGE_SELECTION_CRITERIA]
    ''' this has all the edges that we will be working with in ascending order'''
    sorted_edges = [(u, v) for (u, v, d) in sorted(edges_to_consider,
                                                   key=lambda x:x[2]['weight'])]
    
    ''' this is indexed by an integer and will give you back a vertex at that spot '''
    vertices = []
    for u, v in sorted_edges:
        vertices.append(u)
        vertices.append(v)
    vertices = list(set(vertices))

    print("Edges considered (in ascending order) for this graph = ", len(sorted_edges))

    # A dictionary that has key as edge (u, v) and value as the length of the edge
    length_of_edge = {(u, v):d for (u, v, d) in edges_to_consider}

    # 'Find' function can be easily emulated via dict and
    # initially all vertices form their own componeor nt and point to just themselves
    # 'leader_dict' has key as vertex and value as it's leader vertex
    leader_dict = {v : v for v in vertices}

    # 'components' have key as the leader vertex and
    # value as a list of vertices that are in that component
    # Initially all the vertices form their own components
    components = {find(v) : [v] for v in vertices}

    kruskal_selected_edges = []
    ################################################################################

    # Write your code below to populate the 'kruskal_selected_edges' list
    # with the edges in the MST using the Kruskal's algorithm

    # Note that after the union call, you need to merge the components and
    # update the relevant leaders in 'leader_dict' otherwise find() won't work as expected

    # Your solution can start after this comment. You should also finish the 'union()' function
    # and use it along with the find() to write Kruskal's algorithm to populate
    # 'kruskal_selected_edges' list
    # You are allowed to change the signature of the union function
    
    # populate kruskals_selected_edges with kruskals algorith, refer to pseudocode in notes 
    '''
    - Sort edges in order of increasing costs, this is already done for us under sorted_edges
    - initialized empty set, already done for us kruskal_seleceted_edges []
    - for i to m ( m is the size of sorted_edges
         # need to somehow grab the vertex's of the given edge to be able to check both of them 
        if find(u) != find(v):
            Union(u,b)
            append that edge to kruskal_selected 
    
    print(sorted_edges[1])
    print(sorted_edges[1][0], "<-- PRINTING U")
    print(sorted_edges[1][1], "<-- PRINTING V")
    print("LEADER:",find(sorted_edges[1][0]))
    '''
    # THIS CODE IS FOR FINDING SPACINGS  
    
    for k in range(2,11):
        print("for k =:", k, "spacing is:")
        length_of_edge = {(u, v):d for (u, v, d) in edges_to_consider}
        kruskal_selected_edges = []
        leader_dict = {v : v for v in vertices}
        
        for i in range(len(sorted_edges)):
            u = sorted_edges[i][0]
            v = sorted_edges[i][1]
            if find(u) != find(v):
                union(u,v)
                if len(kruskal_selected_edges) < len(vertices)- 1 -k :
                    kruskal_selected_edges.append(sorted_edges[i])
                    
                else:
                    print(length_of_edge[sorted_edges[i]])
                    print("---------")
                    break
        
    
    
   # THIS IS STRICTLY FOR PRINTING OUT THE MST 
    for i in range(len(sorted_edges)):
        u = sorted_edges[i][0]
        v = sorted_edges[i][1]
        if find(u)  != find(v):
            union(u,v)
            if len(kruskal_selected_edges) < len(vertices):
                kruskal_selected_edges.append(sorted_edges[i])
    
    draw_graph(G, kruskal_selected_edges, sorted_edges)
    # Do not remove this line, it will save the MST as a figure for you
    #draw_graph(G, kruskal_selected_edges, sorted_edges)
    