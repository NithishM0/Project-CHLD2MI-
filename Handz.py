import cv2
import mediapipe as mp
import time
import mouse



cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(

                      min_detection_confidence=0.8,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0




while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    #print(results.multi_hand_landmarks)

    



    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            



            for id, lm in enumerate(handLms.landmark):





                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)

                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    if results.multi_hand_landmarks != None:
        imageHeight, imageWidth, _ = img.shape
        for handLandmarks in results.multi_hand_landmarks:


            for point in mp_hands.HandLandmark:
                normalizedLandmark = handLandmarks.landmark[point]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                       normalizedLandmark.y, imageWidth,
                                                                                       imageHeight)


                point = str(point)
                if point == 'HandLandmark.INDEX_FINGER_TIP':
                    try:
                        indexfingertip_x = pixelCoordinatesLandmark[0]
                        indexfingertip_y = pixelCoordinatesLandmark[1]

                        x, y = 1366 / 480, 768 / 640
                        screen_pos = [indexfingertip_x * x, indexfingertip_y * y]

                        mouse.move(screen_pos[0], screen_pos[1])




                    except:
                        pass


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("img", img)
    cv2.waitKey(1)