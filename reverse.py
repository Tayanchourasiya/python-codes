def reverse(s):
    tayan = " "
    for i in s:
        tayan = i + tayan
    return tayan
s = "chourasiya"
print("the original string :", end=" ")
print(s)
print("the reversed string :", end=" ")
print(reverse(s))
