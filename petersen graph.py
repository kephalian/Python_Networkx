"""Drawing graphs
NetworkX is not primarily a graph drawing package but basic drawing with Matplotlib as well as an interface to use the open source Graphviz software package are included. These are part of the networkx.drawing module and will be imported if possible.
First import Matplotlib’s plot interface (pylab works too) >>> import matplotlib.pyplot as plt To test if the import of nx_pylab was successful draw G using one of
>>> G = nx.petersen_graph() >>> subax1 = plt.subplot(121) >>> nx.draw(G, with_labels=True, font_weight='bold') >>> subax2 = plt.subplot(122) >>> nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight= →
'bold')

"""
from matplotlib import pyplot as plt
import networkx as nx


### FOR PYDRIOD ANDROID UNCOMMENT
#import os
#os.chdir('/storage/emulated/0')

plt.tight_layout()


G = nx.petersen_graph() 
subax1 = plt.subplot(121) 

nx.draw(G,  with_labels=True,  font_weight='bold')


subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight= 'bold')

#er =  nx.random_lobster(10, 0.2, 0.9)

#nx.erdos_renyi_graph(10, 0.75) 
#nx.draw_networkx(er)
#arrows=True)


# tell matplotlib you're done with the plot: https://stackoverflow.com/questions/741877/how-do-i-tell-matplotlib-that-i-am-done-with-a-plot
#plt.clf()
plt.title("Petersen Graph")
#plt.legend()
plt.savefig("Petersen.svg", dpi=300)
plt.show()
	
