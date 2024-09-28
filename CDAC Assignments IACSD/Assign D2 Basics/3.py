# accept amount from user and find the minimum number notes required to 
# get the amount amount =512  

amount = int(input("Enter the Amount - "))

notes = [2000,500,100,50,10,5,2,1]
print(f"₹ {amount} is the Amount \n")

for note in notes:

    current_n = amount // note
    amount = amount - current_n*note;
    print(f"₹{note} x ",current_n," Note",f'\t Remaining         Amount = ₹{amount}',sep="")

# Enter the Amount - 42892
# ₹ 42892 is the Amount

# ₹2000 x 21 Note  Remaining         Amount = ₹892
# ₹500 x 1 Note    Remaining         Amount = ₹392
# ₹100 x 3 Note    Remaining         Amount = ₹92
# ₹50 x 1 Note     Remaining         Amount = ₹42
# ₹10 x 4 Note     Remaining         Amount = ₹2
# ₹5 x 0 Note      Remaining         Amount = ₹2
# ₹2 x 1 Note      Remaining         Amount = ₹0
# ₹1 x 0 Note      Remaining         Amount = ₹0