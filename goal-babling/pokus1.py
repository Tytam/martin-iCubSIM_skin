import pprint
import yarp;
yarp.Network.init();
# prepare a property object
props = yarp.Property()
props.put("device","remote_controlboard")
props.put("local","/client/left_arm")
props.put("remote","/icubSim/left_arm")

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
tmp.set(0, -50)
tmp.set(1, 20)
tmp.set(2, 20)
tmp.set(3, 30)
tmp.set(4, 0)

# move to new position
iPos.positionMove(tmp.data())

#iPos.positionMove(home.data())
