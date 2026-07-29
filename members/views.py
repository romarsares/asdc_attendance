# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Member


@login_required
def member_list(request):
    members = Member.objects.select_related('region', 'municipality').all()
    return render(request, 'members/list.html', {'members': members})
