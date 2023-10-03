from django.shortcuts import render
from .form import FileForm
from django.http import HttpResponse
from .form import FileForm
import pandas as pd
from . import dataformattingmodule

# Create your views here.


def mainpage(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        file_list = []
        for x in request.FILES.getlist("file_field"):
            with open('fileformatter/pool/' + x.name, 'wb+') as destination:
                for chunk in x.chunks():
                    destination.write(chunk)
            file_list.append(x.name)
        res = dataformattingmodule.pass_to_formatter(file_list)
        print(res)

        print(file_list)
        print(request.FILES.getlist("file_field"))

        file_content = []
        for file in file_list:
            if not file.endswith('.parquet'):
                with open('fileformatter/pool/' + file, 'r') as f:
                    file_content.append([file, f.read()])
            else:
                file_content.append([file,pd.read_parquet(
                    'fileformatter/pool/' + file).to_string()])

        clean_content = []
        for file in file_list:
            if not file.endswith(".parquet"):
                with open('fileformatter/pool/formatted_' + file, 'r') as f:
                    clean_content.append([file, f.read()])
            else:
                clean_content.append([file, pd.read_parquet(
                    'fileformatter/pool/formatted_' + file).to_string()])
        logfilecontent = ""
        with open("fileformatter/pool/logfile.txt", 'r') as f:
            logfilecontent = f.read()

        return render(request, "mainpage.html", {'form': form, 'filecontent': file_content, 'cleancontent': clean_content, 'logfilecontent': logfilecontent})
    else:
        form = FileForm()
        file_content = []
        clean_content = []
        logfilecontent = ""
        return render(request, "mainpage.html", {'form': form, 'filecontent': file_content, 'cleancontent': clean_content, "logfilecontent": logfilecontent})


