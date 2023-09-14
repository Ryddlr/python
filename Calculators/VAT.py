#VAT calculator for standard rated invoices
#Allow user to input gross amount or work done

print("VAT calculation for standard rated invoices")

Gross_Amount = input("Please Enter Gross Amount")

result = Gross_Amount

print(result)

a = float(Gross_Amount)
b = 0.06
c = a+b
d = 0.15*(a+c)

print("GetFund/NHIL & Covid Levies")

print(a+b)

print("Vat Exclusive Amount")

print(a+c)

print("VAT")

print(d)

print("Total Invoice Amount")

print(a+c+d)

#END
