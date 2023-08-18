from baseclass import BaseTable
import csv


def ceildiv(a, b):  #returns number of tables when no_of_seats is given
    return (-(a // -b))

def check_availability(no_of_seats,slot):   #returns True if required number of tables are available, else false
    no_of_tables = ceildiv(no_of_seats,4)
    no_of_tables_available = 0
    for i in BaseTable:
        if slot in i[1]:
            no_of_tables_available+=1
    if no_of_tables_available < no_of_tables:
        return False
    else:
        return True

def show_all_tables():  #returns string that shows the availability of tables
    final_str = '''6 slots are available   
        1st slot - 11:00 am to 12:00 pm
        2nd slot - 12:00 pm to 1:00 pm
        3rd slot - 1:00 pm to 2:00 pm
        4th slot - 7:00 pm to 8:00 pm
        5th slot - 8:00 pm to 9:00 pm
        6th slot - 9:00 pm to 10:00 pm\n\n       ____________Seats Available____________\n\n''' #default string with timing/slot info
        
    for a in range(1,7):
        seats = 0
        for i in BaseTable:
            if a in i[1]:
                seats+=4
        final_str += "Slot: " + str(a) + " --  " + str(seats) +" seats remaining \n"
        
    return final_str

def Book_table(no_of_seats,slot):   #modifies the data structure, and changes the availability of tables
    if check_availability(no_of_seats,slot) == True:
        no_of_tables = ceildiv(no_of_seats,4)
        while no_of_tables != 0:
            for i in BaseTable:
                if slot in i[1]:
                    BaseTable.book_slot(i[0],slot)
                    break
            no_of_tables-=1
            
def cancel_table(no_of_seats,slot):     #modifies the data structure, and changes the availability of tables
    no_of_tables = ceildiv(no_of_seats,4)
    while no_of_tables != 0:
        for i in BaseTable:
            if slot not in i[1]:
                BaseTable.cancel_slot(i[0],slot)
                break
        no_of_tables-=1





