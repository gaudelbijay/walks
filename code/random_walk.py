'''Random walk used in DeepWalk Methods'''

import networkx as nx 
import random 

class RandomWalk():
    def __init__(self,graph):
        self.G = graph
    
    def random_walk(self,walk_length,start_node = None):
        if start_node:
            walk = [start_node]
        else:
            walk = [random.choice(list(self.G.nodes()))]
        while len(walk) < walk_length:
            cur = walk[-1]
            cur_nbrs = list(self.G.neighbors(cur))
            if(len(cur_nbrs)>0):
                walk.append(random.choice(cur_nbrs))
            else:
                break 
        return walk 
    
    def random_walk_corpus(self,num_walks=50,walk_length=10):
        walk_corpus = []
        nodes = list(self.G.nodes())
        for _ in range(num_walks):
            random.shuffle(nodes)
            for v in nodes:
                walk_corpus.append(self.random_walk(walk_length=walk_length,start_node=v))
        
        return walk_corpus


def main():
    graph = nx.read_edgelist('../data/Wiki_edgelist.txt',create_using=nx.DiGraph(),nodetype=None,data=[('weight',int)])
    walk = RandomWalk(graph)
    print(walk.random_walk_corpus(num_walks=25,walk_length=12))

if __name__ == '__main__':
    main()