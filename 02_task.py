import itertools

# divisible_by_three(4311)
def divisible_by_three(x):
    if x % 3 == 0:
        return True
    else:
        return False

# x = l
# n = 4
def get_combinations(x, n):
    res = [y for y in itertools.permutations(x, n)]
    return res

# x = (4, 1)
# input = res
def collapse_tuples(input):
    outer = []
    for x in input:
        inner = []        
        for y in x: 
            temp = str(y)
            inner.append(temp)
        outer.append(int(''.join(inner)))
    return outer

def validate_combination(combos):
    # combos = res    
    combos = collapse_tuples(combos)
    is_divisible_by_three = [divisible_by_three(combo) for combo in combos]    

    if any(is_divisible_by_three):
        res = list(itertools.compress(combos, is_divisible_by_three))
        return max(res)
    else:
        return 0

# input: a list of digits 
# return: largest number that can be made by some or all of the digits AND
#           is divisible by 3 
#         if not possible: return 0
# constraints: each element can be used only once
#
# solution.solution([3, 1, 4, 1])
# Output:
#     4311

# Input:
# solution.solution([3, 1, 4, 1, 5, 9])
# Output:
#     94311
def solution(l):
    # find all combinations of num_length entries
    res = []
    seq_lengths = [x + 1 for x in range(len(l))]
    for seq_length in seq_lengths:
        # seq_length = 2
        combos = get_combinations(l, seq_length)
        res.append(validate_combination(combos))

    return max(res)
