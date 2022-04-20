from itertools import permutations

ops = ["*", "+", "-"]

def splitString(s):
    new_s = s.replace("*", "-").replace("+","-")
    return list(map(int, new_s.split("-")))

def calc(op, n1, n2):
    if op == "*":
        return n1 * n2
    elif op == "-":
        return n1 - n2
    else:
        return n1 + n2

def calc_lists(n_list, o_list, order):
    for op in order:
        for _ in range(o_list.count(op)):
            for i in range(len(o_list)):
                if o_list[i] == op:
                    res = calc(o_list.pop(i), n_list.pop(i), n_list.pop(i))
                    n_list.insert(i, res)
                    break
    return n_list[0]
    
def solution(expression):
    answers = []
    nums = splitString(expression)
    op_list = []
    for i in expression:
        if i in ops:
            op_list.append(i)
    orders = permutations(ops, 3)
    for order in orders:
        temp_n = nums.copy()
        temp_o = op_list.copy()
        answers.append(calc_lists(temp_n, temp_o, order))
    return max(max(answers), -min(answers))
