#=============================
# Library maintain Project   |
#=============================
#import os
#os.chdir('G:\\Librrary maintain txt')
class Libary:
   _book_list = []
   def __init__(self,ahave_book,aowner_name,aemail,apas):
      self.have_book = ahave_book
      self.owner_name = aowner_name 
      self.email = aemail
      self.pas = apas
   def add_book(self):
      book_n = input('\ninput name: ')
      self._book_list.append(book_n)
      book_lis = open('Book_list.txt','a')
      book_lis.write(f'{book_n}\n')
      book_lis.close()
      print('\n Add Sacssessfully\n')
   def remove_(self):
      try:
         book_li = open('Book_list.txt','r')
         ttr = book_li.read()
         book_li.close()
         ty = ttr.split('\n')
         for x in range(len(ty)):
            have = ty[x]
            ty.remove(have)
         try: 
            while True:
               ty.remove("")
         except: pass
      except: pass
      print('\n')
   def display_book(self):
      self.remove_()
      shukur.remove_()
      alam.remove_()
      hw = input('\nshow available / scharch by name (sa/sn): ')
      if hw == 'sa' or hw == 'SA' or hw == 'Sa' or hw == "sA":
         try:
            book_li = open('Book_list.txt','r')
            ttr = book_li.read()
            book_li.close()
            ty = ttr.split('\n')
            print('\nAvailable Book',end=" : ")
            for k in ty:
               print(k,end=',')
            print(f'\n')
         except: print(f"\n Have no book")       
      elif hw == 'sn' or hw == 'SN' or hw == 'Sn' or hw == "sN":
         name = input('\nBook name : ')
         try:
            book_li = open('Book_list.txt','r')
            ttr = book_li.read()
            book_li.close()
            ty = ttr.split('\n')
            ty.index(name)
            print('\nBook Available\n')
         except: print('\nBook Not Available\n')     
   def return_book(self):
      try:
         rt = open(f'{self.owner_name}.txt','r')
         tt = rt.read()
         rt.close()
         rr = tt.split('\n')
         print('\n My have book',end=' : ')
         for c in range(len(rr)):
            print(rr[c],end=',')
         print('\n')
         r_book = input("Book Name: ")
         rr.remove(r_book)
         try:
            while True:
               rr.remove("")
         except: pass
         rk = open(f'{self.owner_name}.txt','w')
         for d in range(len(rr)):
            rk.write(f'{rr[d]}\n')
         rt.close()
         rr = tt.split('\n')
         gg = open('Book_list.txt','a')
         gg.write(f"{r_book}\n")
         gg.close()
         print('sacsessfullay retaurn')
      except: print("\nHave no book")
   def book_naw_ami(self):
      try:
         book_li = open('Book_list.txt','r')
         ttr = book_li.read()
         book_li.close()
         ty = ttr.split('\n')
         print('\nAvailble',end=' : ') 
         for dr in ty:
            print(dr,end=',')
         print('\n')
         book_nam = input('\nBook Name: ')
         ty.remove(book_nam)
         try:
            for i in ty:
               ty.remove("")
         except: pass
         book_li = open('Book_list.txt','w')
         for i in range(len(ty)):
            book_li.write(f'{ty[i]}\n')
         book_li.close()
         self.have_book.append(book_nam)
         print('\nSaccessfully give\n')
         pp = self.owner_name.lower()
         wr = open(f'{pp}.txt','a')
         wr.write(f'{book_nam}\n')
         wr.close()

      except: print('\nBook Not Available\n')

class own(Libary):
   def __init__(self,oemail,opass):
      self.email = oemail
      self.pas = opass
   @classmethod
   def uu(cls,ff):
      return cls(*ff.split('-'))

#===============================================================================  
# 1stgive book list,  2nd name 3d gamil, 4th password                          |
owner = own.uu("admin-alam")  #owner ar address                                |
shukur = Libary([],'Shukur Alam','x','y')  # x is Email and y is password #|
alam = Libary([],'alam man','x@gmail.com','y')           # x is Email and y is password #|
                                                                              #|
#===============================================================================


