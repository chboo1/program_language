
class Number():
	def __init__(self, value):
		self.value = value
	def eval(self):
		return int(self.value)


class BinaryOp():
	def __init__(self, left, right):
		self.left = left
		self.right = right


class Sum(BinaryOp):
	def eval(self):
		return self.left.eval() + self.right.eval()
class Sub(BinaryOp):
	def eval(self):
		return self.left.eval() - self.right.eval()
class Times(BinaryOp):
	def eval(self):
		return self.left.eval() * self.right.eval()
class Divide(BinaryOp):
	def eval(self):
		return self.left.eval() / self.right.eval()
class Montrer():
	def __init__(self, text):
		self.text=text
	def eval(self):
		return self.text
	
