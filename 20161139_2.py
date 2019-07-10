
import sys


arr = ['COMMIT', 'START', 'END']

def do_recovery(lines):

	for lyn in lines:

		if arr[0] in lyn:
			lyn = lyn.strip()
			lyn = lyn.split(" ")[1]
			lyn = lyn.split(">")[0]
			tmp = lyn.strip()
			lyn = tmp
			if tmp not in finish:
				finish.append(tmp)

	for lyn in reversed(lines):
		lyn = lyn.strip()
		# print finish
		

		if arr[1] not in lyn and arr[2] not in lyn and arr[0] not in lyn:
			lyn = lyn[1:]
			tmp = lyn[:-1].split(",")
			tmp = map(lambda x: x.strip(), tmp)
			tm0 = tmp[0]
			tm1 = tmp[1]
			tm2 = tmp[2]
			if tm0 not in finish:
				dvar[tm1] = tm2


# def print_vars():
# 	s = ""
# 	for v in sorted (dvar.keys()):
# 		s += v+" "+str(dvar[v])+" "
# 	print(s.strip())


dvar = {}
fyl = sys.argv[1]
finish = []
s = ""
with open(fyl) as f:
	flines = f.readlines()
l = flines[0].split(' ')
linlen = (len(l)-1)
for i in range(linlen):
	if i%2 == 0:
		dvar[l[i]] = int(l[i+1])
do_recovery(flines[2:])
for vv in sorted(dvar.keys()):
	s += vv+" "
	s += str(dvar[vv])+" "
print(s.strip())

