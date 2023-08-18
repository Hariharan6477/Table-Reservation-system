#main_window

from ast import Add
from email import message
from tkinter import *
from tkinter import messagebox
from tkinter.tix import Tree
from abspath import relative_to_assets
from baseclass import *
from modify_ds import *
from send_mail_module import check, Send_Mail
from customer_data import *
from history import add_history, cancel_history
import random
import time

BaseTree = CustomerData_Tree()
root_node = None
guest_id = 0

mainwindow = Tk() #calling the Tk() function creates a whole tkinter instance
   
mainwindow.geometry("1100x600")
mainwindow.configure(bg = "#FFFFFF")

    
#class containing all stationary pages like menu, contact, aboutus and location
class Static_pages():
    def __init__(self,parent_window):
        self.pw = parent_window
        
    #method to create the contact page
    def contact(self):
        self.window = Toplevel(self.pw) #toplevel class is used as we need more than one window in the gui at a time
        self.window.geometry("1100x600")    #Calling the Toplevel function creates a window under the root tkinter instance
        
        self.window.wm_transient(self.pw) #wm_transient is used to put the child window in front of the parent window
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
    
        image_image_1 = PhotoImage(
            file=relative_to_assets("Contact.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )

        self.window.resizable(False,False)
        self.window.mainloop()
        
    #method to create the about us page
    def aboutus(self):
        self.window = Toplevel(self.pw)
        self.window.geometry("1100x600")
        
        self.window.wm_transient(self.pw) #wm_transient is used to put the child window in front of the parent window
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
    
        image_image_1 = PhotoImage(
            file=relative_to_assets("About_us.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )

        self.window.resizable(False,False)
        self.window.mainloop()
    
    #method to create the location page
    def location(self):
        self.window = Toplevel(self.pw)
        self.window.geometry("1100x600")
        
        self.window.wm_transient(self.pw)
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
    
        image_image_1 = PhotoImage(
            file=relative_to_assets("Frame1.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )

        self.window.resizable(False,False)
        self.window.mainloop()
     
    #method to create the menu page
    def Menu(self):
        self.window = Toplevel(self.pw)
        self.window.geometry("1100x600")
        
        self.window.wm_transient(self.pw)
        
        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
    
        image_image_1 = PhotoImage(
            file=relative_to_assets("Menucard.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )

        self.window.resizable(False,False)
        self.window.mainloop()



#class containing all pages to book a table or check availability
class _page():
    


    def __init__(self,parent_window):
        self.pw = parent_window
        self.password = '1234'

    
    #method to open the book table window
    def Book_table_window(self):

        book_table_win=Toplevel(self.pw) #creates window under root instance
        
        book_table_win.geometry("1100x600")
        book_table_win.configure(bg = "#FFFFFF")


        canvas = Canvas(
            book_table_win,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("bg.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("sidebar.png"))
        image_2 = canvas.create_image(
            225.0,
            300.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("fill_details.png"))
        image_3 = canvas.create_image(
            221.0,
            58.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("plan_day.png"))
        image_4 = canvas.create_image(
            769.0,
            61.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("Name.png"))
        image_5 = canvas.create_image(
            109.0,
            154.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("seats.png"))
        image_6 = canvas.create_image(
            784.0,
            182.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("time.png"))
        image_7 = canvas.create_image(
            770.0,
            311.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("mail.png"))
        image_8 = canvas.create_image(
            109.0,
            267.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("phone.png"))
        image_9 = canvas.create_image(
            109.0,
            389.0,
            image=image_image_9
        )
        
        #the entry boxes are made global so that they can be called wherever required
        global entry_slot 
        global entry_no_of_seats 
        global entry_phone 
        global entry_name 
        global entry_mail_id 
        
        #text widget is used to get inputs
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        entry_bg_1 = canvas.create_image(
            769.0,
            352.5,
            image=entry_image_1
        )
        entry_slot = Text(book_table_win,
            bd=0,
            bg="#000000",
            highlightthickness=0,
            fg="#FFFFFF",
            font=("Courier","15")
        )
        entry_slot.configure(insertbackground="white")
        entry_slot.place(
            x=602.0,
            y=330.0,
            width=334.0,
            height=43.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_22.png"))
        entry_bg_2 = canvas.create_image(
            769.0,
            230.5,
            image=entry_image_2
        )
        entry_no_of_seats = Text(book_table_win,
            bd=0,
            bg="#000000",
            fg="#FFFFFF",
            highlightthickness=0,
            font=("Courier","15")
        )
        entry_no_of_seats.configure(insertbackground="white")
        entry_no_of_seats.place(
            x=602.0,
            y=208.0,
            width=334.0,
            height=43.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_33.png"))
        entry_bg_3 = canvas.create_image(
            221.0,
            429.5,
            image=entry_image_3
        )
        entry_phone = Text(book_table_win,
            bd=0,
            bg="#000000",
            highlightthickness=0,
            fg="#FFFFFF",
            font=("Courier","15")
        )
        entry_phone.configure(insertbackground="white")
        entry_phone.place(
            x=44.0,
            y=406.0,
            width=354.0,
            height=45.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_44.png"))
        entry_bg_4 = canvas.create_image(
            221.0,
            193.5,
            image=entry_image_4
        )
        entry_name = Text(book_table_win,
            bd=0,
            bg="#000000",
            highlightthickness=0,
            fg="#FFFFFF",
            font=("Courier","15")
        )
        entry_name.configure(insertbackground="white")
        entry_name.place(
            x=44.0,
            y=170.0,
            width=354.0,
            height=45.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_55.png"))
        entry_bg_5 = canvas.create_image(
            221.0,
            306.5,
            image=entry_image_5
        )
        entry_mail_id = Text(book_table_win,
            bd=0,
            bg="#000000",
            highlightthickness=0,
            fg="#FFFFFF",
            font=("Courier","15")
        )
        entry_mail_id.configure(insertbackground="white")
        entry_mail_id.place(
            x=44.0,
            y=283.0,
            width=354.0,
            height=45.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_show.png"))
        button_1 = Button(book_table_win,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Show_table_window,
            relief="flat"
        )
        button_1.place(
            x=44.0,
            y=519.0,
            width=354.0,
            height=47.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_book.png"))
        button_2 = Button(book_table_win,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.BOOK_TABLE,
            relief="flat"
        )
        button_2.place(
            x=602.0,
            y=460.0,
            width=339.0,
            height=45.0
        )
        
        
        book_table_win.resizable(False, False)
        book_table_win.mainloop()
        
        
        
    #method to create availability page
    def Show_table_window(self):

        show=Toplevel(self.pw) #creates a new window under the root tkinter instance
        
        show.title("availability")
        show.geometry("900x550")
        show.configure(bg="black")
        
        txt = show_all_tables() #retrieves the data from ds as string
        
        label_time = Label(show, font=("Lucida Bright",15),fg="red",bg="black") #label to display time
        label = Label(show,text = txt,font=("Lucida Bright",15),fg="#FFFFFF",bg="black") #label to display availability
        
        #button to close the window
        button_exit = Button(show,borderwidth=0,bg="black",fg="white", text = "Exit",font=("Lucida Bright",15), command = show.destroy)
        
        #the update function runs itself every 1000 ms
        #thus the page is refreshed every second and updates the data
        def update():
            current_time = ' \n   Time :    ' + str(time.ctime(time.time())) + '\n' #time.time() returns the current time of the system
            label_time['text'] = current_time
            label['text'] = show_all_tables()
            show.after(1000, update) # run itself again after 1000 ms

        # run the update fn manually for the first time alone
        update()
        
        label_time.pack()
        label.pack()
        button_exit.pack()
        
        show.mainloop()
        
        
    
    #method to book table and send a notifying mail
    def BOOK_TABLE(self):
        global BaseTree
        global root_node
        global guest_id
        #list is in the form [name,email,phone]
        #list for table details [no of seats,slot]
        user_details = [entry_name.get("1.0",'end-1c'), entry_mail_id.get("1.0",'end-1c'), entry_phone.get("1.0",'end-1c')]
        table_details = [entry_no_of_seats.get("1.0",'end-1c'), entry_slot.get("1.0",'end-1c')]

        #[ name, mail, phone, seats, slot, id]
        entire_details = [entry_name.get("1.0",'end-1c'), entry_mail_id.get("1.0",'end-1c'), entry_phone.get("1.0",'end-1c'),
            entry_no_of_seats.get("1.0",'end-1c'), entry_slot.get("1.0",'end-1c')]

        #check if any of the fields are empty
        for i in entire_details:
            if (not i) or i.isspace() :
                messagebox.showerror("ERROR","*All fields are mandatory")
                return True
        #check if the given mail id is valid
        if check(user_details[1]) == False:
            messagebox.showerror("Invalid Email", "Enter a valid mail id")
            return True
        #check if the phone number is valid
        elif user_details[2].isnumeric() == False or len(user_details[2]) != 10:
            messagebox.showerror("Invalid phone number","Enter a valid number")
            return True
        #check if the given slot is valid
        elif table_details[0].isnumeric() == False:
            messagebox.showerror("Invalid slot","slot should be an integer(bw 1-6")
            return True
        elif table_details[1].isnumeric():
            if int(table_details[1]) > 6 or int(table_details[1]) <= 0 :
                messagebox.showerror("Invalid slot","enter a valid slot!")
                return True
        else:   #if all conditions are satisfied, proceed further
            pass
        
        no_of_seats = int(table_details[0])
        slot = int(table_details[1])
        
        
        #make the entry slots empty for further bookings
        entry_slot.delete("1.0","end")
        entry_no_of_seats.delete("1.0","end")
        entry_phone.delete("1.0","end")
        entry_name.delete("1.0","end")
        entry_mail_id.delete("1.0","end") 

        
        #check if the required seats are available at gien slot, then proceed further
        if check_availability(no_of_seats,slot):
            
            b_id = guest_id
            guest_id+=1
            entire_details.append(b_id)
            
            Book_table(no_of_seats,slot)
            add_history(entire_details)
            #add the entire data to the avl tree
            root_node = BaseTree.insert_node(root_node, entire_details)

            user_message = '''
            Hi {},
            Booking details:
            Booking ID: {}
            Name: {}
            mail id: {}
            phone number: {}
            
            {} seats booked at slot {} successfully!!
            
            Thank you, have a nice day! 
            '''.format(user_details[0],b_id,user_details[0],user_details[1],user_details[2],table_details[0],table_details[1])
            

            manager_message = '''
            
            Booking details:
            Booking ID: {}
            Customer Name: {}
            Customer mail id: {}
            Customer phone number: {}
            
            {} seats booked at slot {}

            '''.format(b_id, user_details[0],user_details[1],user_details[2],table_details[0],table_details[1])
            
            #send a mail to both user and manager notifying abt the booking
            Send_Mail(user_details[1], user_message, manager_message)
            
            new_win = Toplevel()
            new_win.geometry("500x500")
            image_success = PhotoImage(
                file=relative_to_assets("Book_s.png"))
            label1 = Label( new_win, image = image_success)
            label1.place(x = 0, y = 0)
            label1.pack()
            new_win.mainloop()        
           
        else:
            new_win_f = Toplevel()
            new_win_f.geometry("500x500")
            image_success_not = PhotoImage(
                file=relative_to_assets("Book_ns.png"))
            label1 = Label( new_win_f, image = image_success_not)
            label1.place(x = 0, y = 0)
            label1.pack()
            new_win_f.mainloop()
            
        return True
    


    def cancel_table_window(self):
        
        global c_win

        
        c_win = Toplevel(self.pw)
        
        c_win.title("cancel_table (admin only)")
        c_win.geometry("1100x600")
        c_win.configure(bg="black")
        
        canvas = Canvas(
            c_win,
            bg = "#FFFFFF",
            height = 600,
            width = 1100,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
    
        image_image_1 = PhotoImage(
            file=relative_to_assets("CancelImage.png"))
        image_1 = canvas.create_image(
            550.0,
            300.0,
            image=image_image_1
        )
        

        global entry_id
        global entry_pass
        
        entry_id = Entry(c_win, borderwidth = 0, bg="white")
        entry_pass = Entry(c_win, borderwidth = 0, bg="white")
        
        b_can = Button(c_win,borderwidth=0,bg="#F32424",fg="white", text = "Cancel Table",font=("Lucida Bright",15), command = self.cancel_table_button)
        

        
        entry_id.place(x = 458,
        y =  261,
        width =  447,
        height = 42)
        
        entry_pass.place(x = 458,
        y =  347,
        width =  447,
        height = 42)
        
        b_can.place(x = 588,
        y =  424,
        width =  220,
        height = 35)
        
        c_win.mainloop()
        


    def cancel_table_button(self):
    
        global BaseTree
        global root_node
        global guest_id

        entry_id_val = entry_id.get()
        passw = entry_pass.get()
        
        if int(entry_id_val) >= guest_id:
            messagebox.showerror("ID invalid","enter a valid guest_id")
            return True
        elif passw != '1234':
            messagebox.showerror("Error","incorrect password")
            return True
        else:
            pass
            
    
        cancel_history(entry_id_val)

        e_id = int(entry_id_val)
        no_of_seats_tbd = BaseTree.search_seats(root_node, e_id)
        no_of_slot_tbd = BaseTree.search_slot(root_node, e_id)

        root_node = BaseTree.delete_node(root_node, e_id)

 
        na = int(no_of_seats_tbd)
        nb = int(no_of_slot_tbd)
        cancel_table(na,nb)
        
        c_win.destroy()
        
        cancelled_win = Toplevel(self.pw)
        
        cancelled_win.title("cancel_table_succesfull ")
        cancelled_win.geometry("300x100")
        cancelled_win.configure(bg="black")
        cancelled_win.wm_transient(self.pw)
        
        label = Label(cancelled_win, text = "Table cancelled successfully",font=("Lucida Bright",15),fg="white",bg="black")
        
        label.pack()
        
        cancelled_win.mainloop()
        
        return True




canvas = Canvas(
    mainwindow,
    bg = "#FFFFFF",
    height = 600,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    550.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    550.0,
    28.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=_page(mainwindow).Book_table_window,
    relief="flat"
)
button_1.place(
    x=661.0,
    y=450.0,
    width=314.0,
    height=44.0
)

button_image_cancel = PhotoImage(
    file=relative_to_assets("cancel_table.png"))
button_cancel = Button(
    image=button_image_cancel,
    borderwidth=0,
    highlightthickness=0,
    command=_page(mainwindow).cancel_table_window,
    relief="flat"
)
button_cancel.place(
    x=661.0,
    y=526.0,
    width=314.0,
    height=44.0
)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Static_pages(mainwindow).location,
    relief="flat"
)
button_2.place(
    x=748.0,
    y=13.0,
    width=300.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Static_pages(mainwindow).contact,
    relief="flat"
)
button_3.place(
    x=505.0,
    y=13.0,
    width=188.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Static_pages(mainwindow).aboutus,
    relief="flat"
)
button_4.place(
    x=246.0,
    y=13.0,
    width=188.0,
    height=30.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=Static_pages(mainwindow).Menu,
    relief="flat"
)
button_5.place(
    x=29.0,
    y=13.0,
    width=188.0,
    height=30.0
)
image_image_name = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    549.0,
    280.0,
    image=image_image_name
)
image_image_s = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    550.0,
    369.0,
    image=image_image_s
)

mainwindow.resizable(False, False)
mainwindow.mainloop() 

