age = int(input('Введите возраст:\n'))

is_citizen = input('Вы гражданин этой страны? (да/нет):\n')
if is_citizen.lower() == 'да':
    is_citizen = True
else:
    is_citizen = False

is_disqualified = input('Имеется ли дисквалификация/запрет на участие в голосовании? (да/нет):\n')
if is_disqualified.lower() == 'да':
    is_disqualified = True
else:
    is_disqualified = False

if age >= 18 and is_citizen and not is_disqualified:
    print('Вы имеете право голосовать')
else:
    print('Вы не имеете права голосовать')
