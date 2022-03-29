import cv2

# Read the image of qr code
qr_img = cv2.imread("/content/Create_qr_code.png")

# using the QRCodeDetector() function  
qr_det = cv2.QRCodeDetector()  

# using the detectAndDecode() function  
val, pts, st_code = qr_det.detectAndDecode(qr_img)

# printing the value  print(val)
print(val)
