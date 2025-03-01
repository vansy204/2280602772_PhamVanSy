lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
for line in lines:
    print(line)