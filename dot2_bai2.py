#BAI 2:2. Given an array of integers, every element appears three times except for one. Find that single one.
# kiem ra cac phan tu, neu la la single thi la True 

def find(a):
	def kiemTra(x): # Kiem tra neu co 3 phan tu giong a[x] thi do khong phai Single
		c = [x] 
		for  y in range (x +1, len(a)):
			if a[y] == a[x]:
				c = c + [y]
		if len(c) == 3:
			for y in range (3):
				b[c[y]] = False
			

	result = -1
	b = [True] * len(a)     # Ban dau tat ca cac phan tu deu co kha nang la Single
	for i in range(len(b)) :
		if b[i] == False : # Khong phai single thi bo qua
			continue
		if b[i] == True:   # Co kha nang la single thi thuc hien kiem tra
			kiemTra(i)
		if b[i] == True:  # Sau khi kiem tra, xac dinh la single
			result = i
			break
	return(result)
	
	
def Input():
	s = input(" Your array=   ") 
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
	Result = find(day)
	print (" The single one:  ", day[Result] )

	