from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job
from ai_engine.utils import evaluate_application


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        resume = request.FILES['resume']
        answers = request.POST.get('answers')

        # TEMP: later replace with real PDF extraction
        resume_text = answers  

        result = evaluate_application(resume_text, job.description)

        # ⚠️ IMPORTANT: result is text, so we store it properly for now
        application = Application.objects.create(
            user=request.user,
            job=job,
            resume=resume,
            answers=answers,
            score=0,  # will fix AI parsing later
            strengths=result,
            weaknesses="",
            recommendations=""
        )

        return redirect('dashboard')

    return render(request, 'apply.html', {'job': job})


@login_required
def dashboard(request):
    applications = Application.objects.filter(user=request.user)

    return render(request, 'accounts/dashboard.html', {
        'applications': applications
    })