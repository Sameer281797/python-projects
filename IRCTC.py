class train:
    def __init__(self , name , seats , fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        
    print("Welcome to the Ticket Counter!")
    
    def getstatus(self):
        print("********************************************************")
        print(f"The name of the train is {self.name}")
        print(f"Seats available in the train are {self.seats}")
        print(f"The fare of the train is rs : {self.fare}")
        print("********************************************************")
        
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked ! Your seat number is {self.seats}")
            self.seats = self.seats-1
            
        else:
            print("Sorry all seats are booked !")
            
            
memo = train("memo" , 100 , 50)
memo.getstatus()
memo.bookticket()
memo.getstatus()
        
