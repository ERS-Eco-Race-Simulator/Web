## Web

> Web interfaces for the ERS project



### hostcam

Simple webcam streaming over lan

```bash
python3 hostcam/hostcam.py [camera]
```

+ `camera` camera index

  ```bash
  # find camera index
  apt install v4l-utils libv4l-dev
  v4l2-ctl --list-devices
  ```

  ```bash
  # sample output
  USB2.0 HD UVC WebCam: USB2.0 HD (usb-0000:00:14.0-7):
  	/dev/video0
  	/dev/video1
  
  # so
  python3 hostcam/hostcam.py 0
  ```



