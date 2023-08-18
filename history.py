import os.path
import csv

#the exists function checks whether the file is present or not and accordingly return True/False
file_exists = os.path.exists('customer_history.csv')

#function to add the user and table details to a csv file
def add_history(entire_details):
    
    if file_exists:  #if file exists, data is appended in the existing file
        with open("customer_history.csv","a") as file:
            file_w = csv.writer(file)
            
            file_w.writerow(entire_details) #writerow() is used as we are writing a single row at a time
            
    else:   #if file does not exist, it is created and data is written using 'w' mode
        with open("customer_history.csv","w") as file:
            file_w = csv.writer(file)
            file_w.writerow(entire_details)

    return

def cancel_history(id_val):
        with open("customer_history.csv",'r') as file:
            csvreader = csv.reader(file)
            data = []
            for row in csvreader:
                if row != []:
                    data.append(row)
        
        for single_row in data:
            if id_val in single_row:
                single_row[5] = "--cancelled--"
               
        with open("customer_history.csv","w") as f:
            file_m = csv.writer(f)
            for i in data:
                file_m.writerow(i)
