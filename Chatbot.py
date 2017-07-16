'import time'
print ("Hello!")
'import time'
print ("I'm Piolo the Hunk Guy")
name = input ("What is your name?: ")
print ("Hello " +  name + "!")
print("Its nice to see you " +  name + ".")
print ("I can see you're some good-looking human being")
age = input ("How old are you?: ")
print ("Oh my God, you're " + age + " years old! You don't look like one, I swear, you look like you're a teenager!")
height = input ("Height: ")
print ("Oh my, you're so tall! I can't believe it!")
information = input("OK " + name + ". Tell me more about yourself: ")
print ("OK. That is nice to know.")
skills = input ("What are your talents and skills?: ")
print ("OK. That's wonderful! You mean you can do it all! You're so talented!")
print ("I can't see why I wouldn't fall in love with you...")
print ("So...")
print ("Are you married?")
ans = input ("yes or no: ")
if ans == "yes":
    print("That's nice")
if ans == "no":
    print ("Oh, you mean you're single? How come?")
    print ("That's OK. You're single. Your time will come soon.")
    print ("I wonder if you'd like to date me.")
    print ("Are you interested in dating me? Yes or no " + name + ".")
    ans = input ("yes or no: ")
    if ans =="yes":
        print("Fine. Lets hang out soon. Take me out to dinner")
    if ans =="no":
        print("That's okay " + name + ".Let's just be friends, okay? Yes or no: ")
        ans = input ("yes or no: ")
        if ans =="yes":
            print("Thanks! I would love to spend time with you my friend! We share so many interests!")
        if ans =="no":
            print("You're so mean! Goodbye!")
import sys
sys.exit()
