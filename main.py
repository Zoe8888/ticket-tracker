from tkinter import *
from tkinter import messagebox


# Window initialized
class TicketSales:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Ticket Tracker")
        self.parent.geometry("600x500")
        self.parent.resizable("False", "False")
        self.parent.config(bg="#bd615b")

        # Cell label & entry point created & positioned
        self.lblcell = Label(self.parent, text="Please enter your cell number:")
        self.lblcell.place(relx=0.1, rely=0.1)
        self.cellentry = Entry(self.parent)
        self.cellentry.place(relx=0.5, rely=0.1)

        # Ticket label created & positioned
        self.lblticket = Label(self.parent, text="Select ticket category:")
        self.lblticket.place(relx=0.1, rely=0.2)
        # Ticket option menu created & positioned
        self.variable = StringVar()
        self.variable.set("Select Ticket")
        self.options = ["Soccer", "Movie", "Theater"]
        self.ticket_menu = OptionMenu(self.parent, self.variable, *self.options)
        self.ticket_menu.place(relx=0.5, rely=0.2)

        # Number of tickets label & entry point created & positioned
        self.lblnum = Label(self.parent, text="Number of tickets bought:")
        self.lblnum.place(relx=0.1, rely=0.3)
        self.num_spinbox = Spinbox(self.parent, width=15, bg="white")
        self.num_spinbox.place(relx=0.5, rely=0.3)

        # Calculate button created & positioned
        self.calc_btn = Button(self.parent, text="Calculate Button", command=self.calc_prepayment)
        self.calc_btn.place(relx=0.1, rely=0.4)
        # Clear Entries button created & positioned
        self.clear_btn = Button(self.parent, text="Clear Entries", command=self.clear)
        self.clear_btn.place(relx=0.5, rely=0.4)

        # Frame created & positioned
        self.frame = Frame(self.parent, width=400, height=150)
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
            if len(self.cellentry.get()) > 10 or len(self.cellentry.get()) < 10:
                # If cell number is > or < then 10 digits it will raise an error
                raise ValueError

            elif "Select Ticket" == self.variable.get():
                # If the type of ticket is not selected it will raise an error
                raise ValueError

            elif ticket == 0:
                # If amount of tickets = 0 it will raise an error
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
        self.lblcell.config(text="")


root = Tk()
TicketSales(root)
root.mainloop()