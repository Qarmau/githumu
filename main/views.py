# main/views.py
from django.shortcuts import render,redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
import json
from django.core.serializers.json import DjangoJSONEncoder
from .forms import ContactForm
from .forms import JobApplicationForm

def home(request):
    events = CalendarEvent.objects.all()
    events_json = json.dumps(list(events.values()), cls=DjangoJSONEncoder)
    return render(request, 'main/home.html', {'events_json': events_json})

"""def home(request):
    events = Event.objects.all().order_by('-date')[:5]
    news = News.objects.all().order_by('-date')[:5]
    calendar_events = CalendarEvent.objects.all().order_by('date')[:10]
    return render(request, 'main/home.html', {'events': events, 'news': news, 'calendar_events': calendar_events})"""


# main/views.py
def about(request):
    about = About.objects.first()
    #sections = AboutSection.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            try:
                send_mail(
                    f'Contact form submission from {name}',
                    f'From: {email}\n\nMessage:\n{message}',
                    email,  # From email
                    [about.email],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, f'An error occurred while sending your message: {str(e)}')
            
            return redirect('about')
    else:
        form = ContactForm()

    #return render(request, 'main/about.html', {'sections': sections,'form': form})
    return render(request, 'main/about.html', {'about': about, 'form': form})


























"""def about(request):
    sections = AboutSection.objects.all()
    
    return render(request, 'main/about.html', {'sections': sections})"""






"""def about(request):
    about = About.objects.first()
    return render(request, 'main/about.html', {'about': about})"""

def administration(request):
    administrators = Administrator.objects.all().order_by('order')
    return render(request, 'main/administration.html', {'administrators': administrators})


# main/views.py



def teaching_staff(request):
    staff = TeachingStaff.objects.all()
    return render(request, 'main/teaching_staff.html', {'staff': staff})




"""def teaching_staff(request):
    staff = TeachingStaff.objects.all().order_by('order')
    return render(request, 'main/teaching_staff.html', {'staff': staff})"""

"""def achievements(request):
    university_rates = Achievement.objects.all().order_by('year')
    awards = CoCurricularAward.objects.all().order_by('-year')
    return render(request, 'main/achievements.html', {'university_rates': university_rates, 'awards': awards})"""

# main/views.py



def achievements(request):
    university_rates = Achievement.objects.all().order_by('year')
    awards = CoCurricularAward.objects.all()
    return render(request, 'main/achievements.html', {'university_rates': university_rates, 'awards': awards})





def holiday_assignments(request):
    assignments = HolidayAssignment.objects.all().order_by('-upload_date')
    grades = set(assignment.grade for assignment in assignments)
    return render(request, 'main/holiday_assignments.html', {'assignments': assignments, 'grades': grades})







def job_list(request):
    jobs = JobPosting.objects.all().order_by('-date_posted')
    return render(request, 'main/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, pk=job_id)
    
    if request.method == 'POST':
        if not job.is_active():
            messages.error(request, "Sorry, the deadline for this job has passed.")
            return redirect('job_detail', job_id=job.id)
        
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('application_success')
    else:
        form = JobApplicationForm() 
    
    return render(request, 'main/job_detail.html', {
        'job': job, 
        'form': form,
        'is_active': job.is_active()
    })

def application_success(request):
    return render(request, 'main/application_success.html')