import os

clear = lambda: os.system('cls')

bid_list={}

def input_details() :
    
    name=input("What is your name? ")
    bid=input("What is your bid? ")
    lengthOfBid= len(bid)
    bid_list[name]=int(bid[1:lengthOfBid])
    get_decision()
    

def get_decision():
    decision=input("Are there any other users who want to bid ? type yes or no :").lower()
    if decision=="yes":
        clear()
        input_details()

    elif decision=="no":
        clear()

        max_bid=0
        bid_person=""

        for bidder in bid_list:
            bid_amount=bid_list[bidder]
            if bid_amount>max_bid :
                max_bid=bid_amount
                bid_person=bidder

        print(f"The winner is {bid_person} with a bid of ${max_bid}")
        
            
input_details()





