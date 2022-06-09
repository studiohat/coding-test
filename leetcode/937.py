dig, let = [],[]

logs = ["dig1 9 1 5 1","let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

for i in logs:
    if i.split()[1].isdigit():
        dig.append(i)
    else:
        let.append(i)


let.sort(key=lambda x: (x.split()[1:],x.split()[0]))

logs = let + dig

print(logs)


