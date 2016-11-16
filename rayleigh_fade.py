import os
import sys
import random

def rayleigh_fade(input):
	##Main method in out simple simulator
	##
	## @input - path to file with samples. Assume that every sample in input file is in new line. 
	
	input_data =[]
	print type(input_data)
	file = open(input, 'r')
	for data in file:
		input_data.append(data)
	_random()
	
	

def _random(length):
	##Methods return random set of number. Set size is equal to the quantity of input_data probes.
	rnd = random.SystemRandom()
	random_set = []
	for i in range(length):
		random_set.append(rnd.randint(1,100))
	return random_set


if __name__ == '__main__':
	input_file = sys.argv[1]
	rayleigh_fade(input_file)