import alsaaudio, time, audioop, math, datetime

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

f = open("SoundData.txt", "w")
samples = []

def avg(samples):
	return float(sum(samples))/len(samples)

while True:
	l, data = inp.read()
	if l:
		level = audioop.max(data, 2)
		db = 21.2632181*math.log(level) + 24.8486585
		samples.append(db)
		if len(samples) > 50:
			samples.pop(0)
		f.write(str(avg(samples)) + ";"+datetime.datetime.now().strftime("%X")+"/\n")
	time.sleep(.02)


