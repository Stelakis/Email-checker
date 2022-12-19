#-*-coding:cp1253-*-
x=raw_input("Δώσε το E-mail σου :")
i=0
email=''
while i<len(x):
   if x[i]=='@':
      y=0
      while x[i+y]!='.':
         email+=x[i+y]
         y+=1
   i+=1
if email!='':
   print"Το domail σας είναι το :",email[1:]
else:
   print"Άκυρο email!"
