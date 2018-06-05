import os
def filenames(dirname):
    filename=[]
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            filename.append(path)
        else:
            filename.extend(filenames(path))
    return filename
def checksum(filename):
    cmd='md5sum'+filename
    return pipe(cmd)
def diff(a,b):
    cmd='diff %s %s'%(a,b)
    return pipe(cmd)
def pipe(cmd):
    fp=os.popen(cmd)
    res=fp.read()
    stat=fp.close()
    if stat is None:
        return res,stat
    else:
        raise ValueError()
def checks(dirname,suffix='py'):
    names=filenames(dirname)
    di={}
    for name in names:
        if name.endswith(suffix):
            res,stat=checks(name)
            checksum=res.split()[0]
            if checksum in di:
                di[checksum].append(name)
            else:
                di[checksum]=[name]
    return di
def pairs(names):
    for a in names:
        for b in names:
            if a<b:
                res,stat=diff(a,b)
                if res:
                    return False
    return True
def duplicates(di):
    for key,names in di.items():
        if len(names)>1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)
            if pairs(names):
                print('And they are identical.')
d=checks(dirname='C:\\Users\\acer e15\\Desktop\\python',suffix='py')
duplicates('python')
