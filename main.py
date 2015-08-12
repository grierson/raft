'Parse mup file'
import json
from termcolor import colored


def read(impact_map=None):
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
    tree = []

    class Node:
        'Node in Tree'
        def __init__(self, title=None, ideas=None, indent=0):
            self.title = title

            for key in ideas.keys():
                if indent == 0:
                    style = colored('Actor / Who?: ', 'cyan')
                elif indent == 1:
                    style = colored('Impact / What?: ', 'green')
                elif indent == 2:
                    style = colored('Deliverable / How?: ', 'blue')
                elif indent == 3:
                    style = colored('Feature: ', 'magenta')
                elif indent == 4:
                    style = colored('User Story: ', 'yellow')
                elif indent == 5:
                    style = colored('Example: ', 'white')

                if 'ideas' in ideas[key]:
                    tree.append('{}{}{}'.format('\t' * indent,
                                                style,
                                                Node(ideas[key]['title'],
                                                     ideas[key]['ideas'],
                                                     indent+1)))
                else:
                    tree.append('{}{}{}'.format('\t' * indent,
                                                style,
                                                ideas[key]['title']))

        def __str__(self):
            return self.title

        def __repr__(self):
            return self.title

    with open(impact_map, 'r') as mindmap:
        root = json.load(mindmap)
        Node(root['title'], root['ideas'], 0)

        print(colored('Goal / Why?: ', 'blue') + '{}\n'.format(root['title']))

        for node in reversed(tree):
            print(node)


def main():
    'main'
    read('1MPlayers.mup')


if __name__ == '__main__':
    main()
