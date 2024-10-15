from django.shortcuts import render
from django.http import HttpResponse
from .models import Family, FamilyMember
from django.views import generic

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

#Generic class-based view - it queries the db to get all records for the specified models
class FamilyListView(generic.ListView):
    model = Family
    context_object_name ='family_list'
    ordering = ['id']
 
class FamilyMemberDetailView(generic.DetailView):
    model = FamilyMember

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        family_id = self.object.id
        context['familymembers'] = FamilyMember.objects.filter(family_id=family_id)
        context['family'] = Family.objects.get(id=family_id)
        return context
