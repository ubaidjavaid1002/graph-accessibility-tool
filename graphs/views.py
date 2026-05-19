from django.shortcuts import render
from .forms import GraphUploadForm
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def home(request):

    uploaded_image = None
    extracted_text = None

    if request.method == 'POST':

        form = GraphUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            graph = form.save()

            uploaded_image = graph.image.url

            image = Image.open(graph.image.path)

            extracted_text = pytesseract.image_to_string(image)

    else:

        form = GraphUploadForm()

    return render(request, 'graphs/home.html', {
        'form': form,
        'uploaded_image': uploaded_image,
        'extracted_text': extracted_text
    })