# logical operators

# if applicant has high income "AND" good Credit 
    #Eligible for loan

# "and" operator  must have to pass both conditons otherwise it will not run 
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")




# loical "or" operator , one of any condition must need to true to make code exicute

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

# logical "NOT" operator - it make False value code to run 

has_good_credit = True
criminal_record = False

if has_good_credit and not criminal_record:
    print("You are eligible for loan")