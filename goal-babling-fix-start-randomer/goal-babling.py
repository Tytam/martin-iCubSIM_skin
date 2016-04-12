import copy
import pprint
import time
import random
from armreader import armReader
from adjacencymatrix import adjacencymatrix
from left_arm_init import left_arm_init
import yarp;
yarp.Network.init();

class senso_motor_pair:
	def __init__(self):
		self.skin_cube_ID = None
		self.joints = [None] * 7
		return
	def __init__(self, ID, j):
		print ID
		self.skin_cube_ID = str(ID.split())
		self.joints = copy.deepcopy(j);
		return
	
	def write(self):
		vysledok = ""
		for item in self.skin_cube_ID:
			vysledok += str(item)
		print vysledok
		for x in range(0,7):
			print self.joints[x]
		return

	def writefile(self):
		vysledok = ""
		for item in self.skin_cube_ID:
			vysledok  += str(item)
		for x in range(0,7):
			vysledok += ' '
			vysledok +=  str(self.joints[x])
		return vysledok
	
citac = armReader()
#print citac.getData()

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
	pocet = 0
	suma = [0,0,0,0,0,0,0]
	for item in model:
		if preklad(index) in item.skin_cube_ID:
			pocet+=1 
			for i in range(0, 7):
				suma[i] += item.joints[i]
	for i in range(0, 6):
		suma[i] = suma[i] / pocet
	return suma
				 

#prepare pasive hand
left = left_arm_init()
left.set()

###########################################################################
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

# move to new position
iPos.positionMove(tmp.data())

tmp.set(1, 15)
tmp.set(2, 40)
tmp.set(3, 70)
tmp.set(4, 20)

iPos.positionMove(tmp.data())

print "posunute"

zname = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
joint_setting= [-30, 15, 40, 70, 20, 0, 0]
semafor = True
x = 0
while semafor:
	x += 1
	r = random.uniform(-66, -70)
	tmp.set(0, r)
	joint_setting[0] = r
	r = random.uniform(18, 20)
	tmp.set(1, r)
	joint_setting[1] = r
	r = random.uniform(70, 74)
	joint_setting[2] = r
	tmp.set(2, r)
	r = random.uniform(80, 84)
	joint_setting[3] = r
	tmp.set(3, r) 
	r = random.uniform(33, 36)
	joint_setting[4] = r
	tmp.set(4, r)    
	r = random.uniform(-2, -3) #(-50, 0)
	joint_setting[5] = r
	tmp.set(5, r) 
	r = random.uniform(11, 13)
	joint_setting[6] = r
	tmp.set(6, r) 
	iPos.positionMove(tmp.data())
	#print "zaspal"
	time.sleep(3)
	dat = citac.getData()
	#print dat
	dat = str(dat) 
	if dat != "":
		model.append(senso_motor_pair(dat, joint_setting))
		d = dat.split()
		for item in d:
    			if item == "011":
				zname[0] = 1
			elif item == "012":
				zname[1] = 1
			elif item == "013":
				zname[2] = 1
			elif item == "021":
				zname[3] = 1
			elif item == "022":
				zname[4] = 1
			elif item == "023":
				zname[5] = 1
			elif item == "024":
				zname[6] = 1
			elif item == "025":
				zname[7] = 1
			elif item == "026":
				zname[8] = 1
			elif item == "027":
				zname[9] = 1
			elif item == "028":
				zname[10] = 1
			elif item == "005":
				zname[11] = 1
			elif item == "006":
				zname[12] = 1
			elif item == "007":
				zname[13] = 1
			elif item == "008":
				zname[14] = 1
			elif item == "009":
				zname[15] = 1

		suma = 0
		for j in range(0, 16):
			suma += zname[j]
		if suma > 0:
			if len(model) > 0:
				print "zaciname cielene hladat"
				semafor = False
				
	
	#print "zobudeny"
	iPos.positionMove(hom.data())
	time.sleep(2)
	print x


semafor = True
while semafor:
	x += 1
	print x
	#vyberieme nechytenu kocku s aspon 1 znamim kamaratom
	vybrana = False
	i = -1
	kamaratiindexy = []
	while vybrana == False:
		i = int(random.uniform(0,16))
		kamaratiindexy = distmat.getkamaratov(i, zname)
		if len(kamaratiindexy) > 0 and zname[i] == 0:
			vybrana = True

	print "hladame na indexe " + str(i)
	print "zname "
	print zname
	kamarati = []
	for item in kamaratiindexy:
		kamarati.append(getaveragemotor(item))
	
	#urcime zonu prehladavania a prehladavame

	
	a = int(random.uniform(0, len(kamarati))) 
	item = kamarati[a]
		
			
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
	iPos.positionMove(tmp.data())
	print "hladame"
	time.sleep(3)
	dat = citac.getData()
	print dat
	#dat = str(dat)  
	if dat != "":
		model.append(senso_motor_pair(dat, joint_setting))
		d = dat.split()
		for vec in d:
    			if vec == "011":
				zname[0] = 1
			if vec == "012":
				zname[1] = 1
			if vec == "013":
				zname[2] = 1
			if vec == "021":
				zname[3] = 1
			if vec == "022":
				zname[4] = 1
			if vec == "023":
				zname[5] = 1
			if vec == "024":
				zname[6] = 1
			if vec == "025":
				zname[7] = 1
			if vec == "026":
				zname[8] = 1
			if vec == "027":
				zname[9] = 1
			if vec == "028":
				zname[10] = 1
	iPos.positionMove(hom.data())
	time.sleep(2)

		 
	
	#nasli sme 8/10 prehladavanie konci
	suma = 0
	for j in range(0, 10):
		suma += zname[j]
	if suma > 7:
		semafor = False
	












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
	

	

