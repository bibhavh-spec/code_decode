def y():
    option = input("Enter 1 to code the message and 2 to decode the message: ")
    if option=="1":
        m = input("Enter the message: ")
        if (len(m)>3):
            m = m[1:]+m[0]
            m2 = "nrr"+m+"ive"
            print ("Coded: ",m2)
        else:
            m3 = m[::-1]
            print("Coded: ",m3)
    elif option =="2":
        m4 = input("Enter the message: ")
        if len(m4)>6:
            m4 = m4[3:-3]

            
            print("Decoded message: ",m4)
        else:
            print("Message to short to decode properly")
    else:
        print("INVALID OPTION.")

y()
