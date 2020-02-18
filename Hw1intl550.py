# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:39:48 2020

@author: user
"""
import random 
class Portfolio():                                                                  #Creates Portfolio Object 
    def __init__(self,name):
        self.name=name
        self.Cash=0
        self.Stocks=[]                                                              #Keeps the bought Stocks for a certain Portfolio
        self.Mfund=[]                                                               #Keeps the bought Mutual Funds for a certain Portfolio
        self.history=[]                                                             #To keep the track of Transaction History
    def addCash(self,newCash):
        self.newCash=newCash
        self.Cash=self.Cash+newCash                                                 #Adds money to account
        self.history.append(str(self.newCash)+"$ added to the account")             #Adds the Succesful Transactions to History
        print("Transaction is Successful")
        print("Current Balance: "+str(self.Cash)+"$")
    def withdrawCash(self,nCash):
        self.nCash=nCash
        if self.Cash<nCash:
            print("Transaction is Unsuccessful")                                    #When the money which wanted to be withdrawn is
            print("Current Balance is "+str(self.Cash))                             #Less than money in the account gives an Error
        else:
            self.Cash=self.Cash-nCash                                               #Removes money form the account 
            print("Transaction is Successful")
            print("Current Balance "+str(self.Cash))
            self.history.append(str(self.nCash)+"$ removed from the account by withdrawn") #Adds the Succesful Transactions to History 
    def buyStock(self,piece,stock):
        self.piece=piece
        self.stock=stock                                                            #Checks if the number of the stocks multiply by
        if self.piece*stock.svalue<=self.Cash:                                      #the value is less or equal to Cash in the Account
            if stock.sname in self.Stocks:                                          #Checks if the stock with this name bought before         
                i=self.Stocks.index(stock.sname)                                    #if it is then it only adds the numbes of shares to it
                self.Stocks[i+1]+=self.piece
            else:                                                                   #if not it creates in the Stocks list for that certain Portfolio
                self.Stocks.append(stock.sname)
                self.Stocks.append(piece)
            self.Cash -=self.piece*stock.svalue                                     #Removes cash from the account calculated by number of shares and the value of stock
            j=self.Stocks.index(stock.sname)                                        #finds where the stock is in the list which have been just bought
            print("Transaction is successful")
            print("Current Balance "+ str(self.Cash))
            print("Current stock you have "+ str(self.Stocks[j])+" is "+str(self.Stocks[j+1]))
            self.history.append("Stock "+str(self.stock.sname)+": "+str(self.piece)+" shares bought for "+str(self.piece*stock.svalue)+"$") #Adds the Succesful Transactions to History 
        else:                                                                       #Gives an Error when the Balance is not sufficent to buy
            print("Transaction in not possible")
            print("Current Balance is not sufficent "+str(self.Cash))
            print("Required Balance is "+ str(stock.svalue*self.piece))
    def sellStock(self,name,share):
        self.share=share
        self.name=name
        if self.name in self.Stocks:                                                #Checks if the Stock which portfolio want to sell, is owned by him/her
            i=self.Stocks.index(self.name)                                          #Determines where the stock is in the list that portfolio wants to sell
            if self.share<=self.Stocks[i+1]:                                        #By using previous determination,checks either the portfolio has the number of stocks or not
                P=self.Stocks[i+1]*self.stock.svalue*random.uniform(0.5,1.5)        #if it has sells according to formula
                self.Cash +=P                                                       #adds the Cash to account
                self.Stocks[i+1] -=self.share                                       #removes share from Stocks list
                print("Transaction is Successful")
                print("Current Balance "+ str(self.Cash))
                print("Current "+str(self.Stocks[i])+" stock left: "+str(self.Stocks[i+1]))
                self.history.append("Stock "+str(self.name)+": "+str(self.share)+" shares sold for "+str(P)+"$") #Adds the Succesful Transactions to History 
                if self.Stocks[i+1]==0:                                             #Checks if portfolio sold all his stock with that name
                    self.Stocks.remove(self.name)                                   #if it has removes the stock name from the list
                    self.Stocks.pop(i)                                              #removes the number of stock left which is 0 from the list
            else:                                                                   #gives the error because of number of stocks portfolio wants to sell
                print("Transaction is Unsuccessful")
                print("You do not have "+str(self.share)+" of "+str(self.Stocks[i])+" stock ")
        else:                                                                       #Gives a name error
            print("Transaction is Unsuccessful")
            print("There is no stock named "+str(self.name))

    def buyMutualFund(self,share,Mvar):
        self.share=share*1.0                                                        #converts the integer share values the floats
        self.Mvar=Mvar.name
        if self.share<=self.Cash:                                                   #checks if the shares wanted to be bought is affordable
            self.Cash-=self.share                                                   #removes Cash according to the required share
            if self.Mvar in self.Mfund:                                             #checks if the mutual fund bought before
                i=self.Mfund.index(self.Mvar)                                       #determines location in the list Mfund
                self.Mfund[i+1]+=self.share                                         #increases number of shares in Mfund with the same name
                self.history.append("Mutual Fund "+str(self.Mvar)+": "+str(self.share)+" shares bought for "+str(self.share)+"$")#Adds the Succesful Transactions to History 
            else:
                self.Mfund.append(self.Mvar)                                        #Adds the Mutual Fund with that name to the Mfund
                self.Mfund.append(self.share)                                       #Adds the Mutual Fund with that share to the Mfund
                self.history.append("Mutual Fund "+str(self.Mvar)+": "+str(self.share)+" shares bought for "+str(self.share)+"$")#Adds the Succesful Transactions to History
    def sellMutualFund(self,name,share):
        self.name=name
        self.share=share*1.0                                                        #Converst the integer share to float
        if self.name in self.Mfund:                                                 #Checks if the fund wanted to be sold is in the list Mfund
            i=self.Mfund.index(self.name)                                           #determines the location of the fund wanted to be sold in the list Mfund 
            if self.share<=self.Mfund[i+1]:                                         #Using previous determination,cheks if the number of shares wanted to be sold is owned
                P=self.share*random.uniform(0.9,1.2)                                #determines the selling value
                self.Cash+=P                                                        #adds cash by previous determination
                self.Mfund[i+1]-=self.share                                         #decreases the number of shares sold from the list
                print("Transaction is successful")
                print("Current Balance "+ str(self.Cash))
                self.history.append("Mutual Fund "+str(self.Mvar)+": "+str(self.share)+" shares sold for "+str(P)+"$") #Adds the Succesful Transactions to History
                if self.Mfund[i+1]==0:                                              #Checks if portfolio sold all mutual funds with this name
                    self.Mfund.remove(self.name)                                    #if it has removes the name form list Mfund
                    self.Mfund.pop(i)                                               #And removes the number of shares left which is 0
            else:                                                                   #Gives an error for not having enough share to sell
                print("Transaction is Unsuccessful")
                print("Current share of "+str(self.Mfund[i]) +" you can sell "+str(self.Mfund[i+1]))
        else:                                                                       #gives a name error
            print("No Mutual Fund found with the name "+ str(self.name))
class Stock():                                                                      #Creates an object Stock
    def __init__(self,svalue,sname):
        self.svalue=svalue
        self.sname=sname
        
class MutualFund():                                                                 #Creates an object Mutual Fund
    def __init__(self,name):
        self.name=name

portfolio1 = Portfolio("Barney Stinson") #Creates a new portfolio
portfolio2=Portfolio("Ragnar Lothbrok")
portfolio1.addCash(7000) #Adds cash to the portfolio
portfolio2.addCash(200)
portfolio2.withdrawCash(50)
s=Stock(20,"Dunder Mifflin")
m=Stock(50,"Shelby Comp lmt")
l=MutualFund("Winterfell")
n=MutualFund("Wyk")
portfolio1.addCash(30)
print(portfolio1.Cash)
portfolio1.withdrawCash(500)
portfolio1.buyStock(15,s)
portfolio1.buyStock(30,m)
portfolio1.buyStock(3,s)
portfolio2.buyStock(1,m)
print(portfolio1.Stocks)
portfolio1.sellStock("Shelby Comp lmt",10)
portfolio1.sellStock("Dunder Mifflin",5)
portfolio1.sellStock("Dunder Mifflin",13)
print(portfolio1.Stocks)
portfolio1.buyMutualFund(7.3,l)
portfolio1.buyMutualFund(3.1,n)
portfolio1.buyMutualFund(2.1,l)
print(portfolio1.Mfund)
portfolio1.sellMutualFund("Winterfell",5)
portfolio1.sellMutualFund("Wyk",3.1)
portfolio1.sellMutualFund("Winterfell",5)
#print(portfolio1.Mfund)
print(portfolio1.history)
#print(portfolio2.history)