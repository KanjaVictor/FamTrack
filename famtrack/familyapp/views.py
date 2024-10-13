from django.shortcuts import render
from django.http import HttpResponse
from .models import Family, FamilyMember

# Create your views here.
def index(request):
    num_families = Family.objects.all().count()
    num_members = FamilyMember.objects.all().count()

    #num_parents = FamilyMember.objects.filter(type_of_member_description='Parent').count()

    context = {
        'num_families': num_families,
        'num_members': num_members,
        #'num_parents': num_parents,
    }

    #return HttpResponse("Association of Family Members")
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')