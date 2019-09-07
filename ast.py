
class Number():
	def __init__(self, value):
		self.value = value
	def eval(self):
		return int(self.value)
	def __repr__(self):
		return 'Number({})'.format(self.value)


class BinaryOp():
	def __init__(self, left, right):
		self.left = left
		self.right = right


class Sum(BinaryOp):
	def eval(self):
		return self.left.eval() + self.right.eval()
	def __repr__(self):
		return 'Sum({},{})'.format(self.left, self.right)

class Sub(BinaryOp):
	def eval(self):
		return self.left.eval() - self.right.eval()
	def __repr__(self):
		return 'Sub({},{})'.format(self.left, self.right)

class Times(BinaryOp):
	def eval(self):
		return self.left.eval() * self.right.eval()
	def __repr__(self):
		return 'Times({},{})'.format(self.left, self.right)

class Divide(BinaryOp):
	def eval(self):
		return self.left.eval() / self.right.eval()
class Montrer():
	def __init__(self, text):
		self.text=text
	def eval(self):
		return self.text

class NoOp():
	def eval(self):
		return
class AC():
	def __init__(self, left, right):
		self.left=left
		self.right=right
	def eval(self):
		return self.left + self.right
