

class FourCal:

	def __init__(self,first,second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def sub(self):
		result = self.first - self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result
		
	def div(self):
		result = self.first / self.second
		return result

class SafeFourCal(FourCal):
	def div(self):
		if self.second == 0:
			return 0
		else:
			return FourCal().div()  #(self)도 같은 결과

a = SafeFourCal(4, 0)

print(a.first, '+', a.second, '=', a.sum())
print(a.first, '-', a.second, '=', a.sub())
print(a.first, '*', a.second, '=', a.mul())
print(a.first, '/', a.second, '=', a.div())