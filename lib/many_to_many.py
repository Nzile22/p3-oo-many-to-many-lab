class Author:
    all_authors = []  
    def __init__(self, name):
        self.name = name  # Initialize the author's name
        self._contracts = []  # Private list to store contracts for this author
        Author.all_authors.append(self)  # Add this instance to the all_authors list

    def get_info(self):
        return f"Author: {self.name}"

    def contracts(self):
        return self._contracts  # Return the list of contracts for this author

    def books(self):
        return [contract.book for contract in self._contracts]  # Return related books

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("royalties must be a non-negative number.")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)  # Add the contract to the author's contracts
        return contract  # Return the created contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)  # Calculate total royalties


class Book:
    all_books = []  # Class variable to keep track of all Book instances

    def __init__(self, title):
        self.title = title  # Initialize the title attribute
        self._contracts = []  # Private list to store contracts for this book
        Book.all_books.append(self)  # Add this instance to the all_books list

    def get_info(self):
        return f"Book Title: {self.title}"

    def contracts(self):
        return self._contracts  # Return the list of contracts for this book

    def authors(self):
        return [contract.author for contract in self._contracts]  # Return related authors


class Contract:
    all_contracts = []  # Class variable to keep track of all Contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("royalties must be a non-negative number.")

        self.author = author  # Author object
        self.book = book      # Book object
        self.date = date      # Date as a string
        self.royalties = royalties  # Royalties as a percentage
        Contract.all_contracts.append(self)  # Add this instance to the all_contracts list

        # Add this contract to the author's and book's contracts
        author._contracts.append(self)
        book._contracts.append(self)

    def get_contract_info(self):
        return (f"Contract Details:\n"
                f"{self.author.get_info()}\n"
                f"{self.book.get_info()}\n"
                f"Date: {self.date}\n"
                f"Royalties: {self.royalties}%")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]  # Return contracts by date

