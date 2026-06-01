from django.shortcuts import render
from .forms import GraphUploadForm

import pytesseract
import cv2
import numpy as np

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

            # using opencv to preprocess the image before extracting text
            # cv2 reads image as matrix
            image = cv2.imread(graph.image.path)

            # convert to grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

            # apply thresholding to get binary image
            thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]

            extracted_text = pytesseract.image_to_string(thresh)
    else:

        form = GraphUploadForm()

    return render(request, 'graphs/home.html', {
        'form': form,
        'uploaded_image': uploaded_image,
        'extracted_text': extracted_text
    })