from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", "")
        school = request.POST.get("school", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        skills = request.POST.get("skills", "")
        about_you = request.POST.get("about_you", "")
        previous_job = request.POST.get("previous_job", "")

        profile = Profile(name=name, email=email, mobile=mobile, school=school, degree=degree, university=university, skills=skills, about_you=about_you, previous_job=previous_job)
        profile.save()

    return render(request, "accept.html")

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({"user_profile": user_profile})
    options = {
            'page-size': 'letter',
            'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition']='attachment'
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request, "list.html", {'profile': profile})

