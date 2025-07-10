from django.shortcuts import render, get_object_or_404
from .models import Property
from django.db.models import Q

def property_list(request):
    query = request.GET.get('q')
    if query:
        properties = Property.objects.filter(
            Q(title__icontains=query) | Q(address__icontains=query) | Q(description__icontains=query)
        )
    else:
        properties = Property.objects.all()
    return render(request, 'listing/property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'listing/property_detail.html', {'property': property})
