Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
import string
print("WELCOME TO OUR PASSWORD GENRATOR")
length=int (input("ENTER THE LENGTH OF PASSWORD YOU WANT:"))
lowerD=string.ascii_lowercase
upperD=string.ascii_uppercase
digitD=string.digits
symbolsD=string.punctuation
combine=lowerd+upperD+digitd+symbolsD
x=random.sample(combine,length)
password="".join(x)
print(password)
main()
main()