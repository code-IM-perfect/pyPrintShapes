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
