import csv
import simplejson as json
import re

f = open('input.txt')
t = f.read()

data = t.split('\n\n')
requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

cleanedData = []


for d in data:
	cleanedData.append(json.loads('{"' + d.replace('\n', ' ').replace(':', '":"').replace(' ', '","') + '"}'))

def PartOne():
	validPassports = 0

	for cd in cleanedData:
		cd['valid'] = True
		for f in requiredFields:
			if f not in (cd.keys()):
				cd['valid'] = False
		if cd['valid'] == True:
			validPassports += 1

	return validPassports

def PartTwo():
	validPassports = 0
	validColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

	for cd in cleanedData:
		cd['valid'] = True

		for f in requiredFields:
			if f not in (cd.keys()):
				cd['valid'] = False

		if cd['valid']:
			if not 2020 <= int(cd['eyr']) <= 2030:
				cd['valid'] = False
			if not 1920 <= int(cd['byr']) <= 2002:
				cd['valid'] = False
			if not 2010 <= int(cd['iyr']) <= 2020:
				cd['valid'] = False
			if cd['hgt'][-2:] == 'cm':
				if not 150 <= int(cd['hgt'][:len(cd['hgt']) - 2]) <= 193:
					cd['valid'] = False
			elif cd['hgt'][-2:] == 'in':
				if not 59 <= int(cd['hgt'][:len(cd['hgt']) - 2]) <= 76:
					cd['valid'] = False
			else:
				cd['valid'] = False
			if not cd['ecl'] in validColours:
				cd['valid'] = False
			if not re.match('#([a-fA-F0-9]{6})', cd['hcl']):
				cd['valid'] = False
			if len(cd['pid']) != 9:
				cd['valid'] = False
			try:
				t = int(cd['pid'])
			except Exception as e:
				cd['valid'] = False

		if cd['valid'] == True:
			validPassports += 1

	return validPassports

def main():
    print(PartOne())
    print(PartTwo())

if __name__ == '__main__':
    main()