count = 1
total1 = 1
total2 = 1
number1 = 4
number2 = 8
sum1 = 0
sum2 = 0

for number in range (5):
	total1 *= number1
	sum1 += total1
print(sum1 , end= " ")

for number1 in range (5):
	total2 *= number2
	sum2 += total2
print(sum2 , end= " " )