import time

while True:
	try:
		f = open("SoundData.txt", "r")
		str = f.read().split("\n")
		f.close()
		if len(str) > 50:
			str = str[(len(str) - 50):(len(str))]
			str = [x + "\n" for x in str]
			f = open("SoundData.txt", "w")
			f.write("".join(str))
			f.close()
			print("Shortet the file!")
		else:
			print("File is too short!")
	except IOError as e:
		print(e)
	time.sleep(1)
