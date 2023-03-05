DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def timestamp_to_date(seconds):
    year = 1970
    month = 0
    day = 0
    hours = 0
    minutes = 0
    seconds_t = 0

    days_till_now = 0     # Дни с начала эпохи
    remaining_time = 0    # Количество секунд после вычета дней с начала эпохи
    extra_days = 0        # Количество оставшихся дней после вычета лет
    is_leap = False       # Флаг високосного года

    month_index = 0       # Индекс для обхода DAYS_OF_MONTH


    days_till_now = seconds // (24*60*60)
    remaining_time = seconds % (24*60*60)


    # Подсчет лет
    while (days_till_now >= 365):
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):    # Учет високосности
            if days_till_now < 366:
                break

            days_till_now -= 366
        else:
            days_till_now -= 365

        year += 1


    # Включаем текущий день (для подсчета времени)
    extra_days = days_till_now+1


    # Високосность года (для февраля)
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        is_leap = True


    # Подсчет месяцев
    if (is_leap):                     # Год.Високосный == True
        while True:
            if (month_index == 1):    # В феврале, в високосном году, 29 дней
                if (extra_days-29 < 0):
                    break

                month += 1
                extra_days -= 29
            else:
                if (extra_days-DAYS_OF_MONTH[month_index] < 0):
                    break

                month += 1
                extra_days -= DAYS_OF_MONTH[month_index]

            month_index += 1
    else:
        while True:
            if (extra_days-DAYS_OF_MONTH[month_index] < 0):
                break

            month += 1
            extra_days -= DAYS_OF_MONTH[month_index]
            month_index += 1


    # Подсчет дня
    if (extra_days > 0):
        month += 1
        day = extra_days
    else:
        if (month == 2 and is_leap == 1):
            day = 29
        else:
            day = DAYS_OF_MONTH[month-1]


    # Подсчет времени (ЧЧ:ММ:СС)
    hours = remaining_time // (60*60)
    minutes = (remaining_time % (60*60)) // 60
    seconds_t = (remaining_time % (60*60)) % 60


    return f"{year}-{month}-{day} {hours}:{minutes}:{seconds_t}"


if __name__ == "__main__":
    ts = 1677567398
   #ts = int(input("Timestamp: "))

    print(timestamp_to_date(ts))
