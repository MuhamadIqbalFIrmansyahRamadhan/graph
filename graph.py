# YNKTS
class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertex(self):
        return list(self.gdict.keys())
    
    def getEdges(self):
        edges=[]
        for v in self.gdict:
            for e in self.gdict[v]:
                if {e,v} not in edges:
                    edges.append({e,v})
        return edges
    
    def addVertex(self,v):
        if v not in self.gdict:
            self.gdict[v]=[]

    def addEdge(self,e):
        (v1 , v2) = e
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1]=[v2]
        if v2 in self.gdict:
            self.gdict[v2].append(v1)
        else:
            self.gdict[v2]=[v1]

#graph={"a":["b","c"],"b":["a","d"],"c":["a","d"],"d":["e"],"e":["d"]}
graph5 = { "F" : ["G","H"],
          "G" : ["F","I"],
          "H" : ["F","I"],
          "I" : ["J"],
          "J" : ["I"]
        }
g = graph (graph5)
print("awal",g.getVertex())
print("awal",g.getEdges())
g.addVertex("K")
print("tambah",g.getVertex())
g.addEdge({"K","G"})
print("tambah",g.getEdges())
g.addEdge({"K","N"})
print("tambah ke-2",g.getVertex())
print("tambah ke-2",g.getEdges())

print("Oleh Muhamad Iqbal Firmansyah Ramadhan")
