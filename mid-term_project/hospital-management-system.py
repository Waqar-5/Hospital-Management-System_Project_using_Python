# ===========================================
# Hospital Management System (Advanced CLI)
# ===========================================


import datetime   # Import datetime module → used for handling dates and times (like admission date, receipt date)


patients = []     # Empty list to store all patient records (each patient is saved as a dictionary)
next_id = 1       # Counter for unique patient ID numbers (starts from 1)


# ------------------------------
# Utility Functions
# ------------------------------

def generate_patient_id():
    """ Generate unique hospital-style patient ID like HSP-001 """
    return f"HSP-{next_id:03d}"  # Format ID with leading zeros → Example: HSP-001, HSP-002


def print_menu():
    """ Print the main menu options """
    print("\n" + "="*50)   # Print 50 equal signs (=) to make a border
    print(" 🏥  WELCOME TO CITY HOSPITAL MANAGEMENT SYSTEM 🏥 ")   # Title of program
    print("="*50)   # Print 50 equal signs (=) again for styling
    print("1) Admit Patient")   # Option 1: Add new patient
    print("2) View Patients")   # Option 2: Show all admitted patients
    print("3) Search Patient")  # Option 3: Search patient by ID or Name
    print("4) Discharge Patient (with Receipt)")  # Option 4: Discharge patient and print receipt
    print("5) Generate Receipt (Manually)")   # Option 5: Manually generate receipt for a patient
    print("6) Exit")   # Option 6: Exit program
    print("="*50)   # Print 50 equal signs (=) again



# ------------------------------
# Patient Management Functions
# ------------------------------

def add_patient():
    """ Admit a new patient to the hospital """
    global next_id  # Use global variable next_id to assign unique IDs



    
    print("\n-- 📝 Admit New Patient --")
    name = input("Enter Patient Name: ").strip().title()      # Take name, remove spaces, format properly (Ex: "john" → "John")
    age = input("Enter Patient Age: ").strip()                # Take age as input
    disease = input("Enter Disease: ").strip().title()        # Take disease name, format properly
    doctor = input("Assigned Doctor: ").strip().title()       # Take doctor name, format properly
    room = input("Enter Room Number: ").strip()               # Take room number
    bill = input("Enter Treatment Bill Amount (PKR): ").strip()  # Take bill amount


    # Create dictionary for new patient
    patient = {
        "id" : generate_patient_id(), #Auto-generate unique ID
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor,
        "room": room,
        "bill": bill,
        "admission_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),   # Save current date/time
        "status": "Admitted"   # Default status when admitted
    }

    patients.append(patient)   # Add patient dictionary to patients list
    print(f"✅ Patient Admitted Successfully! ID: {patient['id']} | Name: {name}")   # Confirmation message
    next_id += 1   # Increase ID counter for next patient

def view_patients():
    """ Display all admitted patients """
    print("\n-- 👥 All Patients  --")

    if not patients:  # If no patients are in the list
        print(" ⚠️ No patients admitted yet. ")  # Show message
        return
    
     # Print table header
    print("-"*90)   
    print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Disease':<15} {'Doctor':<15} {'Room':<6} {'Status':<10}")
    print("-"*90)

    # Print each patient details in table format
    for p in patients:
        print(f"{p['id']:<10} {p['name']:<20} {p['age']:<5} {p['disease']:<15} {p['doctor']:<15} {p['room']:<6} {p['status']:<10}")
    
    print("-"*90)  #End line after printing all patients


def search_patient():
    """ Search for a patient by ID or Name """
    print("\n-- 🔎 Search Patient --")

    key = input("Search by 'id' or 'name': ").strip().lower()   # Ask user what to search (id or name)
    if key not in ("id", "name"): #if wrong choice
        print("❌ Invalid choice. Please choose ''id' or 'name'. ")
        return
    
    query = input("Enter search value: ").strip().lower()   # Take input value to search


    # loop through patients and check
    for p in patients:
        if key == "id" and p["id"].lower() == query:     # If searching by ID
            print(f"✅ Found: {p}") # Show patient dictionary
            return
        if key == "name" and p["name"].lower() == query: # If searching by name
            print(f"✅ Found: {p}")   # Show patient dictionary
            return
        
        print("⚠️ No matching patient found.")  #if no match found





