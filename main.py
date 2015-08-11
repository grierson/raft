'Parse mup file'
import json

LEAFS = []


class Node:
    'Leaf in Tree'
    def __init__(self, title=None, ideas=None):
        self.title = title

        for key in ideas.keys():
            if 'ideas' in ideas[key]:
                LEAFS.append("{}".format(
                    Node(ideas[key]['title'], ideas[key]['ideas'])))
            else:
                LEAFS.append("{}".format(ideas[key]['title']))

    def __str__(self):
        return self.title


if __name__ == '__main__':
    with open('1MPlayers.mup', 'r') as mindmap:
        root = json.load(mindmap)
        tree = Node(root['title'], root['ideas'])

        print('Goal / Why?: {}\n'.format(root['title']))

        for node in reversed(LEAFS):
            print(node)

        '''
        Example Layout:
        ===

        Goal / Why?: 1M Players

            Actor / Who?: Players
                Impact / How?: Inviting Friends
                    Deliverables / What?:
                        Viral Content
                        Personalisation
                        More Compelling Product
                Impact / How?: Recommending
                    Deliverables / What?:
                        Bookmarking

            Actor / Who?: Internal
                Impact / How?: Organise PR Event
                    Deliverables / What?:
                        Invites
                        Engaging out network
        '''
