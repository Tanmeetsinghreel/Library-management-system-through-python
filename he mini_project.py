# Library management system:-

# The task is to create an online library system for this you have to create a library
# class which includes the following methods:-

# Displaybook():-To display the available books.
# Lendbook():- To lend a book to a user.
# Addbook():- To add a book in library.
# Returnbook():- To return the book in library.

class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenDict = {}

    def Displaybook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def Lendbook(self,user,book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("Lender-book Database had been updated.You can take the book now\n")
        else:
            print(f"Book is already taken by {self.lenDict[book]}")

    def Addbook(self,book):
      self.booklist.append(book)
      print("Book has been added to the book list\n")

    def Returnbook(self,book):
       self.lenDict.pop(book)

if __name__ == '__main__':

    Tanmeet = library(['python', 'Rich daddy poor daddy', 'Harry potter', 'c++ Basics', 'Algorithms by CLRS'], "TanmeetSingh")

    while (True):
        print(f"Welcome to the {Tanmeet.name} library management system.Enter your choice to continue...\n")
        print("1. Display Books\n")
        print("2. Lend a Book\n")
        print("3. Add a Book\n")
        print("4. Return a Book\n")
        user_choice = int(input())
        # if user_choice not in ['1','2','3','4']:
        #     print("Please enter a valid option\n")
        #     continue
        # else:
        #     user_choice = int(user_choice)

        if user_choice ==1:
            Tanmeet.Displaybook()

        elif user_choice == 2:
             book = input("Enter the name of the book you want to lend\n")
             user = input("Enter your name\n")
             Tanmeet.Lendbook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add\n")
            Tanmeet.Addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return\n")
            Tanmeet.Returnbook(book)

        else:
            print("Not a valid option\n")

        print("Press q to quit and c to continue\n")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice != "q"):
             user_choice2 = input()

             if user_choice2 == "q":
                   exit()
             elif user_choice2 == "c":
                 continue



