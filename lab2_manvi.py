#Exercise-1
num=5
new_num=num*(10-3)
print(f"Exercise 1's new_num is: {new_num}")

'''
now the output will be 35 instead of 47
'''

#Exercise-2
dividend = 10
divisor = 3
decimal_quotient = dividend / divisor 
quotient = dividend // divisor 
remainder = dividend % divisor 
print(f"Exercise 2's quotient is: {quotient}, remainder is: {remainder}.")

'''
for quotient the operator is // and for remainder the operator is %
'''

#Exercise-3
rectangular_width = 5
rectangular_length = 3
perimeter = 2*(rectangular_width + rectangular_length)                                                                                                                                   # Modify it to calculate perimeter
area = rectangular_width * rectangular_length 
print(f"Exercise 3's rectangular has perimeter of: {perimeter}, area of: {area}.")


#Exercise-4
marks = [80.5, 86.5]
mark_mid = marks[0]
mark_final = marks[1]
mark_average =(mark_mid + mark_final)/2 
print(f"Exercise 4's average mark is: {mark_average}")


#Exercise-5
words = ["apple", "pear"]
if len(words[0]) < len(words[1]): 
    longer_word = words[1]
else:
    longer_word = words[0]

print(f"Exercise 5's longer word is: {longer_word}")


#Exercise-6
increase = 0.2
increase_percentage = increase * 100
print(f"Exercise 6's increase percentage is: {increase_percentage}%")

#Exercise-7
x = 2
count = 0
while count < 8: 
    print(x)
    x = x + 2
    count = count + 1





