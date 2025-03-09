class library:
    book_dict={'python':20,'java':6,'sql':10,'js':4,'c++':8}

    def __init__(self,name,phno,sid,book=[]):
        self.name=name
        self.phno=phno
        self.sid=sid
        self.book=book

    def disp_obj(self):
        print(self.name,self.phno,self.sid,self.book)

    def return_books (self):
        bn=input("enter the book")
        self.book.remove(bn)
        self.book_dict[bn]+=1

    def get_books (self):
        bn=input("Enter the book:")
        if bn in self.book_dict and self.book_dict[bn]>0:
            self.book.append(bn)
            self.book_dict[bn]-=1
        else:
            print("nan")

    @classmethod
    def library_details(cls):
        print(cls.book_dict)


obj = library('abhi',9218918,1234)

while True:
    print(" 1. return 2.get books 3.display 4.exit 5.For Library Details")
    val = int(input("enter the value: "))

    if val == 1:
        obj.return_books()

    elif val == 2:
        obj.get_books()
    
    elif val == 3:
        obj.disp_obj()

    elif val == 4:
        break

    else:
        obj.library_details()

    
