import rospy

rospy.init_node('sexxxx', anonymous=True, disable_signals = True)

print("ros works lol")

i = 0
j = 0

while not rospy.is_shutdown():
	i+=1
	if i%10000000 == 0:
		print("haha outside")
	try:
		while True:
			j+=1
			if j%10000000 == 0:
				print("haha inside")
	except KeyboardInterrupt:
		print("leaving inside")

	print("left inside")

	lol = input("do u still wanna cont? if so press sth if not ctrl-c")