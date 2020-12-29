import fileinput

inputs = []
current_input = ""
for line in fileinput.input():
    line = line.strip()
    if line == "":
        inputs.append(current_input.strip())
        current_input = ""
    else:
        current_input += line + " "
inputs.append(current_input.strip())
        
valid = 0
for input in inputs:
    data = input.split()
    if len(data) == 8 or len(data) == 7 and 'cid' not in input:
        valid += 1

print(valid)
