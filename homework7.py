"""
Task 1: Time
Используя таймер мотоцикла, рассчитайте текущее время.
Возвращает ответ в виде суммы цифр, которую покажет цифровой таймер в формате чч:мм.
Task 2: LevelUP
Учитывая значения опыта, порога и награды,
проверьте, достигнете ли вы следующего уровня после убийства монстра.
Task 3: TimeConvert
Переконвертировать время из 24-часового формата в 12-часовой, используя следующие правила:
выходной формат должен быть 'чч:мм a.m.' (для часов до полудня)
или 'чч:мм p.m.' (для часов после полудня),
если часы меньше 10 - не пишите '0' перед ними.
"""


def main():
    # Task 1 Time
    time_after = int(input("enter amount of minutes "))
    day_time = "00:00"
    hours, minutes = map(int, day_time.split(":"))
    total_minutes = hours * 60 + minutes + time_after
    new_h = (total_minutes // 60) % 24
    new_m = total_minutes % 60
    time_str = f"{new_h:02d}{new_m:02d}"
    # results = sum(int(amount) for amount in time_str) - due to "too many variables"
    print(sum(int(amount) for amount in time_str))

    # Task 2 LevelUP
    experience = int(input("Enter experience value "))
    threshold = int(input("Enter threshold value "))
    reward = int(input("Enter reward value "))
    total_value = experience + reward
    if total_value >= threshold:
        print("true")
    else:
        print("false")

    # Task 3 Time converter
    entered_time = input("enter time in format hh:mm ")
    time_split = entered_time.split(":")
    hours = int(time_split[0])
    minutes = int(time_split[1])
    if hours == 0:
        hours = 12
        period = "a.m"
    elif hours < 12:
        period = "a.m"
    elif hours == 12:
        period = "p.m"
    else:
        hours = hours - 12
        period = "p.m"

    print(f"{hours}:{minutes} {period}")


if __name__ == '__main__':
    main()
