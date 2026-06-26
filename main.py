from database import load_doctors , add_doctor , delete_doctor , save_doctors, find_doctors
df= load_doctors()
print(df)

def cli_menu():
    print("====== Doctors CRM ======")
    print("1. Add Doctor")
    print("2. Delete Doctor")
    print("3. Search Doctor")
    print("4. List Doctors")
    print('5. Exit') 
def get_choose():
    choice=int(input("..."))    
    if choice ==1 :
        df= add_doctor()
        return df
    elif choice ==2 :
    df= delete_doctor()    
        return df
    elif choice ==3 :
    df= find_doctors()
        return df
    elif choice ==4 :
    df= load_doctors()    
        return df
    elif choice == 5 :
        break

