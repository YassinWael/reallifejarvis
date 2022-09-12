
while True:
    keyword=input("enter a keyword")
    if keyword=="quit":
        print("you typed quit so bye!")
        quit()
    if keyword=="last":
        print(last,"is the last question answer")
    x = input("enter an equation")
    try:
        y = eval(x)
        print(y,"is the answer")
        last=y
    except Exception as e:
        print("Please only enter numbers")
 

    
    
