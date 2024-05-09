# Define a class for an Information Management Expert System
class InformationManagementExpertSystem:
    # Constructor to initialize the data dictionary
    def __init__(self):
        self.data = {}

    # Method to add information to the system
    def add_information(self, key, value):
        # Add key-value pair to the data dictionary
        self.data[key] = value
        # Print a success message
        print(f"Information '{key}' added successfully.")

    # Method to get information from the system
    def get_information(self, key):
        # Check if the key exists in the data dictionary
        if key in self.data:
            # Return the value corresponding to the key
            return self.data[key]
        else:
            # Print a message if the key is not found
            print(f"Information '{key}' not found.")

    # Method to remove information from the system
    def remove_information(self, key):
        # Check if the key exists in the data dictionary
        if key in self.data:
            # Delete the key-value pair from the data dictionary
            del self.data[key]
            # Print a success message
            print(f"Information '{key}' removed successfully.")
        else:
            # Print a message if the key is not found
            print(f"Information '{key}' not found.")

    # Method to display all information stored in the system
    def display_all_information(self):
        # Check if there is any information stored
        if self.data:
            # Print header for all information
            print("All information:")
            # Iterate over each key-value pair in the data dictionary
            for key, value in self.data.items():
                # Print key and corresponding value
                print(f"{key}: {value}")
        else:
            # Print a message if no information is available
            print("No information available.")

# Create an instance of the InformationManagementExpertSystem class
expert_system = InformationManagementExpertSystem()
# Add some information to the system
expert_system.add_information("Name", "John Doe")
expert_system.add_information("Age", 30)
# Display all information stored in the system
expert_system.display_all_information()
# Get and print specific information from the system
print(expert_system.get_information("Name"))
# Remove specific information from the system
expert_system.remove_information("Age")
