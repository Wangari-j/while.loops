#set up the password

password = "super secret"
user_entry = ""

#while loop

while user_entry != password:
    user_entry = input("What's the password? ")

    
#example 2
    n = 5

    while n > 0:
        print(n)
        n = n - 1

    print("Blastoff!")

#example 2
    a = 1
    while a < 10:
        print(a)
        a+=2
#example 3
i = 10
while i > 13:
    print ('This is a while loop')
    i = i + 1

    #infinite loop

    x =4
    while x >0:
        print("Run on!")
    print("Done!")