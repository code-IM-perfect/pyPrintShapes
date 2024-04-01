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
