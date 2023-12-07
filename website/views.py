from django.shortcuts import render
from job.models import Job, ApplyJob
from .filter import Jobfilter


# Create your views here.
def home(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter':filter}
    return render(request, 'website/home.html', context)


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'website/job_listing.html', context)




from django.shortcuts import get_object_or_404

def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    has_applied = False
    if request.user.is_authenticated:
        has_applied = ApplyJob.objects.filter(user=request.user, job=job).exists()

    context = {'job': job, 'has_applied': has_applied}
    return render(request, 'website/job_details.html', context)




#===========================================================================

def about(request):
    return render(request, 'about.html')


def error(request):
    return render(request, '404.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == "POST":
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        massage = request.POST.get('massage')  

    
        contact_instance = Contact(name=name, email=email, subject=subject, massage=massage)
        contact_instance.save()

        
        messages.success(request, 'Thank you for contacting us, We will contact you soon')

        
        return redirect('contact')

    return render(request, 'contact.html')












