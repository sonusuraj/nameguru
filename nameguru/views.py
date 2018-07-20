from django.shortcuts import render
from django.http import HttpResponse

import string

from .models import Name

from django.db import connection

# Create your views here.
'''def index(request):
    return HttpResponse("Hello welcome to NameGuru!")'''

def index(request):
    # Post method if data post
    if request.method == 'POST':
        religion = request.POST['religion']
        gender = request.POST['gender']
        lfirstletter = request.POST['firstletter'].lower()
        ufirstletter = request.POST['firstletter'].upper()
        nofletters = request.POST['nofletters']
        if nofletters:
            nm = []
            lt = []
            for i in range(1, int(nofletters) + 1):
                nofletter = request.POST['lt' + str(i)]
                if nofletter:
                    nm.append(i)
                    lt.append(nofletter)

        #SQL Query
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM nameguru_name WHERE religion = %s AND gender = %s  AND (LEFT(name, 1) = UPPER(%s) OR LEFT(name, 1) = LOWER(%s)) AND LENGTH(name) = %s",
                [religion, gender, lfirstletter, ufirstletter, nofletters])
            # row = cursor.fetchall()
            row = [item[0] for item in cursor.fetchall()]
            dl = []
            for i in row:
                if (i.lower()).count('a') == 2 and i[nm[0]-1].lower() == 'a' and i[nm[1]-1].lower() == 'a':
                    dl.append(i)

            dst = []
            for l in dl:
                row2 = Name.objects.values('name', 'meaning').filter(name__contains=l)
                dst.append(row2[0])
            return render(request, 'name.html', {'dts':dst})

            # return HttpResponse(row2)


    else:
        # name_list = Name.objects.all()
        context = {'arange': range(3,11), 'rrange': range(5), 'string': string.ascii_uppercase }
    return render(request, 'index.html', context)

