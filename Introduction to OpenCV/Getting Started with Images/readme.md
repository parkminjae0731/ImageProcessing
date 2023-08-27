# 코드 분석

### 필요한 모듈 불러오기

```python
import cv2 as cv
import sys
import os
```

### 파일 경로 설정

```py
path = os.getcwd()
path += "\\Introduction to OpenCV\\Getting Started with Images\\starry_night.jpg"
```

### image 읽어오기 및 검증

```
img = cv.imread(cv.samples.findFile(path))
if img is None:
    sys.exit("Could not read the image.")
```

### 이미지를 보여주기

```py
cv.imshow("Display window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
```