def se(x):
   while True:
      how = input('\nAdd book (Ab/1)\nDisplay Book (DB/2)\nBook Nai (BN/3)\nMy book (MB/4)\nReturn Book (RB/5)\nClose (CL/6)\nChoise One : ')
      if how == '1' or how == 'AB' or how =='Ab' or how == 'aB' or how == 'ab':
         x.add_book()
      elif how == '2' or how == 'DB' or how =='Db' or how == 'dB' or how == 'db':
         x.display_book()
      elif how == '3' or how == 'BN' or how =='Bn' or how == 'bN' or how == 'bn':
         x.book_naw_ami()
      elif how == '4' or how == 'MB' or how =='Mb' or how == 'mB' or how == 'mb':
         try:
            rt = x.owner_name.lower()
            wr = open(f'{rt}.txt','r')
            kn = wr.read()
            wr.close()
            ll = kn.split('\n')
            print(f'\n')
            print('My book',end=' : ')
            for i in ll:
               print(i,end=',')
            print(f'\n')
         except : print(f'\n You have no book')
      elif how == '5' or how == 'RB' or how =='Rb' or how == 'rB' or how == 'rb':
         x.return_book()
      elif how == '6' or how == 'CL' or how =='Cl' or how == 'cL' or how == 'cl':
         break
def info(e):
   while True:
      print(f'\n')
      rwr = input("Details (DE/1)\nExit (EX/2)\nchose one : ")
      if rwr == '1' or rwr =='De' or rwr == 'DE' or rwr == 'dE' or rwr == 'de':
         try:
            rtt = e.owner_name.lower()
            wr = open(f'{rtt}.txt','r')
            kn = wr.read()
            wr.close()
            ll = kn.split('\n')
            print(f'\n')
            print('have book',end=' : ')
            for i in ll:
               print(i,end=',')
            print(f'\n')
            print(f'{e.owner_name} Email {e.email} and password {e.pas}')
         except:
            print(f'\n Have No BOOK \n')
            print(f'{e.owner_name} Email {e.email} and password {e.pas}')
      elif rwr == '2' or rwr =='Ex' or rwr == 'EX' or rwr == 'eX' or rwr == 'ex':
         break

def admin():  
   while True:                                                                                          
      hh = input('Remove Book (RB/1)\nUser Details (UD/2)\nAdd Book(AB/3)\nExit (EX/4)\nChose one: ')      
      if hh == '1' or hh =='Rb' or hh == 'RB' or hh == 'rB' or hh == 'rb':
         try:
            book_li = open('Book_list.txt','r')
            ttr = book_li.read()
            book_li.close()
            ty = ttr.split('\n')
            print('\nAvailble',end=' : ') 
            for dr in ty:
               print(dr,end=',')
            print('\n')
            book_nam = input('\nBook Name: ')
            ty.remove(book_nam)

            book_li = open('Book_list.txt','w')

            for i in range(len(ty)):

               book_li.write(f'{ty[i]}\n')
            book_li.close()  
            print('\nSaccessfully remove from library\n')    
         except: print('\nHave no book\n')

      elif hh == '2' or hh =='Ud' or hh == 'UD' or hh == 'uD' or hh == 'ud':
         print(f"User name\n{shukur.owner_name} and {alam.owner_name}")                                       
         name_us = input('\nchose User name : ')  



#-------------------------------------Change it if You Add New mamber------------------
#======================================================================================
         if name_us == shukur.owner_name or name_us == shukur.owner_name.lower():     #|                      
            info(shukur)                                                              #|                    
         elif name_us == alam.owner_name or name_us == alam.owner_name.lower():       #|                     
            info(alam)                                                                #|
#======================================================================================       


      elif hh == '3' or hh == 'AB' or hh == "Ab" or hh == "aB" or hh == 'ab':
         owner.add_book()
      elif hh == '4' or hh =='Ex' or hh == 'EX' or hh == 'eX' or hh == 'ex':
         break

while True:
   email = input('\nEmail : ')
   pas = input('Password : ')
   print('\n\n')


#-------------------------------------Change it if You Add New mamber-----------------------------------
#=======================================================================================================
   if email == shukur.email or email == shukur.email.split('@')[0] and pas == shukur.pas:              #|
      se(shukur)                                                                                       #|
   elif email == owner.email or email == shukur.email.split('@')[0] and pas == owner.pas:              #|
      admin()                                                                                          #|
   elif email == alam.email or email == alam.email.split('@')[0] and pas == alam.pas:                  #|
      se(alam)                                                                                         #|
#========================================================================================================