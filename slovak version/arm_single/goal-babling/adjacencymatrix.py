class distancematrix:
    	def __init__(self):
		#self.matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.matrix = [[] for i in range(11)]
	
		# cube 11
		self.matrix[0].append(0)#
		self.matrix[0].append(1)
		self.matrix[0].append(1)
		self.matrix[0].append(3)	
		self.matrix[0].append(3)
		self.matrix[0].append(2)
		self.matrix[0].append(2)
		self.matrix[0].append(3)
		self.matrix[0].append(3)	
		self.matrix[0].append(2)
		self.matrix[0].append(2)

		# cube 12
		self.matrix[1].append(1)
		self.matrix[1].append(0)#
		self.matrix[1].append(1)
		self.matrix[1].append(2)	
		self.matrix[1].append(2)
		self.matrix[1].append(1)
		self.matrix[1].append(1)
		self.matrix[1].append(3)
		self.matrix[1].append(3)	
		self.matrix[1].append(2)
		self.matrix[1].append(2)

		# cube 13
		self.matrix[2].append(1)
		self.matrix[2].append(1)
		self.matrix[2].append(0)#
		self.matrix[2].append(3)	
		self.matrix[2].append(3)
		self.matrix[2].append(2)
		self.matrix[2].append(2)
		self.matrix[2].append(2)
		self.matrix[2].append(2)	
		self.matrix[2].append(1)
		self.matrix[2].append(1)
		# cube 21
		self.matrix[3].append(3)
		self.matrix[3].append(2)
		self.matrix[3].append(3)
		self.matrix[3].append(0)#
		self.matrix[3].append(1)
		self.matrix[3].append(1)
		self.matrix[3].append(1)
		self.matrix[3].append(1)
		self.matrix[3].append(1)	
		self.matrix[3].append(2)
		self.matrix[3].append(2)

		# cube 22
		self.matrix[4].append(3)
		self.matrix[4].append(2)
		self.matrix[4].append(3)
		self.matrix[4].append(1)
		self.matrix[4].append(0)#
		self.matrix[4].append(1)
		self.matrix[4].append(1)
		self.matrix[4].append(1)
		self.matrix[4].append(1)	
		self.matrix[4].append(2)
		self.matrix[4].append(2)
		# cube 23
		self.matrix[5].append(2)
		self.matrix[5].append(1)
		self.matrix[5].append(0)
		self.matrix[5].append(1)
		self.matrix[5].append(1)
		self.matrix[5].append(2)#
		self.matrix[5].append(1)
		self.matrix[5].append(2)
		self.matrix[5].append(2)	
		self.matrix[5].append(2)
		self.matrix[5].append(2)

		# cube 24
		self.matrix[6].append(2)
		self.matrix[6].append(1)
		self.matrix[6].append(2)
		self.matrix[6].append(1)
		self.matrix[6].append(1)
		self.matrix[6].append(1)
		self.matrix[6].append(2)#
		self.matrix[6].append(2)
		self.matrix[6].append(2)	
		self.matrix[6].append(2)
		self.matrix[6].append(2)
		# cube 25
		self.matrix[7].append(3)
		self.matrix[7].append(3)
		self.matrix[7].append(2)
		self.matrix[7].append(1)
		self.matrix[7].append(1)
		self.matrix[7].append(2)
		self.matrix[7].append(2)
		self.matrix[7].append(2)#
		self.matrix[7].append(1)	
		self.matrix[7].append(1)
		self.matrix[7].append(1)

		# cube 26
		self.matrix[8].append(3)
		self.matrix[8].append(3)
		self.matrix[8].append(2)
		self.matrix[8].append(1)
		self.matrix[8].append(1)
		self.matrix[8].append(2)
		self.matrix[8].append(2)
		self.matrix[8].append(1)
		self.matrix[8].append(2)#	
		self.matrix[8].append(1)
		self.matrix[8].append(1)

		# cube 27
		self.matrix[9].append(2)
		self.matrix[9].append(2)
		self.matrix[9].append(1)
		self.matrix[9].append(2)
		self.matrix[9].append(2)
		self.matrix[9].append(2)
		self.matrix[9].append(2)
		self.matrix[9].append(1)
		self.matrix[9].append(1)	
		self.matrix[9].append(2)#
		self.matrix[9].append(1)

		# cube 28
		self.matrix[10].append(2)
		self.matrix[10].append(2)
		self.matrix[10].append(1)
		self.matrix[10].append(2)
		self.matrix[10].append(2)
		self.matrix[10].append(2)
		self.matrix[10].append(2)
		self.matrix[10].append(1)
		self.matrix[10].append(1)	
		self.matrix[10].append(1)
		self.matrix[10].append(2)#

	def getkamaratov(self, toto, zname):
		result = []
		for i in range(0, 10):
			if zname[i] == 1:
				a = self.matrix[toto][i]
				if a[0] == 1:
					result.append(i)
		return result		
		
