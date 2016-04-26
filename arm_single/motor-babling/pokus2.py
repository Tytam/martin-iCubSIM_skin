import pprint
import time
import random
import yarp;
yarp.Network.init();
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
tmp.set(2, 20)
tmp.set(3, 50)
tmp.set(4, 0)
tmp.set(5, 0)
tmp.set(6, 0)
tmp.set(7, 59)
tmp.set(8, 20)
tmp.set(9, 20)
tmp.set(10, 20)
tmp.set(11, 10)
tmp.set(12, 10)
tmp.set(13, 10)
tmp.set(14, 10)
tmp.set(15, 10)

hom=yarp.Vector(jnts)
hom.set(0, -30)
hom.set(1, 10)
hom.set(2, 20)
hom.set(3, 50)
hom.set(4, 0)
hom.set(5, 0)
hom.set(6, 0)
hom.set(7, 59)
hom.set(8, 20)
hom.set(9, 20)
hom.set(10, 20)
hom.set(11, 10)
hom.set(12, 10)
hom.set(13, 10)
hom.set(14, 10)
hom.set(15, 10)

# move to new position
iPos.positionMove(tmp.data())

tmp.set(1, 15)
tmp.set(2, 35)
tmp.set(3, 70)
tmp.set(4, 20)

iPos.positionMove(tmp.data())

print "posunute"
for x in range(0, 10):
	tmp.set(1,random.uniform(0, 20))
	tmp.set(2, random.uniform(30, 45))
	tmp.set(4, random.uniform(50, 80))    
	iPos.positionMove(tmp.data())
	print "zaspal"
	time.sleep(5)
	print "zobudeny"



