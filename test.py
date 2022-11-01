a = -7
b = -8
c = '+'

def math(input_func):
    def answer(a,b,c):
        if c == '+':
            print(a+b)
        elif c == '-':
            print(a-b)

    return answer

@math
def output(a,b,c):
    a+b
output(a,b,c)