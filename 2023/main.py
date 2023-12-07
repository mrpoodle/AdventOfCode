import click

def day01_1(input_file):
	lines = [line.strip("\n") for line in open(input_file)]
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

def day01_2(input_file):
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
	lines = [line.strip("\n") for line in open(input_file)]
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

def day02_1(input_file):
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
	lines = [line.strip("\n") for line in open(input_file)]
	for line in lines:
		id, turns = line.removeprefix("Game ").split(":")
		out += int(id) if test_game(turns) else 0
	return out


def day02_2(input_file):

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
	lines = [line.strip("\n") for line in open(input_file)]
	for line in lines:
		id, turns = line.removeprefix("Game ").split(":")
		out += test_game(turns)
	return out


def day03_1(input_file):
	"""every number adjacent to a symbol in the matrix should be added to the sum"""
	lines = [line.strip("\n") for line in open(input_file)]

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


def day03_2(input_file):
	"""only two numbers ajacent to a * should be multiplied and added to the sum"""
	lines = [line.strip("\n") for line in open(input_file)]
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

def day04_1(input_file):
	lines = [[set([int(number)
			for number in numbers.split()])
				for numbers in line.strip("\n").split(":")[1].strip(" ").split(" | ")]
					for line in open(input_file)]
	out = 0
	for line in lines:
		points = 2**(len(line[0] & line[1])-1)
		if points >= 1:
			out += points
	return out

def day04_2(input_file):
	lines = [[set([int(number)
			for number in numbers.split()])
				for numbers in line.strip("\n").split(":")[1].strip(" ").split(" | ")]
					for line in open(input_file)]

	cards = [1 for x in lines]
	print(cards)
	for i, line in enumerate(lines):
		points = len(line[0] & line[1])
		for x in range(points):
			try:
				cards[i+x+1] += cards[i]
			except IndexError:
				pass
	print(cards)
	out = sum(cards)
	return out

### for day 5
def find_location(seed, maps):
	for step in maps:
		seed = find_next(seed, step)
	return seed

def find_next(seed, step):
	for my_map in step:
		if seed >= my_map[1] and seed < my_map[1]+my_map[2]:
			seed = my_map[0] + (seed - my_map[1])
			return seed
	return seed

def day05_1(input_file):
	chunks = "\n".join([line.strip("\n") for line in open(input_file)])
	maps = []
	minimum = []
	maximum = []
	for chunk in chunks.split("\n\n"):
		if chunk.startswith("seeds:"):
			seeds = [int(seed) for seed in chunk.removeprefix("seeds: ").split(" ")]
			continue
		my_map = chunk.split("\n")
		maps.append([[int(num) for num in string.split()] for string in my_map[1:]])

	out = None
	for seed in seeds:
		seed=find_location(seed, maps)
		if out == None or seed < out:
			out = seed
	return out

def day05_2(input_file):
	chunks = "\n".join([line.strip("\n") for line in open(input_file)])
	maps = []
	length = 0
	maximum = 0
	for chunk in chunks.split("\n\n"):
		if chunk.startswith("seeds:"):
			seeds=[]
			numbers = [int(x) for x in chunk.removeprefix("seeds: ").split(" ")]
			for first, second in zip(numbers[::2], numbers[1::2]):
				seeds.append(range(first, first+second))
				if first+second>maximum:
					maximum=first+second
				length+=second
			continue
		my_map = chunk.split("\n")
		maps.append([[int(num) for num in string.split()] for string in my_map[1:]])

	out = None
	counter = 0

	for seed_range in seeds:
		for seed in seed_range:
			seed=find_location(seed, maps)
			if out == None or seed < out:
				out = seed
			counter += 1
			print(counter/length*100, "%    ", out, " "*30, end="\r")
			
	#print(maximum)
	#for seed_range in [range(maximum)]:
	#	for seed in seed_range:
	#		seed=find_location(seed, maps)
	#		if out == None or seed < out:
	#			out = seed
	#		counter += 1
	#		print(counter/maximum*100, "%    ", out, " "*30, end="\r")
			
	print()
	return out

def day06_1(input_file):
	lines = [line.strip("\n") for line in open(input_file)]
	time_dist = zip(
		[int(number) for number in lines[0].split()[1:]], 
		[int(number) for number in lines[1].split()[1:]]
	)
	score = 1
	for round in time_dist:
		wins = 0
		for i in range(round[0]):
			travelled = i*(round[0]-i)
			if travelled > round[1]:
				wins += 1
		score *= wins
	out = score
	return out

