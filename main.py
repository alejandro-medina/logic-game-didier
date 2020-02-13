counter = 1
direction = 1
i = 1
while (i <= 10 and counter <= 100):

	# print(f"i equals {i}")
	# print(f"Player #{i}")

	# print(f"direction is {direction}")

	if(i%11 != 0):
		print(f"Player {i} says {counter}")

	if(counter%7 == 0):
		print("======== S W A P ==========")
		direction = direction*(-1)
	
	if (counter%11 == 0):
		print("======== S K I P ==========")
		i = i + 2*direction
		if(i > 10):
			i = i - 10
		elif(i<1):
			i = i + 10

	if (i == 10 and direction == 1):
		i = 1
	elif (i == 1 and direction == -1):
		i = 10


	# print(f"Counter is on {counter}")
	counter = counter + 1

	if(direction == 1):
		i = i + 1
	elif(direction == -1):
		i = i - 1
	else:
		print("Error, i is not either 1 or -1")
	

	

