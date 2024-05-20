graph = []


def addedge(tup):
    graph.append(list(tup))


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, set1, set2):
    s1 = find(parent, set1)
    s2 = find(parent, set2)

    if rank[s1] < rank[s2]:
        parent[s1] = s2
    elif rank[s2] < rank[s1]:
        parent[s2] = s1
    else:
        parent[s2] = s1
        rank[s1] += 1


def boruvka(vertices):
    parent = []
    rank = []
    num_tree = vertices
    min_cost = 0
    ans = []

    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    while num_tree > 1:
        cheapest_edge = [-1] * vertices

        for i in range(len(graph)):
            src, dest, wght = graph[i]
            set1 = find(parent, src)
            set2 = find(parent, dest)

            if set1 != set2:
                if cheapest_edge[set1] == -1 or cheapest_edge[set1][2] > wght:
                    cheapest_edge[set1] = [src, dest, wght]
                if cheapest_edge[set2] == -1 or cheapest_edge[set2][2] > wght:
                    cheapest_edge[set2] = [src, dest, wght]

        for node in range(vertices):
            if cheapest_edge[node] != -1:
                src, dest, wght = cheapest_edge[node]
                set1 = find(parent, src)
                set2 = find(parent, dest)

                if set1 != set2:
                    min_cost += wght
                    union(parent, rank, set1, set2)
                    ans.append([src + 1, dest + 1, wght])
                    num_tree -= 1

    ans.append(min_cost)
    return ans


def callAlgo(inp):
    global graph
    graph = []

    vertices_set = set()
    for u in inp:
        vertices_set.add(int(u) - 1)
        v = inp[u][0].split(",")
        for vertex in v:
            vertices_set.add(int(vertex) - 1)

    vertices = len(vertices_set)

    for u in inp:
        v = inp[u][0].split(",")
        w = inp[u][1].split(",")
        for i in range(len(v)):
            addedge((int(u) - 1, int(v[i]) - 1, int(w[i])))

    ans = boruvka(vertices)
    Final_Path = ans[:-1]
    Final_Cost = ans[-1]

    return Final_Path, Final_Cost


# Main
if __name__ == "__main__":
    # Test Case
    test_case_1 = {
        "1": ["2,3,4", "7,9,14"],
        "2": ["3,5", "10,15"],
        "3": ["4,5,6", "2,11,6"],
        "4": ["6", "9"],
        "5": ["6", "5"],
    }
    # test_case_2 = {
    #     "1": ["2,3,4", "1,3,4"],
    #     "2": ["3,4", "2,5"],
    #     "3": ["4", "6"]
    # }
    a, b = callAlgo(test_case_1)
    print("Final Path:", a)
    print("Final Cost:", b)
