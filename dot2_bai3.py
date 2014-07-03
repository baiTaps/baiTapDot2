"""
BAI 3:3. There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these bchildren subjected to the following requirements:
Each child must have at least one candy.Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

"""
#Y tuong:
#		Chay trong a (a : la mang cac rating value), tim cac phan tu cuc dai, cuc tieu
#       Dien so keo tang dan : tu phan tu "cuc tieu" ->     phan tu "cuc dai" 
#                                            1      ->            ...
#VD:        input:  5,6,7,8,6,3,2
#     Dien so keo:  1,2,3,4,3,2,1
#           Tong :  16
def run(a):
	b = [0] * len(a) # b[i] la so keo cua nguoi thu i
	max1 = 0
	min1 = 0
	for i in range (len(a) - 1):  #Chay trong a
		# Neu gap phan tu cuc tieu, dien tu  phan tu cuc tieu do den phan tu cuc dai ngay truoc
		if (a[i -1] > a[i]) and (a[i] < a[i +1]): 
			min1 = i
			j = min1
			b[j] = 1
			while j > max1 +1 :
				j = j -1 
				b[j] = b[j + 1] + 1
			if b[j] + 1 > b[max1] :
				b[max1] = b[j] + 1 
		# Neu gap phan tu cuc dai, dien tu phan tu cuc tieu ngay truoc den phan tu cuc dai do
		if (a[i -1] < a[i]) and (a[i] > a[i +1]):
			max1 = i
			j = min1
			b[j] = 1
			while j < max1 :
				j = j +1
				b[j] = b[j -1] + 1
	# Dien tu phan tu cuc dai( hoac cuc tieu) gan cuoi den phan tu cuoi cung
	if a[len(a) -1 -1] < a[len(a) -1]: 
		j= min1+ 1 
		while j <= len(a) -1 :
			b[j] = b[j-1] + 1
			j = j + 1
	if a[len(a) -1 -1] > a[len(a) -1]:
		j = max1+ 1
		while j <= (len(a) -1):
			b[j] = b[j -1] - 1
			j = j + 1
	#
	print(b)
	# Tinh tong :
	Sum = 0
	for i in range (len(b)):
		Sum = Sum + b[i]
	# Xuat ket qua
	print("Result :   ",Sum)

def Input():
	s = input(" rating value list =   ") 
	# chuyen sang kieu list
	a = [0] 
	i = 0
	j = 0
	t1 = 0 #
	while j < len(s):
		if s[j] == ",":
			a[len(a)-1] = int(s[t1:j])
			t1 = j + 1
			a = a +[0]
		j = j + 1
	a[len(a)-1] = int(s[t1:j])
	return (a)

if __name__ == '__main__':
	day = Input()
	print (day)
	run(day)
