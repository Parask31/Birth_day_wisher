import pandas
import smtplib
import datetime as dt
import random

templates = []
# Reading all the letter templates and storing them in list as string
with open("letter_templates/letter_1.txt", 'r') as file1:
    template1 = file1.read()
    templates.append(template1)
with open("letter_templates/letter_2.txt", 'r') as file2:
    template2 = file2.read()
    templates.append(template2)
with open("letter_templates/letter_3.txt", 'r') as file3:
    template3 = file3.read()
    templates.append(template3)


MY_EMAIL = "testingsmtpparas@gmail.com"
MY_PASSWORD = "tester_101"

data = pandas.read_csv("birthdays.csv")
# These dict looks like these {'name':[all names list], 'email':[all emails list], 'year':[years list].....}
# In short dict of key:value pair as column_name:[All values in list]
data_dict = data.to_dict(orient="list")
now = dt.datetime.now()


if now.day in data_dict['day'] and now.month in data_dict['month']:
    # Index function to get index all list values are having corresponding value like
    # birthday year,date,month of same person
    index = data_dict['day'].index(now.day)

    name = data_dict['name'][index]
    email = data_dict['email'][index]

    # Choosing an random template from
    template = random.choice(templates)

    # Replace function to put the name of person to wish
    letter = template.replace("[NAME],", f"{name}")

    # Sending email via smtp
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )
