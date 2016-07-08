import yarp;
yarp.Network.init();
class rightStateReader:
    def __init__(self):
        self.in_port = yarp.BufferedPortBottle()
        self.in_port.open("/example/inputright:i")
        yarp.Network.connect("/icubSim/right_arm/state:o", "/example/inputright:i")
        return

    def getData(self):
        btl = self.in_port.read(True)
	
	my_data = btl.toString()
	mydata = my_data.split(' ')
        return mydata



