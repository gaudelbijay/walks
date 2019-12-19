'''Random walk used in node2vec papers'''
import random 
import networkx as nx 

class BiasedRandomWalk:
    def __init__(self,graph,p=1,q=1):
        self.G = graph 
        self.p = p 
        self.q = q 
    
    def preprocess_transition_probability(self):
        G = self.G
        alias_node = {}
        




def main():
    graph = nx.read_edgelist('../data/Wiki_edgelist.txt',create_using=nx.DiGraph(),nodetype=None,data=[('weight',int)])

if __name__ == '__main__':
    main()
