import datetime
import uuid
import random
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OccurenceRecordsForm
from django.contrib import messages
from .models import PoliceRegistration, OccurenceRecords, OccurenceReport, UserReport
from user import forms as u_forms
from user import models as u_models

from .function import *
# Create your views here.
@login_required(login_url='login')
def police_dashboard_view(request):
    police = PoliceRegistration.objects.get(user=request.user.id)

    return render(request, 'police/police_dashboard.html',
                  {'police': police})


@login_required(login_url='login')
def add_occurence_view(request):
    police = PoliceRegistration.objects.get(user=request.user.id)
    recordForm = OccurenceRecordsForm()

    mydict = {'recordForm': recordForm}
    if request.method == 'POST':
        print('<>')
        recordForm = OccurenceRecordsForm(request.POST)
        if recordForm.is_valid():
            print('<>')
            user = recordForm.save(commit=False)
            user.station_id = police.station_id.station_name
            user.save()

            # notify_admin_about_new_donor(donor, user_name)  # remove when uploading to server

            messages.success(request, "Occurence record has been saved.")
            return render(request, 'police/create-record.html', context=mydict)
        else:
            messages.error(request, 'There was an error in adding record')
            messages.error(request, recordForm.errors)
            return render(request, 'police/create-record.html', context=mydict)

    return render(request, 'police/create-record.html', context=mydict)


@login_required(login_url='login')
def add_user_record(request):
    recordForm = u_forms.UserRegistrationForm()

    mydict = {'recordForm': recordForm}
    if request.method == 'POST':
        print('<>')
        recordForm = u_forms.UserRegistrationForm(request.POST)
        if recordForm.is_valid():
            print('<>')
            user = recordForm.save()

            user_code = user.user_no

            # user_name = user.first_name + " " + user.last_name
            # notify_admin_about_new_donor(donor, user_name)  # remove when uploading to server
            user_data = u_models.UserRegistration.objects.get(user_no=user_code)
            user.user = create_user_account(user_data)
            user_data.save(update_fields=['user'])

            messages.success(request, "User details have been saved.")
            return render(request, 'police/create_user_record.html', context=mydict)
        else:
            messages.error(request, 'There was an error in registering the user')
            messages.error(request, recordForm.errors)
            return render(request, 'police/create_user_record.html', context=mydict)

    return render(request, 'police/create_user_record.html', context=mydict)


@login_required(login_url='login')
def occurence_records_view(request):
    police = PoliceRegistration.objects.get(user=request.user.id)
    records = OccurenceRecords.objects.all().filter(police_id=police.police_id)
    return render(request, 'police/occurence_records.html', context={'records': records})


def create_user_account(user):
    random_num = random.randrange(0, 100)
    # Create a new user
    user = User.objects.create_user(username=f'{user.name}{random_num}',
                                    password=f'{user.id_card}')

    # Add the user to the "Volunteers" group
    group = Group.objects.get_or_create(name='USER')
    # user.groups.add(group)
    group[0].user_set.add(user)

    # Save the user
    user.save()
    print('user has been generated', user)

    return user

def occurence_report_view(request):
    the_police = PoliceRegistration.objects.get(user=request.user.id)
    reports = OccurenceReport.objects.filter(police=the_police.police_id)
    return render(request, 'police/occurence_reports.html', {'reports': reports})


# this view is dedicated to generate individual volunteer donation reports
def generate_occurence_report(request):
    the_police = PoliceRegistration.objects.get(user=request.user.id)

    all_reports = OccurenceRecords.objects.all()

    reports_count = OccurenceReport.objects.all().count()

    # donation_array = list(all_donations)
    donation_array = [d.json() for d in all_reports]

    print("XXXXXXXXXXXXXXXXXXXXX")
    print(donation_array)
    # print(donation_array[0].donor.user.first_name)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    payload = {
        "station_name": f"{the_police.station_id.station_name}",
        "station_id": f"{the_police.station_id.station_id}",
        "the_police": f"{the_police.police_id}",
        "document_number": f"000{reports_count}",
        "document_date": f"{current_date}",

        "records": donation_array
    }
    report_data = generate_o_report('occurence', "occurence_template.html", payload)
    #
    if report_data != 'error':
        generated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #doc_path = generate_doc_path(report_data['document']['id'], report_data['document']['meta'], 'donation-reports')

        # save the new report to the database
        new_report = OccurenceReport(the_police.police_id, report_data['id'],
                                    the_police.station_id.station_id,
                                    "Occurence_report", report_data['doc_path'], generated_date)
        new_report.save()
        messages.success(request, "Occurence_report generated successfully and saved to files")
        return HttpResponseRedirect('/police/occurence-reports/')
    else:
        messages.error(request, "There was an error generating a new report")
        print('An error occurred')
        return HttpResponseRedirect('/police/occurence-reports/')

    return HttpResponseRedirect(('/police/occurence-reports/'))


def user_report_view(request):
    the_police = PoliceRegistration.objects.get(user=request.user.id)
    reports = UserReport.objects.filter(police=the_police.police_id)
    return render(request, 'police/users_reports.html', {'reports': reports})


def generate_users_report(request):
    the_police = PoliceRegistration.objects.get(user=request.user.id)

    reports_count = UserReport.objects.all().count()

    all_users = u_models.UserRegistration.objects.all()
    # donation_array = list(all_donations)
    users_array = [d.json() for d in all_users]


    # print(donation_array[0].donor.user.first_name)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    payload = {
        "station_name": f"{the_police.station_id.station_name}",
        "station_id": f"{the_police.station_id.station_id}",
        "police_id": f"{the_police.police_id}",
        "document_number": f"000{reports_count}",
        "document_date": f"{current_date}",

        "users": users_array
    }
    report_data = generate_u_report('user', "users_template.html", payload)
    #
    if report_data['status'] == 'success':
        generated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # save the new report to the database
        new_report = UserReport(the_police.police_id, report_data['id'],
                                 the_police.station_id.station_id,
                                 "users-report", report_data['doc_path'], generated_date)
        new_report.save()
        messages.success(request, "User report generated successfully and saved to files")
        return HttpResponseRedirect('/police/users-reports')
    else:
        messages.error(request, "There was an error generating a new report")
        print('An error occurred')
        return HttpResponseRedirect('/police/users-reports')

    return HttpResponseRedirect('/police/users-reports')

def download_user_report(request, pk):
    #report_url = get_document_url(pk)
    report = UserReport.objects.get(report_id=pk)

    return HttpResponseRedirect(report.file.url)
def download_occurence_report(request, pk):
    #report_url = get_document_url(pk)
    report = OccurenceReport.objects.get(report_id=pk)

    return HttpResponseRedirect(report.file.url)

