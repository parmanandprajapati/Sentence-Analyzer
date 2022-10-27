
from re import A
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Home")
    params={'name':'harry','place':'Neptune'}
    return render(request,'index.html',params)
def analyze(request):
    #get text
    text1=request.POST.get('text','default')
    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    countchar=request.POST.get('charcount','off')
    # print(text1)
    analyzed=''
    def newliner(s):
        st=''
        for char in s:
            if char!='\n' and char!='\r':
                st+=char
        return st
    def spacer(s):
        st=''
        for index,char in enumerate(s):
             if not (index<=len(s)-2 and s[index]==' ' and s[index+1]==' '):
                st+=char
        return st
   

    if removepunc=='on':
   
        punctuation="#,'.]\"[!@$%^&*()<>?/\|_-+=}{"
        for char in text1:
            if char not in punctuation:
                analyzed+=char


    if fullcaps=='on':
        if len(analyzed)==0:
            analyzed=text1.upper()
        else:
            analyzed=analyzed.upper()
       
    if newlineremover=='on':
        if len(analyzed)==0:
            analyzed=newliner(text1)
        else:
            analyzed=newliner(analyzed)
    
    if spaceremover=='on':
        if len(analyzed)==0:
            analyzed=spacer(text1)
        else:
            analyzed=spacer(analyzed)

    if countchar=='on':
        count=0
        for char in text1:
            if char==' ' or char =="\n" :
                pass
            else:
                count+=1
        params={'purpose':'counting character','analyzed_text':count}
        
        return render(request,'analyze.html',params)



   
    params={'purpose':'Remove Punctuation/UpperCase/Space remover/newLine remover','analyzed_text':analyzed}
    
    return render(request,'analyze.html',params)
