amount = float(input("Enter the dollaramount to wihdraw: \n"))
#calculating number of notes

note_1 = amount // 100 #notes of 100
note_2 = (amount % 100) // 50 #notes of 50
note_3 = ((amount % 100)%50) // 20 #notes of 20
note_4 = ((amount % 100)%50) // 10 #notes of 10
note_5 = (((amount % 100)%50) %10) // 5 #notes of 5
coin_1 = ((((amount % 100)%50) %10) %5) // 2 #coins of 2
coin_2 = (((((amount % 100)%50) %10) %5) %2) // 1 #coins of 1
cent_1 = (((((amount % 100)%50) %10) %5) %2) // 0.5 #cents of 50
cent_2 = ((((((amount % 100)%50) %10) %5) %2) %1) // 0.2 #cents of 20
cent_3 = (((((((amount % 100)%50) %10) %5) %2) %1) %0.5) // 0.1 #cents of 10

print("The number of notes you will receive are:")
print("Notes of 100:", int(note_1))
print("Notes of 50:", int(note_2))
print("Notes of 20:", int(note_3))
print("Notes of 10:", int(note_4))
print("Notes of 5:", int(note_5))
print("Coins of 2:", int(coin_1))
print("Coins of 1:", int(coin_2))
print("Cents of 50:", int(cent_1))
print("Cents of 20:", int(cent_2))
print("Cents of 10:", int(cent_3))
















