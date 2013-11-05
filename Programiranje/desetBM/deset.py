import re, string

sentence = "Tako je rekel (brez obotavljanja): Ce ne gremo, bomo ostali tu... Drzi?!"
punctuation = string.punctuation
print(punctuation)

sentence = re.sub(r"[!?:,.()]"," ",sentence)
print(sentence)
print()

sentence = "besedE, kI sE KoncajO Z mAlO"
sentence = re.findall(r"\w.+[A-Z]",sentence)
print("".join(sentence))

phone_numb_one = "12-34-56-7"
phone_numb_two = "1 2 3-45 6 7"
phone_numb_three = "+386 1234"
phone_numb_four = "123 - 4567"
phone_numb_five = "+386 1 123 4567"

telephone_numbers = [phone_numb_one, phone_numb_two, phone_numb_three, phone_numb_four, phone_numb_five]

for i,phone in enumerate(telephone_numbers):
    phone = re.findall(r"[+386]?\s?[1-7]?-?[1-9]",phone)
    phone = "".join(phone)
    if phone == telephone_numbers[i]:
        print("phone number: ", phone, "indeks: ",i)

#stevilka ulice
address_one = "Zofke Kvedrove ulica 25,"
address_two = "Trzaska ulica,"
address_three = "Trzaska ulica 1234324345,"

addresses = [address_one, address_two, address_three]
for a in addresses:
    address = re.findall("[^,]+[1-9],",a)
    address = "".join(address)
    if a == address:
        print(a + "==" + address)
    else:
        print(a + "!=" + address)

sentences = ["tule jih pa res ni", "a preudarno, govoriti o njihovem neobstoju bi bilo preuranjeno"]

def samoglasniki(sentence):
    samoglasniki_skupaj = re.findall(r"\w+[aeiou][aeiou]\w+",sentence)
    return samoglasniki_skupaj

for sentence in sentences:
    samo = samoglasniki(sentence)
    print(samo)