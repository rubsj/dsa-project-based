"""
You are given a list of user access logs — each log is a string of actions (e.g. "foo", "app", "egg").
Group together all logs that have the same structural pattern — even if the letters are different.

Group isomorphic strings together — strings that follow the same character-to-character pattern.

Two strings are isomorphic if the characters in one string can be remapped to get the second string, while preserving the order.
"""
from collections import defaultdict

def get_pattern_key(s):
    pattern = []
    char_map = {}
    index =0
    for c in s :
        if c not in char_map:
            char_map[c] = index
            index +=1
        pattern.append(char_map[c])
    return tuple(pattern)

def patterned_access_sequence(sequences):
    access_seq = defaultdict(list)
    for seq in sequences:
        pattern  = get_pattern_key(seq)
        access_seq[pattern].append(seq)
    return list(access_seq.values())

logs = ["foo", "app", "bar", "egg", "add"]

result = patterned_access_sequence(logs)
print(result)