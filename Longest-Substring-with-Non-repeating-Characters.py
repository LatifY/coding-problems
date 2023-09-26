def longest_nonrepeating_substring(txt):
    c=""
    for i in txt:
        if i not in c:c+=i
    return c

print(longest_nonrepeating_substring("abcabcbb")) # "abc"
print(longest_nonrepeating_substring("aaaaaa")) # "a"
print(longest_nonrepeating_substring("abcde")) # "abcde"
print(longest_nonrepeating_substring("abcda")) # "abcd"