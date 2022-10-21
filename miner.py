import igraph as ig
import matplotlib.pyplot as plt
import random

# weighted selection:
# random.choices(list, weights=(10, 20, 70), k=1)[0] # (returns a list)

class GraphMiner:
    def __init__(self, graph=None):
        self.graph = graph if graph else ig.Graph() # underlying graph to solve
        
        # solutions are represented as a list of edges
        self.individuals = [] # possible solutions in the population

    def initGraph(self, file):
        edges = []
        n_vertices = float('-inf')

        with open(file, "r") as inputFile:
            lines = inputFile.readlines()
            for line in lines[2:]:
                data = line.split()
                vertexOne = int(data[0])
                vertexTwo = int(data[1])

                if max(vertexOne, vertexTwo) > n_vertices:
                    n_vertices = max(vertexOne, vertexTwo)
                    
                edges.append([vertexOne, vertexTwo])

        self.graph = ig.Graph(n_vertices + 1, edges)

    def plot(self, individual=None):
        # Set attributes for the graph, nodes, and edges
        self.graph.vs["vertex"] = [x for x in range(self.graph.vcount())]
        # self.graph.es["path"] = [False, False, False, False, False, False, False, True]

        # Plot
        _, ax = plt.subplots(figsize=(10, 10))
        ig.plot(
            self.graph,
            target=ax,
            layout="circle",
            vertex_size=0.15,
            # vertex_color=["steelblue" if gender == "M" else "salmon" for gender in g.vs["gender"]],
            vertex_color="gray",
            vertex_frame_width=4.0,
            vertex_frame_color="white",
            vertex_label=self.graph.vs["vertex"],
            vertex_label_size=10.0,
            vertex_label_color="#0f0"
            # edge_width=[2 if married else 1 for married in g.es["married"]],
            # edge_color=["#7142cf" if married else "#AAA" for married in g.es["married"]]
        )

        plt.show()

    def generateIndividuals(self):
        pass

    def fitness(self):
        pass

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

    def runLoop(self):
        while self.best_fitness < 1:
            pass


def main():
    miner = GraphMiner()
    miner.initGraph("hw3_cost329.txt")
    miner.plot()


main()