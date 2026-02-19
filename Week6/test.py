def withdraw(balance,amount):
      
      if not isinstance(balance,(int, float)):
            raise TypeError("Balance must be a number")
      
      if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
      
      if amount <= 0:
            raise ValueError("Amount must be greater than 0")
      
      if balance < amount:
            raise ValueError("Balance must be greater than 0")
      if (amount < 0):
            raise ValueError("Amount must be greater than 0")
      
      return balance-(amount)

withdraw(500,56)
withdraw("500",56)
withdraw(500,"56")
withdraw(500,560)
withdraw(555,-55)

