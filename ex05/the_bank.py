class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name

        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """
    The Bank class.
    """

    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """
        Add new_account in the Bank
        @new_account : Account() new account to append
        @return  True if success, False if an error occured
        """
        # Check if new_account is an instance of Account
        if not isinstance(new_account, Account):
            print("Account must be an instance of Account.")
            return False

        # Check if new_account is already in the accounts list
        if new_account in self.accounts:
            print("Account already exists.")
            return False

        if self.is_corrupted(new_account):
            print("Account is corrupted.")
            return False
        self.accounts.append(new_account)
        return True
    
    # def get_account(self, account_id):
    #     for acc in self.account:
    #         if acc.id == account_id:
    #             return acc
    #     return None
    
    def transfer(self, origin, dest, amount):
        """
        Perform the fund transfer
        @origin:  str(name) of the first account
        @dest:    str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return   True if success, False if an error occured
        """

        # Check if the origin and destination accounts exist
        if origin not in self.accounts or dest not in self.accounts:
            print("Transfer failed: origin or destination account does not exist.")
            return False

        # Check if the transfert is negative
        if amount < 0:
            print("Transfer failed: amount must be positive.")
            return False
        
        # Check if the transfert is more than the origin account value
        if origin.value < amount:
            print("Transfer failed: insufficient funds.")
            return False

        # Check if the origin and destination accounts are the same
        if origin == dest:
            print("No transfer: origin and destination accounts are the same.")
        else:
            origin.transfer(-amount)
            dest.transfer(amount)
        return True

    def is_corrupted(self, account):
        """
        Check if the account associated to name is corrupted
        @name: str(name) of the account
        @return True if corrupted, False if not
        """
        attributes = vars(account)

        #  Check if the attributes of the account are correct
        if len(attributes) % 2 == 0:
            return True

        # Check if the attributes of the account are corrupted
        for attr_name in attributes:
            if attr_name.startswith('b'):
                return True
            if attr_name.startswith('zip'):
                return True
            if attr_name.startswith('addr'):
                return True
        
        # Check if the attributes "zip" and "addr" are not in the account
        if 'zip' not in attributes or 'addr' not in attributes:
            return True
    
        # Check incorrect type of the attributes
        if not isinstance(attributes["name"], str):
            return True
        if not isinstance(attributes["value"], (int, float)):
            return True
        if not isinstance(attributes["id"], int):
            return True
        return False

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """

        # Check if the account associated to name exists
        if name not in self.accounts:
            print("Account does not exist.")
            return False

        # Check if the account associated to name is corrupted
        if self.is_corrupted(name):
            print("Account is corrupted.")
            return False

        # Fix the account associated to name
        for acc in self.accounts:
            if acc.name == name:
                acc.name = name
                acc.value = 0
                acc.id = 0
                return True
        return False
