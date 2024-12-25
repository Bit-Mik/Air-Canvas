from IMPORTS import *
genai.configure(api_key=os.getenv('API_KEY'))

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        return fingers,lmList
    else:
        return None

def draw(info,prev_pos,canvas):
    fingers,lmList = info
    cur_pos=None
    if fingers == [0,1,1,0,0]:
        cur_pos=lmList[8][0:2]
        if prev_pos==None:
            prev_pos=cur_pos
        cv2.line(canvas,cur_pos,prev_pos, (0, 255, 0), 10)
    return cur_pos

def sendToAi(canvas):
    pil_image = Image.fromarray(canvas)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(["Solve this",pil_image])
    print(response.text)    

prev_pos=None  
canvas=None 
image_combined=None

while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    if canvas is None:
        canvas = np.zeros_like(img)
        image_combined=img.copy()

    info = getHandInfo(img)
    if info:
        fingers,lmList = info
        # print(fingers)
        prev_pos=draw(info,prev_pos,canvas)

        if fingers == [0,1,0,0,1]:canvas=np.zeros_like(img)
        if fingers == [1,1,1,0,1]:sendToAi(canvas)
    image_combined=cv2.addWeighted(img,0.7,canvas,0.3,0)    
    
    # Display the image in a window

    # cv2.imshow("Image", img)
    # cv2.imshow("Canvas", canvas)
    cv2.imshow("image_combined",image_combined)
    cv2.waitKey(1)

