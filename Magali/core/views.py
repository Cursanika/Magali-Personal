from django.shortcuts import render, HttpResponse


# barra de navegacion
html_base = """

<h1>Magali</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/projects">Proyectos</a></li>
    <li><a href="/about">Acerca</a></li>
    <li><a href="/contact">Contacto</a></li>
</ul>

"""

# Create your views here.

def home(request):
    return render(request, 'core/home.html')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
