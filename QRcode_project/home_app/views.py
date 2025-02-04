from django.shortcuts import render

def render_home(request):
    return render(request=request, template_name='home_app/home_app.html')



# Create your views here.
