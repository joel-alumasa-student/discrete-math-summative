from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import matplotlib.pyplot as plt


graph_number = 0
euler_conn_graph = 0

while True:
    n = 10
    p = 0.5
    the_g = erdos_renyi_graph(n, p)
    print(f"The graph's vertices: {the_g.nodes}")
    print(f"The graph's edges: {the_g.edges}")

    nodes = the_g.nodes
    edges = the_g.edges

    counter1 = 0
    missing_num = False
    for each in nodes:
        counter = 0
        for every in edges:
            if each in every:
                counter += 1
        if counter == 0:
            missing_num = True

    if missing_num:
        print("graph is disconnected")
    else:
        counter1 += 1
        print("graph is connected")

    allEdges = the_g.edges
    allVertices = the_g.nodes

    lst = []
    for node in allVertices:
        for edge in allEdges:
            if node in edge:
                lst.append(node)
    counter2 = 0
    failed = False
    for n in allVertices:
        if n in lst:
            var = lst.count(n)  # var = 1
            if var % 2 != 0:
                failed = True
    if failed:
        print("The graph is not an Euler Circuit")
    else:
        counter2 += 1
        print("The graph is an Euler Circuit")
    print("Do you want another graph?\nFirst close the graph's panel...")

    if counter2 and counter1 == 1:
        euler_conn_graph += 1

    pos = nx.spring_layout(the_g)
    nx.draw_networkx_nodes(the_g, pos, node_size=500)
    nx.draw_networkx_edges(the_g, pos, edgelist=the_g.edges(), edge_color='black')
    nx.draw_networkx_labels(the_g, pos)
    plt.show()
    graph_number += 1

    keep_graphing = input("Enter Y for another one and N to end the operation:").upper()
    if keep_graphing == "Y":
        continue
    else:
        probability = euler_conn_graph/graph_number
        print(f"After the generation of the graph; {graph_number} times, and {euler_conn_graph} of them being euler circuit and connected, \nThe probability of graph(s) printed out to be euler circuit and connected is: {probability}")
        break


