"""
Design a cash register drawer function checkCashRegister() that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument. cid is a 2D array listing available currency. Return the string "Insufficient Funds" if cash-in-drawer is less than the change due. Return the string "Closed" if cash-in-drawer is equal to the change due.
"""

def check_cash_register(price, cash, cid):
    change = 0
    total = 0
    cash_values = {
        "PENNY": .01,
        "NICKEL": .05,
        "DIME": .1,
        "QUARTER": .25,
        "ONE": 1,
        "TEN": 10
    }
    for lst in cid:
        total += cash_values[lst[0]] * lst[1]
    print(total)

check_cash_register(10, 15, [["PENNY", 8], ["NICKEL", 4], ["DIME", 3], ["QUARTER", 4], ["ONE", 6]])
