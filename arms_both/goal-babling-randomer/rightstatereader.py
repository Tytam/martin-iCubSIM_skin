import yarp;
yarp.Network.init();
class rightStateReader:
    def __init__(self):
        self.in_port = yarp.BufferedPortBottle()
        self.in_port.open("/example/inputright:i")

	#ports I use for testing uncomment line that you want to try
        yarp.Network.connect("/icubSim/right_arm/state:o", "/example/inputright:i")
	#yarp.Network.connect("/icubSim/left_arm/state:o", "/example/input:i") #there must be skin contact active in simulator otherwise no data
	#yarp.Network.connect("/pokus", "/example/input:i") #i created port /pokus via "yarp write /pokus"

        return

    def getData(self):
        #in this example, I assume the data is a single integer
        #we use read() where the parameter determines if it is 
        #blocking (True) or not.
	
        btl = self.in_port.read(True)
	
	my_data = btl.toString()
	mydata = my_data.split(' ')
        return mydata

#citac = ExampleReader()
#print "haaaaahahahahahahahahahahahahahahhahaah"
#print citac.getData()

#dat = citac.getData()
#print dat


