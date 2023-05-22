import hashlib
filename = 'passwrd.txt'


def convert_text_to_sha_1(text):
    digest = hashlib.sha1(
        text.encode()).hexdigest()
    
    return digest



def main():
    user_sha1 = input('Enter the SHA1 to crack: ')
    cleaned_user_sha1 = user_sha1.strip().lower()

    with open(filename) as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha_1(password)

            if cleaned_user_sha1 == converted_sha1:
                print(f"Password Found: {password}")
                return
        
    print('Could Not Find The Password')




if __name__ == '__main__':
    main()