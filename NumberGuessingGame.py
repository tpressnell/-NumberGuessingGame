import sys

def main():
    counter = 0
    guessed_correctly = False
    ceiling = 100
    floor = 1
    

    print("Pick a number between 1 and 100, and I will try and guess it!")
    print("If my guess is too high, type \"h\", if it is too low, type \"l\", and if it is correct, type \"c\"")

    while(not guessed_correctly):
        
        counter += 1
        a = int((ceiling + floor)/2)
        b = input("Is your number " + str(a) + "? ")

        if (b == 'h'):
            ceiling = int(a-1)

        elif(b == 'l'):
            floor = int(a+1)

        elif(b == 'c'):
            print("I guessed your number in " + str(counter) + " tries!")

            sys.exit()
            
                


main()
        

        
        
    
