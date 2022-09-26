import pickle

def  Writerecord(sroll,sname,marks):
    with open ('students.dat','ab') as fl:        
        pickle.dump({"SROLL":sroll,"SNAME":sname,"MARKS":marks},fl)
       
def Readrecord():
    with open ('students.dat','rb') as fl:
        while True:
           try:
               rec=pickle.load(fl)
               print(f"Roll No: {rec['SROLL']}, Name: {rec['SNAME']}, Marks: {rec['MARKS']}\n")
           except EOFError:
                break
def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        marks=float(input("Enter Marks: "))
        Writerecord(sroll,sname,marks)
        

def Modify(r):
    with open ('students.dat','rb') as fl:
        newRecord=[]
        while True:
           try:
               rec=pickle.load(fl)
               newRecord.append(rec)
           except EOFError:
                break
    found=False
    for i in range(len(newRecord)):
        if newRecord[i]['SROLL']==r:
            name=input("Enter Name: ")
            marks=float(input("Enter Marks: "))

            newRecord[i]['SNAME']=name
            newRecord[i]['MARKS']=marks
            found =True

    if found==False:
        print("Record not found")
    with open ('students.dat','wb') as fl:
         for j in newRecord:
             pickle.dump(j,fl)


if __name__ == '__main__':
    while True:
        c=int(input('Enter Your Choice: \n1.Insert\n2.Dispaly\n3.Update\n0.Exit\n>>> '))
        if c==1:
            Input()
        elif c==2:
            Readrecord()
        elif c==3:
            r =int(input("Enter rollno: "))
            Modify(r)
        else:
            break