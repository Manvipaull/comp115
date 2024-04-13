#Exercise-1
def reverse_str(s):
    return s[::-1]

print(reverse_str("Abd"))      
print(reverse_str("COMP115"))


#Exercise-2
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Apple"))  
print(count_vowels("Hmmm"))   


#Exercise-3
def remove_duplicates(s):
    seen = set()
    result = ''
    for char in s:
        if char.lower() not in seen:
            seen.add(char.lower())
            result += char
    return result

print(remove_duplicates("apple"))       
print(remove_duplicates("Popsipple"))   
print(remove_duplicates("pear"))


#Exercise-4
def find_index(s, t):
    for i, char in enumerate(s):
        if char == t:
            return i
    return -1

print(find_index("Abd", 'b'))      
print(find_index("Abdccc", 'c'))   
print(find_index("Abd", 'w'))


#Exercise-5
def project_completion_day(current_day, days_to_completion):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_day_index = days_of_week.index(current_day.capitalize())
    completion_day_index = (current_day_index + days_to_completion) % 7
    return days_of_week[completion_day_index]


print(project_completion_day('Monday', 4))     
print(project_completion_day('Monday', 7))     
print(project_completion_day('Saturday', 2))   


