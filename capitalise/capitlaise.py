s = input()

def solve(s):
    n1 = s.split(' ')
    name = ' '.join(i.capitalize() for i in n1)
    print(name)

solve(s)