from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about_section.html')
def services(request):
    return render(request, 'core/services_page.html')
def contact(request):
    # We will hook up active POST processing here later, for now it just renders the page view.
    return render(request, 'core/contact_section.html')


