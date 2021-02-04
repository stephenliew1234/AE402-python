d)import os.path

def={}

def buildmenu:
    print('=>')
    print('1.Choose words')
    print('2.list out all thw words')
    print('3.English translate to Chinese')
    print('4.Chinese tranlate to English')
    print('5.Test skills that you learn')
    print('6.leave system')
    

if not os.path.isfile('my dictionary.text'):
    fo=open('mydictionary.txt','w')
    print('new file')
else:
    fo=open('mydictionary.txt,'r')
            print('old file')

fow row in fo.readliness():
            data=row.split(':')

            key=data[0]
            value=data[1]
            value=value strip()


            d[key]=value
            print(d)

            fo.close()


while True:
    build menu

    
 while True:           
    if sel=='1':
        while True:
            voc=input('please enter new word(press0 to go out')
            if voc=='0':
                break
            if voc not in d:
                m=input('please enter chinses translation')
                d[voc]=m
            else:
                print('word already exist')
        print(D)
        fo=open('my dictionary.txt,'w')
        for k,v in d.items():
          fo.write(k)
          fo.write(':')
          fo.write(v)
          fo.write('/n')
        fo.close()
        elif sel=='2':
            if not os.path.isfile('mydictionary.txt'):
                print('right nowthe dictionary is blank!!!')
                else:
                    fo=open('mydictionsry.txt','r')
                    foc=fo.read()

                    print(foc)


                 elif sel=='3':
                     voc=inout('please search the englsih word:')
                     if voc in d:
                         print(d[voc])
                         else:  
                
    elif sel=='3':
        voc=input('search english word(press0 to go out):')
        if voc=='0':
            break
        if voc in d:
                print(d[voc])
        else:
            print('My dictionary does not have this word')
    elif sel=='4':
        got=False
        ch=input('please enter chinses word')
        if ch=='0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,'in english is',k)
                got=True
        if not got:    
             print("sorry we can't find it")
    elif sel=='5':
        score=0
        print('the total scoreis',len(d),'points')
        for k,v in d.items():   
            print(v,':')
            ans=input() 
            if ans==k:
                score+=1
                print('correct! you got',score,'points now')
            else:
                print('wrong! you got',score,'points now')
    elif sel=='6':
        break
    else:
        print('enter wrongly , please retry!')
                    
                    
