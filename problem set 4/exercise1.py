#!/usr/bin/python

# 1. 5-line fuzzer below is from Charlie Miller's
#	"Babysitting an Army of Monkeys"
#	-- Part 1 - http://www.youtube.com/watch?v=Xnwodi2CBws (verified)
#	-- Part 2 - http://www.youtube.com/watch?v=lK5fgCvS2N4 (verified)

# List of files to use as initial seed.
file_list = [
	"pdf-sample.pdf"
	]


# List of applications to test
apps = [
	"/usr/bin/pdf2ps"
	]

fuzz_output = "fuzz.pdf"

FuzzFactor = 250
num_tests = 60

############### end configuration #################

import math
import random
import string
import subprocess
import time

okCount = 0
failCount = 0
for i in range(num_tests):
	file_choice = random.choice(file_list)
	app = random.choice(apps)

	buf = bytearray(open(file_choice, 'rb').read())

	# start Charlie Miller code
	numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1

	for j in range(numwrites):
		while True:
			rbyte = random.randrange(256)
			rn = random.randrange(len(buf))
			# only accept if value in document differs from random value
			if buf[rn] != "%c"%(rbyte): break
		buf[rn] = "%c"%(rbyte)
	# end Charlie Miller code

	open(fuzz_output, 'wb').write(buf)

	process = subprocess.Popen([app, fuzz_output])

	time.sleep(1)
	crashed = process.poll()
	if not crashed:
		process.terminate()
		print i, "OK", file_choice
		okCount += 1
	else:
		print i, "FAIL", file_choice
		failCount += 1

print "OK", okCount
print "FAIL", failCount

