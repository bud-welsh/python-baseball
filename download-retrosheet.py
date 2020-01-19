# https://www.retrosheet.org/events/1918eve.zip
# https://www.retrosheet.org/events/1919eve.zip

year_download = 1918

while year_download < 2020:
    file_address = "https://www.retrosheet.org/events/" + str(year_download) + "eve.zip"
    print(file_address)
    year_download += 1


