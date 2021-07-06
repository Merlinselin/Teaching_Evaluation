from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from .models import TeachersDetails,StudentFeedback,register_table

# Create your views here.

def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")

def studentfeedback(request):
	return render(request,"studentfeedback.html")

def studentfeedback(request):
    try:
        Name_of_The_Teacher=request.POST['Name_of_The_Teacher']
        Subject=request.POST['Subject']
        Punctuality=request.POST['Punctuality']
        Portion_Completion=request.POST['Portion_Completion']
        Doubt_Clearing=request.POST['Doubt_Clearing']
        Other_Comments=request.POST['Other_Comments']
        feedbackdtls=StudentFeedback(Name_of_The_Teacher=Name_of_The_Teacher,Subject=Subject,Punctuality=Punctuality,Portion_Completion=Portion_Completion,Doubt_Clearing=Doubt_Clearing,Other_Comments=Other_Comments)
        feedbackdtls.save()
        return render(request,"sucess.html",{'msg5':"Feedback Submitted"})
    

    except Exception as e:
        print(e)
        return render(request,"studentfeedback.html",{'msg6':"Cannot be Added"})

def sucess(request):
	return render(request,"sucess.html")


def teacherdetails(request):
	try:
		Firstname=request.POST['Firstname']
		LastName=request.POST['LastName']
		Gender=request.POST['Gender']
		Qualification=request.POST['Qualification']
		Experience=request.POST['Experience']
		teacherdtls=TeachersDetails(Firstname=Firstname,LastName=LastName,Gender=Gender,Qualification=Qualification,Experience=Experience)
		teacherdtls.save()
		return render(request,"teacher-home.html")
	except Exception as e:
		print(e)
		return render(request,"teacherdetails.html")






def teacherhome(request):
	return render(request,"teacher-home.html")


def viewfeedback(request):
	ob=StudentFeedback.objects.all()
	return render(request,"viewfeedback.html",{'ob':ob})



def register(request):
	if request.method=="POST":
		fname=request.POST["first_name"]
		last=request.POST["last_name"]
		un=request.POST["username"]
		em=request.POST["email"]
		phn=request.POST["phn_number"]
		pwd=request.POST["psw"]
		rpwd=request.POST["psw-repeat"]
		tp=request.POST["utype"]

		usr=User.objects.create_user(username=un,email=em,password=pwd)
		usr.first_name=fname
		usr.last_name=last
		if tp=="teacher":
			usr.is_staff=True
		usr.save()
		reg=register_table(user=usr,phone_number=phn)
		reg.save()
		return render(request,"registration/login.html",{"status":"{} Register Successfully".format(fname)})

	return render(request,"registration.html")



def user_login(request):
	if request.method=="POST":
		un=request.POST["username"]
		ps=request.POST["password"]
		
		user=authenticate(username=un,password=ps)
		if user:
			login(request,user)
			if user.is_superuser: 
				return redirect("/admin")
			if user.is_staff:
				return redirect("studentfeedback")
			if user.is_active:
				return redirect("teacherhome")
	else:
		return render(request,'user_login.html',{"status":"Invalid User Name or Password"})