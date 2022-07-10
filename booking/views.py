from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from sso_user.models import Sso_Register
from visitor.models import Visitor_Register
from django.core import serializers

def booking_process(request):
    if request.method == "POST":
        print("Hi")
        zone = request.POST.get('zone')
        date = request.POST.get('date')
        shift = request.POST.get('shift')
        vehicle_type = request.POST.get('vehicle_type')
        data_obj = Visitor_Register.objects.filter(zone=zone,visit_date=date, choose_shift=shift, vehicle_type=vehicle_type)
        data = serializers.serialize('json', data_obj)
        return JsonResponse(data, safe=False) 
        # filter_arr = []
        # if request.POST.get('zone') is not None:
        #     print("Detected")
        #     zone = request.POST.get('zone')
        #     filter_arr.append(zone)
        #     zone_ = Visitor_Register.objects.filter(zone=zone)
        #     data = serializers.serialize('json', zone_)
        #     #return JsonResponse(data, safe=False)

        # if request.POST.get('date') is not None:
        #     print("Detected")
        #     date = request.POST.get('date')
        #     filter_arr.append(date)
        #     print("date:", date)
        #     date_ = Visitor_Register.objects.filter(visit_date=date)
        #     data = serializers.serialize('json', date_)
        #     print(data)
        #     #return JsonResponse(data, safe=False) 
        
        # if request.POST.get('shift') is not None:
        #     print("Detected")
        #     shift = request.POST.get('shift')
        #     filter_arr.append(shift)
        #     shift_ = Visitor_Register.objects.filter(choose_shift=shift)
        #     data = serializers.serialize('json', shift_)
        #     #return JsonResponse(data, safe=False) 
        
        # if request.POST.get('vehicle_type') is not None:
        #     print("Detected")
        #     vehicle_type = request.POST.get('vehicle_type')
        #     filter_arr.append(vehicle_type)
        #     vehicle_type_ = Visitor_Register.objects.filter(vehicle_type=vehicle_type)
        #     data = serializers.serialize('json', vehicle_type_)
        #     #return JsonResponse(data, safe=False) 
        # else:
        #     print("Not Detected")
        # print(filter_arr)
        
    context = {"sso":Sso_Register.objects.filter(user=request.user)}

    return render(request, 'booking-process.html', context)

def submitted_visitor_report(request):
    data_obj = Visitor_Register.objects.filter(user=request.user)
    context = ({'data_obj': data_obj})
    return render(request, 'submitted-visitor-report.html', context)

