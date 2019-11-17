import  cv2
img_s=cv2.imread('flower.jpg',0)
img=cv2.resize(img_s,(500,500))

ret,thr=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# cv2.imshow('threshold',thr)

contour,heir = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contour)
print("Number of Contours found = " + str(len(contour)))
draw=cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
for i in contour:
    x,y,h,w=cv2.boundingRect(i)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('contour',img)
cv2.waitKey(0)