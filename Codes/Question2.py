# Question 2

class Finder:
	def __init__(self, arr, num):
		self.arr = arr
		self.num = num

	def finding(self):
		values = {}
		n = len(self.arr)
		key=1
		for i in range(n):
			for j in range(0, n):
				if(self.arr[j]+self.arr[i] == num):
					values[key] = [i,j]
					key+=1
		print(values)
		return 0

arr = [10,20,10,40,50,60,70]
num = 50
obj1 = Finder(arr, num)
obj1.finding()