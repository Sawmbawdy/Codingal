Amount = int(input("Enter you withdrawal amount "))
note_100 = Amount//100
note_50 = (Amount%100)//50
note_10 = ((Amount%100)%50)//10
print("You will recieve \n")
print(note_100, "-100 bills,")
print(note_50, "-50 bills and")
print(note_10, "-10 bills.")
