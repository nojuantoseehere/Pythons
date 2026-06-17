import random
import string

from exercises.Exer11_Rock_Paper_Scissor import play_again
from exercises.Exer13_BankingProgram import display_mgs

def init_cipher():
    chars = string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)
    return chars, keys

def get_original_text():
    while True:
        original_txt = input("Enter Text: ")

        if original_txt.strip() == "":
            display_mgs("Input cannot be blank!")
            continue

        return original_txt
            

def encrypt_text(chars,keys,original_txt):
    encrypted_txt=""
    for letter in original_txt:
        index = chars.index(letter)
        encrypted_txt += keys[index]

    return encrypted_txt

def decrpyt_text(chars,keys,original_txt):
    decrpyted_txt=""
    for letter in original_txt:
        index = keys.index(letter)
        decrpyted_txt += chars[index]
    return decrpyted_txt

def display_encrypted_decrypted_text(original_txt,encrypted_txt,decrypted_txt):
    print(f"Original Text: {original_txt}")
    print(f"Encrypted Text: {encrypted_txt}")
    print(f"Decrypted Text: {decrypted_txt}")



def main():
    chars,keys = init_cipher()
    is_running = True

    while is_running:
        original_txt = get_original_text()
        encrypted_txt = encrypt_text(chars,keys,original_txt)
        decrpyted_txt = decrpyt_text(chars,keys,encrypted_txt)
        display_encrypted_decrypted_text(original_txt,encrypted_txt,decrpyted_txt)
        is_running = play_again()


if __name__ == '__main__':
    main()