import yarp;
yarp.Network.init();
class ExampleReader:
    def __init__(self):
        self.in_port = yarp.BufferedPortBottle()
        self.in_port.open("/example/input:i")

	#ports I use for testing uncomment line that you want to try
        yarp.Network.connect("/icubSim/skinManager/skin_events:o", "/example/input:i")
	#yarp.Network.connect("/icubSim/left_arm/state:o", "/example/input:i") #there must be skin contact active in simulator otherwise no data
	#yarp.Network.connect("/pokus", "/example/input:i") #i created port /pokus via "yarp write /pokus"

        return

    def getData(self):
        #in this example, I assume the data is a single integer
        #we use read() where the parameter determines if it is 
        #blocking (True) or not.
	
        btl = self.in_port.read(True)
	
	my_data = btl.toString()
	#if btl != None:
		#my_data += btl.get(0).asString() #fist word
		#my_data += btl.get(1).asString() #second word
		#my_data += btl.get(2).asString()
		
		
        #if you have doubles, you can use asDouble()
        #or strings can be obtained using asString() 
	
        return my_data

citac = ExampleReader()
print citac.getData()
while True:
	dat = citac.getData()
	cis = ""
	if "(0 1 2 3 4 5 6 7 8 9 10 11)" in dat:
		# zapestie
		if " 121 " in dat:
			cis += "01 "
		if " 102 " in dat:
			cis += "02 "
		if " 97 " in dat:
			cis += "03 "
		if " 109 " in dat:
			cis += "04 "
		if " 133 " in dat:
			cis += "05 "
		cisla = ""
		# vrchna cast predlaktia
		if " 299 300 " in dat:
			cisla += "11 "
		if " 215 336 " in dat:
			cisla += "12 "
		if " 263 312 " in dat:
			cisla += "13 "

		#spodna cast predlaktia
		if " 143 168 " in dat:
			cisla += "21 "
		if " 167 144 " in dat:
			cisla += "22 "
		if " 35 12 " in dat:
			cisla += "23 "
		if " 11 180 " in dat:
			cisla += "24 "
		if " 131 60 " in dat:
			cisla += "25 "
		if " 107 108 " in dat:
			cisla += "26 "
		if " 95 72 " in dat:
			cisla += "27 "
		if " 47 48 " in dat:
			cisla += "28 "
	
		if cisla != "":
			print cisla
		else:
			print cis

