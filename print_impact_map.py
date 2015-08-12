#!/usr/bin/python3
'''
Parse mup file

Usage:
    print_impact_map.py (-f | --file <file>)
    print_impact_map.py -h | --help

Options:
    -h --help   Show this screen.
    -f --file   File to read potential
'''
import json
from termcolor import colored
import os.path
from docopt import docopt


def print_impact_map(impact_map=None):
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
    def node(ideas=None, indent=0):
        'Print Tree'
        for key in sorted(ideas.keys()):
            if indent == 0:
                style = colored('\nActor / Who?: ', 'cyan')
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
                print('{}{}{}'.format('\t' * indent,
                                      style,
                                      ideas[key]['title']))
                node(ideas[key]['ideas'], indent+1)
            else:
                print('{}{}{}'.format('\t' * indent,
                                      style,
                                      ideas[key]['title']))

    with open(impact_map, 'r') as mindmap:
        root = json.load(mindmap)
        print(colored('Goal / Why?: ', 'blue') + '{}'.format(root['title']))
        node(root['ideas'], 0)


def main():
    'main'
    args = docopt(__doc__, version='1')
    if os.path.isfile(args['<file>']) and args['<file>'].endswith('.mup'):
        print_impact_map(args['<file>'])
    else:
        print('Error: Not .mup file')


if __name__ == '__main__':
    main()
else:
    main()
