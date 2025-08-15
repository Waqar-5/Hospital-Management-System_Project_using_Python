



# ===========================================
# Hospital Management System (Basic CLI)
# Using Python: Lists, Dictionaries, Loops, Conditions, Functions
# ===========================================

# ------------------------------
# Global Data Structures
# ------------------------------


patients = []  # List to store patient records as dictionaries
next_id = 1    # Unique ID counter for patients

# ------------------------------
# Utility Functions
# ------------------------------

def print_menu():
    """
    Print the main menu options
    """
    print("\n" + "="*40)  # Decorative separator
    print("🏥 HOSPITAL MANAGEMENT SYSTEM 🏥") # stylish header
    print("="*40)
    print("1) Add Patient")
    print("2) View Patients")
    print("3) Search Patient")
    print("4) Delete Patient")
    print("5) Exit")
    print("="*40)  #Result: "========================================"


# ------------------------------
# Patient Management Functions
# ------------------------------

def add_patient():
    """
    Add a new patient to the system
    """

    global next_id # Access and update global patient ID counter

    print("\n-- Add New Patient -- ") # Section header
    name = input("Enter Patient Name: ").strip() # Get patient name and remove extra spaces
    age = input("Enter Patient Age: ").strip()  #Get patient age
    disease = input("Enter Disease: ").strip()  #Get disease info
    room = input("Enter Room Number: ").strip()  #Get room number

    # Create a patient dictionary
    # Values come from the user input
    patient = {
        "id": next_id,
        "name": name,
        "age": age,
        "disease": disease,
        "room": room,
    }

    patients.append(patient)  #Add patient to the global list
    print(f"✅ Added Patient #{next_id}: {name}") #confirmation message
    next_id += 1 #Increament patient ID counter for next patient

def view_patients():
    """
    Display all patients in a table format
    """
    print("\n-- All Patients --") # Section header

    if not patients: #Check if list is empty
        print("⚠️ No patients in the system yet..")
        return # exit function if no patients
    
    #print table header
    print("-"*70)
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Disease':<25} {'Room':<6}")  # to get this: ID    Name                 Age   Disease                  Room  
    print("-"*70)

    # Loop through patients and print each record
    for p in patients:
        print(f"{p['id']:<5} {p['name']:<20} {p['age']:<5} {p['disease']:<25} {p['room']:<6}")

    print("-"*70)


def search_patient():
    """
    Search for a patient by name or ID
    """

    print("\n-- Search Patient --") # section header

    # Ask the user weather to search by name or ID
    key = input("Search by 'name' or 'id': ").strip().lower()
    if key not in ("name", "id"):
        print("❌ Invalid choice. Please choose 'name' or 'id'.")
        return
    
    query = input("Enter value: ").strip()  # Value to search

    # Loop through all patients to find a match
    for p in patients:
        if key == "name"  and p["name"].lower() == query.lower():  # Search by name (case-insensitive)
            print(f"✅ Found: #{p['id']} {p['name']} | Age {p['age']} | Disease: {p['disease']} | Room {p['room']}")
            return
        if key == "id":
            try:
                if p["id"] == int(query): #Search by ID
                    print(f"✅ Found: #{p['id']} {p['name']} | Age {p['age']} | Disease: {p['disease']} | Room {p['room']}")
                    return
            except ValueError:
                print("❌ ID must be a number.")
                return
            
    print("⚠️ No matching patient found.") # if no patient matches

def delete_patient():
    """
    Delete a patient by ID
    """

    print("\n-- Delete Patient --")  # Section header

    pid = input("Enter Patient ID to delete: ").strip()  # Ask for ID
    if not pid.isdigit():
        print("❌ Invlaid ID. Must be a number.")
        return
    
    pid = int(pid)
    for i, p in enumerate(patients):
        if p["id"] == pid:  #Find patient by ID
            deleted = patients.pop(i) # Remove patient from list
            print(f"🗑️  Deleted Patient #{deleted['id']}: {deleted['name']}")
            return
        
    print("⚠️ Patient ID not found.")  # if no patient matches


# ------------------------------
# Main Program Loop
# ------------------------------


def main():
    """
    Main program loop for CLI menu navigation
    """
    while True: # Keep running until user exits
        print_menu()  # Show main menu
        choice = input("Enter Choice (1-5): ").strip()  # get user input

        if choice == "1":
            add_patient()  # Call add patient function
        elif choice == "2":
            view_patients() # Call view patients function
        elif choice == "3":
            search_patient()  # call search patient function
        elif choice == "4":
            delete_patient()   # Call delete patient function
        elif choice == "5":
            print("👋 Goodbye! Exiting Hospital Management System...")
            break  # Exit loop and program
        else:
            print("❌ Invalid choice. Please enter a number between 1-5.")

# ------------------------------
# Run the program
# ------------------------------


if __name__ == "__main__":  #→ run this file, not when imported.” ✅
    main()  # Start the program
