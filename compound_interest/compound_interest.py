class CompoundInterest:

    def __init__(self, principal, interest_rate, time_period):
        self.principal = principal
        self.interest_rate = interest_rate/100.00
        self.time_period = time_period
        self.number_invervals = 12
    
    def compound_interest(self):  
        return self.principal * (((1 + (self.interest_rate/self.number_invervals)) ** (self.number_invervals * self.time_period)))
    