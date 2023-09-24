def permonth(filnavn):
    ordbok = {}
    fil = open(filnavn, "r")
    for linje in fil:
        data = linje.strip().split(",")
        month = data[0]
        temp = float(data[1])
        ordbok[month]=temp
        fil.close()
    return ordbok
monthly_records = permonth("max_temperatures_per_month.csv")
print(permonth("max_temperatures_per_month.csv"))

def sjekking_av_høyeste_temp(ordbok, filnavn):
    fil = open(filnavn, "r")
    for linje in fil:
        data = linje.strip().split(",")
        måned, dag, temp = data[0], data[1], float(data[2])
        if måned in ordbok:
            if temp> ordbok[måned]:
                ordbok[måned]=temp
    fil.close()
    return ordbok
oppdatert_ordbok = sjekking_av_høyeste_temp(monthly_records, "max_daily_temperature_2018.csv")

def updated_ennyfil(ordbok, filnavn):
    fil = open(filnavn, "w")
    for month, temperature in ordbok.items():
        line = "{}, {:.1f}\n".format(month, temperature)
        fil.write(line)


updated_ennyfil(oppdatert_ordbok, "updated_max_temperatures_per_month")


def varmebølgen(filnavn):
    fil = open(filnavn, "r")
    consecutive_hot_days = 0
    in_heatwave = False

    for linje in fil:
        måned, dag, temperatur = linje.strip().split(',')
        temperatur = float(temperatur)

        if temperatur > 25:
            consecutive_hot_days += 1
            if consecutive_hot_days >= 5 and not in_heatwave:
                in_heatwave = True
                start_date = f"{måned} {dag}"
        else:
            if in_heatwave:
                end_date = f"{måned} {dag}"
                print(f"Heatwave from {start_date} to {end_date}")
                in_heatwave = False
            consecutive_hot_days = 0

    fil.close()

# Example usage
varmebølgen("max_daily_temperature_2018.csv")




