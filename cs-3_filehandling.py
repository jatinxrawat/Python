file = "record.txt"

# Function to insert new record
def insert_record():
    f = open(file, "a")
    
    task_no = input("Enter Task Number: ")
    task_text = input("Enter Task Detail: ")
    task_state = "Pending"
    
    line = task_no + "," + task_text + "," + task_state + "\n"
    f.write(line)
    
    f.close()
    print("Record Saved Successfully\n")


# Function to display records
def display_record():
    f = open(file, "r")
    lines = f.readlines()
    
    if lines == []:
        print("No Records Available\n")
    else:
        print("\n--- All Tasks ---")
        for i in lines:
            num, text, state = i.strip().split(",")
            print("Task No:", num)
            print("Work:", text)
            print("Status:", state)
            print("------------------")
    
    f.close()


# Function to modify record
def modify_record():
    search_id = input("Enter Task Number to Modify: ")
    
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    
    f = open(file, "w")
    found = False
    
    for i in lines:
        num, text, state = i.strip().split(",")
        
        if num == search_id:
            print("1. Change Work")
            print("2. Complete Task")
            ch = input("Enter option: ")
            
            if ch == "1":
                text = input("Enter new work: ")
            elif ch == "2":
                state = "Completed"
            
            found = True
        
        f.write(num + "," + text + "," + state + "\n")
    
    f.close()
    
    if found:
        print("Record Updated\n")
    else:
        print("Record Not Found\n")


# Function to remove record
def remove_record():
    search_id = input("Enter Task Number to Delete: ")
    
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    
    f = open(file, "w")
    found = False
    
    for i in lines:
        num, text, state = i.strip().split(",")
        
        if num != search_id:
            f.write(i)
        else:
            found = True
    
    f.close()
    
    if found:
        print("Record Deleted\n")
    else:
        print("Record Not Found\n")


# Main control
while True:
    print("===== TASK RECORD SYSTEM =====")
    print("1. Add Record")
    print("2. Show Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")
    
    opt = input("Choose option: ")
    
    if opt == "1":
        insert_record()
    elif opt == "2":
        display_record()
    elif opt == "3":
        modify_record()
    elif opt == "4":
        remove_record()
    elif opt == "5":
        print("Program Closed")
        break
    else:
        print("Wrong Choice\n")