from django.shortcuts import render
from .forms import GraphUploadForm

def home(request):

    uploaded_image = None

    if request.method == 'POST':

        form = GraphUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            graph = form.save()

            uploaded_image = graph.image.url

    else:

        form = GraphUploadForm()

    return render(request, 'graphs/home.html', {
        'form': form,
        'uploaded_image': uploaded_image
    })