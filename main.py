class printShapes:
	"""
		Easily print shapes like squares, triangles and circles on the terminal.
	"""
	class square:
		"""
			Functions for printing squares
		"""
		def monotonic( side, value=0,spacing=2):
			"""
				Print a Square using a single integer
			"""
			for i in range(side):
				print((str(value)+(" "*spacing))*side)
	
	class rectangle:
		def monotonic( l, b,  value=0,spacing=2):
			for i in range(b):
				print((str(value)+(" "*spacing))*l)
	class triangle:
		class right:
			class bottom_left:
				def monotonic( h, b, value=0,spacing=2):
					for i in range(h):
						print((str(value)+(" "*spacing))*(int(b*(i+1)/h)))
			class top_left:
				def monotonic(h,b,value=0,spacing=2):
					for i in range(h,1,-1):
						print((str(value)+(" "*spacing))*(int(b*(i)/h)))
			# class bottom_right:
			# 	def monotonic( h, b, value=0,spacing=2):
			# 		for i in range(h):
			# 			print((str(value)+(" "*spacing))*(int(b*(i+1)/h)))
			# class top_right:
			# 	def monotonic(h,b,value=0,spacing=2):
			# 		for i in range(h,1,-1):
			# 			print((str(value)+(" "*spacing))*(int(b*(i)/h)))
	class circle:
		def monotonic(d, value=0, spacing=2):
			if(d%2):
				for i in range(d):
					if(i<=(d-1)/2):
						print(" "*((1+spacing)*(((d-1)/2)-i))+str(value)*((2*i)+1))
					else:
						print(" "*((1+spacing)*(i-((d-1)/2)))+str(value)*(i-(d-1)/2))
			else:
				for i in range(d):
					if(i<d/2):
						print(" "*(1+spacing)*(d/2-i-1)+str(value)*2*(i+1)) 
					else:
						print(" "*(1+spacing)*(i-(d/2))+str(value)*2*(d-i)) 


						
		


# printShapes.rectangle.monotonic()
printShapes.triangle.right.top.monotonic(5, 12,5)