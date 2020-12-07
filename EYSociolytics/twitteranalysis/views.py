from django.shortcuts import render,redirect
from .scrapers import scraper1,scraper2,scraper3
from .nlpengine import nlpenginetwitter
import time

sentiment_values=''
hashtags=''
# Create your views here.
def twitterhome(request):
    return render(request,'twitteranalysis/home.html')

def options(request):
    return render(request,"twitteranalysis/options.html")

def inputform1(request):
    if request.method=='POST':
        username=request.POST.get("username")
        scraper1.csv_creator_one(username)
        time.sleep(20)
        global sentiment_values
        sentiment_values=nlpenginetwitter.sentiment_average_calculator()
        global hashtags
        hashtags=nlpenginetwitter.hashtags_finder()
        return redirect("result")
    
    return render(request,"twitteranalysis/inputform1.html")

def inputform2(request):
    if request.method=='POST':
        search=request.POST.get("search")
        scraper2.csv_creator_two(search)
        time.sleep(20)
        global sentiment_values
        sentiment_values=nlpenginetwitter.sentiment_average_calculator()
        global hashtags
        hashtags=nlpenginetwitter.hashtags_finder()
        return redirect("result")

    return render(request,"twitteranalysis/inputform2.html")

def inputform3(request):
    if request.method=='POST':
        username=request.POST.get("username")
        keyword=request.POST.get("keyword")
        since=request.POST.get("since")
        until=request.POST.get("until")
        limit=request.POST.get("limit")
        scraper3.csv_creator_three(username,keyword,since,until,limit)
        time.sleep(60)
        global sentiment_values
        sentiment_values=nlpenginetwitter.sentiment_average_calculator()
        global hashtags
        hashtags=nlpenginetwitter.hashtags_finder()
        return redirect("result")
    return render(request,"twitteranalysis/inputform3.html")

def inputform4(request):
    if request.method=='POST':
        username=request.POST.get("username")
        scraper2.csv_creator_two(username)
        time.sleep(20)
        global sentiment_values
        sentiment_values=nlpenginetwitter.sentiment_average_calculator()
        global hashtags
        hashtags=nlpenginetwitter.hashtags_finder()
        return redirect("result")
    return render(request,"twitteranalysis/inputform4.html")

def result(request):
    context={
        'sentiment':sentiment_values,
        'hashtags':hashtags
    }
    print(context)
    return render(request,"twitteranalysis/result.html",context)