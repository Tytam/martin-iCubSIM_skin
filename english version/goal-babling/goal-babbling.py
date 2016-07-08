import copy
import pprint
import time
import random
from armreader import armReader
from rightstatereader import rightStateReader
from adjacencymatrix import adjacencymatrix
import yarp;
yarp.Network.init();

class senso_motor_pair:
	def __init__(self):
		self.skin_cube_ID = None
		self.joints = [None] * 14
		return
	def __init__(self, ID, j):
		print ID
		self.skin_cube_ID = str(ID.split())
		self.joints = copy.deepcopy(j);
		return
	
	def write(self):
		result = ""
		for item in self.skin_cube_ID:
			result += str(item)
		print result
		for x in range(0,14):
			print self.joints[x]
		return

	def writefile(self):
		result = ""
		for item in self.skin_cube_ID:
			result  += str(item)
		for x in range(0,14):
			result += ' '
			result +=  str(self.joints[x])
		return result
	
reader = armReader()
#print reader.getData()
rightreader = rightStateReader()

model = []
distmat = adjacencymatrix()

def preklad(index):
	if index == 0:
		return "011"
	elif index == 1:
		return "012"
	elif index == 2:
		return "013"
	elif index == 3:
		return  "021"
	elif index == 4:
		return  "022"
	elif index == 5:
		return  "023"
	elif index == 6:
		return  "024"
	elif index == 7:
		return  "025"
	elif index == 8:
		return  "026"
	elif index == 9:
		return  "027"
	elif index == 10:
		return  "028"

	elif index == 11:
		return  "005"
	elif index == 12:
		return  "006"
	elif index == 13:
		return  "007"
	elif index == 14:
		return  "008"
	elif index == 15:
		return  "009"	

def getaveragemotor(index):
	count = 0
	suma = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for item in model:
		if preklad(index) in item.skin_cube_ID:
			count+=1 
			for i in range(0, 14):
				suma[i] += item.joints[i]
	for i in range(0, 14):
		suma[i] = suma[i] / count
	return suma
				 



###########################################################################
# Right arm
# prepare a property object
props = yarp.Property()
props.put("device","remote_controlboard")
props.put("local","/client/right_arm")
props.put("remote","/icubSim/right_arm")

# create remote driver
armDriver = yarp.PolyDriver(props)
#query motor control interfaces
iPos = armDriver.viewIPositionControl()
iEnc = armDriver.viewIEncoders()

#retrieve number of joints
jnts=iPos.getAxes()
print 'Controlling', jnts, 'joints'

# read encoders
encs=yarp.Vector(jnts)
iEnc.getEncoders(encs.data())
# store as home position
home=yarp.Vector(jnts, encs.data())

#########################################################################
# Left arm

prop = yarp.Property()
prop.put("device","remote_controlboard")
prop.put("local","/client/left_arm")
prop.put("remote","/icubSim/left_arm")

# create remote driver
armDriver2 = yarp.PolyDriver(prop)
#query motor control interfaces
iPos2 = armDriver2.viewIPositionControl()
iEnc2 = armDriver2.viewIEncoders()

#retrieve number of joints
jnts2=iPos2.getAxes()
print 'Controlling', jnts2, 'joints'

# read encoders
encs2=yarp.Vector(jnts2)
iEnc2.getEncoders(encs2.data())
# store as home position
home2=yarp.Vector(jnts2, encs2.data())


pprint.pprint(home.data())

#initialize a new tmp vector identical to encs
tmp=yarp.Vector(jnts)
for x in range(0, 4):
    print tmp.get(x)
# add 10 degrees to the first four joints
tmp.set(0, -30)
tmp.set(1, 10)
tmp.set(2, 40)
tmp.set(3, 50)
tmp.set(4, 0)
tmp.set(5, 0)
tmp.set(6, 0)
tmp.set(7, 59)
tmp.set(8, 20)
tmp.set(9, 20)
tmp.set(10, 145)
tmp.set(11, 10)
tmp.set(12, 10)
tmp.set(13, 58)
tmp.set(14, 154)
tmp.set(15, 167)

tmp2=yarp.Vector(jnts2)
tmp2.set(0, -30)
tmp2.set(1, 10)
tmp2.set(2, 40)
tmp2.set(3, 50)
tmp2.set(4, 0)
tmp2.set(5, 0)
tmp2.set(6, 0)
tmp2.set(7, 59)
tmp2.set(8, 20)
tmp2.set(9, 20)
tmp2.set(10, 20)
tmp2.set(11, 10)
tmp2.set(12, 10)
tmp2.set(13, 0)
tmp2.set(14, 0)
tmp2.set(15, 0)

hom=yarp.Vector(jnts)
hom.set(0, -90)
hom.set(1, 30)
hom.set(2, 40)
hom.set(3, 70)
hom.set(4, 20)
hom.set(5, 0)
hom.set(6, 0)
hom.set(7, 59)
hom.set(8, 20)
hom.set(9, 20)
hom.set(10, 20)
hom.set(11, 10)
hom.set(12, 10)
hom.set(13, 58)
hom.set(14, 154)
hom.set(15, 167)

