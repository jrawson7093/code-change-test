import time
for i in range(10, 0, -1): #Count down from 10 to 1
    for j in range(2): #Do this twice
        print("{0} green bottle(s), hanging on the wall".format(i))

    print("And if 1 green bottle should accidently fall,")
    print("They'll be {0} green bottle(s) hanging on the wall.\n".format(i-1))
    time.sleep(1) #Wait for a second
