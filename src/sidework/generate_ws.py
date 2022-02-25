import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

def degree_distribution(G):
    degs = {}

    for n in G.nodes():
        deg = G.degree(n)
        if deg not in degs:
            degs[deg] = 0
        degs[deg] += 1
    items = sorted(degs.items())
    
    return items

def plot_degree_distributions(degrees_to_plot, i, graphs_to_plot):
    fig = plt.figure()
    
    for j in range(len(degrees_to_plot)):
        plt.plot([k for (k, v) in degrees_to_plot[j]], [v for (k, v) in degrees_to_plot[j]], label = 'Graph {}'.format(graphs_to_plot[j]+1))
        plt.xlabel('Average degree')
        plt.ylabel('Number of nodes')
        plt.title('Average Degree Distribution - Watts Strogatz')
        plt.legend()
    
    fig.savefig("Figures\sidework\degree_distribution_configuration_{}.png".format(i+1))

def generate_ws(num_nodes, k_neighbors, prob, iters):
    G_list = []

    for num_iters in range(iters):
        print("Running loop on graph number:", num_iters+1)
        G = nx.watts_strogatz_graph(num_nodes, k_neighbors, prob, seed = np.random)
        G_list.append(G)

    return G_list

def analyse_ws(G_list):

    avgDList = []
    avgCList = []
    avgPLList = []
    count = 1

    for graph in G_list:
        print("Analysing graph...", count)
        degrees = [val for (node, val) in graph.degree()]
        average_degree = sum(degrees)/len(degrees)
        average_clustering = nx.algorithms.cluster.average_clustering(graph)
        average_path_length = nx.average_shortest_path_length(graph)
        
        avgDList.append(average_degree)
        avgCList.append(average_clustering)
        avgPLList.append(average_path_length)
        count += 1

    return avgDList, avgCList, avgPLList

# Driver code
'''

    Configuration 1:
                    number of nodes -> num_nodes = 2.5 * (10**3) = 2500
                    linking probability -> prob = 10**(-2) = 0.01
                    number of iterations -> iters = 30

    Configuration 2:
                    number of nodes -> num_nodes = 2.5 * (10**3) = 1000
                    linking probability -> prob = 10**(-2) = 0.05
                    number of iterations -> iters = 30

    Configuration 3:
                    number of nodes -> num_nodes = 2.5 * (10**3) = 500
                    linking probability -> prob = 10**(-2) = 0.25
                    number of iterations -> iters = 30

'''

num_nodes = [2500, 1000, 500]
k_neighbors = [50, 20, 10]
prob = [0.01, 0.05, 0.25]
iters = 30

for i in range(3):
    ws_graphs = generate_ws(num_nodes[i], k_neighbors[i], prob[i], iters)
    avg_degrees, avg_clusterings, avg_path_lengths = analyse_ws(ws_graphs)

    print("Average Degree of the network =", np.average(avg_degrees))
    print("Average Clustering Coefficient of the network is =", np.average(avg_clusterings))
    print("Average Path Length of the network is =", np.average(avg_path_lengths))

    graphs_to_plot = random.sample(range(0, iters), 5)
    degrees_to_plot = []
    for index in graphs_to_plot:
        print("Plotting degree distribution of graph number:", index+1)
        degrees_to_plot.append(degree_distribution(ws_graphs[index]))

    plot_degree_distributions(degrees_to_plot, i, graphs_to_plot)
    print("----------------------------------------------------------------------")