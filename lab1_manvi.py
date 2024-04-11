#Exercise-1
x=0
while (x<10):
    x=x+2
    print(x)

'''
output=
    2
    4
    6
    8
    10

'''

#Exercise-2
print("There is a rectangle, of which one side is 3 and the other side is 4.") 
side_1 = 3
side_2 = 4
print(f"I think the area of the rectangle is: {side_1 + side_2}.")

'''
sematic error is in the forth line which stats area of rectangle is: {side_1 * side_2}.")

'''
#Exercise-3
my_instructor_name = "Alice"
my_name = "Manvi"
my_github_account = "https://github.com/Manvipaull/comp115"
my_hobby = "Badminton"
hours_coding_per_week = "3" 
coding_experience_types = ["newbie", "beginner", "intermediate", "advanced"]
my_coding_experience = coding_experience_types[0] 
project_types = ["game developing", "website application", "data analysis", "machine learning"]
project_interested = project_types[2]
project_another_interested = project_types[1]


print(f"""
Hi {my_instructor_name},

I am {my_name}. I like {my_hobby}.

My experience level in coding is {my_coding_experience}, at least I think.
I would love to learning coding {hours_coding_per_week} hours per week.
The projects I'd like to do in this term are: {project_interested} and {project_another_interested}.
Here is my GitHub account: {my_github_account}.

Hope we will have fun in learning Python together this term! 

Cheers,
{my_name}
""")

'''
output:
Hi Alice,

I am Manvi. I like Badminton.

My experience level in coding is newbie, at least I think.
I would love to learning coding 3 hours per week.
The projects I'd like to do in this term are: data analysis and website application.
Here is my GitHub account: https://github.com/Manvipaull/comp115.

Hope we will have fun in learning Python together this term! 

Cheers,
Manvi
'''


