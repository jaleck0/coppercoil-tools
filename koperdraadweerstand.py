import math

copperresistance = 0.0000000175

while True:

	diameter = 0
	length = 0
	
	while True:
		try:
			diameter = float(input('Enter diameter of given wire in mm: '))
			break
		except:
			print("Enter a valid number.")
			continue
	while True:
		try:
			length = float(input('Enter length of given wire in m: '))
			break
		except:
			print("Enter a valid number.")
			continue
	

	radius = (diameter / 2000)

	surface = ((radius * radius) * math.pi)

	resistance = ((copperresistance * length) / surface)

	print('resistance = ' + str(resistance) + ' Ω\n')
