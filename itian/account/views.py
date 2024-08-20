from lib2to3.fixes.fix_input import context

from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def account_list(request):
    #return HttpResponse('<H2>List of Accounts')
    account= [
        {'id':1 , 'email':'safa.suli.2@gmail.com', 'password':'112233'},
        {'id': 2, 'email': 'safa.abduallah2001@hotmail.com', 'password': '332211'},

    ]

    context={}
    context['account']=account
    return render(request,'account/accountList.html',context)

def create_account(request):
    #return HttpResponse('<H2>Create Account')
    return render(request,'account/createAccount.html')

def update_account(request, id):
    #return HttpResponse('<H2>Update Account')
    context = {}
    context = {'id': id}
    return render(request,'account/updateAccount.html', context)

def delete_account(request, id):
    #return HttpResponse('<H2>Delete Account')
    context = {}
    context = {'id': id}
    return render(request,'account/deleteAccount.html', context)

def account_info(request, id):
    #return HttpResponse('<H2>Account Info: {id}</H2>')
    context = {}
    context = {'id': id}
    return render(request,'account/accountInfo.html', context)