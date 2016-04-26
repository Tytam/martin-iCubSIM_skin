class distancematrix:
    def __init__(self):
	#self.matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	self.matrix = []
	for x in range(0, 10):
		self.matrix[x] = [];
	
	# cube 11
	self.matrix[0,0] = [0, 0]#
	self.matrix[0,1] = [1, 0.0717]
	self.matrix[0,2] = [1, 0.0717]
	self.matrix[0,3] = [0, 0.0687]	
	self.matrix[0,4] = [0, 0.1048]
	self.matrix[0,5] = [0, 0.0915]
	self.matrix[0,6] = [0, 0.0465]
	self.matrix[0,7] = [0, 0.0687]
	self.matrix[0,8] = [0, 0.1048]	
	self.matrix[0,9] = [0, 0.0915]
	self.matrix[0,10] = [0, 0.0465]

	# cube 12
	self.matrix[1,0] = [1, 0.0717]
	self.matrix[1,1] = [0, 0]#
	self.matrix[1,2] = [1,  0.0545]
	self.matrix[1,3] = [0, 0.0868]	
	self.matrix[1,4] = [0, 0.0730]
	self.matrix[1,5] = [1, 0.0478]
	self.matrix[1,6] = [1, 0.0700]
	self.matrix[1,7] = [0, 0.0979]
	self.matrix[1,8] = [0, 0.0859]	
	self.matrix[1,9] = [0, 0.0658]
	self.matrix[1,10] = [0, 0.0833]

	# cube 13
	self.matrix[2,0]  = [1, 0.0717]
	self.matrix[2,1]  = [1, 0.0545]
	self.matrix[2,2]  = [0, 0]#
	self.matrix[2,3]  = [0, 0.0979]	
	self.matrix[2,4]  = [0, 0.0859]
	self.matrix[2,5]  = [0, 0.0658]
	self.matrix[2,6]  = [0, 0.0833]
	self.matrix[2,7]  = [0, 0.0868]
	self.matrix[2,8]  = [0, 0.0730]	
	self.matrix[2,9]  = [1, 0.0478]
	self.matrix[2,10]  = [1, 0.0700]

	# cube 21
	self.matrix[3,0] = [0, 0.0687]
	self.matrix[3,1] = [0, 0.0868]
	self.matrix[3,2] = [0, 0.0979]
	self.matrix[3,3] = [0,  0]#
	self.matrix[3,4] = [1, 0.0643]
	self.matrix[3,5] = [1, 0.0699]
	self.matrix[3,6] = [1, 0.0242]
	self.matrix[3,7] = [1, 0.0375]
	self.matrix[3,8] = [1, 0.0744]	
	self.matrix[3,9] = [0, 0.0793]
	self.matrix[3,10] = [0, 0.0446]

	# cube 22
	self.matrix[4,0] = [0, 0.1048]
	self.matrix[4,1] = [0, 0.0730]
	self.matrix[4,2] = [0, 0.0859]
	self.matrix[4,3] = [0, 0.0643]
	self.matrix[4,4] = [0, 0]#
	self.matrix[4,5] = [1, 0.0264]
	self.matrix[4,6] = [1, 0.0705]
	self.matrix[4,7] = [1, 0.0744]
	self.matrix[4,8] = [1, 0.0375]	
	self.matrix[4,9] = [0, 0.0459]
	self.matrix[4,10] = [0, 0.0799]

	# cube 23
	self.matrix[5,0] = [0, 0.0915]
	self.matrix[5,1] = [1, 0.0478]
	self.matrix[5,2] = [0, 0.0658]
	self.matrix[5,3] = [1, 0.0699]
	self.matrix[5,4] = [1, 0.0264]
	self.matrix[5,5] = [0, 0]#
	self.matrix[5,6] = [1, 0.0667]
	self.matrix[5,7] = [0, 0.0793]
	self.matrix[5,8] = [0, 0.0459]	
	self.matrix[5,9] = [0, 0.0375]
	self.matrix[5,10] = [0, 0.0765]

	# cube 24
	self.matrix[6,0] = [0, 0.0465]
	self.matrix[6,1] = [1, 0.0700]
	self.matrix[6,2] = [0, 0.0833]
	self.matrix[6,3] = [1, 0.0242]
	self.matrix[6,4] = [1, 0.0705]
	self.matrix[6,5] = [1, 0.0667]
	self.matrix[6,6] = [0, 0]#
	self.matrix[6,7] = [0, 0.0446]
	self.matrix[6,8] = [0, 0.0799]	
	self.matrix[6,9] = [0, 0.0765]
	self.matrix[6,10] = [0, 0.0375]

	# cube 25
	self.matrix[7,0] = [0, 0.0687]
	self.matrix[7,1] = [0, 0.0979]
	self.matrix[7,2] = [0, 0.0868]
	self.matrix[7,3] = [1, 0.0375]
	self.matrix[7,4] = [1, 0.0744]
	self.matrix[7,5] = [0, 0.0793]
	self.matrix[7,6] = [0, 0.0446]
	self.matrix[7,7] = [0, 0]#
	self.matrix[7,8] = [1, 0.0643]	
	self.matrix[7,9] = [1, 0.0699]
	self.matrix[7,10] = [1, 0.0242]

	# cube 26
	self.matrix[8,0] = [0, 0.1048]
	self.matrix[8,1] = [0, 0.0859]
	self.matrix[8,2] = [0, 0.0730]
	self.matrix[8,3] = [1, 0.0744]
	self.matrix[8,4] = [1, 0.0375]
	self.matrix[8,5] = [0, 0.0459]
	self.matrix[8,6] = [0, 0.0799]
	self.matrix[8,7] = [1, 0.0643]
	self.matrix[8,8] = [0, 0]#	
	self.matrix[8,9] = [1, 0.0264]
	self.matrix[8,10] = [1, 0.0705]

	# cube 27
	self.matrix[9,0] = [0, 0.0915]
	self.matrix[9,1] = [0, 0.0658]
	self.matrix[9,2] = [1, 0.0478]
	self.matrix[9,3] = [0, 0.0793]
	self.matrix[9,4] = [0, 0.0459]
	self.matrix[9,5] = [0, 0.0375]
	self.matrix[9,6] = [0, 0.0765]
	self.matrix[9,7] = [1, 0.0699]
	self.matrix[9,8] = [1, 0.0264]	
	self.matrix[9,9] = [0, 0]#
	self.matrix[9,10] = [1, 0.0667]

	# cube 28
	self.matrix[10,0] = [0, 0,0465]
	self.matrix[10,1] = [0, 0,0833]
	self.matrix[10,2] = [1, 0,0700]
	self.matrix[10,3] = [0, 0,0446]
	self.matrix[10,4] = [0, 0,0799]
	self.matrix[10,5] = [0, 0,0765]
	self.matrix[10,6] = [0, 0,0375]
	self.matrix[10,7] = [1, 0,0242]
	self.matrix[10,8] = [1, 0,0705]	
	self.matrix[10,9] = [1, 0,0667]
	self.matrix[10,10] = [0, 0]#

	

	
