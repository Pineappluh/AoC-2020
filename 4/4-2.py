import fileinput

def check_valid(input):
    data = input.split()
    passport = dict()
    
    for pair in data:
        split_pair = pair.split(":")
        passport[split_pair[0]] = split_pair[1]
    print(passport)
        
    return check_valid_passport(passport)


def check_valid_passport(passport):
    if not ('byr' in passport and 1920 <= int(passport['byr']) <= 2002):
        return False
       
    if not ('iyr' in passport and 2010 <= int(passport['iyr']) <= 2020):
        return False
    
    if not ('eyr' in passport and 2020 <= int(passport['eyr']) <= 2030):
        return False
        
    if not ('hgt' in passport and \
           (passport['hgt'].endswith('cm') or passport['hgt'].endswith('in')) and \
           (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193 \
            or passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76)):
        return False
    
    if not ('hcl' in passport and len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all('a' <= x <= 'f' or '0' <= x <= '9' for x in passport['hcl'][1:])):
        return False
        
    if not ('ecl' in passport and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    
    if not ('pid' in passport and len(passport['pid']) == 9 and passport['pid'].isnumeric()):
        return False
        
    return True
    

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
    if check_valid(input):
        valid += 1

print(valid)
