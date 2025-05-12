from os import system
import art

print(art.logo)
bidder = {}
bidding = True

# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

def highest_bid(bid_record):
    high_bid = 0
    winner = ""

    for bet in bid_record:
        bid_amount = bid_record[bet]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bet
    print(f"The winner is {winner} with a bid of ${high_bid}")

while bidding:
    name = input("What's your name? ")
    bid = int(input("what is your bid? $"))
    bidder[name] = bid
    then = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    if then == "yes":
        clear()
    elif then == "no":
        bidding = False
        highest_bid(bidder)
