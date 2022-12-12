def make_number(numbers, start=""):
    generated =[0 if start == "" else int(start)]
    for i, number in enumerate(numbers):
        generated += make_number(numbers[:i] + numbers[i+1:], start+str(number))
    return set(generated)

def solution(l):
    n_list = list(filter(lambda x: x%3 == 0, make_number(l)))
    return max(n_list)

print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))