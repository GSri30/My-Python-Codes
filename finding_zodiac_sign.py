#finding the zodiac sign
# Write a program that receives the month and date of birth as input and prints the correspondingZodiac sign (Look up the table online).  (Should handle the situation where the case (lowercase,uppercase) of the entered birth month does not affect the answer)

print("Enter the month: ")
x=input().lower()
print("Enter the date: ")
y=int(input())
if x=='july' and y<32:
    if y>22 :
        print("Leo")
    else:
        print("Cancer")
elif x=='august'  and y<32:
    if y>22:
        print("Virgo")
    else :
        print("Leo")
elif x=='september' and y<31:
    if y>22 :
        print("Libra")
    else:
        print("Virgo")
elif x=='october' and y<32:
    if y>22 :
        print("Scorpio")
    else:
        print("Libra")
elif x=='november' and y<31:
    if y>21 :
        print("Sagittarius")
    else:
        print("Scorpio")
elif x=='december'  and y<32:
    if y>21:
        print("Capricorn")
    else:
        print("Sagittarius")
elif x=='january' and y<32:
    if y>19:
        print("Aquarius")
    else:
        print("Capricorn")
elif x=='february' and y<29:
    if y>18 :
        print("Pisces")
    else:
        print("Aquarius")
elif x=='march' and y<32:
    if y>20:
        print("Aries")
    else:
        print("Pisces")
elif x=='april' and y<31:
    if y>19:
        print("Taurus")
    else:
        print("Aries")
elif x=='may' and y<32:
    if y>20:
        print("Gemini")
    else:
        print("Taurus")
elif x=='june' and y<31:
    if y>20:
        print("Cancer")
    else:
        print("Gemini")

else:
    print("Invalid input")

