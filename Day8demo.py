def life_in_weeks(age):
    t_age=90
    weekin_year=52

    year_left=t_age-age
    week_left=year_left*weekin_year

    print(f"You have {week_left} week left")


def greet(name,location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")

greet("sai","pune")

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caeser(original_text,shift_ammount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_ammount+=-1
        shifted_position = alphabet.index(letter) + shift_ammount
        shift_ammount %= len(alphabet)
        output_text = alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result={output_text}")

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text=input("Type your message: \n").lower()
shift=int(input("Type the shift number: \n"))



#encrypt(original_text=text,shift_ammount=shift)
#ecrypt(original_text=text,shift_ammount=shift)
caeser(original_text=text,shift_ammount=shift,encode_or_decode=direction)