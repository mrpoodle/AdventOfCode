def read_in(file):
    connections = {}
    computers = set()
    for line in open(file):
        connection = line.strip().split("-")
        #computers.update(connection)
        connections = add_connection(connections, connection)
    return connections #, computers

def add_connection(connections, connection):
    connections = add_to_dict(connections, *connection)
    return  connections


def add_to_dict(d, a, b):
    if d == {}:
        d[a] = [b]
        d[b] = [a]
    else:
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]
    return d

# find cluster of connections
def find_cluster_3(connections):  #, computers):
    clusters = set()
    for computer1 in connections:
        for computer2 in connections[computer1]:
            for computer3 in connections[computer2]:
                if computer1 in connections[computer3]:
                    cluster = [computer1, computer2, computer3]
                    cluster.sort()
                    cluster = ",".join(cluster)
                    if "t" in [computer1[0], computer2[0], computer3[0]]:
                        clusters.add(cluster)
    return clusters


def find_cluster_biggest(connections):
    cluster = []
    for computer1 in connections:
        clique = find_biggest_clique(connections, [computer1])
        if len(clique) > len(cluster):
            cluster = clique
    cluster.sort()
    return ",".join(cluster)

def find_biggest_clique(connections, current_clique):
    for node in current_clique:
        for next_node in connections[node]:
            if set(current_clique).issubset(set(connections[next_node])):
                new_clique = find_biggest_clique(connections, current_clique + [next_node])
                if len(new_clique) > len(current_clique):
                    current_clique = new_clique
    return current_clique





def test2():
    connections = read_in("day23.tst")
    cluster = find_cluster_biggest(connections)
    print(cluster)

def run2():
    connections = read_in("day23.txt")
    cluster = find_cluster_biggest(connections)
    print(cluster)

def test():
    connections = read_in("day23.tst")
    clusters = find_cluster_3(connections)
    print(len(clusters))

def run():
    connections = read_in("day23.txt")
    clusters = find_cluster_3(connections)
    print(len(clusters))


test()
run()
test2()
run2()