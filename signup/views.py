from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
dob=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,dob,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="swathi@12",database="django")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_name":
                fn=value
            if key=="Last_name":
                ln=value
            if key=="Date_of_Birth":
                dob=value
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value 
        c="insert into details values('{}','{}','{}','{}','{}')".format(fn,ln,dob,em,pwd)
        
        cursor.execute(c)
        m.commit()
    
    return render(request,'signuppage.html') 
    

    