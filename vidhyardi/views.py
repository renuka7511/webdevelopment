from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
	return HttpResponse("<h1>welcome to reya tutorial</h1>")

def centerexample(request):
	return HttpResponse("<center> <h1>Hii....! THIS IS RENUKA</h1> </center>")

def paragraph(request):
	return HttpResponse("<p> <h1>THIS IS DIVYA</h1>")

def example(request):
	return HttpResponse("<h1>welcome to reya tutorial</h1><br><h2>THIS IS DIVYA</h2><p>we are learning django")

def stringvalueex(request,name):
	return HttpResponse("hello.......!"+name)

def inte(request,num):
	return HttpResponse("age is ......%d"%num)

	
def samplehtmlex(request):
	return render(request,'student/sample.html')

def htmlcss(request):
	return render(request,'student/demo.html')

def ex(request):
    return render(request,'student/rrr.html')

def bootstrapex(request):
	return render(request,'student/bootstrapex.html')

def login(request):
	return render(request,'student/login.html')

def registration(request):
	if request.method=='POST':
		Fname=request.POST.get('fname')
		Lname=request.POST.get('lastname')
		Username=request.POST.get('username')
		Rollno=request.POST.get('rollnos')
		Email=request.POST.get('email')
		Password=request.POST.get('password')
		Mobile=request.POST.get('mobilenumber')
		#print(Fname,Lname,Username)
		data={'Fname':Fname,'Lname':Lname,'Username':Username,'Rollno':Rollno,'Email':Email,'Password':Password,'Mobile':Mobile}
		return render(request,'student/details.html',{'data':data})
	return render(request,'student/res.html')




