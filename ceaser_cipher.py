class CeaserCipher():

    
    def _shift_text(self, plaintext: str, jumps:int) -> str:
        """
        Shifts the text according to the "jumps", it's how many shifts it'll make
        Example in Ceaser Cipher: I want to shift 3 times, and in this case we have the sentence ('abc')
        it'll will become ('cde')
        This function is the core of the encryption and decryption logic.
        It works like a service in the backend.
        """
        result = ""
        for char in plaintext:
                if char.islower():
                    modified_code = ((ord(char) - ord('a') + jumps) % 26) + ord('a')
                    result = result + chr(modified_code)
                elif char.isupper():
                    modified_code = ((ord(char) - ord('A') + jumps)% 26 ) + ord('A')
                    result = result + chr(modified_code)
                else:
                    result += char
        return result
    
    def encrypt(self, plaintext: str, jumps:int) -> str:
         '''This is like, anti-dumb, it's encrypt the text'''
         return  self._shift_text(plaintext, jumps)
   
    def decrypt(self, ciphertext: str, jumps:int) -> str:
         '''And this in otherhand, decrypt the text'''
         return  self._shift_text(ciphertext, -jumps)

    def bruteforce(self, ciphertext:str) -> None:
         '''Tries all possible shifts. One of the results should match the correct plaintext.'''
         for jump in range(26):
              print(f"The text with jump: {jump}: {self.decrypt(ciphertext,jump)}")


def app_menu():
    cipher_engine = CeaserCipher() 
    while True:

        try:
            option = int(input('''
    1. Encrypt
    2. Decrypt (only in case you know how many shifts has the text)
    3. Bruteforce a ceaser cipher cipher text
    0. Exit
    '''))
                     
            match option:
                case 1:
                    text = str(input(f"What is the plaintext?\n"))
                    jump = int(input(f"How many shifts you want to make?\n"))
                    print(f"Your ciphertext: {cipher_engine.encrypt(plaintext=text,jumps=jump)}")
                
                case 2: 
                    text = str(input(f"What is the ciphertext?\n"))
                    jump = int(input(f"How many shifts you want to undo?\n"))
                    print(f"Your plaintext: {cipher_engine.decrypt(ciphertext=text, jumps=jump)}")
                
                case 3: 
                    cipher_text = str(input("So now we're breaking texts, are we? you cheeky bugger. Tell me then:\n"))  
                    cipher_engine.bruteforce(ciphertext=cipher_text)
                    print("\nNow find matching text, good luck!")
                case 0:
                    print("Drink water, alcohool and smoking only if it's to the death. Otherwise, don't even start to.")
                    exit()
        except ValueError as error:
            print(f"We're cooked: {error}")

if __name__ == "__main__":
    app_menu()                    

