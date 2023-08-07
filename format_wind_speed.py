from scrape import raw_wind_speed

METER_PER_SECONDS = 0.277778

separated_wind_speed = []

# Wind speed kilometer per hours.
wind_speed_km_h = []
# Wind speed meters per seconds.
wind_speed = []

# This for loop take all scrape data and append only data which is necessary.
for row in raw_wind_speed.find_all("td"):
    all_mobile_and_no_mobile = row.text
    separated_wind_speed.append(all_mobile_and_no_mobile)

# This for loop take every data for speed.
for i in range(0, 8):
    wind_speed_km_h.append(separated_wind_speed[i].split()[2])

    speed = wind_speed_km_h[i].split("-")
    min_speed = round(int(speed[0]) * METER_PER_SECONDS)
    max_speed = round(int(speed[1]) * METER_PER_SECONDS)
    wind_speed.append(f"{min_speed}-{max_speed}")