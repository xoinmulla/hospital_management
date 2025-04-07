from django.shortcuts import render

def home(request):
    return render(request, 'core/homepage.html')

def contact(request):
    if request.method == "POST":
        # Extract form data
        name    = request.POST.get("name")
        email   = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # Here you could add code to send an email or save this data to your database.
        # For now, we simply render a success page.
        context = {"name": name}
        return render(request, "core/contact_success.html", context)
    
    # For GET requests, render the contact form
    return render(request, "core/contact.html")
