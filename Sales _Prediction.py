class Sales:

    def __init__(self,amt,year):
        self.year = int(year)
        self.amt = amt

    def profit(self, year):
        yearSales = self.amt + (self.amt*(int(year)-1)*0.05)
        return float(yearSales+yearSales*0.23)

user_amt=float(input("input the sales:"))
#user_year=input("input the year of sales:"))
user_year=input("input the Number of years you want to report:")
userSales=Sales(user_amt, user_year)

#print("The profit for the year", userSales.year,":", userSales.profit(int(user-year)))
for i in range(int(user_year)):
    i+1,":", userSales.profit(i)
#print("The profit for the year", i+1,":", userSales.profit(i)"):
