from itertools import product

possible_ops = product("+-*/", repeat=3)
answers = {}
for op in possible_ops:
    op_as_string = "4 " + " ".join([x + " 4" for x in op])
    answer = eval(op_as_string.replace("/", "//"))
    answers[int(answer)] = "{} = {}".format(op_as_string, int(answer))

n = int(input())
for i in range(n):
    l = int(input())
    if int(l) in answers:
        print(answers[int(l)])
    else:
        print("no solution")
