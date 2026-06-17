import cv2
import face_recognition
import os

# Check if registered face exists
if not os.path.exists("Registered_Face.jpg"):
    print("No registered face found.")
    exit()

# Load registered face
known_image = face_recognition.load_image_file("Registered_Face.jpg")

known_encodings = face_recognition.face_encodings(known_image)

if len(known_encodings) == 0:
    print("No face detected in Registered_Face.jpg")
    exit()

known_encoding = known_encodings[0]

# Start webcam
cam = cv2.VideoCapture(0)

print("Show your face to unlock")
print("Press Q to quit")

while True:
    ret, frame = cam.read()

    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in current frame
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for face_encoding in face_encodings:

        match = face_recognition.compare_faces(
            [known_encoding],
            face_encoding,
            tolerance=0.5
        )

        if match[0]:
            print("Face Matched. Access Granted!")

            cv2.putText(
                frame,
                "UNLOCKED",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow("Face Unlock", frame)
            cv2.waitKey(2000)

            cam.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Face Unlock", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()