print("Hello again!")

five_numbers = input("Could you write five-digit number, please? ")

a = int(five_numbers) // 10000
b = int(five_numbers) % 10000 // 1000
c = int(five_numbers) % 1000 // 100
d = int(five_numbers) % 100 // 10
e = int(five_numbers) % 10

# inverted_number = f"{e}{d}{c}{b}{a}"

inverted_number = e * 10000 + d * 1000 + c * 100 + b * 10 + a

print(inverted_number)

