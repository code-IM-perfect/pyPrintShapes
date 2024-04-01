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
	
