# SELBAC
_Implementation of Minimum Spanning Tree (MST) Using Boruvka's Algorithm_
<br><br><br>


### PROTOTYPE VIDEO
https://github.com/raghavtwenty/selbac/assets/126254197/e37d01bb-47d7-4612-86e1-a3a9456f3d10

<br><br>

### HOW TO EXECUTE

#### Terminal

```
git clone https://github.com/raghavtwenty/selbac.git
```
<br>

```
cd selbac/code/
```
<br>

```
pip install -r requirements.txt
```
<br>

```
python main.py
```
<br>

#### Web Browser

```
http://127.0.0.1:5000/
```
<br>

### PROBLEM STATEMENT

A cable service provider is tasked with efficiently connecting a network of houses with TV cable connections. Utilize Boruvka's algorithm to recommend the most optimal path for connecting these houses, ensuring minimal total cable length and efficient coverage. 
<br><br><br>


### DOMAIN

Design and Analysis of Algorithms
<br><br><br>


### OBJECTIVE

Implement Boruvka's algorithm, Provide user friendly interface, Cables (Selbac) cost estimator.
<br><br><br>


### INTRODUCTION

The Boruvka (also known as Boruvka's) algorithm is a classical method in Design and Analysis of Algorithms (DAA) for finding the Minimum Spanning Tree (MST) of a connected, weighted graph. Developed by Otakar Borůvka in 1926, this algorithm repeatedly adds the shortest edge from each component to a different component, thereby merging them until a single connected component is formed. The algorithm is efficient for parallel computation and lays the foundation for more advanced MST algorithms like Kruskal's and Prim's.
<br><br><br>


### WORKING

1. Start with a graph G=(V,E) where V is the set of vertices and E is the set of edges. Initially, each vertex is considered as a separate component (tree).<br>
2. For each component, select the smallest weight edge that connects the component to any other component. <br>
3. Add all the selected edges to the MST and merge the connected components. If multiple edges are the same weight, choose any to break the tie. <br>
4. Repeat steps 2 and 3 until there is only one component left, which will be the MST. <br>
5. The algorithm terminates when all vertices are part of a single component.
<br><br>


### FEATURES

- Displays Network Graph <br>
- Finds the Optimal Path <br>
- Minimum Spanning Tree (MST) 
<br><br><br>


### TECHNOLOGIES USED

- Networkx Grpahs <br>
- Flask Web framework
<br><br><br>


### END USERS

1. Students
2. Researchers
<br><br><br>


### OUTPUTS

- Home Page <br><br>
![1](https://github.com/raghavtwenty/selbac/assets/126254197/fa0e931c-5f86-4e8e-888b-950bf76f80d5)


- Input Page <br><br>
![2](https://github.com/raghavtwenty/selbac/assets/126254197/a2b0009a-7697-4f4a-baf4-3d4b0f658262)


- Input Page <br><br>
![3](https://github.com/raghavtwenty/selbac/assets/126254197/a855d73e-5057-4eaf-9cc2-847848394dc3)


- Input Page <br><br>
![4](https://github.com/raghavtwenty/selbac/assets/126254197/03e44730-5bd2-482f-b647-0273e6837512)


- Output Page <br><br>
![5](https://github.com/raghavtwenty/selbac/assets/126254197/0497d632-390b-4a4f-89dd-8e82fafadec9)


- Output Page <br><br>
![6](https://github.com/raghavtwenty/selbac/assets/126254197/cf05099a-574f-4916-b0ba-3b25451ece4a)


- Network Graph <br><br>
![7](https://github.com/raghavtwenty/selbac/assets/126254197/feaa426c-d4b2-4ba7-a7da-1ca0d7cb9cd5)

<br>

### DESIGNED & DEVELOPED BY

- FARHAAN
- NAVEEN
- RAGHAVA
<br><br>


_END OF README_
