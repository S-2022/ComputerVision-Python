#PRESS esc TO STOP
import cv2
v=cv2.VideoCapture(0)
r,f1=v.read()
r,f2=v.read()
while(v.isOpened()):
    d=cv2.absdiff(f1,f2)
    g=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    b=cv2.GaussianBlur(g,(5,5),0)
    _,th=cv2.threshold(b,20,255,cv2.THRESH_BINARY)
    dil=cv2.dilate(th,None,iterations=1)
    cs,_=cv2.findContours(dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in cs:
        (x,y,w,h)=cv2.boundingRect(c)
        if(cv2.contourArea(c)<2000):
            continue
        cv2.rectangle(f1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(f1,"MOVEMENT",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
    cv2.imshow('Movement Detection',f1)
    f1=f2
    ret,f2=v.read()
    if(cv2.waitKey(1)==27):
        break
v.release()
cv2.destroyAllWindows()
