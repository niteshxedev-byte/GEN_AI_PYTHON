"""Explanation
A while loop allows code to be repeated an unknown number of times
as long as a condition is being met. This may be 100 times, just the once or
even never. In a while loop the condition is checked before the code is run,
which means it could skip the loop altogether if the condition is not being
met to start with. It is important, therefore, to make sure the correct
conditions are in place to run the loop before it starts.
"""

total = 0 
while total <=50:
    num = int(input("enter the num "))
    total = total + num
    print("the total is ",total)


num = 0 
while num<=5:
    num = int(input("enter the number: "))
print("the last number you entered was a", num)




num1 = int(input("enter a number "))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter another number "))
    total = total + num2
    again = input("do yo want to add anoter number (y/n) ?")
print("the total is ", total)



again = "y"
count = 0 
while again == "y":
    name = input("enter a name of somebody you want to invite to your party : ")
    print(name,"has now been invited ")
    count = count +1
    again = input("Do you want to invite somebody else (y/n) ?? ")
print("you have ",count,"people comming to your party")


compnum =50 
guss = int(input("can you guss the number im thinking of ??"))
count = 1
while guss!= compnum:
    if guss<compnum:
        print("too low")
    else:
        print("too high")
    count = count+1
    guss = int(input("have another guss ??"))
print("well done , you took ", count ,"attempts")


num = int(input("enter a number between 10 and 20: "))
while num <10 or num >20:
    if num < 10:
        print("too low")
    else:
        print("too high")
    num = int(input("try again :"))
print("thankyou")




num = 10 
while num>0:
    print("There are",  num , "green bottels hangin on the wall")
    print(num,"green bottles hanging on the wall")
    print("And if 1 green bottle should accidentally fall")
    num = num -1
    ans = int(input("how many green bottels will be hanging on the wall ??"))
    if ans == num:
         print("there will be ",num , "green bottles hanging on the wall")
    else:
        while ans != num:
            ans = int(input("no, try again :"))
print("there are no more green bottles hanging on wall")