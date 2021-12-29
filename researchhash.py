# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:22:37 2021

@author: iamku
"""
def numgenerator(key):
   num=key
   if(num%64==0):
       return num
   else:
       while(num%64!=0):
           num=num+1
       return num         
def xor(bin1,bin2):
    out=""
    for i in range(64):
        if(bin1[i]==bin2[i]):
            out=out+'0'
        else:
            out=out+'1'
    return out
def AND(bin1,bin2):
    out=""
    for i in range(64):
        if(bin1!=bin2):
            out=out+'0'
        elif(bin1[i]=='0' and bin2[i]=='0'):
            out=out+'0'
        else:
            out=out+'1'
    return out
def OR(bin1,bin2):
    out=""
    for i in range(64):
       if(bin1!=bin2):
            out=out+'1'
       elif(bin1[i]=='0' and bin2[i]=='0'):
            out=out+'0'
       else:
            out=out+'1' 
    return out
def NOT(bin1):
    out=""
    for i in range(64):
        if(bin1[i]=='0'):
            out=out+'1'
        elif(bin1[i]=='1'):
            out=out+'0'
    return out
def ls(string,n):
    out=""
    for i in range(64):
        out=out+string[(i-n)%64]
    return out
def rs(string,n):
    out=""
    for i in range(64):
        out=out+string[(i+n)%64]
    return out
def str2bin(string):
    return ''.join(bin(ord(c)) for c in string).replace('b','')
def int2bin(n):
    x=bin(n)
    x1=x[2:]
    if(len(x1)%64==0):
        return x1
    else:
        while(len(x1)%64!=0):
            x1='0'+x1
        return x1
def appension(string):
    if(len(string)%64==0):
        return string
    else:
        while(len(string)%64!=0):
         string='0'+string
        return string
def avcgen(avc,num):
   while(num%len(avc)!=0):
       avc='0'+avc
   return avc    
def msggen(avc,num,msg):
    times=int(num/len(avc))
    for i in range(times):
        msg=msg+avc
    return msg
def agen(msg,key):
    a=0
    b=64
    msglist=[]
    while(b<=len(msg)):
        msglist.append(msg[a:b])
        a=b
        b=64+b
    keylist=[]
    c=0
    d=64
    bkey=int2bin(key)
    while(d<=len(bkey)):
        keylist.append(bkey[c:d])
        c=d
        d=64+d
    keylen=len(keylist)
    i=1
    j=i%keylen
    R=xor(msglist[0],keylist[0])
    A=""
    while(i!=len(msglist)):
     A=xor(R,xor(msglist[i],keylist[j]))
     R=A
     i=i+1
     j=i%keylen
    return A
def bgen(newmsg,key):
    pos=key
    startpos=pos-63
    B=newmsg[startpos:pos+1]
    return B 
def cgen(key):
    bkey=int2bin(key)
    C=bkey[0:64]
    return C
def dgen(msg,key):
    msgint=int(msg,2)
    quo=int(msgint/key)
    D=int2bin(quo)
    if(len(D)>64):
        return D[64:128]
    else:
        return D
def egen(avc,key):
    bkey=int2bin(key)
    i=0
    if(len(avc)==64):
        return(xor(avc,key[0:64]))
    elif(len(avc)>64):
        
        return xor(avc[0:64],bkey[0:64])
    else:
        while(len(avc)!=64):
            avc=avc+avc[i]
            i=i+1
        return(xor(avc,bkey[0:64]))
def fgen(msg,key,avc,num):
    newmsg=msggen(avc,num,msg)
    A=agen(msg,key)
    B=bgen(newmsg,key)
    C=xor(A,B)
    return C
def ggen(msg,key):
    C=cgen(key)
    D=dgen(msg,key)
    G=xor(C,D)
    return G
def hgen(msg,key,avc,num):
    newmsg=msggen(avc,num,msg)
    B=bgen(newmsg,key)
    C=cgen(key)
    H=xor(B,C)
    return H
def fun0(a,b,c,d,e,f,g,h,n):
    if(n%24==0):
       a=xor(AND(xor(a,ls(f,2)),OR(c,NOT(d))),ls(xor(AND(e,NOT(b)),OR(h,g)),2))
       b=AND(OR(OR(ls(b,3),d),xor(f,c)),OR(AND(ls(g,2),e),xor(a,NOT(h))))
       c=xor(OR(AND(c,a),xor(b,e)),xor(rs(AND(g,ls(f,2)),3),AND(NOT(d),h)))
       d=AND(xor(rs(AND(d,h),2),OR(c,a)),OR(xor(b,g),AND(f,NOT(e))))
       e=xor(OR(AND(e,a),xor(NOT(c),d)),OR(AND(ls(b,3),h),xor(f,g)))
       f=AND(OR(AND(f,NOT(D)),ls(OR(c,e),2)),xor(xor(g,h),AND(b,a)))
       g=xor(xor(AND(NOT(g),e),OR(f,c)),AND(AND(A,NOT(D)),xor(b,h)))
       h=AND(AND(OR(h,f),xor(a,d)),OR(AND(g,b),NOT(OR(c,ls(e,2)))))
       return a,b,c,d,e,f,g,h
    elif(n%16==0):
        a=OR(ls(xor(OR(a,f),NOT(AND(b,e))),2),AND(xor(c,g),AND(d,h)))
        b=xor(xor(AND(b,h),xor(c,ls(a,2))),xor(OR(g,d),AND(e,NOT(f))))
        c=OR(AND(AND(c,g),AND(a,e)),ls(xor(xor(d,b),OR(f,NOT(h))),3))
        d=AND(OR(AND(ls(d,3),e),AND(a,b)),xor(OR(c,f),xor(g,h)))
        e=xor(xor(AND(e,h),xor(a,f)),NOT(AND(OR(b,c),xor(d,NOT(G)))))
        f=xor(AND(xor(f,c),xor(e,b)),xor(xor(a,ls(h,3)),xor(d,g)))
        g=AND(xor(AND(g,e),AND(b,f)),xor(OR(a,c),AND(d,h)))
        h=xor(AND(OR(h,ls(c,2)),NOT(AND(a,f))),xor(OR(b,d),xor(e,NOT(G))))
        return a,b,c,d,e,f,g,h
    elif(n%8==0):
        a=xor(xor(OR(a,NOT(g)),AND(ls(c,3),d)),AND(OR(b,h),AND(e,f)))
        b=xor(xor(AND(b,c),xor(d,e)),xor(xor(f,g),xor(a,h)))
        c=OR(OR(AND(c,g),xor(f,NOT(A))),OR(AND(e,b),AND(d,h)))
        d=AND(xor(OR(d,e),xor(a,h)),ls(AND(xor(f,NOT(c)),AND(b,g)),2))
        e=xor(OR(AND(e,f),AND(d,g)),ls(xor(AND(c,b),xor(a,h)),3))
        f=OR(xor(AND(f,b),AND(c,NOT(a))),ls(xor(AND(e,g),NOT(xor(d,h))),2))
        g=AND(xor(AND(g,a),AND(c,d)),xor(OR(b,e),OR(f,h)))
        h=OR(AND(xor(h,b),AND(c,d)),AND(xor(e,a),NOT(xor(f,g))))
        return a,b,c,d,e,f,g,h
    else:
        return a,b,c,d,e,f,g,h
def fun1(a,b,c,d,e,f,g,h,n):
    if(n%24==0):
       a=xor(AND(xor(c,ls(g,2)),OR(d,NOT(a))),ls(xor(AND(b,NOT(h)),OR(f,e)),2))
       b=AND(OR(OR(ls(h,3),a),xor(g,d)),OR(AND(ls(e,2),b),xor(c,NOT(f))))
       c=xor(OR(AND(d,c),xor(h,b)),xor(rs(AND(e,ls(g,2)),3),AND(NOT(a),f)))
       d=AND(xor(rs(AND(a,f),2),OR(d,c)),OR(xor(h,e),AND(g,NOT(b))))
       e=xor(OR(AND(b,c),xor(NOT(d),a)),OR(AND(ls(h,3),f),xor(g,e)))
       f=AND(OR(AND(g,NOT(D)),ls(OR(d,b),2)),xor(xor(e,f),AND(h,c)))
       g=xor(xor(AND(NOT(e),b),OR(g,d)),AND(AND(A,NOT(D)),xor(h,f)))
       h=AND(AND(OR(f,g),xor(c,a)),OR(AND(e,h),NOT(OR(d,ls(b,2)))))
       return a,b,c,d,e,f,g,h
    if(n%16==0):
        a=OR(ls(xor(OR(c,g),NOT(AND(h,b))),2),AND(xor(d,e),AND(a,f)))
        b=xor(xor(AND(h,f),xor(d,ls(c,2))),xor(OR(e,a),AND(b,NOT(g))))
        c=OR(AND(AND(d,e),AND(c,b)),ls(xor(xor(a,h),OR(g,NOT(f))),3))
        d=AND(OR(AND(ls(a,3),b),AND(c,h)),xor(OR(d,g),xor(e,f)))
        e=xor(xor(AND(b,f),xor(c,g)),NOT(AND(OR(h,d),xor(a,NOT(G)))))
        f=xor(AND(xor(g,d),xor(b,h)),xor(xor(c,ls(f,3)),xor(a,e)))
        g=AND(xor(AND(e,b),AND(h,g)),xor(OR(c,d),AND(a,f)))
        h=xor(AND(OR(f,ls(d,2)),NOT(AND(c,g))),xor(OR(h,a),xor(b,NOT(G))))
        return a,b,c,d,e,f,g,h
    if(n%8==0):
        a=xor(xor(OR(c,NOT(e)),AND(ls(d,3),a)),AND(OR(h,f),AND(b,g)))
        b=xor(xor(AND(h,d),xor(a,b)),xor(xor(g,e),xor(c,f)))
        c=OR(OR(AND(d,e),xor(g,NOT(A))),OR(AND(b,h),AND(a,f)))
        d=AND(xor(OR(a,b),xor(c,f)),ls(AND(xor(g,NOT(d)),AND(h,e)),2))
        e=xor(OR(AND(b,g),AND(a,e)),ls(xor(AND(d,h),xor(c,f)),3))
        f=OR(xor(AND(g,h),AND(d,NOT(c))),ls(xor(AND(b,e),NOT(xor(a,f))),2))
        g=AND(xor(AND(e,c),AND(d,a)),xor(OR(h,b),OR(g,f)))
        h=OR(AND(xor(f,h),AND(d,a)),AND(xor(b,c),NOT(xor(g,e))))
        return a,b,c,d,e,f,g,h
    else:
        return a,b,c,d,e,f,g,h
def hashgen(newmsg,a,b,c,d,e,f,g,h,key):
    prehash=""
    st=0
    en=64
    msglist=[]
    while(en<=len(newmsg)):
        msglist.append(newmsg[st:en])
        st=en
        en=64+en
    if(newmsg[key]=='0'):
        for i in range(len(msglist)):
            if(i%8==0):
                a=xor(a,msglist[i])
            elif(i%8==1):
                b=xor(b,msglist[i])
            elif(i%8==2):
                c=xor(c,msglist[i])
            elif(i%8==3):
                d=xor(d,msglist[i])
            elif(i%8==4):
                e=xor(e,msglist[i])
            elif(i%8==5):
                f=xor(f,msglist[i])
            elif(i%8==6):
                g=xor(g,msglist[i])
            else:
                h=xor(h,msglist[i])
            print(a+' A '+b+' B '+c+' C '+d+' D '+e+' E '+f+' F '+g+' G '+h+' H')
            a,b,c,d,e,f,g,h=fun0(a,b,c,d,e,f,g,h,i)
        prehash=prehash+a+b+c+d+e+f+g+h
        binhash=ls(prehash,3)
        dechash=int(binhash,2)
        hexhash=hex(dechash)
        return hexhash
    elif(newmsg[key]=='1'):
        for i in range(len(msglist)):
            if(i%8==0):
                a=xor(a,msglist[i])
            elif(i%8==1):
                b=xor(b,msglist[i])
            elif(i%8==2):
                c=xor(c,msglist[i])
            elif(i%8==3):
                d=xor(d,msglist[i])
            elif(i%8==4):
                e=xor(e,msglist[i])
            elif(i%8==5):
                f=xor(f,msglist[i])
            elif(i%8==6):
                g=xor(g,msglist[i])
            else:
                h=xor(h,msglist[i])
            print(a+' A '+b+' B '+c+' C '+d+' D '+e+' E '+f+' F '+g+' G '+h+' H')
            a,b,c,d,e,f,g,h=fun1(a,b,c,d,e,f,g,h,i)
        prehash=prehash+a+b+c+d+e+f+g+h
        binhash=ls(prehash,3)
        dechash=int(binhash,2)
        hexhash=hex(dechash)
        return hexhash
ogmsg=input("enter your message")
binmsg=str2bin(ogmsg)
msg=appension(binmsg)
key=int(input("Enter Key"))
binkey=int2bin(key)
intmsg=int(binmsg,2)
ogavc=intmsg%key
binavc=bin(ogavc)
avc=binavc[2:]
num=numgenerator(key)
avc=avcgen(avc,num)
newmsg=msggen(avc,num,msg)
A=agen(msg,key)
B=bgen(newmsg,key)
C=cgen(key)
D=dgen(msg,key)
E=egen(avc,key)
F=fgen(msg,key,avc,num)
G=ggen(msg,key)
H=hgen(msg,key,avc,num)
hexhash=hashgen(newmsg,A,B,C,D,E,F,G,H,key)
print(hexhash)
      
    
           
        
    
        
                         
                         
    

       
    