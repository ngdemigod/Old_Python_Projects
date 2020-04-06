import cv2, time, pandas
from datetime import datetime

first_frame = None #empty variable - during the 1st While loop run, it will store the static background image to compare with other images to indicate motion. 
status_list = [None,None] #for each frame, a status is assigned (0 or 1) to indicate motion. This list will store those values.
times = [] #This will store a list of timestamps indicating when motion is detected and when motion is no long detected.
df = pandas.DataFrame(columns=["Start", "End"]) #creates a dataframe with two columns for the Start & End timestamps



video=cv2.VideoCapture(0) #triggers video capture object. In args, use either a number i.e. 0 for the camera or pass in a filepath string to a video file.

video.read()
time.sleep(3)
""" I added video.read() & time.sleep() above because some cameras are slow to initialize which can affect the captured frames   """

while True:
    check, frame = video.read() #cv2.VideoCapture.read() - grabs, decodes & returns next video frame
    #check - is a boolean function to check if the video is working

    status=0 #This refers to a status with no motion detected


    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts imshow() to greyscale
    grey=cv2.GaussianBlur(grey,(21,21),0) 
    """ cv2.GaussianBlur() - used to smoothing the image captured for accuracy when determining the difference 
        between first_frame & current image """

    if first_frame is None:
        first_frame = grey
        continue 
        """ continue - used to skip the rest of the code inside a loop for the current iteration only. 
            The loop does not terminate but continues on with the next iteration. """

    delta_frame=cv2.absdiff(first_frame,grey) #finds the absolute difference between first_frame & current greyscale image frame
    
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] 
    """ cv2.threshold() - takes in the deltaframe (method only works with greyscale images), 
        Threshold limit to used to classify a pixel (i.e. whether the pixel will be white or black in this program),
        Value assigned if the pixel value was above the threshold limit (i.e. 255 = white),
        Type of thresholding you want to perform (e.g. THRESH_BINARY i.e. simple thresholding)

        The method returns a tuple (x,y) - which THRESH_BINARY the 1st number is not needed but the 2nd value is ß
        the returned pixel value hence an index value of [1] """

    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2) 
    """ cv2.dilate(source, Kernel, iterations) - used to smooth the threshold frame.
        Kernel - this is a structuring element which is not needed for this program
        iterations - number of times the dilate() method will run i.e. for this script it runs 2 times """

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    """ .findContours(source,mode,method) - used to find contours in the frame
        source - source of frame (note: we are using a copy of Thresh_Frame in order to not alter the orginal value while finding contours)
        mode - a set retrival mode for contours (RETR_EXTERNAL - retrieves only the extreme outer contours)
        method - the approximation method used to find contours (CHAIN_APPROX_SIMPLE - compresses horizontal, vertical, 
        and diagonal segments and leaves only their end points) """

    for contour in cnts: # this for loop is to filter the contour with areas less than 10000 pixels 
        if cv2.contourArea(contour) < 10000: 
            continue
        """ coutourArea() - finds the area of a contour
            If the area of the contour is less than 1000 pixels, the script will restart the While loop
            If greater than 1000 pixels the script will move to the next step """

        status=1 #At this point, small contours have been filtered out hence and contours detected indicates motion (indicated with the value of 1)

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    status_list.append(status) #Appends the status of an image frame (i.e. 0 or 1) for each iteration of the while loop
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    """ This IF statement checks the status_list last two values (for each while loop iteration) to see if the status changed from 0 to 1.
        When this is True, it indicates when motion is detected and then it will append the timestamp to the times list  """

    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    """ This IF statement checks the status_list last two values (for each while loop iteration) to see if the status changed from 1 to 0.
        When this is True, it indicates when motion is NO LONGER detected and then it will append the timestamp to the times list  """    



    cv2.imshow("Grey Frame", grey) #imshow(title of the window displaying image, source) - displays image
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame", frame)

    key=cv2.waitKey(1) #this is capture a new image frame every millisecond

    
    if key==ord('q'): #this ends the program when the 'Q' key is pressed
        if status==1:
            times.append(datetime.now())
        """ If motion is still detected when the program ends, it means the last to values of the status_list will not change from 1 to 0.
            To ensure a timestamp indictating the end of motion detection is recorded, we use an IF statement to append the END timestamp to 
            the times list  """

        break

for i in range(0, len(times),2): #iterates over the lenght of times list using a step value of 2
    df=df.append({"Start":times[i], "End":times[i+1]},ignore_index=True) 
    """ appends the Start & Stop time to the df dataframe.
        ignore_index - when set to True, will not use the index labels 
        (i.e. each iteration adds a row to the frame and the row index will increase by 1 for each row)  """ 

df.to_csv("Timestamp.csv") #convert dataframe to a csv file
video.release() #always end with this to close the connection
cv2.destroyAllWindows()















































