from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')


def register(request):
    return render(request, 'main/register.html')  # Renders register.html

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        with open('contact_data.txt', 'a') as f:
            f.write(f'Name: {name}\nEmail: {email}\nMessage: {message}\n\n')

        # JavaScript alert and redirection
        return HttpResponse("""
            <html>
            <head>
                <script type="text/javascript">
                    alert('Thank you for contacting us!');
                    window.location.href = '/';  // Redirect to index.html or the homepage URL
                </script>
            </head>
            <body>
            </body>
            </html>
        """)

    return render(request, 'main/index.html')


