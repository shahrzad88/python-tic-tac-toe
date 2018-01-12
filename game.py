import sys
import copy

class Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.positions = [[' ' for i in range(width)] for j in range(height)]
    self.turn = None
  
  def is_empty(self):
    sum = 0
    for i in range(width):
      for j in range(height):
        if self.positions[i][j] == 'X' or self.positions[i][j] == 'O':
          sum += 1
    if sum == 0:
      return True
    else:
      return False

  def is_full(self):
    sum = 0
    for i in range(self.width):
      for j in range(self.height):
        if self.positions[i][j] == 'X' or self.positions[i][j] == 'O':
          sum += 1
    if sum == self.width * self.height:
      return True
    else:
      return False

  def get_cell_value(self, x, y):
    return self.positions[x][y]

  def is_horizontal_row(self, x, y):
    cell_value = self.positions[x][y]
    sum = 0
    for j in range(self.height):
      if self.positions[x][j] == cell_value:
        sum += 1
    return sum == 3

  def is_vertical_row(self, x, y):
    cell_value = self.positions[x][y]
    sum = 0
    for i in range(self.width):
      if self.positions[x][y] == cell_value:
        sum += 1
    return sum == 3

  def is_diagonal_row(self, x, y):
    cell_value = self.positions[x][y]
    sum = 0
    if 


  def update(self, position):
    temp_positions = position.split(',')
    position_x = int(temp_positions[0])
    position_y = int(temp_positions[1])
    self.positions[position_x][position_y] = self.turn
  
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
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol
    self.points = 0
    self.turn = False

  def increase_points(self):
    self.points += 1

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

def ask_move(player_x, player_o, turn):
  prop_player_x = copy.deepcopy(player_x)
  prop_player_o = copy.deepcopy(player_o)
  prop_turn = copy.copy(turn)
  position = None
  if turn == 'X':
    position = input(player_x.name + ', what is your move? ')
  else:
    position = input(player_o.name + ', what is your move? ')
  try:
    test_position = position.replace(",", "").replace(" ", "")
    if test_position.isdigit() is False:
      print ('Invalid input!')
      ask_move(prop_player_x, prop_player_o, prop_turn)
  except Exception as e:
    print (e)
    ask_move(prop_player_x, prop_player_o, prop_turn)
  return position

def main():
  player_x = None
  player_o = None
  turn = None
  #temp_dimensions = input('Enter board dimensions: ').split(',')
  width = 3 #int(temp_dimensions[0])
  height = 3 # int(temp_dimensions[1])
  board = Board(width, height)
  player_x = Player('k', 'X') #input('X player, What is your name? '), 'X')
  player_o = Player('s', 'O') #input('O player, What is your name? '), 'O')
  board.turn = check_first_player()
  while board.is_full() == False:
    position = ask_move(player_x, player_o, board.turn)
    board.update(position)
    board.draw()
    board.change_turn()

if __name__ == "__main__":
  main()
