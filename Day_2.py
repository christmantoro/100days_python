print ("Hari kedua adalah calculator tip dan total bill")

total_bill = int(input("Masukkan total bill: Rp "))
percentage_tip = int(input("Masukkan percentage tip: %"))
amount_of_people = int(input("Masukkan amount of people: "))

total_tip = total_bill * percentage_tip / 100
total_bill_per_person = round(total_tip + total_bill) / amount_of_people


print (f"Total yang harus dibayar sebesar: ", total_tip + total_bill, "Total yang harus dibayarkan per orang: ",total_bill_per_person)

print(type(total_bill_per_person))

if total_bill_per_person > 5000:
    print (f"wah ternyata kita harus pay more than 5000 per orang karena per orang harus bayar", total_bill_per_person)
else:
    print ("Tenang we should pay less than 5000")

