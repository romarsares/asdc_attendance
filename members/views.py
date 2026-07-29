from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Member
from .forms import MemberForm
from chapters.models import Province, Municipality, Barangay


@login_required
def member_list(request):
    members = Member.objects.select_related('region', 'municipality').all()
    return render(request, 'members/list.html', {'members': members})


@login_required
def member_create(request):
    form = MemberForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Member registered successfully.')
        return redirect('members:list')
    return render(request, 'members/form.html', {'form': form, 'title': 'Add Member'})


# HTMX endpoints for cascading dropdowns
def load_provinces(request):
    region_id = request.GET.get('region')
    provinces = Province.objects.filter(region_id=region_id) if region_id else Province.objects.none()
    return render(request, 'members/partials/dropdown_options.html', {'options': provinces})


def load_municipalities(request):
    province_id = request.GET.get('province')
    municipalities = Municipality.objects.filter(province_id=province_id) if province_id else Municipality.objects.none()
    return render(request, 'members/partials/dropdown_options.html', {'options': municipalities})


def load_barangays(request):
    municipality_id = request.GET.get('municipality')
    barangays = Barangay.objects.filter(municipality_id=municipality_id) if municipality_id else Barangay.objects.none()
    return render(request, 'members/partials/dropdown_options.html', {'options': barangays})
