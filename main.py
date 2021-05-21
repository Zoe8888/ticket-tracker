from tkinter import *
from tkinter import messagebox

root = Tk()
# Creating a title for the program
root.title("Ticket Tracker")
# Setting the dimensions
root.geometry("600x500")
# Ensuring the size of the program cannot be resized
root.resizable("False", "False")
# Setting a background color
root.config(bg="#bd615b")


# Window initialized
class TicketSales:
    def __init__(self, window):
        # Cell label & entry point created & positioned
        self.window = window
        self.lblcell = Label(self.window, text="Please enter your cell number:")
        self.lblcell.place(relx=0.1, rely=0.1)
        self.cellentry = Entry(self.window)
        self.cellentry.place(relx=0.5, rely=0.1)

        # Ticket label created & positioned
        self.lblticket = Label(self.window, text="Select ticket category:")
        self.lblticket.place(relx=0.1, rely=0.2)
        # Ticket option menu created & positioned
        self.variable = StringVar()
        self.variable.set("Select Ticket")
        self.options = ["Soccer", "Movie", "Theater"]
        self.ticket_menu = OptionMenu(self.window, self.variable, *self.options)
        self.ticket_menu.place(relx=0.5, rely=0.2)

        # Number of tickets label & entry point created & positioned
        self.lblnum = Label(self.window, text="Number of tickets bought:")
        self.lblnum.place(relx=0.1, rely=0.3)
        self.num_spinbox = Spinbox(self.window, width=15, bg="white")
        self.num_spinbox.place(relx=0.5, rely=0.3)

        # Calculate button created & positioned
        self.calc_btn = Button(self.window, text="Calculate Button", command=self.calc_prepayment)
        self.calc_btn.place(relx=0.1, rely=0.4)
        # Clear Entries button created & positioned
        self.clear_btn = Button(self.window, text="Clear Entries", command=self.clear)
        self.clear_btn.place(relx=0.5, rely=0.4)

        # Frame created & positioned
        self.frame = Frame(self.window, width=400, height=150)
        self.frame.place(relx=0.1, rely=0.6)

        # Receipt labels & entry points created & positioned
        self.amount = Label(self.frame, text="")
        self.amount.place(relx=0, rely=0)
        self.reserved = Label(self.frame, text="")
        self.reserved.place(relx=0, rely=0.1)
        self.cell = Label(self.frame, text="")
        self.cell.place(relx=0, rely=0.2)

    # Variables and constants initialized
    def calc_prepayment(self):
        ticket = int(self.num_spinbox.get())
        vat = 0.14

        # ValueError indicates that an error has occurred
        try:
            int(self.cellentry.get())
            # If cell number is > or < then 10 digits it will raise an error
            if len(self.cellentry.get()) > 10 or len(self.cellentry.get()) < 10:
                raise ValueError

            # If the type of ticket is not selected it will raise an error
            elif self.variable.get() == "Select Ticket":
                raise ValueError

            # If amount of tickets = 0 it will raise an error
            elif ticket == 0:
                raise ValueError

            # Calculation of soccer ticket(s)
            elif self.variable.get() == "Soccer":
                # Price in Rands
                price = 40
                amount_due = (price * ticket) + (price * vat * ticket)
                text = ("Amount due: R{}".format(amount_due))
                self.amount.config(text=text)

            # Calculation of movie ticket(s)
            elif self.variable.get() == "Movie":
                # Price in Rands
                price = 75
                amount_due = (price * ticket) + (price * vat * ticket)
                text = ("Amount due: R{}".format(amount_due))
                self.amount.config(text=text)

            # Calculation of theater ticket(s)
            elif self.variable.get() == "Theater":
                # Price in Rands
                price = 100
                amount_due = (price * ticket) + (price * vat * ticket)
                text = ("Amount due: R{}".format(amount_due))
                self.amount.config(text=text)

            # Receipt information displayed
            reserved_txt = "Reserved for {} for {}".format(self.variable.get(), ticket)
            self.reserved.config(text=reserved_txt)
            cell_txt = "was done by {}".format(self.cellentry.get())
            self.cell.config(text=cell_txt)

        except ValueError:
            messagebox.showerror(messagebox="Combination is invalid")

    # Defining the function that makes the "Clear" button operational
    def clear(self):
        self.cellentry.delete(0, END)
        self.cellentry.focus()
        self.variable.set("Select Ticket")
        self.num_spinbox.delete(0, END)
        self.num_spinbox.insert(0, 0)
        self.amount.config(text="")
        self.reserved.config(text="")
        self.cell.config(text="")


TicketSales(root)
root.mainloop()