def discharge_patient():
    """ Discharge a patient and auto-generate receipt """
    print("\n-- 🏠 Discharge Patient --")

    pid = input("Enter Patient ID to discharge: ").strip().lower()   # Ask ID of patient to discharge
    for p in patients:
        if p["id"].lower() == pid:   # Check if ID matches
            if p["status"] == "Discharged":   # If already discharged
                print("⚠️ Patient already discharged.")
                return
            p["status"] = "Discharged"   # Update status to Discharged
            print(f"✅ Patient {p['name']} ({p['id']}) has been discharged.")

            # Generate receipt after discharge
            print("\n-- 🧾 Receipt Generated Automatically --")
            print("="*50)
            print("         🏥 CITY HOSPITAL RECEIPT 🏥")
            print("="*50)
            print(f"Receipt Date : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            print(f"Patient ID   : {p['id']}")
            print(f"Name         : {p['name']}")
            print(f"Age          : {p['age']}")
            print(f"Disease      : {p['disease']}")
            print(f"Doctor       : {p['doctor']}")
            print(f"Room Number  : {p['room']}")
            print(f"Status       : {p['status']}")
            print(f"Bill Amount  : {p['bill']} PKR")
            print("="*50)
            print("✅ Thank you for choosing City Hospital!")
            print("   Get Well Soon ❤️")
            print("="*50)
            return

    print("⚠️ Patient ID not found.")   # If ID not found


# ------------------------------
# Receipt Function
# ------------------------------



def generate_receipt():
    """ Generate hospital treatment receipt for a patient (manual option) """
    print("\n-- 🧾 Generate Receipt --")

    pid = input("Enter Patient ID: ").strip().lower()   # Ask ID for manual receipt
    for p in patients:
        if p["id"].lower() == pid:   # If patient exists
            print("\n" + "="*50)
            print("         🏥 CITY HOSPITAL RECEIPT 🏥")
            print("="*50)
            print(f"Receipt Date : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            print(f"Patient ID   : {p['id']}")
            print(f"Name         : {p['name']}")
            print(f"Age          : {p['age']}")
            print(f"Disease      : {p['disease']}")
            print(f"Doctor       : {p['doctor']}")
            print(f"Room Number  : {p['room']}")
            print(f"Status       : {p['status']}")
            print(f"Bill Amount  : {p['bill']} PKR")
            print("="*50)
            print("✅ Thank you for choosing City Hospital!")
            print("   Get Well Soon ❤️")
            print("="*50)
            return

    print("⚠️ Patient ID not found.")   # If ID not found


# ------------------------------
# Main Program Loop
# ------------------------------

def main():
    """ Main program loop """
    while True:   # Infinite loop until user exits
        print_menu()   # Show menu options
        choice = input("Enter Choice (1-6): ").strip()   # Take input for menu

        if choice == "1":   # If choice is 1 → admit new patient
            add_patient()
        elif choice == "2":   # If choice is 2 → view all patients
            view_patients()
        elif choice == "3":   # If choice is 3 → search patient
            search_patient()
        elif choice == "4":   # If choice is 4 → discharge patient
            discharge_patient()
        elif choice == "5":   # If choice is 5 → generate receipt manually
            generate_receipt()
        elif choice == "6":   # If choice is 6 → exit program
            print("👋 Goodbye! Thank you for using City Hospital System.")
            break   # Exit loop
        else:   # If wrong input
            print("❌ Invalid choice. Please enter a number between 1-6.")


# Run main program only if file is run directly
if __name__ == "__main__":
    main()   # Call main function