Creating a Webcam Motion Detector

Process:
- Capture the intial static background image frame as a variable i.e. First_Frame
- Covert the all captured frames to greyscale i.e. Grey
- Create a frame holding the absolute difference between the static frame & all other captured frames i.e. Delta_Frame
- Apply a threshold to the pixels which convert the frames to either white or black based on a threshold pixel value
- Find contours of the white pixels
- Filter out contours with areas less than a 1000 pixels
- On the color frame (i.e. unaltered color frames), apply a green rectangle around contours with areas over a 1000 pixels
- Store timestamps & display them in a graph

motion_detector.py - handles the capturing of frames and storage in a csv file (i.e. Timestamp.csv)
plotting.py - handles importing the timestamp data and plotting the data in a graph
