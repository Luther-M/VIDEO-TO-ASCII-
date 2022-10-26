# VIDEO-TO-ASCII-

The code was build on Python 3.9, so i assumme it should work for same version of Python or close to it.

Package you will need to run it:
- cv2		
```
pip install opencv-python
```
- numpy 	
```
pip install numpy
```

##Running it

To run it, the code and the video must be in the same directory (same folder). 
```
C:\Users\AMD\Bad_Apple\example
```
![pic1](https://user-images.githubusercontent.com/76024496/197989555-54d67b4f-62eb-49d3-b9aa-ad04a03a88b4.png)

At line 17 in the test_video_v1, change ''lagtrain.mp4' to the video you want to play in terminal, in this case, 
'Bad Apple.p4'.

```python
cap = cv2.VideoCapture("lagtrain.mp4")  
```
to 
```python
cap = cv2.VideoCapture("Bad_Apple.mp4")  
```
Open terminal with the directory of the video and type "python test_video_v1.py".
```
C:\Users\AMD\Bad_Apple\example\python test_video_v1.py
```
Hold and behold it should run assuming that the requiments are filled.

However some tinkering is needed on the terminal to ensure it run smoothly. 
