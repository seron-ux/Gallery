from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    
    return render(request, 'home.html',{"images":images})

# def view_image(request,image_id):
#         '''    Method to get image by id    '''    
#         try:        
#             image = Image.objects.get(id =  image_id)    
            
#         except DoesNotExist:        
#             raise Http404()    
#         return render(request, "post.html", {"image":image})


def search_results(request):

    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})