class distancematrix:
    	def __init__(self):
		#self.matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.matrix = [[] for i in range(11)]
	
		# cube 11
		self.matrix[0].append([0, 0])#
		self.matrix[0].append([1, 0.0717])
		self.matrix[0].append([1, 0.0717])
		self.matrix[0].append([0, 0.0687])	
		self.matrix[0].append([0, 0.1048])
		self.matrix[0].append([0, 0.0915])
		self.matrix[0].append([0, 0.0465])
		self.matrix[0].append([0, 0.0687])
		self.matrix[0].append([0, 0.1048])	
		self.matrix[0].append([0, 0.0915])
		self.matrix[0].append([0, 0.0465])

		# cube 12
		self.matrix[1].append([1, 0.0717])
		self.matrix[1].append([0, 0])#
		self.matrix[1].append([1, 0.0545])
		self.matrix[1].append([0, 0.0868])	
		self.matrix[1].append([0, 0.0730])
		self.matrix[1].append([1, 0.0478])
		self.matrix[1].append([1, 0.0700])
		self.matrix[1].append([0, 0.0979])
		self.matrix[1].append([0, 0.0859])	
		self.matrix[1].append([0, 0.0658])
		self.matrix[1].append([0, 0.0833])

		# cube 13
		self.matrix[2].append([1, 0.0717])
		self.matrix[2].append([1, 0.0545])
		self.matrix[2].append([0, 0])#
		self.matrix[2].append([0, 0.0979])	
		self.matrix[2].append([0, 0.0859])
		self.matrix[2].append([0, 0.0658])
		self.matrix[2].append([0, 0.0833])
		self.matrix[2].append([0, 0.0868])
		self.matrix[2].append([0, 0.0730])	
		self.matrix[2].append([1, 0.0478])
		self.matrix[2].append([1, 0.0700])

		# cube 21
		self.matrix[3].append([0, 0.0687])
		self.matrix[3].append([0, 0.0868])
		self.matrix[3].append([0, 0.0979])
		self.matrix[3].append([0,  0])#
		self.matrix[3].append([1, 0.0643])
		self.matrix[3].append([1, 0.0699])
		self.matrix[3].append([1, 0.0242])
		self.matrix[3].append([1, 0.0375])
		self.matrix[3].append([1, 0.0744])	
		self.matrix[3].append([0, 0.0793])
		self.matrix[3].append([0, 0.0446])

		# cube 22
		self.matrix[4].append([0, 0.1048])
		self.matrix[4].append([0, 0.0730])
		self.matrix[4].append([0, 0.0859])
		self.matrix[4].append([0, 0.0643])
		self.matrix[4].append([0, 0])#
		self.matrix[4].append([1, 0.0264])
		self.matrix[4].append([1, 0.0705])
		self.matrix[4].append([1, 0.0744])
		self.matrix[4].append([1, 0.0375])	
		self.matrix[4].append([0, 0.0459])
		self.matrix[4].append([0, 0.0799])

		# cube 23
		self.matrix[5].append([0, 0.0915])
		self.matrix[5].append([1, 0.0478])
		self.matrix[5].append([0, 0.0658])
		self.matrix[5].append([1, 0.0699])
		self.matrix[5].append([1, 0.0264])
		self.matrix[5].append([0, 0])#
		self.matrix[5].append([1, 0.0667])
		self.matrix[5].append([0, 0.0793])
		self.matrix[5].append([0, 0.0459])	
		self.matrix[5].append([0, 0.0375])
		self.matrix[5].append([0, 0.0765])

		# cube 24
		self.matrix[6].append([0, 0.0465])
		self.matrix[6].append([1, 0.0700])
		self.matrix[6].append([0, 0.0833])
		self.matrix[6].append([1, 0.0242])
		self.matrix[6].append([1, 0.0705])
		self.matrix[6].append([1, 0.0667])
		self.matrix[6].append([0, 0])#
		self.matrix[6].append([0, 0.0446])
		self.matrix[6].append([0, 0.0799])	
		self.matrix[6].append([0, 0.0765])
		self.matrix[6].append([0, 0.0375])

		# cube 25
		self.matrix[7].append([0, 0.0687])
		self.matrix[7].append([0, 0.0979])
		self.matrix[7].append([0, 0.0868])
		self.matrix[7].append([1, 0.0375])
		self.matrix[7].append([1, 0.0744])
		self.matrix[7].append([0, 0.0793])
		self.matrix[7].append([0, 0.0446])
		self.matrix[7].append([0, 0])#
		self.matrix[7].append([1, 0.0643])	
		self.matrix[7].append([1, 0.0699])
		self.matrix[7].append([1, 0.0242])

		# cube 26
		self.matrix[8].append([0, 0.1048])
		self.matrix[8].append([0, 0.0859])
		self.matrix[8].append([0, 0.0730])
		self.matrix[8].append([1, 0.0744])
		self.matrix[8].append([1, 0.0375])
		self.matrix[8].append([0, 0.0459])
		self.matrix[8].append([0, 0.0799])
		self.matrix[8].append([1, 0.0643])
		self.matrix[8].append([0, 0])#	
		self.matrix[8].append([1, 0.0264])
		self.matrix[8].append([1, 0.0705])

		# cube 27
		self.matrix[9].append([0, 0.0915])
		self.matrix[9].append([0, 0.0658])
		self.matrix[9].append([1, 0.0478])
		self.matrix[9].append([0, 0.0793])
		self.matrix[9].append([0, 0.0459])
		self.matrix[9].append([0, 0.0375])
		self.matrix[9].append([0, 0.0765])
		self.matrix[9].append([1, 0.0699])
		self.matrix[9].append([1, 0.0264])	
		self.matrix[9].append([0, 0])#
		self.matrix[9].append([1, 0.0667])

		# cube 28
		self.matrix[10].append([0, 0.0465])
		self.matrix[10].append([0, 0.0833])
		self.matrix[10].append([1, 0.0700])
		self.matrix[10].append([0, 0.0446])
		self.matrix[10].append([0, 0.0799])
		self.matrix[10].append([0, 0.0765])
		self.matrix[10].append([0, 0.0375])
		self.matrix[10].append([1, 0.0242])
		self.matrix[10].append([1, 0.0705])	
		self.matrix[10].append([1, 0.0667])
		self.matrix[10].append([0, 0])#

	def getkamaratov(self, toto, zname):
		result = []
		for i in range(0, 10):
			if zname[i] == 1:
				a = self.matrix[toto][i]
				if a[0] == 1:
					result.append(i)
		return result		
		
		

	

	
