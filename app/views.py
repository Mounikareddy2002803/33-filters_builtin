from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    t=datetime.datetime.now()

    d={'data':'hai python how r u','t':t,'c':10}

    return render(request,'filters.html',d)