from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.shortcuts import get_object_or_404, render
from models import *

def index(request):
    answer='Select view:<br/><a href=./files>Files</a>'
    return HttpResponse(answer)

def fileshashes(request):
    flist = File.objects.all()
    answer = ''

    for f in flist:
        hashes = FileHash.objects.filter(file=f.id)
        answer += f.id.__str__() + ':' 
        answer += ','.join('%s' % h for h in hashes)

        answer += '\n'

    return HttpResponse(answer)

def fileshashesjson(request):
    flist = File.objects.all()
    answer = '{['

    for file in flist:
        hashes = FileHash.objects.filter(file=file.id)
        answer += ',\n'.join(hash.__json__() for hash in hashes)

    answer += ']}'
    return HttpResponse(answer, mimetype='application/json')

def fileedit(request, fileid):
    if request.method == 'GET':
        f = get_object_or_404(File, pk=fileid)
        dirs = Directory.objects.all()
        context = Context({ 'file': f,
                            'dirs': dirs})

        return render(request, 'cygapp/fileedit.html', context)

    elif request.method == 'POST':
        f = get_object_or_404(File, pk=fileid)
        f.name = request.POST['name']
        context = {}
        if request.POST['path'] is None or request.POST['path'] == '':
            context['file'] = f
            context['dirs'] = Directory.objects.all()
            context['message'] = 'Path cannot be empty!'
            return render(request, 'cygapp/fileedit.html', context)

        dir, created = Directory.objects.get_or_create( path = request.POST['path'] )
        if created:
            print('Warning: had to create new directory (' + str(dir.id) + ')')

        print(str(dir.id) + ': ' + dir.path)
        f.directory = dir
        f.save()
        return HttpResponseRedirect('/cygapp/files/' + str(f.id) + '/edit')
    
    #No valid HTTP method
    raise Http500


def filejson(request, fileid):
    f = get_object_or_404(File, pk=fileid)
    return HttpResponse(f.__json__(), mimetype='application/json')

def filehashes(request, fileid):
    f = get_object_or_404(File, pk=fileid)
    hashes = FileHash.objects.filter(file=f.id)
    if hashes.count() == 0:
        return HttpResponse('No hashes')
    
    return HttpResponse('<br/>\n'.join(hash.__str__() for hash in hashes))

def filehashesjson(request, fileid):
    f = get_object_or_404(File, pk=fileid)
    hashes = FileHash.objects.filter(file=f.id)
    if hashes.count() == 0:
        return HttpResponse('{}', mimetype='application/json')

    return HttpResponse('\n'.join(hash.__json__() for hash in hashes), mimetype='application/json')

def startlogin(request, deviceID):
    try:
        device = Device.objects.get(value=deviceID)
    except Device.DoesNotExist:
        return HttpResponse(status=404,content=None)
    
    device.createWorkItems()
    return HttpResponse(content=None)

def finishlogin(request, deviceID):
    raise NotImplementedError
