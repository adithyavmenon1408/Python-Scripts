''' This is a simple brute forcer to force open the zip file enc.zip '''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except Exception as e:
        return False
#     
#
#

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf: # read the zip file as zf
        with open('rockyou.txt', 'rb') as f: #read the password list as f
            
            # Iterate through password entries in rockyou.txt {f}
            for line in f:
                password = line.strip() #extracts each line from the txt file
                if attempt_extract(zf, password):
                    print(f"Password found: {password}")
                    return
                else:
                    print("[-] Incorrect password: %s" % password)
    print("Password not found")
            

if __name__ == "__main__":
    main()
