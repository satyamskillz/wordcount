
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")

def count(request):
    fulltext=request.GET['fulltext']
    words=fulltext.split()
    worddic={}
    for word in words:
        if word in worddic:
            worddic[word]+=1
        else:
            worddic[word]=1
    sortedwords=sorted(worddic.items(),reverse=True)
    return render(request,"count.html",{'username':fulltext,'sortedwords':sortedwords})
