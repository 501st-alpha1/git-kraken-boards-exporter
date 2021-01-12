#!/usr/bin/python

import os
import jsonpickle
from py_glo_boards_api import GloBoard, types

token = os.environ['GIT_KRAKEN_PERSONAL_TOKEN']

globoard = GloBoard(token)

# TODO: get archived boards
# TODO: handle more than one page (default page of 50 boards)
# These fields are the same for the `/boards/{board_id}` endpoint, so no need
# to fetch each one individually.
board_fields = ['archived_columns', 'archived_date', 'columns', 'created_by',
                'created_date', 'invited_members', 'labels', 'members', 'name',
                'milestones']
boards = globoard.get_boards(board_fields)
with open('boards.json', 'w') as file:
  file.write(jsonpickle.encode(boards, unpicklable=False))

card_fields = ['board_id', 'column_id', 'name', 'updated_date', 'is_divider']
single_card_fields = [
  'archived_date', 'assignees', 'attachment_count', 'board_id', 'column_id',
  'comment_count', 'completed_task_count', 'created_by', 'created_date',
  'due_date', 'description', 'labels', 'name', 'total_task_count',
  'updated_date', 'milestone', 'reactions', 'reactions.reacted', 'is_divider'
]
comment_fields = [
  'board_id', 'card_id', 'created_date', 'created_by', 'updated_by',
  'updated_date', 'text', 'reactions', 'reactions.reacted'
]
for board in boards:
  # First see what cards are available, then later fetch the card details.
  # TODO: get archived cards
  # TODO: handle more than one page (default page of 50 cards)
  cards = globoard.get_cards(board.id, card_fields)
  filename = 'cards_for_board_' + board.id + '.cache.json'
  with open(filename, 'w') as file:
    file.write(jsonpickle.encode(cards, unpicklable=False))

  for card in cards:
    # Have to fetch each card individually to get reactions.
    # (Cards by column has reactions but not milestone.)
    # TODO: check local updated_at and skip unless newer.
    card = globoard.get_card(board.id, card.id, single_card_fields)
    filename = 'card_' + card.id + '.json'
    with open(filename, 'w') as file:
      file.write(jsonpickle.encode(card, unpicklable=False))

    # Skip downloads if no comments.  (Result will be `[]` anyway.)
    if card.comment_count == 0:
      continue

    # TODO: handle more than one page (default page of 50 comments)
    comments = globoard.get_comments(board.id, card.id, comment_fields)
    filename = 'comments_for_card_' + card.id + '.json'
    with open(filename, 'w') as file:
      file.write(jsonpickle.encode(comments, unpicklable=False))
