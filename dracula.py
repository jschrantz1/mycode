with open("345-0.txt","r") as foo:

    for line in foo:
        if "vampire" in line.lower():
            print(line)

count= 0
for line in foo:
    if "vampire" in line.lower():
        count += 1
print(count)


