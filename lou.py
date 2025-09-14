def coun(s):
    s = s.upper()
    t ={}

    for i in s:
        if 'A' <= i <='Z':
            t[i] = t.get(i,0)+1
    return t

i = input("enter a string :")
l = coun(i)
for c  in sorted(l):
    print(f"{c} = {l[c]}")

