class printShapes:
	"""Easily print various shapes on the terminal integer digits.
		You can print a huge variety of shapes- squares, rectangles, various triangles, diamonds, circles.
	"""
	def square(self, side, value=0,spacing=2):
		"""
			Print a Square pattern of an integer.

			:param side: The sidelength of square.
        	:type side: int

			:param value:
			:type value: int

			:param spacing: Number of spaces between characters to make it look like an actual shape (Depends on your font tho, so adjust accordingly) 
			:type  spacing: int
		"""
		for i in range(side):
			print((str(value)+(" "*spacing))*side)

	def rectangle( l, b,  value=0,spacing=2):
		for i in range(b):
			print((str(value)+(" "*spacing))*l)

	class triangle:
		class right:
			def bottom_left( h, b, value=0,spacing=2):
					for i in range(h):
						print((str(value)+(" "*spacing))*(int(b*(i+1)/h)))
			def top_left(h,b,value=0,spacing=2):
					for i in range(h,0,-1):
						print((str(value)+(" "*spacing))*(int(b*(i)/h)))
			def bottom_right( h, b, value=0,spacing=2):
					for i in range(h):
						printLen=int(b*(i+1)/h)
						print((str(value)*(b-printLen)+(" "*spacing))*printLen)
			def top_right(h,b,value=0,spacing=2):
					for i in range(h,0,-1):
						print(((" "*(spacing+1))*(b-(int(b*(i)/h))))+(str(value)+(" "*spacing))*(int(b*(i)/h)))

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
	
	def circle(radius, value=0, spacing=2):
		for y in range(-radius,radius+1):
			for x in range(-radius,radius+1):
				if(x*x+y*y<=radius*radius):
					print(value,end=(" "*spacing))
				else:
					print(" ",end=(" "*spacing))
			print("")


# printShapes.diamond(13)
printShapes.triangle.right.bottom_right(10, 5,5)
# printShapes.circle(20)