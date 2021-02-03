from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
arr = 'ABAP ActionScript Ada ALGOL Alice APL ASP.NET Assembly_Language Awk BBC_Basic C C++ C-shop CSS COBOL Delphi Dreamweaver Erlang Elixir FORTH FORTRAN Functional_Programming Go Haskell HTML IDL INTERCAL Java Javascript jQuery LabVIEW Lisp Logo MetaQuotes_Language ML Modula-3 MS_Access MySQL NXT-G Objective-C OCaml Pascal Perl PHP PL/I PL/SQL PostgreSQL PostScript Pure_Data Python R RapidWeaver RavenDB Rexx Ruby S-PLUS SAS Scala Sed SGML Simula Smalltalk SMIL SNOBOL SQL SQLite SSI Stata Swift Tcl/Tk TeX LaTeX Unified_Modeling_Language Unix_Shells Verilog VHDL Visual_Basic Visual_FoxPro VRML WAP/WML XML XSL'.split()
dic = {}
co={}

def home(request):
    dic1 = {
        'arr': arr
    }
    return render(request, 'voting_home.html', context=dic1)


def aquery(request):
    global dic
    if request.GET['lang'] not in dic:
        dic[request.GET['lang']] = 1

    else:
        dic[request.GET['lang']] += 1
    dic1 = {
        'arr': arr,
        'dic': dic,
    }
    return render(request, 'voting_home.html', context=dic1)


def sorte(request):
    global dic
    co=dict(sorted(dic.items() ,reverse=True,key=lambda x: x[1]))
    dic1 = {
        'arr': arr,
        'dic':co
    }
    return render(request, 'voting_home.html', context=dic1)
