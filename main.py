# main.py

from red_black_tree import RedBlackTree
from visualizer import RedBlackTreeVisualizer

def main():
    rb_tree = RedBlackTree()
    visualizer = RedBlackTreeVisualizer(rb_tree)

    # Insert nodes and visualize
    for value in [10, 20, 30, 15, 25, 5,9]:
        rb_tree.insert(value)
        visualizer.draw_tree()

if __name__ == "__main__":
    main()
