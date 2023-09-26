def count_characters(lst):
    c = 0
    for i in lst:
        c+=len(i)
    return c
print(count_characters([
  "###",
  "###",
  "###"
]))