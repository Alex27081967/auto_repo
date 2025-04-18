def is_year_leap(year):
    return year % 4 == 0


year_to_check = int(input("Введите год: "))
is_leap = is_year_leap(year_to_check)
print(f"год {year_to_check}: {is_leap}")
