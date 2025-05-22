#Write a program to find the type of triangle. Input sides from user.

s1 = int(input("Enter 1st side : "))
s2 = int(input("Enter 2nd side : "))
s3 = int(input("Enter 3rd side : "))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1 :
    if s1==s2==s3 :
        print("Triangle is Equilateral")
    elif s1==s2 or s2==s3 or s1==s3 :
        print("Triangle is Isoscale")
    else :
        print("Triangle is Scalane")
else :
    print("Not a Triangle")
