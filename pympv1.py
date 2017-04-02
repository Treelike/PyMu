import os, sys, time
#importing modules    
def pymp():
    db={}
    c=1
    pc=[]
    
    while 1:
        dir='/yourmusicfolder'
        os.chdir(dir)
        i=raw_input('with: ')
        for ld in os.listdir(dir):
            if (ld.startswith(i) or
                ld.startswith(i.upper())):
                print c,ld
                db[c]=ld
                c+=1
        
        while 1:          
            rp=raw_input('Repeat: ')
            
            if rp=='1':
                for dbn in range(1,len(db)+1):
                    for ro in str('1'):
                        print '\n Playing Now ...\n{0}:{1}'.format(dbn,db[dbn])
                        print '{r:>10}:{l}'.format(r='Repeat',l=ro)
                        play=os.system('andplay {0}'.format(db[dbn]))
                    pc.append(play)                    
                                             
            elif rp=='2':
                for dbn in range(1,len(db)+1):
                    for rt in str('12'):        
                        print '\n Playing Now ...\n{0}:{1}'.format(dbn,db[dbn])  
                        print '{r:>10}:{l}'.format(r='Repeat',l=rt)
                        play=os.system('andplay {0}'.format(db[dbn]))
                    pc.append(play)
                        
            elif rp=='':   
                print '\n Repeat:Step*'        
                while 1:
                    for dbn in range(1,len(db)+1):
                        print '\n Playing Now ...\n{0}:{1}'.format(dbn,db[dbn])
                        play=os.system('andplay {0}'.format(db[dbn]))    
                        continue 
                    for dbn in range(1,len(db)+1,2):
                        print '\n Playing Now ...\n{0}:{1}'.format(dbn,db[dbn])
                        play=os.system('andplay {0}'.format(db[dbn]))    
                               
                        
            else:
                print 'Repeat: 1 2 (enter) for All'
    print 'PyMp Stop!'
    if len(pc)<=1:
        print '\n {l:>30} {p}'.format(p='song play in all',l=len(pc))
    elif len(pc)>=1:
        print '\n {l:>30} {p}'.format(p='songs play in all',l=len(pc))
try:
    pymp()
except (KeyboardInterrupt,EOFError):
    print '\nProgram Exit'   
