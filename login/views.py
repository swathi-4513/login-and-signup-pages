from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="swathi@12",database="django")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value 
        c="select * from details where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')

    return render(request,'loginpage.html') 

    
# Create your views here.
 
    