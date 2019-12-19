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
        for node in G.nodes():
            unnormalized_probability = [G[node][nbrs].get('weight',1.0) for nbrs in G.neighbors(node)]
            norm_const = sum(unnormalized_probability)
            normalized_probability = [float(up)/norm_const for up in unnormalized_probability]
            alias_node[node] = create_alias_table(normalized_probability)

        alias_edge = {}
        for edge in G.edges():
            print(edge)
            alias_edge[edge] = self.get_alias_edge(edge[0],edge[1])
        
        self.alias_node = alias_node
        self.alias_edge = alias_edge

    def get_alias_edge(self,u,v):
        G = self.G 
        p = self.p 
        q = self.q 

        unnormalized_probability = []
        for x in G.neighbors(v):
            weight = G[v][x].get('weight',1.0)
            if x == u:
                unnormalized_probability.append(weight/p)
            elif G.has_edge(x,u):
                unnormalized_probability.append(weight)
            else:
                unnormalized_probability.append(weight/q)
            norm_const = sum(unnormalized_probability)
            normalized_probability = [float(up)/norm_const for up in unnormalized_probability]

            return create_alias_table(normalized_probability)

    def node2vec_walk(self,walk_length,start_node):
        
            
def create_alias_table(area_ratio):
    N = len(area_ratio)
    accept,alias = [0]*N,[0]*N
    small,large = [],[]
    for i,val in enumerate(area_ratio):
        if val>1:
            large.append(i)
        else: small.append(i)
    while large and small:
        large_idx,small_idx = large.pop(),small.pop()
        accept[small_idx]=area_ratio[small_idx]
        alias[small_idx]=large_idx
        area_ratio[large_idx] = area_ratio[large_idx] - (1 - area_ratio[small_idx])
        if area_ratio[large_idx]<1.0:
            small.append(large_idx)
        else: large.append(large_idx)
    
    while small:
        small_idx = small.pop()
        accept[small_idx]=1

    while large:
        large_idx = large.pop()
        accept[large_idx]=1
        
    return accept,alias

def alias_sample(accept,alias):
    N = len(accept)
    i = int(np.random.random()*N)
    r = np.random.random()
    if r < accept[i]:
        return i
    else:
        return alias[i]


def main():
    graph = nx.read_edgelist('../data/Wiki_edgelist.txt',create_using=nx.DiGraph(),nodetype=None,data=[('weight',int)])
    brw = BiasedRandomWalk(graph)
    brw.preprocess_transition_probability()


if __name__ == '__main__':
    main()
