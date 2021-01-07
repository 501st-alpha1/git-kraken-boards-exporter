#!/usr/bin/python

import os
import jsonpickle
from py_glo_boards_api import GloBoard, types

token = os.environ['GIT_KRAKEN_PERSONAL_TOKEN']

globoard = GloBoard(token)

boards = globoard.get_boards()
with open('boards.json', 'w') as file:
  file.write(jsonpickle.encode(boards, unpicklable=False))
