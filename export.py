#!/usr/bin/python

import os
import jsonpickle
from py_glo_boards_api import GloBoard, types

token = os.environ['GIT_KRAKEN_PERSONAL_TOKEN']

globoard = GloBoard(token)

# TODO: get archived boards
# TODO: handle more than one page (default page of 50 boards)
board_fields = ['archived_columns', 'archived_date', 'columns', 'created_by',
                'created_date', 'invited_members', 'labels', 'members', 'name',
                'milestones']
boards = globoard.get_boards(board_fields)
with open('boards.json', 'w') as file:
  file.write(jsonpickle.encode(boards, unpicklable=False))
