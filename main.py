class printShapes:
	"""
		Easily print shapes like squares, triangles and circles on the terminal.
	"""
	def square( side, value=0,spacing=2):
		"""
			Print a Square using a single integer
		"""
		for i in range(side):
			print((str(value)+(" "*spacing))*side)

	def rectangle( l, b,  value=0,spacing=2):
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

	def diamond(d, value=0, spacing=2):
		if(d%2):
			for i in range(d):
				if(i<=(d-1)/2):
					print(" "*((1+spacing)*(int((d-1)/2)-i))+(str(value)+" "*spacing)*((2*i)+1))
				else:
					print(" "*((1+spacing)*(i-int((d-1)/2)))+(str(value)+" "*spacing)*(2*d-2*i-1))
		else:
			for i in range(d):
				if(i<d/2):
					print(" "*(1+spacing)*int(d/2-i-1)+(str(value)+" "*spacing)*2*(i+1)) 
				else:
					print(" "*(1+spacing)*(i-int(d/2))+(str(value)+" "*spacing)*2*(d-i)) 


						
		


# printShapes.rectangle.monotonic()
# printShapes.triangle.right.top.monotonic(5, 12,5)
# printShapes.diamond(11)