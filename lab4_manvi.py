#Exercise-1
def usd_to_cad(usd_amount):
    exchange_rate = 1.34
    cad_amount = usd_amount * exchange_rate
    return cad_amount

usd_amount = 100
cad_equivalent = usd_to_cad(usd_amount)
print(f"{usd_amount} US dollars is equivalent to {cad_equivalent} Canadian dollars.")

#Exercise-2
def alarm_time(current_time_string, waiting_time_string):
    current_time_int = int(current_time_string)
    waiting_time_int = int(waiting_time_string)
    hours = current_time_int + waiting_time_int
    timeofday = hours % 24
    return timeofday

assert alarm_time('13', '1') == 14
assert alarm_time('12', '24') == 12
assert alarm_time('13', '11') == 0
assert alarm_time('15', '10') == 1


#Exercise-3
def average(numbers):
    if not numbers:
        return 0 
    total = sum(numbers)
    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]
avg = average(numbers)
print("Average:", avg)


#Exercise-4
def find_max(numbers):
    max_value = numbers[0]  
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

numbers = [10, 30, 20, 50, 40]
max_value = find_max(numbers)
print("Maximum value:", max_value)


#Exercise-5
def evens(nums):
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


print(evens([1, 2, 3, 4]))  
print(evens([2, 4, 6, 7, 8]))  
print(evens([1, 3]))


#Exercise-6
def sum_of_squares(xs):
    sum_squares = 0
    for num in xs:
        sum_squares += num ** 2
    return sum_squares

print(sum_of_squares([2, 3, 4]))


#Exercise-7
def squares(nums):
    squares_list = [num ** 2 for num in nums]
    return squares_list


print(squares([1, 2, 3, 4]))




