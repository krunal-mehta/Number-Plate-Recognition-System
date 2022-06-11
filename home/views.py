from django.shortcuts import render, HttpResponse
from home.models import admindb
from home.models import carmodel

import numpy as np
import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Create your views here.

def index(request):
    context={
        "abc" : "hello",
    }
    return render(request,'home.html',context)

def carimg(request):
    pic = request.FILES['img']
    entry = carmodel(car_img = pic)
    entry.save()
    cars = carmodel.objects.all()
    p = cars[len(cars)-1].car_img
    return_dict = {}
    return_dict['original_pic']=p.url


    image = cv2.imread('D:\\Tops Python\\Django\\nprs\\static\\images\\car\\'+p.url.split("/")[-1])
    
    image = imutils.resize(image, width=500)

    # Display the original image
    # cv2.imshow("Original Image", image)
    # cv2.waitKey(0)

    # RGB to Gray scale conversion
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("1 - Grayscale Conversion", gray)
    # cv2.waitKey(0)

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # cv2.imshow("2 - Bilateral Filter", gray)
    # cv2.waitKey(0)

    # Find Edges of the grayscale image
    edged = cv2.Canny(gray, 170, 200)
    # cv2.imshow("3 - Canny Edges", edged)
    # cv2.waitKey(0)

    # Find contours based on Edges
    cnts, new  = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Create copy of original image to draw all contours
    img1 = image.copy()
    cv2.drawContours(img1, cnts, -1, (0,255,0), 3)
    # cv2.imshow("4- All Contours", img1)
    # cv2.waitKey(0)

    #sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
    NumberPlateCnt = None #we currently have no Number plate contour

    # Top 30 Contours
    img2 = image.copy()
    cv2.drawContours(img2, cnts, -1, (0,255,0), 3)
    # cv2.imshow("5- Top 30 Contours", img2)
    # cv2.waitKey(0)

    # loop over our contours to find the best possible approximate contour of number plate
    count = 0
    
    for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # print ("approx = ",approx)
            if len(approx) == 4:  # Select the contour with 4 corners
                NumberPlateCnt = approx #This is our approx Number Plate Contour

                # Crop those contours and store it in Cropped Images folder
                x, y, w, h = cv2.boundingRect(c) #This will find out co-ord for plate
                new_img = gray[y:y + h, x:x + w] #Create new image
                cv2.imwrite('D:\\Tops Python\\Django\\nprs\\static\\images\\car\\'+p.url.split("/")[-1].split('.')[0] + '_cropped.png', new_img) #Store new image

                break


    # Drawing the selected contour on the original image
    #print(NumberPlateCnt)
    cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
    # cv2.imshow("Final Image With Number Plate Detected", image)
    # cv2.waitKey(0)
    cv2.imwrite('D:\\Tops Python\\Django\\nprs\\static\\images\\car\\'+p.url.split("/")[-1].split('.')[0] + '_1.png', image)

    Cropped_img_loc = 'D:\\Tops Python\\Django\\nprs\\static\\images\\car\\'+p.url.split("/")[-1].split('.')[0] + '_cropped.png'
    # cv2.imshow("Cropped Image ", cv2.imread(Cropped_img_loc))

    # Use tesseract to covert image into string
    text = pytesseract.image_to_string(Cropped_img_loc, lang='eng').split('\n')[0].replace(' ','')
    # print("Number is :", text)

    # cv2.waitKey(0) #Wait for user input before closing the images displayed


    return_dict['detected_pic'] = ''.join(p.url.split('.')[:-1]) + '_1.png'
    return_dict['final_pic'] = ''.join(p.url.split('.')[:-1]) + '_cropped.png'



    return_dict['vno'] = list(admindb.objects.filter(vno = text).values_list('vno',flat=True))[0]
    return_dict['oname'] = list(admindb.objects.filter(vno = text).values_list('oname',flat=True))[0]
    return_dict['mname'] = list(admindb.objects.filter(vno = text).values_list('mname',flat=True))[0]
    return_dict['mno'] = list(admindb.objects.filter(vno = text).values_list('mno',flat=True))[0]
    return_dict['pyear'] = list(admindb.objects.filter(vno = text).values_list('pyear',flat=True))[0]
    return_dict['lno'] = list(admindb.objects.filter(vno = text).values_list('lno',flat=True))[0]
    return_dict['foul'] = list(admindb.objects.filter(vno = text).values_list('foul',flat=True))[0]
    return_dict['fine'] = list(admindb.objects.filter(vno = text).values_list('fine',flat=True))[0]
    return_dict['oaddress'] = list(admindb.objects.filter(vno = text).values_list('oaddress',flat=True))[0]
    return_dict['cdetail'] = list(admindb.objects.filter(vno = text).values_list('cdetail',flat=True))[0]
    return_dict['lexpiredate'] = list(admindb.objects.filter(vno = text).values_list('lexpiredate',flat=True))[0]
    return_dict['lissuedate'] = list(admindb.objects.filter(vno = text).values_list('lissuedate',flat=True))[0]

    return render(request,'display.html',return_dict)

def adminright(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passw = request.POST.get('pass')
        if uname == 'admin' and passw == 'admin':
            vno = request.POST.get('vno')
            oname = request.POST.get('oname')
            mname = request.POST.get('mname')
            mno = request.POST.get('mno')
            pyear = request.POST.get('pyear')
            lno = request.POST.get('lno')
            foul = request.POST.get('foul')
            fine = request.POST.get('fine')
            oaddress = request.POST.get('oaddress')
            cdetail = request.POST.get('cdetails')
            lidate = request.POST.get('lidate')
            ledate = request.POST.get('ledate')

            entry = admindb(vno=vno, oname=oname, mname=mname, mno=mno, pyear=pyear, lno=lno, foul=foul, fine=fine, oaddress=oaddress, cdetail=cdetail, lissuedate=lidate, lexpiredate=ledate)
            entry.save()
            
            context={
                "y" : "Entry Successfully Entered in Database!"
            }
            return render(request,'admin.html',context)
        else:
            context={
                "x" : "Incorrect Username or Password !!!"
            }
            return render(request,'admin.html',context)
    return render(request,'admin.html')
    

def display(request):
    context={
        "abc" : "hello",
    }
    return render(request,'display.html',context)