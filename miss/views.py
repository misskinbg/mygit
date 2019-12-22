from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse,render_to_response,HttpResponseRedirect,HttpResponse
# from django.contrib.auth.models import User
from django.contrib import auth
from .models import Student
from .models import Class



def index(request):
    # print request.method
    # print request.
    return render(request,'login.html')




def login(request):
    if request.method == 'POST':

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password: # 验证用户名和密码是否为空
            try:
                students = Student.objects.get(xuehao=username, mima=password)
                return HttpResponseRedirect('find')
            except:

                return render(request, 'login.html', )
        else:

            return render(request,'login.html',)

    elif request.method == 'GET':
        return render(request,'login.html')



# def reg(request):
#     if request.method == 'POST':
#         user = request.POST.get('user',None)
#         pwd = request.POST.get('pwd',None)
#         print (user,pwd,)
#         if user and pwd:
#             return HttpResponse('注册成功')
#         else:
#             return HttpResponse('用户名与密码不为空')
#
#     elif request.method == 'GET':
#         return render(request,'reg.html')


# def find(request):
#     import pymysql
#     conn = pymysql.connect(host='127.0.0.1',prot = 3306,user='root',password='',db='python')
#     cursor = conn.cursor()
#     cursor.execute("select id,title from class")
#     class_list = cursor.fetchall()
#     cursor.close()
#     conn.close()
#
#     return render(request,'find.html')


def find(request):

    return render_to_response('find.html')
    # return render(request,'tpl.html')

def logout(request):

    return render(request, 'login.html')

def aa2(request):

    return render(request, 'aa2.html')

def aa1(request):
    cls = Class.objects.all()
    a=[[]]
    k=0
    for i in cls:
        for j in i.__dict__.values():
            a[k].append(str(j))
        a[k].pop(0)
        a[k].pop(1)
        k=k+1
        a.append([])
    context={
        'chengji':a
    }
    return render(request,'aa1.html',context=context)

def aa4(request):

    return render(request, 'aa4.html')

def aa3(request):

    return render(request, 'aa3.html')
def aa5(request):

    return render(request, 'aa5.html')
def aa6(request):

    return render(request, 'aa6.html')
def aa7(request):

    return render(request, 'aa7.html')
def aa8(request):

    return render(request, 'aa8.html')
def aa9(request):

    return render(request, 'aa9.html')
def aa10(request):

    return render(request, 'aa10.html')

def admin(request):

    return render(request, 'admin')

