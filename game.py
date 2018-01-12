import sys
import copy

class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.positions = [[' ' for i in range(width)] for j in range(height)]
    self.turn = None
    self.last_move = None

  def is_empty(self):
    for row in self.positions:
      for cell in row:
        if cell != " ":
          return False
    return True

  def is_full(self):
    for row in self.positions:
      for cell in row:
        if cell == " ":
          return False
    return True

  def is_horizontal_row(self):
    if self.is_empty():
      return False
    sum = 0
    cell_value = self.positions[self.last_move[0]][self.last_move[1]]
    for j in range(self.height):
      if self.positions[self.last_move[0]][j] == cell_value:
        sum += 1
    return sum == 3

  def is_vertical_row(self):
    if self.is_empty():
      return False
    cell_value = self.positions[self.last_move[0]][self.last_move[1]]
    sum = 0
    for i in range(self.width):
      if self.positions[i][self.last_move[1]] == cell_value:
        sum += 1
    return sum == 3

  def is_diagonal_row(self):
    if self.positions[1][1] == " ":
      return False
    return (self.positions[0][0] == self.positions[1][1] == \
      self.positions[2][2]) or (self.positions[0][2] == \
      self.positions[1][1] == self.positions[2][0])

  def is_won(self):
    return self.is_diagonal_row() or self.is_vertical_row() or \
    self.is_horizontal_row()

  def update(self):
    self.positions[self.last_move[0]][self.last_move[1]] = self.turn

  def draw(self):
    for row in self.positions:
      s = ''
      for cell in row:
        s += ' ' + cell + ' '
      print (s)

  def change_turn(self):
    if self.turn == 'O':
      self.turn = 'X'
    else:
      self.turn = 'O'

class Player:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.turn = False

def check_first_player():
  first_player = input('Who is starting the game (X or O)? ').upper().replace(
    " ", "")
  if first_player == 'X':
    turn = 'X'
  elif first_player == 'O':
    turn = 'O'
  else:
    print ('Invalid input!')
    return check_first_player()
  return turn

def ask_move(player_x, player_o, board):
  prop_player_x = copy.deepcopy(player_x)
  prop_player_o = copy.deepcopy(player_o)
  prop_board = copy.deepcopy(board)
  position = None
  if prop_board.turn == 'X':
    position = input(prop_player_x.name + ', what is your move? ')
  else:
    position = input(prop_player_o.name + ', what is your move? ')
  try:
    position = position.replace(",", "").replace(" ", "")
    if position.isdigit() is False:
      print ('Invalid input!')
      return ask_move(prop_player_x, prop_player_o, prop_board)
  except Exception as e:
    print (e)
    return ask_move(prop_player_x, prop_player_o, prop_board)
  position = list(map(int, position))
  if position[0] < 0 or position[1] < 0 or position[1] >= prop_board.height or \
    position[0] >= prop_board.width:
    print ('Input is out of range!')
    return ask_move(prop_player_x, prop_player_o, prop_board)
  if prop_board.positions[position[0]][position[1]] != " ":
    print ('Invalid action!')
    return ask_move(prop_player_x, prop_player_o, prop_board)
  return position

def main():
  player_x = None
  player_o = None
  width = 3
  height = 3
  board = Board(width, height)
  player_x = Player('s')
  player_o = Player('k')
  board.turn = check_first_player()
  while not board.is_won() and not board.is_full():
    board.last_move = ask_move(player_x, player_o, board)
    board.update()
    board.draw()
    board.change_turn()
  if board.is_won():
    if board.turn == 'X':
      print (player_o.name + ' won!')
    else:
      print (player_x.name + ' won!')
  elif board.is_full():
    print ("It's a tie!")

if __name__ == "__main__":
  main()
