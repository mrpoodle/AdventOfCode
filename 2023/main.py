
def day01_1():
	lines = [line.strip("\n") for line in open("day01.txt")]
	out = 0
	for l in lines:
		first = None
		last = None
		for x in l:
			if x.isdigit():
				last = x
				if first:
					continue
				first=x
		out += int(first+last)
	return out

def day01_2():
	numbers = {
		"one": "one1one",
		"two": "two2two",
		"three": "three3three",
		"four": "four4four",
		"five": "five5five",
		"six": "six6six",
		"seven": "seven7seven",
		"eight": "eight8eight",
		"nine": "nine9nine"
	}
	lines = [line.strip("\n") for line in open("day01.txt")]
	out = 0
	for l in lines:
		first = None
		last = None
		for x in numbers:
			l = l.replace(x, numbers[x])
		for x in l:
			if x.isdigit():
				last = x
				if first:
					continue
				first=x
		out += int(first+last)
	return out

def day02_1():
	balls = {
		"red": 12,
		"green": 13,
		"blue": 14,
	}

	def test_game(turns):
		for turn in turns.split(";"):
			ball_set = {
				pair.strip().split(" ")[1]:int(pair.strip().split(" ")[0])
				for pair in turn.strip(" ").split(",")
			}
			for color in ball_set:
				if ball_set[color] > balls[color]:
					return False
		return True

	out = 0
	lines = [line.strip("\n") for line in open("day02.txt")]
	for line in lines:
		id, turns = line.removeprefix("Game ").split(":")
		out += int(id) if test_game(turns) else 0
	return out


def day02_2():

	def test_game(turns):
		balls = {
			"red": 0,
			"green": 0,
			"blue": 0,
		}
		for turn in turns.split(";"):
			ball_set = {
				pair.strip().split(" ")[1]:int(pair.strip().split(" ")[0])
				for pair in turn.strip(" ").split(",")
			}
			for color in ball_set:
				if ball_set[color] > balls[color]:
					balls[color] = ball_set[color]
		return balls["red"]*balls["green"]*balls["blue"]

	out = 0
	lines = [line.strip("\n") for line in open("day02.txt")]
	for line in lines:
		id, turns = line.removeprefix("Game ").split(":")
		out += test_game(turns)
	return out


def day03_1():
	"""every number adjacent to a symbol in the matrix should be added to the sum"""
	lines = [line.strip("\n") for line in open("day03.txt")]

	def check_sourrounding(x, y):
		length = 1
		while lines[x][y+length].isdigit(): #(y+length>len(lines[x])-1) and 
			length += 1
			if y+length>len(lines[x])-1:
				break
		number = int(lines[x][y:y+length])
		for i in range(-1, 2):
			for j in range(-1, 1+length):
				if y+j<0 or y+j>len(lines[x])-1 or x+i<0 or x+i>len(lines)-1:
					continue
				if lines[x+i][y+j] not in "1234567890.":
					return(True, length, number)

		return(False, length, number)

	length = 1
	out = 0
	for x, l in enumerate(lines):
		for y,char in enumerate(l):
			if length > 1:
				length -= 1
				continue
			if char.isdigit():
				check,length, number = check_sourrounding(x, y)
				if check:
					print(number)
					out += number
	return out


def day03_2():
	"""only two numbers ajacent to a * should be multiplied and added to the sum"""
	lines = [line.strip("\n") for line in open("day03.txt")]
	out = 0

	def find_number(x, y):
		visited = [(x, y)]
		left = 0
		right = 0

		while lines[x][y+left-1].isdigit():
			left -= 1
			visited.append((x, y+left))
		while lines[x][y+right+1].isdigit():
			right += 1
			visited.append((x, y+right))
		number = int(lines[x][y+left:y+right+1])
		return number, visited

	def check_sourrounding(x, y):
		visited = []
		numbers = []
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if (i,j) in visited:
					continue
				if j<0 or j>len(lines[x])-1 or i<0 or i>len(lines)-1:
					continue
				if lines[i][j].isdigit():
					number, just_visited = find_number(i, j)
					visited += just_visited
					numbers.append(number)
		# print(numbers)
		if len(numbers) == 2:
			print(x, y)
			print(numbers[0], "*", numbers[1])
			return(numbers[0]*numbers[1])
		return(0)

	for x, l in enumerate(lines):
		for y,char in enumerate(l):
			if char=="*":
				check = check_sourrounding(x, y)
				# print(check)
				out += check

	return out


print(day02_2())
