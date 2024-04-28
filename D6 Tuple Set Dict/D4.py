#   3. Write a menu driven program to practice Dictionary functions.
#   Write a program to accept name of a person and their vehicle and store it in a dictionary.
#   Ask user if they want to continue to accept multiple values.
#   Display following menu:

rto_register = dict()

def new_registeration(rto_register): # function to 

    # FUNCTIONS - Check if Name is Duplicateds
    def duplicate_name_check( name, val):
        val = False
        for k in rto_register.keys():
            if k == name:
                print("Name already Exist Pls Enter a new Name",end="\n\n")
                val = True
                break
        return val
    
    while(True):
        val = False

        name = (input("Enter Person Name - ")).title() # Enter Person Name

        val = duplicate_name_check( name, val) # Check for Duplicate Name - function call
        if val == True:
            continue

        v_num = (input("Enter Vehicle Name - ")).title() # Enter Vechile Name 

        rto_register[name] = v_num # Adding entry to Dict

        loop_continue = input("\nPress 'Y' to continue or Press 'N' to Exit - ")  # asking if wanna enter another value
        print("")
        loop_continue = loop_continue.upper()

        if (loop_continue == "Y"):
            continue
        else:
            print("Exiting Program : Registation Successfull\n")
            break

    return rto_register

print("""
Menu
----------------
a. Add New Entry
b. Del Entry
c. Modify Entry
d. Search 
e. Search list of people with give vechile name
f. Display all person name
g. Display all vechile name
e. Exit
----------------
""")

user_input = input("Enter Option - ")
rto_register = new_registeration(rto_register)
print(rto_register)





























#   a. Add new person name and a vehicle name.
#   b. Delete a person name and vehicle name from the dictionary.
#   ----Accept person name from user.
#   ----Check whether person name exists in the dictionary.
#   ----If exists show person name and vehicle name to the user.
#   ----Confirm for deletion, if user enters y
#   then delete otherwise no. Display appropriate message.
#   c. Modify vehicle name for the person
#   ----Accept a person name from user.
#   ----Check whether the person’s name exists.
#    ----If the name exists, show the person’s name and vehicle name to user.
#    Ask for new value and then overwrite the old value.
#    d. Search vehicle for the given person’s name.
#    e. Search list of people, who have given a vehicle
#    f. Display all person names.
#    g. Display all vehicle names.
#    h. Exit


