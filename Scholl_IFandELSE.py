lname = input("Please enter student's last name or ZZZ to quit: ")
while lname != "ZZZ":
    fname = input("Please enter student's first name: ")
    gpa = float(input("Please enter student's GPA: "))
    if gpa >= 3.5:
        print("{} {} has made the Dean's List.".format(fname, lname))
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(fname, lname))
    lname = input("\nPlease enter student's last name or ZZZ to quit: ")