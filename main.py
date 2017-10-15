
class BookManager:
    def __init__(self):
        self.books=dict()
        self.index = 1


    def operator(self):
        while True:
            print("图书管理操作：")
            print("1.添加图书")
            print("2.删除图书")
            print("3.更改图书")
            print("4.查找图书")
            print("0.退出系统")
            num = input("请输入操作码:")
            if num.strip() == '':
                print("不能为空，请重新输入操作码:")
                num = input("请输入操作码:")
            self.select(num.strip())

    def select(self,num):
        if num == '1':
            self.addBook(),
        if num == '4':
            self.selectAllBook()
        if num == '0':
            exit(0)


    def addBook(self):
        print("请输入相应的图书信息：")
        name=input("书名：")
        price=input("价格：")
        author=input("作者：")
        while (name.strip()=='') or (price.strip() == '') or (author.strip() == ''):
            print("不能为空,请重新输入:")
            name = input("书名：")
            price = input("价格：")
            author = input("作者：")


        book = self.initBook(name,price,author)
        self.books[self.index] = book
        self.index=self.index+1
        book.show()
        print("添加成功!")


    def delBook(self,index):
        book = self.books.pop(index)
        return book


    def updateBook(self,index):
        book = self.books.get(index)
        book.show()
        setattr(book,"name",input())
        setattr(book,"price", input())
        setattr(book,"author",input())

    def selectAllBook(self):
        if self.books.__len__() == 0:
            print("数据为空，请添加数据")
            self.operator()

        for index in self.books:
            book = self.books.get(index)
            book.show()


    def initBook(self,name,price,author):
        book = Book(self.index,name, price, author)
        return book



class Book:
    books = list()
    def __init__(self,index,name,price,author):
        self.index = index
        self.name = name
        self.price = price
        self.author = author

    def show(self):
        print("%d.书名:%s,价格:%s,作者:%s"%(self.index,self.name,self.price,self.author))




if __name__ == '__main__':
    manger = BookManager()
    manger.operator()
