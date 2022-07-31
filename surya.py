import tkinter as tk
# push data
from tkinter import filedialog, CENTER

import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm
from pymongo import MongoClient  # import mongo client to connect
import pprint


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
        client = MongoClient("mongodb+srv://test:test@cluster0.9sg1rjo.mongodb.net/?retryWrites=true&w=majority")        # Creating database
        db = client.Exercise
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

        count = 0
        direction = 0

        seatup = 0
        pushup = 0
        form = 0
        elbow_left = 0
        elbow_right = 0
        leg_left = 0
        leg_right = 0
        feedback = "Fix Form"
        angle = 0
        l = 0
        r = 0
        z = []
        # for y in employee.find({},{'_id':0,'pushup_data':1}):
        #   z.append(y.get('pushup_data'))
        #   print(z)

        # print(z[0][1])
        if (variable.get() == "Surya Namashkar"):
            form = 3

            if (b1["state"] == "disabled"):
                cap = cv2.VideoCapture(0)
            else:
                print(filename)
                cap = cv2.VideoCapture(filename)
                if (filename == ""):
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

                # hand
                step1_1 = detector.findAngle(img, 11, 13, 15)
                step1_2 = detector.findAngle(img, 12, 14, 16)
                # leg
                step1_3 = detector.findAngle(img, 23, 25, 27)
                step1_4 = detector.findAngle(img, 24, 26, 28)

                # hand
                step2_1 = detector.findAngle(img, 13, 11, 23)
                step2_2 = detector.findAngle(img, 14, 12, 24)
                # kamar
                step2_3 = detector.findAngle(img, 11, 23, 25)
                step2_4 = detector.findAngle(img, 12, 24, 26)

                # both kamar
                step3_1 = detector.findAngle(img, 11, 23, 25)
                step3_2 = detector.findAngle(img, 12, 24, 26)

                # kamar left
                step4_1 = detector.findAngle(img, 11, 23, 25)
                # leg left
                step4_2 = detector.findAngle(img, 23, 25, 27)

                # kamar both
                step5_1 = detector.findAngle(img, 11, 23, 25)
                step5_2 = detector.findAngle(img, 12, 24, 26)

                # hand
                step7_1 = detector.findAngle(img, 13, 11, 23)
                step7_2 = detector.findAngle(img, 14, 12, 24)
                # kamar
                step7_3 = detector.findAngle(img, 11, 23, 25)
                step7_4 = detector.findAngle(img, 12, 24, 26)

                # kamar both
                step8_1 = detector.findAngle(img, 11, 23, 25)
                step8_2 = detector.findAngle(img, 12, 24, 26)

                # kamar right
                step9_1 = detector.findAngle(img, 12, 24, 26)
                # leg right
                step9_2 = detector.findAngle(img, 24, 26, 28)

                # kamar
                step10_1 = detector.findAngle(img, 11, 23, 25)
                step10_2 = detector.findAngle(img, 12, 24, 26)

                # hand
                step11_1 = detector.findAngle(img, 13, 11, 23)
                step11_2 = detector.findAngle(img, 14, 12, 24)
                # kamar
                step11_3 = detector.findAngle(img, 11, 23, 25)
                step11_4 = detector.findAngle(img, 12, 24, 26)

                # hand
                step12_1 = detector.findAngle(img, 11, 13, 15)
                step12_2 = detector.findAngle(img, 12, 14, 16)
                # leg
                step12_3 = detector.findAngle(img, 23, 25, 27)
                step12_4 = detector.findAngle(img, 24, 26, 28)

                # elbow_left = detector.findAngle(img, 11, 13, 15)
                # elbow_right = detector.findAngle(img, 12, 14, 16)
                # leg_left = detector.findAngle(img,23,25,27)
                # leg_right = detector.findAngle(img, 24, 26, 28)
                # kamar = detector.findAngle(img,11,23,25)
                # step4_1 = detector.findAngle(img,11,23,25)
                # step4_2 = detector.findAngle(img,23,25,27)
                # hand = detector.findAngle(img,13,11,23)
                # step5_1 = detector.findAngle(img, 11,23,25)
                # step5_2 = detector.findAngle(img,12,24,26)

                temp = []
                # temp.append(int(hand))
                # temp.append(int(leg_left))
                # temp.append(int(leg_right))
                """shoulder = detector.findAngle(img, 13, 11, 23)
                hip = detector.findAngle(img, 11, 23,25)"""

                # Percentage of success of pushup
                per_left = np.interp(elbow_left, (90, 160), (0, 100))
                per_right = np.interp(elbow_right, (90, 160), (0, 100))

                # Bar to show Pushup progress
                bar_left = np.interp(elbow_left, (90, 160), (380, 50))
                bar_right = np.interp(elbow_right, (90, 160), (380, 50))

                if step1_1 <= 60 and step1_2 <= 60 and step1_3 >= 165 and step1_4 >= 165:
                    if dir_1 == 0:
                        temp.append(int(step1_1))
                        temp.append(int(step1_2))
                        temp.append(int(step1_3))
                        temp.append(int(step1_4))
                        count += 0.5
                        dir_1 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-1,12")

                        # Creating document
                        # Creating document
                        MyData = db.col_1
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        if dir_2==1 and dir_3==1 and dir_4==1 and dir_5==1 and dir_7==1 and dir_8==1:
                            print("1")
                            dir_1 = 0


                elif step2_3 <= 165 and step2_4 <= 165 and step2_1 >= 160 and step2_2 >= 160 and dir_1==1:
                    if dir_2 == 0:
                        temp.append(int(step2_1))
                        temp.append(int(step2_2))
                        temp.append(int(step2_3))
                        temp.append(int(step2_4))
                        count += 0.5
                        dir_2 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-2,11")

                        # Creating document
                        # Creating document
                        MyData = db.col_2
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        dir_1 = 1

                elif step3_1 <= 60 and step3_2 <= 60 and dir_2==1:
                    if dir_3 == 0:
                        temp.append(int(step3_1))
                        temp.append(int(step3_2))
                        count += 0.5
                        dir_3 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-3,10")

                        # Creating document
                        # Creating document
                        MyData = db.col_3
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        dir_1 = 1
                        dir_2=0

                elif (step4_1 <= 40 and step4_2 <= 90) or (step9_1 <= 40 and step9_2 <= 90) :

                    if((step4_1 <= 40 and step4_2 <= 90)):
                        if dir_4 == 0:
                            temp.append(int(step4_1))
                            temp.append(int(step4_2))
                            count += 0.5
                            dir_4 = 1
                            Data = {
                                "pushup_data": temp
                            }
                            print(temp)
                            print("Push Step-4 or 9")

                            # Creating document
                            # Creating document
                            MyData = db.col_4
                            # Inserting data
                            MyData.insert_one(Data)
                            # Inserting data
                            dir_1 = 0

                    if ((step9_1 <= 40 and step9_2 <= 90)):
                        if dir_9 == 0:
                            temp.append(int(step9_1))
                            temp.append(int(step9_2))
                            count += 0.5
                            dir_9 = 1
                            Data = {
                                "pushup_data": temp
                            }
                            print(temp)
                            print("Push Step-4 or 9")

                            # Creating document
                            # Creating document
                            MyData = db.col_9
                            # Inserting data
                            MyData.insert_one(Data)
                            # Inserting data
                            dir_1 = 1
                            dir_4 = 1
                            dir_2 = 1

                elif step5_1 <= 95 and step5_1 >= 65 and dir_4 == 1:
                    if dir_5 == 0:
                        temp.append(int(step5_1))
                        temp.append(int(step5_2))
                        count += 0.5
                        dir_5 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-5")

                        # Creating document
                        # Creating document
                        MyData = db.col_5
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        dir_1 = 0
                        dir_4 = 0;

                elif (step7_1 <= 50 and step7_2 <= 50 and step7_3 <= 150 and step7_4 <= 150) and dir_5==1:
                    if dir_7 == 0:
                        temp.append(int(step7_1))
                        temp.append(int(step7_2))
                        temp.append(int(step7_3))
                        temp.append(int(step7_4))
                        count += 0.5
                        dir_7 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-6,7")

                        # Creating document
                        # Creating document
                        MyData = db.col_7
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        dir_1 = 0

                elif step8_1 <= 95 and step8_1 >= 65 and dir_7 == 1 :
                    if dir_8 == 0:
                        temp.append(int(step8_1))
                        temp.append(int(step8_2))
                        count += 0.5
                        dir_8 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-8")

                        # Creating document
                        # Creating document
                        MyData = db.col_8
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data
                        dir_1 = 1
                        dir_12 = 0
                        dir_11 = 1
                        dir_2=1
                        dir_3=0

                # elif step9_1 <= 40 and step9_2 <= 90 and dir_8==1:
                #     if dir_9 == 0:
                #         temp.append(int(step9_1))
                #         temp.append(int(step9_2))
                #         count += 0.5
                #         dir_9 = 1
                #         Data = {
                #             "pushup_data": temp
                #         }
                #         print(temp)
                #         print("Push Step-9")
                #
                #         # Creating document
                #         # Creating document
                #         MyData = db.col_9
                #         # Inserting data
                #         MyData.insert_one(Data)
                #         # Inserting data
                #         dir_1 = 0

                # elif step10_1 <= 60 and step10_2 <= 60 and dir_9==1:
                #     if dir_10 == 0:
                #         temp.append(int(step10_1))
                #         temp.append(int(step10_2))
                #         count += 0.5
                #         dir_10 = 1
                #         Data = {
                #             "pushup_data": temp
                #         }
                #         print(temp)
                #         print("Push Step-10")
                #
                #         # Creating document
                #         # Creating document
                #         MyData = db.col_3
                #         # Inserting data
                #         MyData.insert_one(Data)
                #         # Inserting data
                #         dir_1 = 0
                #
                # elif step11_3 <= 165 and step11_4 <= 165 and step11_1 >= 160 and step11_2 >= 160 and dir_10==1:
                #     if dir_11 == 0:
                #         temp.append(int(step11_1))
                #         temp.append(int(step11_2))
                #         temp.append(int(step11_3))
                #         temp.append(int(step11_4))
                #         count += 0.5
                #         dir_11 = 1
                #         Data = {
                #             "pushup_data": temp
                #         }
                #         print(temp)
                #         print("Push Step-11")
                #
                #         # Creating document
                #         # Creating document
                #         MyData = db.col_2
                #         # Inserting data
                #         MyData.insert_one(Data)
                #         # Inserting data
                #         dir_1 = 0
                #
                if step12_1 <= 60 and step12_2 <= 60 and step12_3 >= 165 and step12_4 >= 165 and dir_11==1:
                    if dir_12 == 0:
                        temp.append(int(step12_1))
                        temp.append(int(step12_2))
                        temp.append(int(step12_3))
                        temp.append(int(step12_4))
                        count += 0.5
                        dir_12 = 1
                        Data = {
                            "pushup_data": temp
                        }
                        print(temp)
                        print("Push Step-12")

                        # Creating document
                        # Creating document
                        MyData = db.col_1
                        # Inserting data
                        MyData.insert_one(Data)
                        # Inserting data


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
