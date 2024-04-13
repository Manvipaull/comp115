#Exercise-1
def dna_to_code(base):
    dna_to_code_dict = {'A': '10', 'T': '00', 'G': '11', 'C': '01'}
    code_sequence = ''
    for b in base:
        code_sequence += dna_to_code_dict[b]
    return code_sequence

print(dna_to_code('A'))     
print(dna_to_code('T'))     
print(dna_to_code('G'))      
print(dna_to_code('C'))      
print(dna_to_code('AA'))     
print(dna_to_code('AATT'))


#Exercise-2
import turtle

def draw_line():
    turtle.forward(50)  
    turtle.penup()
    turtle.forward(10)  
    turtle.pendown()

def move_pen():
    turtle.penup()
    turtle.forward(60)  
    turtle.pendown()

def graph_sequence(sequence, color):
    turtle.speed(0)  
    turtle.color(color)  
    for char in sequence:
        if char == '0':
            move_pen()
        elif char == '1':
            draw_line()

    turtle.done()

sequence = '10100000'
color = 'blue'
graph_sequence(sequence, color)


#Exercise-3
def visualize(dna_sequence, color):
    code = dna_to_code(dna_sequence)
    draw_coded(code, color)


dna_sequence = 'AGTTGC'
color = 'red'
visualize(dna_sequence, color)

