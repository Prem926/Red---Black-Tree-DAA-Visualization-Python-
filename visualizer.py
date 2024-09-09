# visualizer.py

import matplotlib.pyplot as plt
import networkx as nx

class RedBlackTreeVisualizer:
    def __init__(self, tree):
        self.tree = tree
        self.G = nx.DiGraph()
        self.pos = {}
        self.node_colors = {}

    def draw_tree(self):
        self.G.clear()
        self.pos.clear()
        self.node_colors.clear()
        self._add_edges(self.tree.root)
        
        color_list = [self.node_colors[node] for node in self.pos]
        
        plt.figure(figsize=(12, 8))
        nx.draw(self.G, pos=self.pos, with_labels=True, node_color=color_list, 
                edge_color='gray', node_size=2000, font_size=16, font_weight='bold', font_color='white')
        plt.title("Red-Black Tree Visualization")
        plt.show()
        plt.pause(1)  # Pause to create animation effect

    def _add_edges(self, node, pos=None, x=0, y=0, layer=1):
        if pos is None:
            pos = {}
        pos[node.key] = (x, y)
        self.node_colors[node.key] = 'red' if node.color == 'red' else 'black'

        if node.left and node.left != self.tree.NIL:
            self.G.add_edge(node.key, node.left.key)
            l = x - 1 / 2**layer
            self._add_edges(node.left, pos=pos, x=l, y=y-1, layer=layer+1)
        if node.right and node.right != self.tree.NIL:
            self.G.add_edge(node.key, node.right.key)
            r = x + 1 / 2**layer
            self._add_edges(node.right, pos=pos, x=r, y=y-1, layer=layer+1)
        self.pos = pos
