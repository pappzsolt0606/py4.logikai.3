'''
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
'''

szam = int(input("Kérek egy számot: "))
if szam % 3 == 0 and szam % 4 == 0:
    print("ez a szám osztható 3-al és 4-el is" )
elif szam % 3 == 0:
    print("ez osztható 3-al")
elif szam % 4 == 0:
    print("ez osztható 4-el")
if szam % 3 != 0 and szam % 4 != 0:
    print("ez a szám egyikkel sem osztható")