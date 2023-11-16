Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fib_serise(a):
    x,y=0,1
    while True:
   z= x+y
    if z<a:
        yield z
        x,y=y,z
    else:
         break
gen_fib=fib_serise(10)
print (gen_fib)