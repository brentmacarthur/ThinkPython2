'''
Think Python, 2nd - Exercise 3-1
'''

def right_justify(s):
    pad = 70 - len(s)
    print(' '*pad + s)

right_justify('monty')
