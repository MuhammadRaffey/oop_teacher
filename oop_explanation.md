```cpp
#include <iostream>
#include <string>

class BankAccount {
private:
    std::string accountHolderName; // Data member to hold the account holder's name
    double balance;                // Data member to hold the account balance

    // Private method to validate the amount
    bool validateAmount(double amount) {
        return amount > 0;
    }

public:
    // Constructor to initialize the account holder's name and initial balance
    BankAccount(std::string name, double initialBalance) {
        accountHolderName = name;
        if (validateAmount(initialBalance)) {
            balance = initialBalance;
        } else {
            balance = 0;
        }
    }

    // Method to get the current balance
    double getBalance() {
        return balance;
    }

    // Method to deposit an amount into the account
    void deposit(double amount) {
        if (validateAmount(amount)) {
            balance += amount;
        } else {
            std::cerr << "Invalid deposit amount!" << std::endl;
        }
    }

    // Method to withdraw an amount from the account
    void withdraw(double amount) {
        if (validateAmount(amount) && balance >= amount) {
            balance -= amount;
        } else {
            std::cerr << "Invalid or insufficient amount for withdrawal!" << std::endl;
        }
    }

    // Method to display account information
    void displayAccountInfo() {
        std::cout << "Account Holder: " << accountHolderName << std::endl;
        std::cout << "Current Balance: $" << balance << std::endl;
    }
};

int main() {
    // Create a BankAccount object
    BankAccount myAccount("John Doe", 1000.0);

    // Display initial account information
    myAccount.displayAccountInfo();

    // Depositing money
    myAccount.deposit(200.0);
    std::cout << "After depositing $200: ";
    myAccount.displayAccountInfo();

    // Withdrawing money
    myAccount.withdraw(150.0);
    std::cout << "After withdrawing $150: ";
    myAccount.displayAccountInfo();

    // Attempt to withdraw an invalid amount
    myAccount.withdraw(1200.0);

    return 0;
}
```

This C++ code demonstrates the concept of encapsulation in object-oriented programming:
- **Encapsulation** is achieved by keeping the data members `accountHolderName` and `balance` private, meaning they cannot be accessed directly from outside the class.
- Instead, public methods like `deposit`, `withdraw`, and `displayAccountInfo` are provided to interact with these data members. These methods serve as the "doors" of the house, ensuring that the internal data is accessed and modified securely and appropriately.
- The `validateAmount` private method is a utility function that helps in maintaining the integrity of operations related to deposits and withdrawals.
- This encapsulation ensures that only valid and authorized modifications can be made to the account's data, providing robustness and security to the handling of a bank account in a software application.