def check_age(age):
    if age >= 18:
        return True
    return False

def is_citizen_check(answer):
    if answer.lower() == 'да':
        return True
    return False

def is_disqualified_check(answer):
    if answer.lower() == 'да':
        return True
    return False

def main_check(is_age, is_citizen, is_disqualified):
    if is_age and is_citizen and not is_disqualified:
        return 'Вы имеете право голосовать'
    else:
        return 'Вы не имеете права голосовать'


user_age = int(input('Введите возраст:\n'))
user_is_citizen = input('Вы гражданин этой страны? (да/нет):\n')
user_is_disqualified = input('Имеется ли дисквалификация/запрет на участие в голосовании? (да/нет):\n')

print(main_check(
    check_age(user_age),
    is_citizen_check(user_is_citizen),
    is_disqualified_check(user_is_disqualified))
)