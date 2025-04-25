import json
path=r'C:\task-1\\library.json'
class libraray:
    def _init_(self):
        pass 
    
    def menu(self):
     while True:
         print(' \t\t1- Add Book ')
         print(' \t\t2- Borrow Book ')
         print(' \t\t3- Return Book ')
         print(' \t\t4- exit ')

         choice=int(input('\t\tenter your choice '))
         if choice == 1:
           self.addbooks()
         if choice == 2:
           self.borrow()
         if choice == 3:
           self.returnbooks()
         if choice== 4:
            exit
           
    def borrow(self):
        borrow={}   
         
        print('How much book u want ')
        borrow['books']=int(input('Enter numbers of books'))
        borrow['name']=input('enter your name here ')
        with open(path,"w") as file:
         json.dump(borrow,file,indent=4)
         print(json.dumps(borrow,indent=4)) 

    def addbooks(self):
       add={}
       add['books']=int(input('Enter Book Name You want to add '))
       add['name']=input('enter your name here ')

       with open(path,"w") as file:
         json.dump(add,file, indent=4)
         print(json.dumps(add,indent=4))

    def returnbooks(self):
     returnbook={}
     returnbook['return']=input('how much book u want to return ')
     returnbook['name']=input('enter your name here ')

     with open(path,'w') as file:
         json.dump(returnbook,file, indent=4)
         print(json.dumps(returnbook,indent=4))


data=libraray()
data.menu()