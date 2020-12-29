import fileinput


def check_valid(message, rules):
	paths = [(rules[0][0], message)]
	
	while paths:
		path = paths.pop()
		current_rules, message = path[0], path[1]
		
		if not current_rules and not message:
			return True
		
		if not current_rules or not message:
			continue
		
		if isinstance(rules[current_rules[0]], str):
			if message[0] == rules[current_rules[0]]:
				paths.append((current_rules[1:], message[1:]))
		else:
			piped_rules = rules[current_rules[0]]
			for rule_set in piped_rules:
				paths.append((rule_set + current_rules[1:], message))
				
	return False
						

rules = dict()
reading_rules = True
messages = []
for line in fileinput.input():
	if line == "\n":
		reading_rules = False
		continue
	
	if reading_rules:
		data = line.strip().split(": ")
		start_rule = int(data[0])
		if '"' in data[1]:
			rules[start_rule] = data[1][1]
		else:
			piped_rules = data[1].split(" | ")
			rules[start_rule] = [[int(x) for x in rule.split()] for rule in piped_rules]
	else:
		messages.append(line.strip())
		
solution = 0
for message in messages:
	if check_valid(message, rules):
		solution += 1
	
print(solution)
