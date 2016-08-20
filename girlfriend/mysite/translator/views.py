from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import userinput_form

# Create your views here.
'''
def save():
	text = request.forms.get('text')
	print(text)

def svm_classify():
	feed_data = save()

def answer():
'''

#page 2
def user_input(request):
	return render(request, 'user_input.html')

#function 3, enter 分類跟計算分數的code
'''
def os_output(request):	
	form = userinput_form()
	return render(request, 'os_output.html',{
		'form': form
		})
'''

def post_new(request):
    form = userinput_form(request.POST)
    return render(request, 'post_edit.html', {'form': form})


