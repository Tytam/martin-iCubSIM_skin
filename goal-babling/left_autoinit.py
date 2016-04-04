import yarp;
import time
class left_arm_init:
	def __init__(self):
		yarp.Network.init();
		self.props = yarp.Property()
		self.props.put("device","remote_controlboard")
		self.props.put("local","/client/left_arm")
		self.props.put("remote","/icubSim/left_arm")

		# create remote driver
		self.armDriver = yarp.PolyDriver(self.props)
		#query motor control interfaces
		self.iPos = self.armDriver.viewIPositionControl()
		self.iEnc = self.armDriver.viewIEncoders()
		self.jnts=self.iPos.getAxes()
		self.encs=yarp.Vector(self.jnts)
		self.iEnc.getEncoders(self.encs.data())
		self.tmp=yarp.Vector(self.jnts)
		return

	def set(self):
		self.tmp.set(0, -85.0)
		self.tmp.set(1, 23.0)
		self.tmp.set(2, -12.0)
		self.tmp.set(3, 20.0)
		self.tmp.set(4, 20)
		self.tmp.set(5, 0)
		self.tmp.set(6, 0)
		self.tmp.set(7, 40)
		self.tmp.set(8, 10)
		self.tmp.set(9, 60)
		self.tmp.set(10, 70)
		self.tmp.set(11, 0)
		self.tmp.set(12, 0)
		self.tmp.set(13, 0)
		self.tmp.set(14, 0)
		self.tmp.set(15, 0)
		self.iPos.positionMove(self.tmp.data())
		time.sleep(3)
		return

left = left_arm_init()
left.set()
