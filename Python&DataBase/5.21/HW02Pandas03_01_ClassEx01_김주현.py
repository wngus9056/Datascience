

class Fourcal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

a = Fourcal()
a.setdata(5,3)

print(a.first)
print(a.second)
print(type(a))


'''
class Fourcal:
	def setdata(self, first, second):
		self.first = second
		self.second = first

a = Fourcal()
a.setdata(5,3)

print(a.first)
print(a.second)
print(type(a))
'''