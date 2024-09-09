from art import art
print(art)
bids = {}
stop = False

def find_highest_bidder(all_bids):     
    highest_bid = 0
    name = ""
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            name = key

    print(f"The winner of the bids is {name} and they bidded ${bids[name]}")

while not stop:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    ask = input("Are there any other bidders? Type 'yes' or 'no': ")
    if ask == 'no':
        stop = True
        find_highest_bidder(bids)
    else:
        print("\n"*10)