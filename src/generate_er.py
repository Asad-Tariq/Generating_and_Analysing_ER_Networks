import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

'''
    A helper function that is used to find the degree
    distribution of a graph.
    Arguments:
            G -> The graph for which we need to find
            the degree distribution.
    Return:
            items -> A sorted list of the degree of each
            node in the graph.
'''

def degree_distribution(G):
    degs = {}

    for n in G.nodes():
        deg = G.degree(n)
        if deg not in degs:
            degs[deg] = 0
        degs[deg] += 1
    items = sorted(degs.items())
    
    return items

'''
    A helper function that is used to plot the degree
    distributions from the input list and save the
    resulting plot.
    Arguments:
            degrees_to_plot -> The sorted list of the
            degrees of the nodes in the graph.
            i -> A counter used to just name the file
            of the degree distribution figure to be saved.
            graphs_to_plot -> A list of indexes of the
            graphs to plot which is used to create the
            legend of the degree distribution figure.
    Return:
            None.
'''

def plot_degree_distributions(degrees_to_plot, i, graphs_to_plot):
    fig = plt.figure()
    
    for j in range(len(degrees_to_plot)):
        plt.plot([k for (k, v) in degrees_to_plot[j]], [v for (k, v) in degrees_to_plot[j]], label = 'Graph {}'.format(graphs_to_plot[j]+1))
        plt.xlabel('Average degree')
        plt.ylabel('Number of nodes')
        plt.title('Average Degree Distribution - Erdos Renyi')
        plt.legend()
    
    fig.savefig("Figures\degree_distribution_configuration_{}.png".format(i+1))

'''
    A helper function that generates the random ER
    graphs.
    Arguments:
            num_nodes -> The number of nodes to be in
            the random ER graph.
            prob -> The linking probability of any two
            nodes in the random ER graph.
            iters -> The number of iterations that need
            to be run for each configuration.
    Return:
            G_list -> The list of graph objects generated.
'''

def generate_er(num_nodes, prob, iters):
    G_list = []

    for num_iters in range(iters):
        print("Running loop on graph number:", num_iters+1)
        G = nx.fast_gnp_random_graph(num_nodes, prob, seed = np.random)
        G_list.append(G)

    return G_list

'''
    A helper function that is used for the analysis of
    the random ER graphs. It is used to find the average
    degree, average clustering coefficient and the average
    path length of each graph.
    Arguments:
            G_list -> The list of graph objects to be
            analysed.
    Return:
            avgDList -> The list of average degree of
            each graph object in the G_list.
            avgCList -> The list of average clustering
            coefficient of each graph object in the
            G_list.
            avgPLList -> The list of average path length
            of each graph object in the G_list.
'''

def analyse_er(G_list):

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
prob = [0.01, 0.05, 0.25]
iters = 30

for i in range(3):
    er_graphs = generate_er(num_nodes[i], prob[i], iters)
    avg_degrees, avg_clusterings, avg_path_lengths = analyse_er(er_graphs)

    print("Average Degree of the network =", np.average(avg_degrees))
    print("Average Clustering Coefficient of the network is =", np.average(avg_clusterings))
    print("Average Path Length of the network is =", np.average(avg_path_lengths))

    graphs_to_plot = random.sample(range(0, iters), 5)
    degrees_to_plot = []
    for index in graphs_to_plot:
        print("Plotting degree distribution of graph number:", index+1)
        degrees_to_plot.append(degree_distribution(er_graphs[index]))

    plot_degree_distributions(degrees_to_plot, i, graphs_to_plot)
    print("----------------------------------------------------------------------")