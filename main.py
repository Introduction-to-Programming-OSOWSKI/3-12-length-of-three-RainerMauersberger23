def length3(w):
    
    for i in range(0, len(w)):
        if w[i] == "l":
            return True

    return False 

print (length3("lightsaber"))
