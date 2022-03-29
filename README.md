# QR-code-scanner
In this repository I have explained how to make qr code scanner using python module opencv and pyzbar.

OpenCV does not have any dedicated modules that can be used to read and decode barcodes and QR codes.However, what OpenCV can do is facilitate the process of reading barcodes and QR codes, including loading an image from disk, grabbing a new frame from a video stream, and processing it.

Once we have the image or frame we can then pass it to a dedicated Python barcode decoding library such as a pyzbar.The pyzar library will then decode the barcode or QR code. OpenCV can come back in to perform any further processing and display the result.

## Installation
Install the required libraries using the following commands.

```python
pip install opencv
```

The official version of ZBar does not support Python 3. So I recommend using pyzbar which supports both python 2 and Python 3. If you just want to work with python 2, you can install zbar and skip installing pyzbar.

```python
pip install pyzbar
```

## Understanding the structure of QR code
A QR code object returned by pyzar has three fields

* **Type**: If the symbol detected by pyzar is a QR code, the type is QR-Code.
* **Data**: This is the data embedded inside the QR code. This data is usually alphanumeric, but other types ( numeric, byte/binary etc. ) are also valid.
* **Location**: This is a collection of points that locate the code. For QR codes, it is a list of four points corresponding to the four corners of the QR code quad.

## Python Code
Decode QR Code Using QR Code Image
```python
import cv2
qr_img = cv2.imread("/content/Create_qr_code.png")

# using the QRCodeDetector() function detect the qr code  
qr_det = cv2.QRCodeDetector()

# using the detectAndDecode() function  
val, pts, st_code = qr_det.detectAndDecode(qr_img)

# printing the value  print("Information:", val)
print(val)
```

## Explanation
For Python, we use pyzbar, which has a simple decode function to locate and decode all symbols in the image. The decode function simply warps pyzbar’s decode function and loops over the located barcodes and QR codes and prints the data.

The decoded symbols from the previous step are passed on to the display function. If the points form a quad ( e.g. in a QR code ), we simply draw the quad. If the location is not a quad, we draw the outer boundary of all the points ( also called the convex hull ) of all the points. This is done using OpenCV function called cv2.convexHull.

Finally, the main function simply reads an image, decodes it and displays the result.

## Conclusion
There are many tools that read QR codes. However, I used OpenCV for this, as it is popular and easy to integrate with the webcam or any video.

Finally, many of the Python concepts aren't discussed in detail here, if you feel you want to dig more into Python.
