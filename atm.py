Line=input().split(" ")
blnc,Mblnc=Line
blnc=float(blnc)
Mblnc=float(Mblnc)

if blnc>=0 and blnc<=2000:
    if Mblnc>=0 and Mblnc<=2000:
        if blnc % 5==0:
            Mblnc=Mblnc-0.50
            Nblnc=Mblnc-blnc
            print(Nblnc)
        else:
            print(Mblnc)
