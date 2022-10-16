
raceV = ["300 ft", "1/8 mile", "1000 ft", "1/4 mile", "2000 ft", "1/2 mile", "1 mile"]

raceQ = [91.44, 201.168, 304.80, 402.366, 609.6, 804.672, 1609.34]

print(" ")
print("*****************************************************")
print("TEST YOUR RIDE / DRAG METRICS FOR PREMIUM AUTOMOBILES")
print("*****************************************************")

print(" ")

print(r"""               ____----------- _____
\~~~~~~~~~~/~_--~~~------~~~~~     \
 `---`\  _-~      |                   \
   _-~  <_         |                     \[]
 / ___     ~~--[""] |      ________-------'_
> /~` \    |-.   `\~~.~~~~~                _ ~ - _
 ~|  ||\%  |       |    ~  ._                ~ _   ~ ._
   `_//|_%  \      |          ~  .              ~-_   /\
          `--__     |    _-____  /\               ~-_ \/.
               ~--_ /  ,/ -~-_ \ \/          _______---~/
                   ~~-/._<   \ \`~~~~~~~~~~~~~     ##--~/
                         \    ) |`------##---~~~~-~  ) )
                          ~-_/_/                  ~~ ~~) """)

print(" ")
print("*****************************************************")
print("DISCLAIMER: Drag racing should only be performed at a")
print("designated racing track with professional supervision")
print("*****************************************************")

def races():
	print(" ")
	print("Which race would you like metrics for?")
	print(" ")
	cursor = 1
	for i in raceV:
		print(str(cursor) + ". " + i)
		cursor = cursor + 1
	print(" ")
	choice = int(input("#: "))

	print(" ")
	zeroToSixty = float(input("0mph to 60mph: "))
	ztsim = (60*1609.34)/3600
	print(" ")
	topSpeed  = float(input("Top Speed in mph: "))
	print(" ")
	a = ztsim/zeroToSixty
	tsim = (topSpeed*1609.34)/3600
	print("Top Speed in m: " + str(tsim))
	print(" ")
	ttts = tsim/a
	print("Time to Top Speed: " + str(ttts) + "s")


	time1 = 0
	time2 = 0
	ii = 1

	print(" ")

	dtts = (a*(ttts**2))/2
	print("Distance to Top Speed: " + str(dtts) + "m")
	print(" ")
	print("Acceleration: " + str(a) + "mps")
	print(" ")
	time = ((2*raceQ[choice-1])/a)**.5
	if time==ttts:
		time = ((2*dtts)/a)**.5
		time = time+(raceQ[choice-1]-dtts)/tsim
	print("Finish: " + str(time))
	print(" ")
	print("Would you like a second by second breakdown of your race?")
	print(" ")
	choice1 = str(raw_input("'Y' or 'N': "))
	print(" ")
	choice1 = choice1.upper()

	if choice1 == "Y":
		while ii < time:
			part1 = (.5*a)*(ii**2)
			if ii<ttts:
				print("Len  @ " + str(ii) + "s: " + str(part1) + "m")
				print("%    @ " + str(ii) + "s: " + str(((part1)/raceQ[choice-1])*100) + "%")
				print("Mph  @ " + str(ii) + "s: " + str(((a*ii)/1609.34)*3600) + "mph")
			else:
				print("Len  @ " + str(ii) + "s: " + str((tsim*(ii))-dtts) + "m")
				print("%    @ " + str(ii) + "s: " + str((((tsim*(ii))-dtts))/(raceQ[choice-1])*100) + "%")
				print("Mph  @ " + str(ii) + "s: " + str(topSpeed) + "mph")
			ii = ii+1
			print(" ")
		print("Lap Finish: " + str(time) + "s")
		print(" ")
		print("Would you like to check metrics for a different race?")
		print(" ")
		choice2 = str(raw_input("'Y' or 'N': "))
		print(" ")
		choice2 = choice2.upper()
		if choice2 == "Y":
			races();
		else:
			exit();
	else:
		exit()

races();

