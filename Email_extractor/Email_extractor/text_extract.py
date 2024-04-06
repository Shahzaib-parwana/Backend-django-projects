from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def index(request):
    djtext = request.GET.get('text', 'default')
    words = djtext.split()
    emails = ''
    i=0
    for word in words:
        if '@' in word and '.' in word:
            if word.count('@') ==1 and word.count('.') >=1:
                i+=1
                email = word.strip('.,?!:;"\'()[]{}')
                # emails.append(email)
                
                emails +=(f'=>({i}) {email} \n')
                 
    object = {'purpose': 'Extrected emails', 'email_extract': emails}
    return render(request, 'response.html', object)   
         