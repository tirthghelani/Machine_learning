 # push data
from fileinput import filename

import cap as cap
import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm
from pymongo import MongoClient  # import mongo client to connect
import pprint
from tkinter import ttk, CENTER, filedialog
import tkinter as tk


# print(z[0][1])

root = tk.Tk()
root.geometry("700x500")
root.title("List")
root.configure()
root['background'] = '#AED6F1'

lbl1 = tk.Label(root, text="Welcome to exercise recognition App", background="#5DADE2", fg="white", font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack(padx=5, pady=25)

frame = tk.LabelFrame(root, background="#5DADE2", text='choice your method')
frame.pack(padx=5, pady=(40, 10))

selection = tk.IntVar()
OPTIONS = [
    "Push Up",
    "Seat Up",
    "Surya Namashkar"
]  # etc

variable = tk.StringVar(root)
variable.set(OPTIONS[0])

def onRadioButtonChange():
    if selection.get() != 0:
        print("1")
        b1["state"] = "active"

    else:
        print("2")
        b1["state"] = "disabled"



def browsefunc():
    global filename
    filename = filedialog.askopenfilename()




tk.Radiobutton(frame, command=onRadioButtonChange, text="Opern camara (Live)", variable=selection, value=0).grid(
    column=0, row=0)
tk.Radiobutton(frame, command=onRadioButtonChange, text="Using local storage", variable=selection, value=1).grid(
    column=1, row=0)


b1 = browsebutton = tk.Button(root, text="Browse", state="disable", command=browsefunc)
b1.pack(pady=(5, 40))

w = tk.OptionMenu(root, variable, *OPTIONS)
w.pack()


def submit():
    # Creating instance of mongoclient
    client = MongoClient("mongodb+srv://test:test@cluster0.9sg1rjo.mongodb.net/?retryWrites=true&w=majority")
    # Creating database
    db = client.Exercise
    employee = db.pushup
    employee = db.seatup
    detector = pm.poseDetector()
    count = 0
    direction = 0
    seatup = 0
    pushup = 0
    form = 0
    feedback = "Fix Form"
    angle = 0
    l = 0
    r = 0
    z = []

    col_1 = db.col_1
    col_2 = db.col_2
    col_3 = db.col_3
    col_4 = db.col_4
    col_5 = db.col_5
    col_6 = db.col_6
    col_7 = db.col_7
    col_8 = db.col_8
    col_9 = db.col_9
    col_10 = db.col_10
    col_11 = db.col_11
    col_12 = db.col_12
    step = 0

    dir_1 = 0
    dir_2 = 0
    dir_3 = 0
    dir_4 = 0
    dir_5 = 0
    dir_6 = 0
    dir_7 = 0
    dir_8 = 0
    dir_9 = 0
    dir_10 = 0
    dir_11 = 0
    dir_12 = 1


    for y in employee.find({}, {'_id': 0, 'pushup_data': 1}):
        z.append(y.get('pushup_data'))
        print(z)

    count=0
    print ("value is:" + variable.get())
    if(variable.get()=="Push Up"):
        form = 1
    elif(variable.get()=="Seat Up"):
        form = 4
    elif(variable.get()=="Surya Namashkar"):
        form = 3

    if(b1["state"]=="disabled"):
        cap = cv2.VideoCapture(0)
    else:
        print(filename)
        cap = cv2.VideoCapture(filename)
        if(filename==""):
            print("no file")



    detector = pm.poseDetector()

    while cap.isOpened():
        ret, img = cap.read()  # 640 x 480
        # Determine dimensions of video - Help with creation of box in Line 43
        width = cap.get(3)  # float `width`
        height = cap.get(4)  # float `height`
        # print(width, height)

        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            elbow_left = detector.findAngle(img, 11, 13, 15)
            elbow_right = detector.findAngle(img, 12, 14, 16)
            leg_left = detector.findAngle(img, 23, 25, 27)
            leg_right = detector.findAngle(img, 24, 26, 28)

            temp = []
            temp.append(int(elbow_left))
            temp.append(int(elbow_right))
            temp.append(int(leg_left))
            temp.append(int(leg_right))
            """shoulder = detector.findAngle(img, 13, 11, 23)
            hip = detector.findAngle(img, 11, 23,25)"""

            # Percentage of success of pushup
            per_left = np.interp(elbow_left, (90, 160), (0, 100))
            per_right = np.interp(elbow_right, (90, 160), (0, 100))

            # Bar to show Pushup progress
            bar_left = np.interp(elbow_left, (90, 160), (380, 50))
            bar_right = np.interp(elbow_right, (90, 160), (380, 50))

            # if( 1 ):
            #     for i in range(4):
            #         if(temp[0]+2>z[i][0] and temp[0]-2<z[i][0] and temp[1] + 2 > z[i][1] and temp[1] - 2 < z[i][1] and
            #         temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2] and temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3]):
            #             seatup+=1

            # print(temp[0]+2)
            # print((z[i][0]))
            # print(temp[0] - 2)
            # print((z[i][0]))
            # if (temp[1] + 2 > z[i][1] and temp[1] - 2 < z[i][1]):
            #      seatup += 1
            #     # print(temp[1]+2)
            #     # print((z[i][0]))
            #     # print(temp[1] - 2)
            #     # print((z[i][0]))
            # if (temp[2] + 2 > z[i][2] and temp[2] - 2 < z[i][2]):
            #      seatup += 1
            #     # print(temp[2] + 2)
            #     # print((z[i][0]))
            #     # print(temp[2] - 2)
            #     # print((z[i][0]))
            # if (temp[3] + 2 > z[i][3] and temp[3] - 2 < z[i][3]):
            #      seatup += 1
            #     # print(temp[3] + 2)
            #     # print((z[i][0]))
            #     # print(temp[3] - 2)
            #     # print((z[i][0]))

            #     if(seatup==1):
            #         print("SeatUpOK")
            #         seatup=0
            #         angle=1
            #         l=temp[2]
            #         print(l)
            #         # print(seatup)
            #     else:
            #         seatup=0
            # else:
            #     print(leg_left)

            # Check to ensure right form before starting the program
            # if elbow_left < 90 and elbow_right < 90:
            #     form = 1

            # elif elbow_left<50:
            #     form = 2
            # elif elbow_right<50:
            #     form = 3
            # elif leg_left<80:
            #     form = 4
            # if(leg_left<80):
            #     form=4

            # Check for full range of motion for the pushup
            if form == 1:
                # if per_left == 0 and  per_right==0:
                if elbow_left <= 80 and elbow_right <= 80:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("push up")

                        # Creating document
                        # Creating document
                        MyData = db.pushup
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                    feedback = "Fix Form"

                # if per_left == 100 and per_right==100:
                if elbow_left > 160 and elbow_right > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
                    # form = 0

            # Check for full range of motion for the pushup
            if form == 2:
                # if per_left == 0 and  per_right==0:
                if elbow_left <= 90:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"

                # if per_left == 100 and per_right==100:
                if elbow_left > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
                    # form = 0

            # Check for full range of motion for the pushup
            if form == 3:
                # if per_left == 0 and  per_right==0:
                if elbow_right <= 90:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"

                # if per_left == 100 and per_right==100:
                if elbow_right > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
                    # form = 0

            # Check for full range of motion for the Seat Up
            if form == 4:
                # if per_left == 0 and  per_right==0:
                if leg_left >= 140:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"

                # if per_left == 100 and per_right==100:
                if leg_left < 80:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Seat Up")

                        # Creating document
                        MyData = db.seatup
                        # Inserting data
                        MyData.insert_one(Data)

                else:
                    feedback = "Fix Form"
                    # form = 0

            # print(count)

            # Draw Bar

            if form == 3:
                cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                cv2.rectangle(img, (580, int(bar_right)), (600, 380), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(per_right)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                            (255, 0, 0), 2)

            if form == 1 or form == 2:
                cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                cv2.rectangle(img, (580, int(bar_left)), (600, 380), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(per_left)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                            (255, 0, 0), 2)

            # Pushup counter
            cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            # Feedback
            cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
            cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 255, 0), 2)

        """if (lmList[25][2] and lmList[26][2] >= lmList[23][2] and lmList[24][2]):
            posiotion = "sit"
        if (lmList[25][2] and lmList[26][2] <= lmList[23][2] and lmList[24][2] and posiotion == "sit"):
            posiotion = "up"
            count += 1
            print("tirth")
            print(count)"""

        cv2.imshow('Pushup counter', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

b2 = tk.Button(root, text="Submit", command=submit)
b2.pack(pady=(10, 50))

root.mainloop()