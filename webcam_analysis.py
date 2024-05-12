import cv2
import pygame
from deepface import DeepFace
import time

def main():
    pygame.init()
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Webcam Analysis")
    cap = cv2.VideoCapture(0)  # Access the default camera
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    clock = pygame.time.Clock()
    fps = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Convert the OpenCV image to a pygame surface
        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Draw a bounding box around the face and display analysis results
        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            analyze = None
            try:
                analyze = DeepFace.analyze(roi, actions=('emotion', 'age', 'gender', 'race'), enforce_detection=False)
                if isinstance(analyze, list) and len(analyze) > 0:
                    analyze = analyze[0]
                    dominant_emotion = {analyze["dominant_emotion"]: None}
                    age = {analyze["age"]: None}
                    gender = analyze["gender"]
                    dominant_race = {analyze["dominant_race"]: None}
            except (ValueError, TypeError, KeyError) as e:
                dominant_emotion = {f"Unknown {e}": None}
                age = {f"Unknown {e}": None}
                gender = {f"Unknown {e}": None}
                dominant_race = {f"Unknown {e}": None}

            cv2.rectangle(cv2_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = f"Race: {list(dominant_race.keys())[0]}"
            cv2.putText(cv2_img, text, (x, y - 10), font, 0.5, (0, 255, 0), 2)
            text = f"Age: {list(age.keys())[0]}"
            cv2.putText(cv2_img, text, (x, y - 25), font, 0.5, (0, 255, 0), 2)
            text = f"Gender: {gender}"
            cv2.putText(cv2_img, text, (x, y - 40), font, 0.5, (0, 255, 0), 2)
            text = f"Emotion: {list(dominant_emotion.keys())[0]}"
            cv2.putText(cv2_img, text, (x, y - 55), font, 0.5, (0, 255, 0), 2)

            img = pygame.image.frombuffer(cv2_img.tobytes(), cv2_img.shape[1::-1], "RGB")
            screen.blit(img, (0, 0))

            # Display FPS
            fps = int(clock.get_fps())
            font = pygame.font.Font(None, 24)
            text = font.render(f"FPS: {fps}", True, (255, 255, 255))
            screen.blit(text, (10, screen_height - 30))
            pygame.display.flip()

            # Check for the 'q' key to quit the program
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    cap.release()
                    pygame.quit()
                    return

        clock.tick(30)

if __name__ == '__main__':
    main()
