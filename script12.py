
weight=int(input('Enter your weight: '))
unit=input('(L)lbs or (K)kgs')
if unit.upper()=='L':
    lbs=weight*0.45
    print(f'your weight in lbs is {lbs}')
else:
    converted=weight/0.45
    print(f'your weight in kgs is {converted}')
