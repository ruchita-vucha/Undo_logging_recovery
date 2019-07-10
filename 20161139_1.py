import sys
def write_l(e):
	temp = e.split('(')[1].split(')')[0].split(',')
	e = e.split('(')[1]
	tmp = e.split(')')[0]
	tmp = tmp.split(',')
	tmp = map(lambda x: x.strip(), tmp)
	tm0 = tmp[0]
	tm1 = tmp[1]
	print("<T"+str(i[0])+", "+tm0+", "+str(mvar[tm0])+">")

	mvar[tm0] = local[tm1]
	


def read_l(e):
	e = e.split('(')[1]
	tmp = e.split(')')[0]
	tmp = tmp.split(',')
			
	tmp = map(lambda x: x.strip(), tmp)
	tm0 = tmp[0]
	tm1 = tmp[1]
	if tm0 not in mvar:
		mvar[tm0] = dvar[tm0]

	local[tm1] = mvar[tm0]
def requal_l(e):
	e = e.split(':=')
	tmp = map(lambda x: x.strip(), e)
	tm0 = tmp[0]
	tm1 = tmp[1]
	local[tm0] = eval(tm1, m, local)
def finalprint():
	mp = ""
	s = ""
	for v in sorted (mvar.keys()):
		mp += v+" "
		mp += str(mvar[v])+" "
	for v in sorted (dvar.keys()):
		s += v+" "
		s += str(dvar[v])+" "
	ab = ""
	print(mp.strip())
	print(s.strip())



def split_trans(lines, x,fl):

	tr = 0
	cnt=-1
	
	
	# print(lines[0])
	for l in (lines):
		l = l.rstrip()
		if(fl == 0):
			l = l.split(' ')
			linlen = (len(l)-1)
			for i in range(linlen):
				if i%2 == 0:
					dvar[l[i]] = int(l[i+1])
			fl = 1
			
		else:

			if(l == ''):
				tr = 0
		
			else:
				if(l[0] == 'T'):
					trans.append([])
					cnt += 1
					tr = 1
					
		 
				elif(tr == 1 ):
					trans[cnt].append(l)

	tlen = []
	for tra in trans:
		tlen.append(len(tra))
	tm = max(tlen)

	i=0
	while i < tm:

		for idx, tra in enumerate(trans):
			lt = len(tra)
			j = i
			if i < lt:
				k = i + x
				while j < k and j < lt:
					a.append((idx+1, tra[j]))
					j += 1
		i+=x


def write_log(tas):        

	
	for ind in range(len(tas)):
		i = tas[ind]
		e = tas[ind][1]
		if i[0] not in active:
			print ("<START T"+str(i[0])+">")
			finalprint()
			active.append(i[0])

		if 'READ' in e:
			read_l(e)

		if ':=' in e:
			requal_l(e)

		if 'WRITE' in e:
			
			e = e.split('(')[1]
			tmp = e.split(')')[0]
			tmp = tmp.split(',')
			tmp = map(lambda x: x.strip(), tmp)
			tm0 = tmp[0]
			tm1 = tmp[1]
			print("<T"+str(i[0])+", "+tm0+", "+str(mvar[tm0])+">")

			mvar[tm0] = local[tm1]
			var[i[0]].append(tm0)
			finalprint()



		if 'OUTPUT' in e:
			
			e = e.split('(')[1]
			tmp = e.split(')')[0]
			dvar[tmp] = mvar[tmp]
			var[i[0]].remove(tmp)
			lvar = len(var[i[0]])
			if lvar == 0:
				active.remove(i[0])
				print("<COMMIT T"+str(i[0])+">")
				finalprint()

#print("hi")




active =[]
dvar = {}
mvar = {}
local = {}
var = []
m = {}


fyl = sys.argv[1]
x = int(sys.argv[2])
with open(fyl) as f:
	flines = f.readlines()
a = []
trans = []
split_trans(flines, x,0)
lT = len(trans)
ruh = 0
while ruh <= lT:
	var.append([])
	ruh += 1
write_log(a)
