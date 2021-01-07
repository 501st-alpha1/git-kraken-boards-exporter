#!/usr/bin/python

import os
from py_glo_boards_api import GloBoard, types

token = os.environ['GIT_KRAKEN_PERSONAL_TOKEN']

globoard = GloBoard(token)
