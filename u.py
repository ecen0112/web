def counted (d):
    d = d.upper()
    t = {}

    for i in d:
        if 'A' <= i <= 'Z':
            t[i] = t.get(i,0)+1

    return t


string = input("enter a string :")
s = counted(string)
for i in sorted(s):
    print(f"{i} = {s[i]}")