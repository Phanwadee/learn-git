print("sawadee kha,welcome to the hamburger shop. Please select a hamburger")
hamburger_type = input('"h" for hamburger or "v" for vegetarian food:')
if hamburger_type.lower() == "h":
    print("Please select a hamburger")
    hamburger_type = input('"p" for Pork hamburger or "b" for Beef hamburger:')
    if hamburger_type.lower() == "p":
       print("Here is your Pork hamburger. Thank you.")
    elif hamburger_type.lower() == "b":
        print("Here is your Beef hamburger. Thank you.")
    else:
        print("Sorry, we don't have",hamburger_type,"choice today.")
elif hamburger_type.lower() == "v":
    print("Here is your vegetarian food. Thank you.")
else:
    print("Sorry,we don't have these input for choice today")
print("sawadee Kha La Korn!")
