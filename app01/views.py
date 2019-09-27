from django.shortcuts import  HttpResponse,render,redirect
from app01.models import *
from django.contrib import auth
import datetime
date = datetime.datetime.now().date()
now_date = str(date)
def index(request):
    get_session = request.session.get('session')
    if get_session=='session':
        pass
    else:
        return redirect('/login/')
    book_choices = Book.time_choices
    room_list = Room.objects.all()
    date_list = Book.objects.all().filter(date=now_date)
    htmls=""
    for room in room_list:
        htmls  += '<tr><td>{}({})</td>'.format(room.caption,room.max_num)
        for book in book_choices:
            flag = False
            for obj in date_list:
                if int(obj.time_id) == book[0] and obj.room.id == room.id:
                    flag = True
                    break
            if flag:
                if request.user.username == obj.user.username:
                     htmls += '<td  class ="postive1" room="{}" book="{}">{}</td>'.format(room.id,book[0],
                                                                                        obj.user.username)
                else:
                     htmls += '<td  class ="active" room="{}" book="{}">{}</td>'.format(room.id, book[0],
                                                                                         obj.user.username )

            else:
                htmls += '<td room="{}" book="{}"></td>'.format(room.id,book[0])

        htmls+='</tr>'

    return render(request,'index.html',locals())

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    user = Userinfo.objects.filter(username=name,password=pwd).first()
    if user:
        auth.login(request,user)
        request.session['session'] = 'session'
        return redirect('/index/')
    else:
        return redirect('/login/')

import json
def ajax_book(request):
    user = Userinfo.objects.filter(username=request.user.username).first()
    # ce_list = [
    #     Book(room_id=2,time_id=11,user=user,date=now_date),
    #     Book(room_id=2,time_id=9,user=user,date=now_date),
    #     Book(room_id=2,time_id=10,user=user,date=now_date),
    #
    # ]
    # Book.objects.bulk_create(ce_list)
    # ce_dic = {
    #     'room_id':2,
    #     'time_id':*ce_list
    #     'user':user,
    #     'date':now_date
    # }

    res = {'status':1,'msg':[]}
    kss =request.POST.get('kss')
    dic_list = request.POST.get('data_dict')
    data = json.loads(dic_list)
    for index,info in data.items():
        if index=='ADD':
            for room_id,field in info.items():
                for  time_id in field:
                    ce_list = [
                        Book(room_id=int(room_id), time_id=int(time_id), user=user, date=now_date),
                    ]
                    Book.objects.bulk_create(ce_list)
        else:
            for room_id,field in info.items():
                for time_id in field:
                    obj = Book.objects.filter(room_id=int(room_id),time_id=int(time_id),date=now_date).delete()
        res['msg']='/index/'
    return  HttpResponse(json.dumps(res))