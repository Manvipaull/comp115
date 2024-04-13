#Exercise-1
def remove_duplicates_set(s):
    seen_set = set()
    res = ''
    for c in s:
        if c not in seen_set:
            res += c
            seen_set.add(c)
    return res
    

assert remove_duplicates_set("apple") == "aple"
assert remove_duplicates_set("Popsipple") == "Popsile"


#Exercise-2
def gem_counting(stones, gems):
    gem_count = 0
    for stone in stones:
        if stone in gems:
            gem_count += 1
    return gem_count

print(gem_counting("abDFMdm", "admMQq"))  
print(gem_counting("abDFMdm", "af"))      
print(gem_counting("awCcM", "cQqW"))      
print(gem_counting("bFfL", "cQqW"))       


#Exercise-3
def students_id(student_ids):
    unique_ids = set(student_ids)
    return len(unique_ids)

print(students_id(['002', '003', '001', '004', '012']))


#Exercise-4
def students_id_occurences(student_ids):
    id_occurrences = {}
    for id in student_ids:
        if id in id_occurrences:
            id_occurrences[id] += 1
        else:
            id_occurrences[id] = 1
    return id_occurrences

print(students_id_occurences(['002', '003', '001', '004', '012'])) 


print(students_id_occurences(['002', '003', '001', '012', '003', '001']))


#Exercise-5

def word_frequency(paragraph):
    words = paragraph.split()  
    word_count = {}
    for word in words:
        
        word = word.strip('.,!?').lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


print(word_frequency("I am alive. I am happy.")) 


print(word_frequency("I do not like water. I like fruits.")) 




