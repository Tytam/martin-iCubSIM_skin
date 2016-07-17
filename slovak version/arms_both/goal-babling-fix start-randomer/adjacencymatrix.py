class adjacencymatrix:
    	def __init__(self):
		#self.matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.matrix = [[] for i in range(16)]
	
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

		self.matrix[0].append(4)
		self.matrix[0].append(3)
		self.matrix[0].append(3)	
		self.matrix[0].append(2)
		self.matrix[0].append(1)

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

		self.matrix[1].append(5)
		self.matrix[1].append(4)
		self.matrix[1].append(4)	
		self.matrix[1].append(3)
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

		self.matrix[2].append(5)
		self.matrix[2].append(4)
		self.matrix[2].append(4)	
		self.matrix[2].append(3)
		self.matrix[2].append(2)

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

		self.matrix[3].append(7)
		self.matrix[3].append(6)
		self.matrix[3].append(6)	
		self.matrix[3].append(5)
		self.matrix[3].append(4)

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

		self.matrix[4].append(7)
		self.matrix[4].append(6)
		self.matrix[4].append(6)	
		self.matrix[4].append(5)
		self.matrix[4].append(4)

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

		self.matrix[5].append(6)
		self.matrix[5].append(5)
		self.matrix[5].append(5)	
		self.matrix[5].append(4)
		self.matrix[5].append(3)

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

		self.matrix[6].append(6)
		self.matrix[6].append(5)
		self.matrix[6].append(5)	
		self.matrix[6].append(4)
		self.matrix[6].append(3)

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
		
		self.matrix[7].append(7)
		self.matrix[7].append(6)
		self.matrix[7].append(6)	
		self.matrix[7].append(5)
		self.matrix[7].append(4)

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
		
		self.matrix[8].append(7)
		self.matrix[8].append(6)
		self.matrix[8].append(6)	
		self.matrix[8].append(5)
		self.matrix[8].append(4)

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
		
		self.matrix[9].append(6)
		self.matrix[9].append(5)
		self.matrix[9].append(5)	
		self.matrix[9].append(4)
		self.matrix[9].append(3)

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

		self.matrix[10].append(6)
		self.matrix[10].append(5)
		self.matrix[10].append(5)	
		self.matrix[10].append(4)
		self.matrix[10].append(3)

		#cube 05
		self.matrix[11].append(4)
		self.matrix[11].append(5)
		self.matrix[11].append(5)
		self.matrix[11].append(7)
		self.matrix[11].append(7)
		self.matrix[11].append(6)
		self.matrix[11].append(6)
		self.matrix[11].append(7)
		self.matrix[11].append(7)	
		self.matrix[11].append(6)
		self.matrix[11].append(6)

		self.matrix[11].append(0)#
		self.matrix[11].append(1)
		self.matrix[11].append(2)	
		self.matrix[11].append(2)
		self.matrix[11].append(3)
		
		#cube 06
		self.matrix[12].append(3)
		self.matrix[12].append(4)
		self.matrix[12].append(4)
		self.matrix[12].append(6)
		self.matrix[12].append(6)
		self.matrix[12].append(5)
		self.matrix[12].append(5)
		self.matrix[12].append(6)
		self.matrix[12].append(6)	
		self.matrix[12].append(5)
		self.matrix[12].append(5)

		self.matrix[12].append(1)
		self.matrix[12].append(0)#
		self.matrix[12].append(1)	
		self.matrix[12].append(1)
		self.matrix[12].append(2)

		#cube 07
		self.matrix[13].append(3)
		self.matrix[13].append(4)
		self.matrix[13].append(4)
		self.matrix[13].append(6)
		self.matrix[13].append(6)
		self.matrix[13].append(5)
		self.matrix[13].append(5)
		self.matrix[13].append(6)
		self.matrix[13].append(6)	
		self.matrix[13].append(5)
		self.matrix[13].append(5)

		self.matrix[13].append(2)
		self.matrix[13].append(1)
		self.matrix[13].append(0)#	
		self.matrix[13].append(1)
		self.matrix[13].append(2)

		#cube 08
		self.matrix[14].append(2)
		self.matrix[14].append(3)
		self.matrix[14].append(3)
		self.matrix[14].append(5)
		self.matrix[14].append(5)
		self.matrix[14].append(4)
		self.matrix[14].append(4)
		self.matrix[14].append(5)
		self.matrix[14].append(5)	
		self.matrix[14].append(4)
		self.matrix[14].append(4)

		self.matrix[14].append(2)
		self.matrix[14].append(1)
		self.matrix[14].append(1)	
		self.matrix[14].append(0)#
		self.matrix[14].append(1)
		
		#cube 09
		self.matrix[15].append(1)
		self.matrix[15].append(2)
		self.matrix[15].append(2)
		self.matrix[15].append(4)
		self.matrix[15].append(4)
		self.matrix[15].append(3)
		self.matrix[15].append(3)
		self.matrix[15].append(4)
		self.matrix[15].append(4)	
		self.matrix[15].append(3)
		self.matrix[15].append(3)

		self.matrix[15].append(3)
		self.matrix[15].append(2)
		self.matrix[15].append(2)	
		self.matrix[15].append(1)
		self.matrix[15].append(0)#

	def getkamaratov(self, toto, zname):
		result = []
		for i in range(0, 16):
			if zname[i] == 1:
				a = self.matrix[toto][i]
				if a == 1:
					result.append(i)
		return result		
		
