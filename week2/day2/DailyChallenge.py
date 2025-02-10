# Daily Challenge : Pagination
import math
class Pagination:
    def __init__(self,items=None, pageSize=10,totalPages=1):  #items is list of content to paginate. PageSize is amount of items in each page.
        self.items=items
        self.pageSize= pageSize
        self.totalPages=math.ceil(len(self.items) / self.pageSize)
        

        
    def getVisibleItems(self):
        
        y=0
        list=[]
        for x in range(0,self.totalPages):
            list.append((self.items[y:y+self.pageSize]))
            y+=self.pageSize
        return list # list with elements in each page

        
        # dictionary={}       #Not use 
        # for x in range(0,totalPages):
        #     dictionary[x]=list[x]
        # return(dictionary) ####

    def firstPage(self):
        print(self.getVisibleItems()[0])


    def lastPage(self):
        print(self.getVisibleItems()[-1])


    def goToPage(self, goToPage=1, CurrentPage=1):
        self.goToPage=goToPage
        page=int(input("Select the page you want to read "))
        if page<=0:
            print(self.getVisibleItems()[0])
            CurrentPage= 1

        elif self.totalPages>=page:
            print(self.getVisibleItems()[page-1])
            CurrentPage=page
        else:
            if page>self.totalPages and page>0:
                print(self.getVisibleItems()[-1])
                CurrentPage=len(self.getVisibleItems())
        print('Current Page is page:',CurrentPage)

        NextPage=CurrentPage+1







alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 10) #4 es num de alphabetlist que muestro por pag de esa lista 


p.getVisibleItems()
# # ["a", "b", "c", "d"]

p.firstPage()
p.lastPage()

p.goToPage()



