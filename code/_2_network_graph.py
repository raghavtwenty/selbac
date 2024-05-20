"""
Project Name: SELBAC - Cable Cost Estimator using Boruvka Algorithm
Filename: _2_network_graph.py
Title: Plot the network diagram for nodes and edges
Author: Raghava | Github: @raghavtwenty
Date Created: May 20, 2023 | Last Updated: May 20, 2024
Version Info: 1.20052024 | Stable Release
Language: Python  | Version: 3.10.14,  64-bit
"""

# Importing required libraries
import networkx as nx
import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as mpl


# Extracting the user input as per required graph format
def userInputExtraction(User_Data_Dic):
    # Connecting edges
    Edges = []
    for key, value in User_Data_Dic.items():
        # From the values take the next nodes at index 0
        Current_Node = value[0].split(",")
        # Convert each string node to int node
        Temp_Dis_List = [int(temp) for temp in Current_Node]
        # Append the key with the connecting node
        for currNode in Temp_Dis_List:
            Edges.append((int(key), currNode))

    # Distance labels
    Distances = []
    # Take the values alone from the dictionary
    for i in User_Data_Dic.values():
        # From the values take the distances at index 1
        Current_Dis = i[1].split(",")
        # Convert each string distance to int distance
        Temp_Dis_List = [int(temp) for temp in Current_Dis]
        # Extend to the new list
        Distances.extend(Temp_Dis_List)

    return Edges, Distances


# Plot each edge and node
def drawGraphDisplay(totalHouseNum, totalEdges, totalEdgeNames):
    # Dynamically generate house number
    totalNodes = [house for house in range(1, totalHouseNum + 1)]

    # Initialize the graph
    Graph = nx.Graph()

    # Add the nodes
    Graph.add_nodes_from(totalNodes)

    # Add the edges
    Graph.add_edges_from(totalEdges)

    # Make the graph circular
    graphPosition = nx.circular_layout(Graph)

    # Make it into dictionary
    edgeNameDic = {}
    for edge in range(len(totalEdges)):
        edgeNameDic[totalEdges[edge]] = totalEdgeNames[edge]

    # Final Show
    nx.draw(Graph, graphPosition, with_labels=True)
    nx.draw_networkx_edge_labels(
        Graph,
        graphPosition,
        edge_labels=edgeNameDic,
        font_color="red",
    )

    # Save the image
    mpl.savefig("static/images/networkgraph.png")

    # Clear the current plot to reset for the next drawing
    mpl.clf()


# Plot
def drawNetwork(User_Data_Dic):
    Total_Edges, Total_Edge_Names = userInputExtraction(User_Data_Dic)
    Total_Houses = len(User_Data_Dic)
    drawGraphDisplay(Total_Houses, Total_Edges, Total_Edge_Names)


# Main
if __name__ == "__main__":
    # Test case
    drawNetwork({"1": ["2,3,4", "10,6,5"], "2": ["4", "15"], "3": ["4", "4"]})
    # drawNetwork({"1": ["2,3,4", "1,3,4"], "2": ["3,4", "2,5"], "3": ["4", "6"]})
