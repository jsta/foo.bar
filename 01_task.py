import re

def solution(s):
    # each possible letter [a-z] corresponds to a color
    # the sequence is given clockwise
    # s: a non-empty string < 200 char 
    # returns: max number of identical substings 

    # s = "abab"
    # s = "ababcab"
    # s = "abccbaabccba" # 2    

len_search = 0
res = []    

while len_search < len(s):
    len_search += 1 # if substrings not equal try splitting by last 2 char
    # print(len_search)
    last_char = s[(len(s)-len_search):(len(s))]
    s_split = re.split(str(last_char), s) # try splitting by it
    s_split = s_split[0:(len(s_split)-1)]
    s_split = [seq + last_char for seq in s_split]
    if all(seq == s_split[0] for seq in s_split):
        res.append(len(s_split))
    else:
        res.append(0)

return max(res)
    

solution(s = "abab")
solution(s = "ababcab")
solution("a")

solution("abcabcabcabc") # 4
solution("abccbaabccba") # 2
solution("abccba abccba") # 2
