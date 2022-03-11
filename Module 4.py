class book:
    def __init__(self,a='Women',b='Chetan',c='Ram',d=100,q=1000 ):
        self.title=a
        self.author=b
        self.publisher=c
        self.price=d
        self.sold=q
        royal=0
    def get_title(self):
        return self._title
    def set_title(self,a):
        self.title=a
        return
    def get_author(self):
        return self.author
    def set_author(self,b):
        self.author=b
        return
    def get_publisher(self):
        return self.publisher()
    def set_publisher(self,c):
        self.publisher=c
        return
    def get_price(self):
        return self.price
    def set_price(self,d):
        self.price=d
        return
    def get_sold(self):
        return self.sold
    def set_sold(self,e):
        self.sold=e
        return
    def royalty(self):
        if self.sold<=500:
            royal=.1*self.price*self.sold
        elif self.sold>500 and self.sold<=1500:
            royal=.125*self.price*(self.sold-500)+.1*self.price*500
        elif self.sold>1500:
            royal=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.sold-1500)
        return royal

class ebook(book):
    def __init__(self,i='PDF'):
        self._format=i
    def get_format(self):
        return self.format
    def set_format(self,b):
        self.format=b
        return
    def royalty(self):
        if self.sold<=500:
            royal=.1*self.price*self.sold
        elif self.sold>500 and self.sold<=1500:
            royal=.125*self.price*(self.sold-500)+.1*self.price*500
        elif self.sold>1000:
            royal=.1*self.price*500+.125*self.price*1000+.15*self.price*(self.sold-1500)
        royal=royal-(.12*royal)
        return royal
a=input(" Enter the title of the book ")
b=input(" Enter the author of the book ")
c=input(" Enter the publisher of book ")
d=int(input(" Enter the price of the book "))
e=int(input(" Enter the total number of books sold "))
f=int(input(" Enter 1 for normal book and enter 2 for e book "))
b=book()
b.set_title(a)
b.set_author(b)
b.set_publisher(c)
b.set_price(d)
b.set_sold(e)
eb=ebook()
if f==1:
    z=b.royalty()
    print("Title is %s \n publisher is %s author is \n price was %d \n total sold is %d royalty is %d \n "  %(b.title,b.publisher,b.author,b.price,b.sold,z) )

if f==2:
    print("b")
    g=input("Enter the format of ebook")
    z=eb.royalty()
    eb.set_format(g)
    print(" Title is %s \n Publisher is %s \n Author is %s \n Price was %d \n Total sold %d \n Format is %s \n Royalty is %d \n"%(eb.title,eb.publisher,eb.author,eb.price,eb.sold,eb.format,z))