hom2=yarp.Vector(jnts2)
hom2.set(0, -90)
hom2.set(1, 30)
hom2.set(2, 40)
hom2.set(3, 70)
hom2.set(4, 20)
hom2.set(5, 0)
hom2.set(6, 0)
hom2.set(7, 59)
hom2.set(8, 20)
hom2.set(9, 20)
hom2.set(10, 20)
hom2.set(11, 10)
hom2.set(12, 10)
hom2.set(13, 0)
hom2.set(14, 0)
hom2.set(15, 0)

# move to new position
iPos.positionMove(tmp.data())
iPos2.positionMove(tmp.data())

tmp.set(1, 15)
tmp.set(2, 40)
tmp.set(3, 70)
tmp.set(4, 20)

iPos.positionMove(tmp.data())

print "moved"

known = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
joint_setting= [-30, 15, 40, 70, 20, 0, 0, -30, 15, 40, 70, 20, 0, 0]
semaphor = True
x = 0
while semaphor:
	x += 1
################################################
	# right arm 
	r = random.uniform(-90, 0)
	joint_setting[0] = r
	tmp.set(0, r)
	r = random.uniform(0, 40)
	joint_setting[1] = r
	tmp.set(1, r)
	r = random.uniform(40, 79)
	joint_setting[2] = r
	tmp.set(2, r)
	r = random.uniform(25, 103)
	joint_setting[3] = r
	tmp.set(3, r) 
	r = random.uniform(-90, 90)
	joint_setting[4] = r
	tmp.set(4, r)    
	r = random.uniform(-3, 10) #(-50, 0)
	joint_setting[5] = r
	tmp.set(5, r) 
	r = random.uniform(0, 30)
	joint_setting[6] = r
	tmp.set(6, r)

	# left arm
	r = random.uniform(-94, 0)
	joint_setting[7] = r
	tmp2.set(0, r)
	r = random.uniform(0, 20)
	joint_setting[8] = r
	tmp2.set(1, r)
	r = random.uniform(-36, 79)
	joint_setting[9] = r
	tmp2.set(2, r)
	r = random.uniform(25, 103)
	joint_setting[10] = r
	tmp2.set(3, r) 
	r = random.uniform(-89, 89)
	joint_setting[11] = r
	tmp2.set(4, r)    
	r = random.uniform(-3, 10) #(-50, 0)
	joint_setting[12] = r
	tmp2.set(5, r) 
	r = random.uniform(-19, 30)
	joint_setting[13] = r
	tmp2.set(6, r)

	# move 
	iPos2.positionMove(tmp2.data())
	time.sleep(1)
	iPos.positionMove(tmp.data())
	#print "sleep"
	time.sleep(3)
	dat = reader.getData()
	#print dat
	dat = str(dat) 
	if dat != "":
		print joint_setting
		setting = rightreader.getData();
		for a in range(0,7):
			joint_setting[a] = float(setting[a])
		print joint_setting
		model.append(senso_motor_pair(dat, joint_setting))
		d = dat.split()
		for item in d:
    			if item == "011":
				known[0] = 1
			elif item == "012":
				known[1] = 1
			elif item == "013":
				known[2] = 1
			elif item == "021":
				known[3] = 1
			elif item == "022":
				known[4] = 1
			elif item == "023":
				known[5] = 1
			elif item == "024":
				known[6] = 1
			elif item == "025":
				known[7] = 1
			elif item == "026":
				known[8] = 1
			elif item == "027":
				known[9] = 1
			elif item == "028":
				known[10] = 1
			elif item == "005":
				known[11] = 1
			elif item == "006":
				known[12] = 1
			elif item == "007":
				known[13] = 1
			elif item == "008":
				known[14] = 1
			elif item == "009":
				known[15] = 1

		suma = 0
		for j in range(0, 16):
			suma += known[j]
		if suma > 0:
			if len(model) > 0:
				print "zaciname cielene hladat"
				semaphor = False
				
	
	#print "awake"
	iPos.positionMove(hom.data())
	iPos2.positionMove(hom2.data())
	time.sleep(2)
	print x

start = x
semaphor = True
control = 0
suma2 = 0
while semaphor:
	control += 1
	x += 1
	print start
	print x
	#randomly choose one unknown region with at least one known neighbour
	chosen = False
	i = -1
	neighbour_index = []
	while chosen == False:
		i = int(random.uniform(0,16))
		neighbour_index = distmat.get_neighbours(i, known)
		if len(neighbour_index) > 0 and known[i] == 0:
			chosen = True

	print "search at index " + str(i)
	print "known "
	print known
	neighbours = []
	for item in neighbour_index:
		neighbours.append(getaveragemotor(item))
	
	#urcime zonu prehladavania a prehladavame

	
	a = int(random.uniform(0, len(neighbours))) 
	item = neighbours[a]
