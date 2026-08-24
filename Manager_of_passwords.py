import random
import string
import csv
habits = []
service = input("Hello, for which service would you like to generate password?")
ps_length = int(input("Please write how many digit password do you need?"))
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = ps_length))
with open("PiT.txt", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([service,  password])
answer = str
while (answer != "4"):
    answer = input("Saved! What would you like to do now? You can add a password by pressing 1, remove a password by pressing 2, see your passwords by pressing 3, or end the programm by pressing 4.")
    if (answer == "1"):
        service = input("For which service would you like to generate password?")
        ps_length = int(input("Please write how many digit password do you need?"))
        password = ''.join(random.choices(string.ascii_letters + string.digits , k = ps_length))
        with open("PiT.txt", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([service , password])
        pass
    elif (answer == "2"):
        removal = input("For which service would you like to remove password?")
        rows = []
        with open("PiT.txt", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
            new_rows = []
            for row in rows:
                if row[0] != removal:
                    new_rows.append(row)
        with open("PiT.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)


    elif (answer == "3"):
        choice = input("Would you like to see some specific passwords for an exact service or all of them, if an exact service press 1, if you wish to view them all press 2")
        if choice == "1":
            service = input("Please write the name of service")
            rows = []
            with open("PiT.txt", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)
                servicerows = []
                for row in rows:
                    if row[0] == service:
                        servicerows.append(row)
                print(servicerows)
        

        if choice == "2":
            with open("PiT.txt", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        
    elif (answer == "4"):
        print("Bye bye")
    else:
        answer = input("Please enter a valid answer!")
        continue
