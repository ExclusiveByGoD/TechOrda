month = int(input("Введите месяц (число от 1 до 12): "))
day = int(input("Введите день (число от 1 до 31): "))

if (month == 12 and day >= 1) or (1 <= month <= 2):
    season = "зима"
elif 3 <= month <= 5:
    season = "весна"
elif 6 <= month <= 8:
    season = "лето"
elif 9 <= month <= 11:
    season = "осень"
else:
    season = "Некорректная дата"

print(f"Дата относится к сезону: {season}.")
