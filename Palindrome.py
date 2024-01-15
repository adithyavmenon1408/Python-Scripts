text = input ("enter text to be checked : ")
l = len(text)
rev = ""
for ch in range(l-1 , -1, -1):
    rev = rev+text[ch]
if rev == text:
    print ("Text is palindrome")
else :
    print("Text is not palindrome")


    
