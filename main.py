'Parse mup file'
import json

LEAFS = []


class Node:
    'Leaf in Tree'
    def __init__(self, title=None, ideas=None):
        self.title = title

        if ideas:
            for key in ideas.keys():
                if 'ideas' in ideas[key]:
                    LEAFS.append("{}".format(
                        Node(ideas[key]['title'], ideas[key]['ideas'])))
                else:
                    LEAFS.append("\t{}".format(ideas[key]['title']))

    def __str__(self):
        return self.title


if __name__ == '__main__':
    with open('1MPlayers.mup', 'r') as mindmap:
        root = json.load(mindmap)

        tree = Node(root['title'], root['ideas'])
        for leaf in reversed(LEAFS):
            print(leaf)
