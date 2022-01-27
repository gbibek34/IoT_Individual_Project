import csv
from datetime import date, datetime

today = date.today()
date = today.strftime("%d-%b-%Y")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def authentication(data):
    matched = None
    with open("Authenticated_users.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count+=1
                continue
            if f"{row[1]},{row[2]}" == f"{data}":
                # print("yay")
                matched = row[0]
                break
            else:
                # print("nay")
                continue
    return matched

def record(user_data):

    with open("Record.csv", 'a') as csv_file:
        csv_fileWriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_fileWriter.writerow([authentication(user_data), date, current_time]) 