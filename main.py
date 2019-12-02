import pandas
import numpy
import pymysql
import os
from tabulate import tabulate
import time

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '1234',
    database = 'hotel'
)

c = conn.cursor()

clear = lambda: os.system('cls')

def create_reservation():
    try:
        print("Type Exit to exit: ")
        display = pandas.read_sql("select type as 'Type', price_per_day as 'Price' from rooms group by type;", conn)
        display.insert(0,'Options',[1,2,3,4])
        print(tabulate(display,
                       showindex=False,
                       tablefmt="fancy_grid",
                       headers='keys',
                       numalign='right'))
        options = int(input("Enter you option: "))
        if options == 1:
            c.execute("select distinct type from rooms limit 1;")
            room = tuple(c.fetchone())[0]
            c.execute(f"""select * from rooms where status != "Reserved" and type = "{room}";""")
            check = c.fetchone()
            if check == None:
                print("No room available.")
                time.sleep(2)
                clear()
            else:        
                print(f"{room}\nPlease enter the number of days")
                no_day = int(input("> "))
                c.execute(f"""select price_per_day from rooms where type = "{room}";""")
                total_price = int(tuple(c.fetchone())[0]) * no_day
                c.execute(f"""select room_no from rooms where status != "Reserved" and type = "{room}" limit 1;""")
                room_no = tuple(c.fetchone())[0]
                print(f"The total price will be Rs {total_price} and the room number will be {room_no}")
                confirm = input("Do you want to confirm you reservation?[y/n] ")
                if confirm == 'y':
                    name = input("Please enter your name: ")
                    phone = input("Pleas enter your phone number: ")
                    c.execute(f"""update rooms set status = 'Reserved' where type = "{room}" and status != 'Reserved' limit 1;""")
                    conn.commit()
                    c.execute(f"""insert into reservations values(Null, "{name}", "{phone}", "{room}", {room_no},{no_day}, {total_price});""")
                    conn.commit()
                    print("Your reservation is confirmed!!")
                    time.sleep(2)
                    clear()
                else:
                    print("Have a good day!!!")
                    time.sleep(2)
                    clear()

        elif options == 2:
            c.execute("select distinct type from rooms limit 1, 1;")
            room = tuple(c.fetchone())[0]
            c.execute(f"""select * from rooms where status != "Reserved" and type = "{room}";""")
            check = c.fetchone()
            if check == None:
                print("No room available.")
                time.sleep(2)
                clear()
            else:        
                print(f"{room}\nPlease enter the number of days")
                no_day = int(input("> "))
                c.execute(f"""select price_per_day from rooms where type = "{room}";""")
                total_price = int(tuple(c.fetchone())[0]) * no_day
                c.execute(f"""select room_no from rooms where status != "Reserved" and type = "{room}" limit 1;""")
                room_no = tuple(c.fetchone())[0]
                print(f"The total price will be Rs {total_price} and the room number will be {room_no}")
                confirm = input("Do you want to confirm you reservation?[y/n] ")
                if confirm == 'y':
                    name = input("Please enter your name: ")
                    phone = input("Pleas enter your phone number: ")
                    c.execute(f"""update rooms set status = 'Reserved' where type = "{room}" and status != 'Reserved' limit 1;""")
                    conn.commit()
                    c.execute(f"""insert into reservations values(Null, "{name}", "{phone}", "{room}", {room_no},{no_day}, {total_price});""")
                    conn.commit()
                    print("Your reservation is confirmed!!")
                    time.sleep(2)
                    clear()
                else:
                    print("Have a good day!!!")
                    time.sleep(2)
                    clear()

        elif options == 3:
            c.execute("select distinct type from rooms limit 2, 1;")
            room = tuple(c.fetchone())[0]
            c.execute(f"""select * from rooms where status != "Reserved" and type = "{room}";""")
            check = c.fetchone()
            if check == None:
                print("No room available.")
                time.sleep(2)
                clear()
            else:        
                print(f"{room}\nPlease enter the number of days")
                no_day = int(input("> "))
                c.execute(f"""select price_per_day from rooms where type = "{room}";""")
                total_price = int(tuple(c.fetchone())[0]) * no_day
                c.execute(f"""select room_no from rooms where status != "Reserved" and type = "{room}" limit 1;""")
                room_no = tuple(c.fetchone())[0]
                print(f"The total price will be Rs {total_price} and the room number will be {room_no}")
                confirm = input("Do you want to confirm you reservation?[y/n] ")
                if confirm == 'y':
                    name = input("Please enter your name: ")
                    phone = input("Pleas enter your phone number: ")
                    c.execute(f"""update rooms set status = 'Reserved' where type = "{room}" and status != 'Reserved' limit 1;""")
                    conn.commit()
                    c.execute(f"""insert into reservations values(Null, "{name}", "{phone}", "{room}", {room_no},{no_day}, {total_price});""")
                    conn.commit()
                    print("Your reservation is confirmed!!")
                    time.sleep(2)
                    clear()
                else:
                    print("Have a good day!!!")
                    time.sleep(2)
                    clear()

        elif options == 4:
            c.execute("select distinct type from rooms limit 3, 1;")
            room = tuple(c.fetchone())[0]
            c.execute(f"""select * from rooms where status != "Reserved" and type = "{room}";""")
            check = c.fetchone()
            if check == None:
                print("No room available.")
                time.sleep(2)
                clear()
            else:        
                print(f"{room}\nPlease enter the number of days")
                no_day = int(input("> "))
                c.execute(f"""select price_per_day from rooms where type = "{room}";""")
                total_price = int(tuple(c.fetchone())[0]) * no_day
                c.execute(f"""select room_no from rooms where status != "Reserved" and type = "{room}" limit 1;""")
                room_no = tuple(c.fetchone())[0]
                print(f"The total price will be Rs {total_price} and the room number will be {room_no}")
                confirm = input("Do you want to confirm you reservation?[y/n] ")
                if confirm == 'y':
                    name = input("Please enter your name: ")
                    phone = input("Pleas enter your phone number: ")
                    c.execute(f"""update rooms set status = 'Reserved' where type = "{room}" and status != 'Reserved' limit 1;""")
                    conn.commit()
                    c.execute(f"""insert into reservations values(Null, "{name}", "{phone}", "{room}", {room_no},{no_day}, {total_price});""")
                    conn.commit()
                    print("Your reservation is confirmed!!")
                    time.sleep(2)
                    clear()
                else:
                    print("Have a good day!!!")
                    time.sleep(2)
                    clear()

        else:
            print("Invalid option")
            time.sleep(2)

    except ValueError:
        print("Exiting")
        time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting")
        time.sleep(2)

def view_reservation():
    reservations = pandas.read_sql("select customer_name, phone, room_type, room_no, no_of_days, total_price from reservations;", conn)
    print(tabulate(reservations,
                   showindex=False,
                   tablefmt="psql",
                   headers=['Reservation Name', 'Phone Number','Room','Room Number', 'Number Of days', 'Price']))
    input()

def main():
    try:
        clear()
        while True:
            print("""Options:
    1. Create Reservations
    2. View Reservations
    3. Exit""")
            opt = input("> ")
            if opt == '1':
                clear()
                create_reservation()
            elif opt == '2':
                clear()
                view_reservation()
            elif opt == '3':
                break
            else:
                print("Invalid Option.")      

    except KeyboardInterrupt:
        pass

main()