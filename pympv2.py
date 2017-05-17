import os,sys
def pymp(dir='/yourmusicfolder'):
    c=1
    db={}
    pc=[]
    rc={'1':'1','2':'12','3':'123'}
    os.chdir(dir)
    i=raw_input('with: ')
    for ld in os.listdir(dir):
        if (ld.startswith(i) or ld.startswith(i.upper())):
            print c,ld
            db[c]=ld
            c+=1
    ri=raw_input('Repeat: ')
    while 1:                  
        for dbn in range(1,len(db)+1):
            for rp in rc[ri]:
                print '\n Playing Now ...\n{0}:{1}'.format(dbn,db[dbn])
                print '{r:>10}:{l}'.format(r='Repeat',l=rp)
                play=os.system('andplay {0}'.format(db[dbn]))
            pc.append(play)     
    print '\nPyMp Stop!'
    if len(pc)<=1:
        print '\n {l:>30} {p}'.format(p='song play in all',l=len(pc))
    elif len(pc)>=1:
        print '\n {l:>30} {p}'.format(p='songs play in all',l=len(pc))
try:
    pymp()
except (KeyboardInterrupt,EOFError):
    print '\nProgram Exit'   
    sys.exit(0)
except KeyError:
    print 'Repeat: 1 2 3'
pymp()