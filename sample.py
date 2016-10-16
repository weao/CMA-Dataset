fin = open('stream.txt', 'r')
lines = fin.readlines()

# dataset
DS = {}

for line in lines:
	vals = line.split(' ')
	aID = int(vals[0])
	if aID == -1:
		break
	N = int(vals[1])

	if aID not in DS:
		DS[aID] = []

	X = [0]*N
	Y = [0]*N
	Z = [0]*N
	T = [0]*N
	for i in range(N):
		X[i] = float(vals[2 + i*4 + 0])
		Y[i] = float(vals[2 + i*4 + 1])
		Z[i] = float(vals[2 + i*4 + 2])
		T[i] = int(vals[2 + i*4 + 3])
	DS[aID].append({'x':X, 'y':Y, 'z':Z})


for aID in DS:
	print aID, len(DS[aID])

fin.close()