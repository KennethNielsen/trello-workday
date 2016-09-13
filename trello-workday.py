#!/usr/bin/env python2

"""Produce a single day burndown from a Trello board"""

# 19:40-20:50

from json import load, dumps
from trello import TrelloClient
from pprint import pprint
import requests

class WorkDay(object):

    def __init__(self, board, auths):
        client = TrelloClient(**auths)
        board = client.get_board(board)
        lists = board.all_lists()
        for list_ in lists:
            print(list_)
            print(list_.list_cards())
        #lists = board.get_list()
        #print(lists)


if __name__ == '__main__':
    auths = load(open('auths.json'))
    WorkDay('3OmA20Pp', auths=auths)
