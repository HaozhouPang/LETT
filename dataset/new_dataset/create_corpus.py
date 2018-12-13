with open('new_data.txt','r') as f:
    lines = f.readlines()
    new = ""
    for i in lines:
        new += i.strip()

with open('data.txt','w') as f:
    f.write(new)
