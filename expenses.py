#MY EXPENSES
#books
print("initial allowance = 2000")
allowance = 2000
spendings_on_books = 400
allowance -= spendings_on_books
print (f"(balance remaining after spending N400 on books is {allowance}")

#MONE UNDER BED
money_under_bed = 100
allowance += money_under_bed
print (f"(balance after you found N100 naira under your bed is {allowance}")

#SNACKS
snacks = 250
allowance -= snacks
print(f"(balance after you use N250 naira to get snack is {allowance}")

#SIBLING
percentage = 0.25 * allowance
allowance -= percentage
print (f"(balance after you gave your siblings 25% is {allowance}")

#DATA
one_third = 1/3 * allowance
allowance -= (one_third)
print(f"balance after buying data with onethird of your allowee is {allowance}")

allowance /= 2
print (f"balance after dividing your money into tithe and savings is {allowance}")

allowance %= 100
print(f"(balance after taking modulus 100 is {allowance}")
 

