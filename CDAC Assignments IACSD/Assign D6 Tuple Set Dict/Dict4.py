#   3. Write a menu driven program to practice Dictionary functions.
#   Write a program to accept name of a person and their vehicle and store it in a dictionary.
#   Ask user if they want to continue to accept multiple values.
#   Display following menu:

# Funtions Definations
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
def print_menu(): # This Functions Prints the Menu    
    print("""
    ------MENU-------
1 - Add New Entry
2 - Del a Entry
3 - Modify a Entry
4 - Search for a Entry
5 - Search vechile owners
6 - Display all person name
7 - Display all vechile name
0 - Exit
    ----------------
    """)

print("\nWELCOME TO VECHILE REGISTRATION CAMP")

rto_register = dict()

while(True):

    # Exit Condition 
    exit_value = False
    if exit_value == True:
        break
    
    # Prints Menu
    print_menu()

    # Takes Input From User 
    user_input = int(input("Enter Option - "))
    print("")

    
    match user_input:           # MATCH CASE - Do Action As per User Request using
        
        case 1: # a. New Entry 

            rto_register = new_registeration(rto_register)
            print(rto_register)   

        case 2: # b. Del Entry 

            print(rto_register)
            del_key = (input("Name of Person to delete his entry - ")).title()
            
            for key in rto_register.keys():
                if key == del_key :
                    print(f"Entey of {del_key} found is begin deleted")
                    del rto_register[del_key]
                    break
            else:
                print(f"Entry of {del_key} not found")

            print(rto_register)

        case 3: # c. Modify Vechinal Name 

            edit_vehicle = (input("Name the person whose Vechinal youu wanna edit - ")).title()

            for p in rto_register.keys():
                if p == edit_vehicle :
                    rto_register[edit_vehicle] = input(f"Enter new vehicle of {edit_vehicle} - ")
            print(f"Entry of {edit_vehicle} not found")
                
            print(rto_register)

        case 4: # d. Search for Person Entry 

            find = (input("Find Entry of - ")).title()

            for p in rto_register.keys():
                if p == find :
                    print(f"Entery Found - [ {find} : {rto_register[find]} ]")
                    break
            else:
                print(f"Entry of {find} not found")

        case 5: # e. Search for Vechile Entry 

            find_vec = input("Enter the name of vechile owner you wanna find - ")

            for name, vec in rto_register.items():
                if vec == find_vec:
                    print(f"This vechile - {vec} is owned by {name}")
            
        case 6: # f. Display all person 
            print(rto_register)

        case 7: # g. Display all vechiles names
            print(rto_register.values())

        case 0: # h. Exit
            exit_value = True
            break






























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


