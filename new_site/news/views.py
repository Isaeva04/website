from django.shortcuts import render
from.models import News


#def news (request):  #html
    #return render(request, 'news.html')

def news_index(request):  # представление модели
    all_news=News.objects.all()
    context={
        'all_news':all_news
    }
    return render(request,'news_index.html', context)

def news_detail(request,pk):  # представление модели
    This_news=News.objects.get(pk=pk)
    context={
        'this_news':This_news
    }
    return render(request,'news_detail.html',context)