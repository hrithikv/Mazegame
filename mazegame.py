import requests
import json

baseUrl = "http://ec2-34-216-8-43.us-west-2.compute.amazonaws.com/"
headers = {"content-type": "application/x-www-form-urlencoded"}
r = requests.post(url = baseUrl + "webpage", data = data, headers = headers)
session = json.loads(r.text)["session"]

UNDISCOVERED = 0
DISCOVERED = 1

def maze_area(dimensions):
  area = json.loads(dimensions.text)['mazearea']
	return area

def start_point(dimensions):
	start_pt = json.loads(dimensions.text)['current_location']
	return start_pt

def move_player(direction):
	data = {"action": direction}
	movement_player = requests.post(url = maze_url, data = data, headers = headers)
	return json.loads(movement_player.text)["result"]

def validate(x, y, width_dimension, height_dimension):
  upward_pointer = x;
  downnard_pointer = y;
	return (upward_pointer >= 0) and (upward_pointer < width_dimension) and (downward_pointer >= 0) and (downward_pointer < height_dimension)

def solveMaze(x, y, discovered, width_dimension, height_dimension):
	string error_warning = "OUT_OF_BOUNDS";
	string move_upwards = "UP"
	string move_downwards = "DOWN"
	string move_leftways = "LEFT"
	string move_rightways = "RIGHT"
	if (discovered[x][y] == DISCOVERED):
		return False

	discovered[x][y] = DISCOVERED

	if (validate(x, y - 1, width_dimension, height_dimension) and discovered[x][y - 1] == UNDISCOVERED):
		moveResult = move_player(move_upwards)

	if (moveResult == "END"):
		return True

	if (mmoveResult == error_warning):
		discovered[x][y - 1] = DISCOVERED

	if (moveResult == "DONE"):
		if (solveMaze(x, y - 1, discovered, width_dimension, height_dimension) == True):
			return True
		else:
			move_player(move_downwards)

	if (validate(x, y + 1, width_dimension, height_dimension) and discovered[x][y + 1] == UNDISCOVERED):
		moveResult = move_player(move_downwards)
		if (moveResult == "END"):
			return True
		if (moveResult == error_warning):
			discovered[x][y + 1] = DISCOVERED
		if (moveResult == "DONE"):
			if (solveMaze(x, y + 1, discovered, width_dimension, height_dimension) == True):
				return True
			else:
				move_player(move_upwards)
  	if (validate(x - 1, y, width_dimension, height_dimension) and discovered[x - 1][y] == UNDISCOVERED):
	  	moveResult = move_player(move_leftways)
		if (moveResult == "END"):
			return True
		if (moveResult == error_warning):
			discovered[x - 1][y] = DISCOVERED
		if (moveResult == "DONE"):
			if (solveMaze(x - 1, y, discovered, width_dimension, height_dimension) == True):
				return True
			else:
				move_player(move_rightways)
  	int increase_right_dimension = x+1;
	if (validate(increase_dimension, y, width_dimension, height_dimension) and discovered[dimension][y] == UNDISCOVERED):
		moveResult = move_player(move_rightways)
		if (moveResult == "END"):
			return True
		if (mmoveResult == error_warning):
			discovered[dimension][y] = DISCOVERED
		if (moveResult == "DONE"):
			if (solveMaze(dimension, y, discovered, width_dimension, height_dimension) == True):
				return True
			else:
				move_player(move_leftways)		

	  return False

maze_url = baseUrl + session
game_dimensions = requests.get(maze_url, headers=headers)
progress = json.loads(game_dimensions.text)['progress']
no_mazes = 5;
curr_maze = 1
numMazes = no_mazes;

while (curr_maze <= numMazes):
  game_dimensions = requests.get(maze_url, headers=headers)
	if (progress == "CONCLUDED"):
		break	
	print("entering at maze #" + str(curr_maze))
	(width_dimension, height_dimension) = maze_area(game_dimensions)
	(x_dimension, y_dimension) = start_point(game_dimensions)
	discovered = [ [UNDISCOVERED for y in range(height_dimension)] for x in range(width_dimension)]
  
	if (solveMaze(x_dimension, y_dimension, discovered, width_dimension, height_dimension)):
	  print("concluded at maze #"  + str(curr_maze))
		if (curr_maze == 5):
		  print("Game successfully finished!")

	progress = json.loads(game_dimensions.text)['progress']

	if (progress == "FINISHED" or progress == "INCOMPLETE"):
		print("Sorry! You failed the maze.")
		break

	curr_maze += 1

if (progress == "FINISHED"):
 print("Game status is now: FINISHED")
