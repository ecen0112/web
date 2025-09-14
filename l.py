t ={

}
for k in range(10):
    i = input("enter a key :")
    a = input("enter a value :")
    t.update({i:a})

for i , c in t.items():
    print(f"keys {i} = values :{c}")