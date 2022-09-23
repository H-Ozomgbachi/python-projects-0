print('Welcome to VOTER ELIGIBILITY checker\n')

ageIntput = input('How old are you ?\nEnter your age : ')

ValidAge = ageIntput.isnumeric() and int(ageIntput) > 0

if not ValidAge:
    print('You have entered an invalid age, please retry')
else:
    age = int(ageIntput)
    if age >= 18:
        print('You are eligible to vote !')
    else:
        remaining = 18 - age
        print('Sorry, you are not eligible to vote. You can start voting in {} years time'.format(remaining))
