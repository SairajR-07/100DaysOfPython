def find_highest_bid(bidingdictinary):
    winner=''
    highe_bid=0
    max(bidingdictinary)
    for bidder in bidingdictinary:
        bid=bidingdictinary[bidder]
        if bid>highe_bid:
            highe_bid=bid
            winner=bidder
    print("The winner is "+winner)

bids={}
bidding=True
while bidding:
    name=input("Enter your name: ")
    price=int(input("Enter your price: "))
    bids[name]=price
    _continue=input("Are there any other bidders? Y/N")
    if _continue=="N":
        bidding=False
        find_highest_bid(bids)
    elif _continue=="Y":
        print("\n" * 28)



