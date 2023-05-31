import random 

code = random.randint(1000, 9999)

with open("random.txt", "a") as f:
    f.write(str(code) + "\n")


print(code)
