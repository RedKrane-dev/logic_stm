def check_age(age):
    if age.isdigit():
        return int(age) >= 18

def is_citizen_check(answer):
    return answer.lower().strip() == 'да'

def is_disqualified_check(answer):
    return answer.lower().strip() == 'да'

def main_check(user_input_tuple):
    is_age, is_citizen, is_disqualified = user_input_tuple
    if is_age and is_citizen and not is_disqualified:
        return 'Вы имеете право голосовать'
    return 'Вы не имеете права голосовать'

def user_input():
    user_age = input('Введите возраст:\n')
    user_is_citizen = input('Вы гражданин этой страны? (да/нет):\n')
    user_is_disqualified = input('Имеется ли дисквалификация/запрет на участие в голосовании? (да/нет):\n')
    return user_age, user_is_citizen, user_is_disqualified

if __name__ == '__main__':
    main_check(user_input())
