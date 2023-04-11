import math

copperdensity = 8960

while True:

	diameter = 0
	mass = 0
	
	while True:
		try:
			diameter = float(input('Enter diameter of given wire in mm: '))
			break
		except:
			print("Enter a valid number.")
			continue
	while True:
		try:
			mass = float(input('Enter mass of given wire in g: '))
			break
		except:
			print("Enter a valid number.")
			continue
	
	masskg = (mass / 1000)

	radius = (diameter / 2000)

	surface = ((radius * radius) * math.pi)

	volume = (masskg / copperdensity)

	length = (volume / surface)

	print('mass = ' + str(length) + ' m\n')
