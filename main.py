class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Transaction(description: {self.description}, amount: {self.amount})"

class FinanceManagementSystem:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []
    
    def add_income(self):
        description = input("Enter income description: ")
        amount = float(input("Enter income amount: "))
       
        self.balance += amount
        self.transactions.append(Transaction(description, amount))
        
        print(f"Income '{description}' added successfully!\n")
        
    def add_expense(self):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        
        self.balance -= amount
        self.transactions.append(Transaction(description, -amount))  # Use -amount for expenses
        
        print(f"Expense '{description}' added successfully!\n")
        
    def view_transaction(self):
        if not self.transactions:
            print("No transactions available.\n")
        else:
            for transaction in self.transactions:
                print(transaction)
            print()
    
    def view_balance(self):
        print(f"Current balance: {self.balance}\n")
    
    def run(self):
        while True:
            print("Finance Management System")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. View Balance")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_transaction()
            elif choice == "4":
                self.view_balance()
            elif choice == "5":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    fms = FinanceManagementSystem()
    fms.run()

            
        
            
        
        
        
                   
                   