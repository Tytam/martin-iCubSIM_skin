import yarp;
yarp.Network.init();
class armReader:
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
	mydata = my_data.split('((')

	cis = ""
	if "(0 1 2 3 4 5 6 7 8 9 10 11)" in my_data:
		for dat in mydata:
			#print dat
			#print "printol som"
			if len(dat) > 10:
				#left hand
				#print dat
				#print dat[10]
				#print dat[11] 
				if " 6 1)" in dat:
					print dat
					#print "lava"
					#prsty
					if " (48 " in dat:
						cis += "000 "
					if " 11) " in dat:
						cis += "001 "
					if " (12 " in dat:
						cis += "002 "
					if " (24 " in dat:
						cis += "003 "
					if " (36 " in dat:
						cis += "004 "
					# dlan
					if " 122 " in dat:
						cis += "005 "
					if " 102 " in dat:
						cis += "006 "
					if " 97 " in dat:
						cis += "007 "
					if " 109 " in dat:
						cis += "008 "
					if " 133 " in dat:
						cis += "009 "
				#left forarm
				if " 4 2)" in dat:
					#print "lava"
					# vrchna cast predlaktia
					if " 299 300 " in dat:
						cis += "011 "
					if " 215 336 " in dat:
						cis += "012 "
					if " 263 312 " in dat:
						cis += "013 "

					#spodna cast predlaktia
					if " 143 168 " in dat:
						cis += "021 "
					if " 167 144 " in dat:
						cis += "022 "
					if " 35 12 " in dat:
						cis += "023 "
					if " 11 180 " in dat:
						cis += "024 "
					if " 131 60 " in dat:
						cis += "025 "
					if " 107 108 " in dat:
						cis += "026 "
					if " 95 72 " in dat:
						cis += "027 "
					if " 47 48 " in dat:
						cis += "028 "
				#right hand
				if " 6 4)" in dat:
					#prsty
					if " (48 " in dat:
						cis += "100 "
					if " 11) " in dat:
						cis += "101 "
					if " (12 " in dat:
						cis += "102 "
					if " (24 " in dat:
						cis += "103 "
					if " (36 " in dat:
						cis += "104 "
					# dlan
					if " 122 " in dat:
						cis += "105 "
					if " 102 " in dat:
						cis += "106 "
					if " 97 " in dat:
						cis += "107 "
					if " 109 " in dat:
						cis += "108 "
					if " 133 " in dat:
						cis += "109 "
				#right forarm
				if " 4 5)" in dat:
					# vrchna cast predlaktia
					if " 299 300 " in dat:
						cis += "111 "
					if " 215 336 " in dat:
						cis += "112 "
					if " 263 312 " in dat:
						cis += "113 "

					#spodna cast predlaktia
					if " 143 168 " in dat:
						cis += "121 "
					if " 167 144 " in dat:
						cis += "122 "
					if " 35 12 " in dat:
						cis += "123 "
					if " 11 180 " in dat:
						cis += "124 "
					if " 131 60 " in dat:
						cis += "125 "
					if " 107 108 " in dat:
						cis += "126 "
					if " 95 72 " in dat:
						cis += "127 "
					if " 47 48 " in dat:
						cis += "128 "
	#print "citac nasiel"
	print cis	
        return cis

#citac = ExampleReader()
#print "haaaaahahahahahahahahahahahahahahhahaah"
#print citac.getData()

#dat = citac.getData()
#print dat


