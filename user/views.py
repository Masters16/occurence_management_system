from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from police import models as p_models
from .models import UserRegistration


# Create your views here.
@login_required(login_url='login')
def user_dashboard_view(request):
    user = UserRegistration.objects.get(user=request.user.id)

    return render(request, 'user/user_dashboard.html',
                  {'user': user})


@login_required(login_url='login')
def occurence_records_view(request):
    user = UserRegistration.objects.get(user=request.user.id)
    requests = p_models.OccurenceRecords.objects.all().filter(user_id=user.user_no)

    return render(request, 'user/occurence_records.html', context={'records': requests})