###################################################################x		
	# right arm
	"""	
	r = random.uniform(float(item[0]) + 1, float(item[0]) - 1)
	tmp.set(0, r)
	joint_setting[0] = r
				

	r = random.uniform(float(item[1]) + 2, float(item[1]) - 2)
	tmp.set(1, r)
	joint_setting[1] = r
	
	r = random.uniform(float(item[2]) + 3, float(item[2]) - 3)
	joint_setting[2] = r
	tmp.set(2, r)
	
	r = random.uniform(float(item[3]) + 4, float(item[3]) - 4)
	joint_setting[3] = r
	tmp.set(3, r)
	 
	r = random.uniform(float(item[4]) + 5, float(item[4]) - 5)
	joint_setting[4] = r
	tmp.set(4, r) 
	   
	r = random.uniform(float(item[5]) + 6, float(item[5]) - 6)
	joint_setting[5] = r
	tmp.set(5, r)
	
	r = random.uniform(float(item[6]) + 7, float(item[6]) - 7)
	joint_setting[6] = r
	tmp.set(6, r)
"""
#####################################################################
	u = 10;
	r = random.uniform(float(item[0]) + u, float(item[0]) - u)
	tmp.set(0, r)
	joint_setting[0] = r
				

	r = random.uniform(float(item[1]) + u, float(item[1]) - u)
	tmp.set(1, r)
	joint_setting[1] = r
	
	r = random.uniform(float(item[2]) + u, float(item[2]) - u)
	joint_setting[2] = r
	tmp.set(2, r)
	
	r = random.uniform(float(item[3]) + u, float(item[3]) - u)
	joint_setting[3] = r
	tmp.set(3, r)
	 
	r = random.uniform(float(item[4]) + u, float(item[4]) - u)
	joint_setting[4] = r
	tmp.set(4, r) 
	   
	r = random.uniform(float(item[5]) + u, float(item[5]) - u)
	joint_setting[5] = r
	tmp.set(5, r)
	
	r = random.uniform(float(item[6]) + u, float(item[6]) - u)
	joint_setting[6] = r
##################################################################x
	# left arm
	v = 1
	rot = 20
	r = random.uniform(float(item[7]) + v, float(item[7]) - v)
	joint_setting[7] = r
	tmp2.set(0, r)	

	r = random.uniform(float(item[8]) + v, float(item[8]) - v)
	joint_setting[8] = r
	tmp2.set(1, r)
		
	r = random.uniform(float(item[9]) + v, float(item[9]) - v)
	joint_setting[9] = r
	tmp2.set(2, r)
	
	r = random.uniform(float(item[10]) + v, float(item[10]) - v)
	joint_setting[10] = r
	tmp2.set(3, r)
	 
	r = random.uniform(float(item[11]) + rot, float(item[11]) - rot)
	joint_setting[11] = r
	tmp2.set(4, r) 
	   
	r = random.uniform(float(item[12]) + v, float(item[12]) - v)
	joint_setting[12] = r
	tmp2.set(5, r)
	
	r = random.uniform(float(item[13]) + v, float(item[13]) - v)
	joint_setting[13] = r
	tmp2.set(6, r)
	
	# move
	iPos2.positionMove(tmp2.data())
	time.sleep(1)
	iPos.positionMove(tmp.data())
	
	
	print "searching"
	time.sleep(3)
	dat = reader.getData()
	print dat
	#dat = str(dat)  
	if dat != "":
		suma2 = 0
		for j in range(0, 16):
			suma2 += known[j]
		
		setting = rightreader.getData();
		for a in range(0,7):
			joint_setting[a] = float(setting[a]) 
		model.append(senso_motor_pair(dat, joint_setting))
		d = dat.split()
		for thing in d:
    			if thing == "011":
				known[0] = 1
			if thing == "012":
				known[1] = 1
			if thing == "013":
				known[2] = 1
			if thing == "021":
				known[3] = 1
			if thing == "022":
				known[4] = 1
			if thing == "023":
				known[5] = 1
			if thing == "024":
				known[6] = 1
			if thing == "025":
				known[7] = 1
			if thing == "026":
				known[8] = 1
			if thing == "027":
				known[9] = 1
			if thing == "028":
				known[10] = 1
			if thing == "005":
				known[11] = 1
			if thing == "006":
				known[12] = 1
			if thing == "007":
				known[13] = 1
			if thing == "008":
				known[14] = 1
			if thing == "009":
				known[15] = 1
	iPos.positionMove(hom.data())
	iPos2.positionMove(hom2.data())
	time.sleep(2)

		 
	
	#found 
	suma = 0
	for j in range(0, 16):
		suma += known[j]
	if suma > 15:
		semaphor = False
	
	if suma > suma2:
		kontorla = 0

	#unpromising search
	if control == 200:
		semaphor = False
		print "bad search"
	












################################################################################
f = open('workfile', 'w')
i = 0
while i < len(model):
	model[i].write()
	#f.write(model[i].writefile())
	#f.write('\n')	
	i += 1

i = 0
while i < len(model):
	f.write(model[i].writefile())
	f.write('\n')	
	i += 1

f.close()

print x
print known
	

	