def day06_2(input_file):
	lines = [line.strip("\n") for line in open(input_file)]
	time = int("".join([number for number in lines[0].split()[1:]]))
	dist = int("".join([number for number in lines[1].split()[1:]]))

	step = time/2
	pointer = step

	while True:
		travelled = pointer*(time-pointer)
		if travelled > dist:
			if step < 1:
				lower=int(pointer+1)
				break
			pointer -= step/2
		else:
			pointer += step/2
		step /= 2

	step = time/2
	pointer = step
	while True:
		travelled = pointer*(time-pointer)
		if travelled < dist:
			if step < 1:
				upper=int(pointer)
				break
			pointer -= step/2
		else:
			pointer += step/2
		step /= 2

	print()
	print(lower, upper)
	out = upper-(lower-1)
	return out

def day07_1(input_file):
	lines = [line.strip("\n").split(" ") for line in open(input_file)]
	def get_hand_value(hand):
		"""returns the value of a hand"""
		# 5	of	a	Kind
		if len(set(hand)) == 1:
			value='G'
		# four of a kind
		elif len(set(hand)) == 2:
			if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
				value='F'
			# full house
			else:
				value='E'
		# 3 of a kind
		elif len(set(hand)) == 3:
			if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
				value='D'
			# 2 pairs
			else:
				value='C'
		# 1 pair
		elif len(set(hand)) == 4:
			value='B'
		# high card
		else:
			value='A'

		# values for cards in order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
		card_values = {
			'2': 'a',
			'3': 'b',
			'4': 'c',
			'5': 'd',
			'6': 'e',
			'7': 'f',
			'8': 'g',
			'9': 'h',
			'T': 'i',
			'J': 'j',
			'Q': 'k',
			'K': 'l',
			'A': 'm'
		}
		for card in hand:
			value += card_values[card]
		
		return value

	lines = sorted(lines, key=lambda x: get_hand_value(x[0]))
	
	out = 0
	multiplyer = 1
	for line in lines:
		#print(multiplyer, "*", int(line[1]))
		out += multiplyer * int(line[1])
		multiplyer += 1
	return out

def day07_2(input_file):
	lines = [line.strip("\n").split(" ") for line in open(input_file)]
	def get_hand_value(hand):
		"""returns the value of a hand"""
		# 5	of	a	Kind
		if len(set(hand)) == 1 or (len(set(hand)) == 2 and "J" in hand):
			value='G'
		# four of a kind
		elif len(set(hand)) == 2 or (len(set(hand)) == 3 and "J" in hand):
			sub_set = list(set(filter(lambda a: a != "J", hand)))
			jokers = hand.count("J")
			
			if hand.count(sub_set[0])+jokers == 4 or hand.count(sub_set[1])+jokers == 4:
				value='F'
			# full house
			else:
				value='E'
		# 3 of a kind
		elif len(set(hand)) == 3 or (len(set(hand)) == 4 and "J" in hand):
			sub_set = list(set(filter(lambda a: a != "J", hand)))
			jokers = hand.count("J")
			
			if hand.count(sub_set[0])+jokers == 3 or hand.count(sub_set[1])+jokers == 3 or hand.count(sub_set[2])+jokers == 3:
				value='D'
			# 2 pairs
			else:
				value='C'
		# 1 pair
		elif len(set(hand)) == 4 or (len(set(hand)) == 5 and "J" in hand):
			value='B'
		# high card
		else:
			value='A'

		# values for cards in order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
		card_values = {
			'2': 'b',
			'3': 'c',
			'4': 'd',
			'5': 'e',
			'6': 'f',
			'7': 'g',
			'8': 'h',
			'9': 'i',
			'T': 'j',
			'J': 'a',
			'Q': 'k',
			'K': 'l',
			'A': 'm'
		}
		for card in hand:
			value += card_values[card]
		
		return value

	lines = sorted(lines, key=lambda x: get_hand_value(x[0]))
	
	out = 0
	multiplyer = 1
	for line in lines:
		#print(multiplyer, "*", int(line[1]))
		out += multiplyer * int(line[1])
		multiplyer += 1
	return out

def get_function_name(day_number, part):
	return f"day{day_number:02d}_{part}"

@click.command()
@click.argument('day_number', type=int)
@click.argument('part', type=int)
@click.argument('input_type', required=False, default='input', type=click.Choice(['input', 'test']))
def main(day_number, part, input_type):
	function_name = get_function_name(day_number, part)
	function = globals().get(function_name)
	if function:
		input_file = f"day{day_number:02d}.tst" if input_type=="test" else f"day{day_number:02d}.txt"
		print(f"Running day{day_number:02d}_{part} with input file: {input_file}")
		print("Output:", function(input_file))


if __name__ == '__main__':
    main()

