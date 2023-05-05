# i have created this page - prasnjit

from django.http import HttpResponse
from django.shortcuts import render
import os
import subprocess
from django.template import Context, loader
# def ping(request):
#     return render(request,'Home.html')

# def ping(request):

#     context = {}

#     if request.GET.get('q', False) == '':
#         context['ping_output'] = 'Please enter a domain name!'

#     elif 'q' in request.GET:
#         ping_output = os.popen('ping -c 4 ' + request.GET['q']).read()
#         context['ping_output'] = ping_output

#     return render(request,'home.html',context)

# Run the pip install command for binwalk

# def tool(request):
    # output={}

    # if request.GET.get('tool',False)=='':
    #     output['tool_output']='Enter the tool name'
    # elif 'tool' in request.GET:
    #      subprocess.run(['pip', 'install', tool, ])
    #     # output['tool_output']=tool_output
#     return render(request,'tool.html')

# def install(request):
#      tool = (request.GET["tools"])
#      subprocess.run(['pip','install',tool])
#      return render(request,'output.html',{"output":tool})

import subprocess

def git_log(request):
    # change directory to your git repo directory
    git_dir = "/path/to/your/git/repo"
    repo = git.Repo(git_dir)
    git_log = subprocess.check_output(['git', 'log', '-n', '10'], cwd=git_dir)
    # render git log in Django template
    return render(request, 'git_log.html', {'git_log': git_log})


def index(request):
    return render (request,'app.html')

# safely running tool

# def app(request):
#     tool = request.GET["tool"]
#     subprocess.run(['pip','install',tool])
#     return render(request,'output.html',{"output":tool})


def app(request):
    tool = request.GET["tool"]
    out=subprocess.check_output(['pip','install',tool])
    look=out.decode('utf-8')
    return render(request,'app.html',{"output":look})
    # tools=os.popen('pip list | seashells' ).read()

        

def dele(request):
    tool = request.GET["tool"]
    out=subprocess.check_output(['pip','uninstall','-y',tool])
    look=out.decode('utf-8')
    return render(request,'app.html',{"output":look})

    # subprocess.run(['pip','uninstall','-y',tool])
    # tools=os.popen('pip list   | seashells ').read()
   

    # return render(request,'output.html',{"output":tools},{"linux":look})
    
    
def list(request):
    out=subprocess.check_output(['pip','list',])
    look=out.decode('utf-8')
    return render(request,'app.html',{"output":look})