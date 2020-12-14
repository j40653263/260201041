month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

if 3<=month<=6:
    if month==3:
        if day>=20:
            season = "Spring"
        else:
            season = "Winter"
    elif month==6:
        if day<21:
            season = "Spring"
        else:
            season = "Summer"
    else:
        season = "Spring"

elif month<=9:
    if month == 9:
        if day<22:
            season = "Summer"
        else:
            season = "Fall"
    else:
        season = "Summer"

elif month<=11:
    if month==11:
        if day<21:
            season = "Fall"
        else:
            season = "Winter"
    else:
        season = "Fall"

else:
    season = "Winter"

print("The season is",season)