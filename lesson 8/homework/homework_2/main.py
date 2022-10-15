def date_second(second):
    minute = second // 60
    second %= 60

    hour = minute // 60
    minute %= 60

    day = hour // 24
    hour %= 24

    year = day // 365
    day %= 365

    return year, day, hour, minute, second
