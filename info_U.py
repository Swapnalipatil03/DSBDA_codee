class InformationManagementExpertSystem:
    def __init__(self):
        self.data = {}

    def add_information(self, key, value):
        self.data[key] = value
        print(f"Information '{key}' added successfully.")

    def get_information(self, key):
        if key in self.data:
            return self.data[key]
        else:
            print(f"Information '{key}' not found.")

    def remove_information(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Information '{key}' removed successfully.")
        else:
            print(f"Information '{key}' not found.")

    def display_all_information(self):
        if self.data:
            print("All information:")
            for key, value in self.data.items():
                print(f"{key}: {value}")
        else:
            print("No information available.")

# Create an instance of the InformationManagementExpertSystem class
expert_system = InformationManagementExpertSystem()

# Loop to interact with the user
while True:
    print("Choose an option:")
    print("1. Add information")
    print("2. Get information")
    print("3. Remove information")
    print("4. Display all information")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter the information key: ")
        value = input("Enter the information value: ")
        expert_system.add_information(key, value)
    elif choice == '2':
        key = input("Enter the information key to get: ")
        print(expert_system.get_information(key))
    elif choice == '3':
        key = input("Enter the information key to remove: ")
        expert_system.remove_information(key)
    elif choice == '4':
        expert_system.display_all_information()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
