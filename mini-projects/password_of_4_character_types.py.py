#To make password of 4 character combination of lowercase,uppercase,digit,special character
l=u=d=s=c=0
while True:
    print("Enter a word containing lowercase,uppercase,digit and special character more then or equal to 4")
    a=input("Enter a word:- ")
    #l=u=d=s=0
    b=len(a)
    if b>=4:
        for i in range(0,b):
            if a[i].islower():                  
                l+=1
            elif a[i].isupper():
                u+=1
            elif a[i].isdigit():
                d+=1
            elif a[i].isalnum():
                c+=1
            else:
                s+=1
        if l>0 and u>0 and d>0 and s>0:
            print("Valid Password")
            break
        else:
            if l==0 :
                if u==0:
                    if d==0:
                        if s==0:
                            print("You have not entered lowercase,uppercase,digit,special character")
                        else:
                            print("You have not entered lowercase,uppercase,digit")
                    else:
                        if s==0:
                            print("You have not entered lowercase,uppercase,special character")
                        else:
                            print("You have not entered lowercase,uppercase")
                else:
                    if d==0:
                        if s==0:
                            print("You have not entered lowercase,digit,special character")
                        else:   
                            print("You have not entered lowercase,digit")
                    else:
                        if s==0:
                            print("You have not entered lowercase,special character")
                        else:
                            print("You have not entered lowercase")
            else:
                if u==0:
                    if d==0:
                        if s==0:
                            print("You have not entered uppercase,digit,special character")
                        else:
                            print("You have not entered uppercase,digit")
                    else:
                        if s==0:
                            print("You have not entered uppercase,special character")
                        else:
                            print("You have not entered uppercase")
                else:
                    if d==0:
                        if s==0:
                            print("You have not entered digit,special character")
                        else:   
                            print("You have not entered digit")
                    else:
                        if s==0:
                            print("You have not entered special character")
                        else:
                            print("You have not entered lowercase")
    else:
        print("Enter a valid password of atleast 4 character!")
    #print("Please enter the correct letter of word!")
