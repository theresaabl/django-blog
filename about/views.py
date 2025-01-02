from django.shortcuts import render, get_object_or_404
from .models import About


# Create your views here.
def about(request):

    queryset = About.objects.all().order_by("-updated_on")
    about = get_object_or_404(queryset.first())

    return render(
        request,
        "about/about.html",
        {
            "about": about,
        },
    )
