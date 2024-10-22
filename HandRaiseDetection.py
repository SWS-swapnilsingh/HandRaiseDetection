# from ultralytics import YOLO
# import cv2

# # Load the YOLO model
# model = YOLO('yolov8n-pose.pt')

# # Open the camera
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Perform detection
#     results = model(frame)

#     for result in results:
#         # Annotate the frame with the detection results
#         ann_frame = result.plot()
        
#         # Check for keypoints
#         if result.keypoints is not None:
#             for keypoints in result.keypoints:
#                 keypoint_data = keypoints.data[0]  # Get keypoints data

#                 # Extract keypoints for shoulders and elbows
#                 right_shoulder = keypoint_data[6]  # Right shoulder
#                 left_shoulder = keypoint_data[5]   # Left shoulder
#                 right_elbow = keypoint_data[8]     # Right elbow
#                 left_elbow = keypoint_data[7]      # Left elbow
                
#                 # Check if either elbow is above the corresponding shoulder
#                 # first check if confidance of each value is greater than 0.5
#                 if right_shoulder[2] > 0.5 or left_shoulder[2] > 0.5:
#                     if right_elbow[2] > 0.5 or left_elbow[2] > 0.5:
#                         if (right_elbow[1] < right_shoulder[1] and right_elbow[1] >0) or (left_elbow[1] < left_shoulder[1] and left_elbow[1] >0):
#                             # print("Hand raised detected!")
#                             #print on the display itself in red color
#                             cv2.putText(frame, "Hand raise detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#                         else:
#                             # print("Hand not raised detected!")
#                             #print on the display itself in red color
#                             cv2.putText(frame, "Hand is not raised", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                



#     # Display the result
#     cv2.imshow('frame',frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# =============================================================
# Code with Proper comments

from ultralytics import YOLO
import cv2

# Load the YOLO model for pose detection
model = YOLO('yolov8n-pose.pt')

# Open the camera (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Main loop to read frames from the camera
while True:
    ret, frame = cap.read()  # Capture a frame from the camera
    if not ret:
        break  # If frame not read successfully, exit the loop

    # Perform pose detection on the captured frame
    results = model(frame)

    # Loop through each detection result
    for result in results:
        # Annotate the frame with the detection results
        ann_frame = result.plot()
        
        # Check if keypoints are detected in the result
        if result.keypoints is not None:
            for keypoints in result.keypoints:
                keypoint_data = keypoints.data[0]  # Extract keypoints data

                # Extract coordinates and confidence scores for keypoints
                right_shoulder = keypoint_data[6]  # Right shoulder (x, y, confidence)
                left_shoulder = keypoint_data[5]   # Left shoulder (x, y, confidence)
                right_elbow = keypoint_data[8]     # Right elbow (x, y, confidence)
                left_elbow = keypoint_data[7]      # Left elbow (x, y, confidence)
                
                # Check if the confidence scores of shoulders and elbows are above 0.5
                if right_shoulder[2] > 0.5 or left_shoulder[2] > 0.5:
                    if right_elbow[2] > 0.5 or left_elbow[2] > 0.5:
                        # Check if either elbow is above the corresponding shoulder
                        if (right_elbow[1] < right_shoulder[1] and right_elbow[1] > 0) or (left_elbow[1] < left_shoulder[1] and left_elbow[1] > 0):
                            # Display "Hand raise detected" on the frame in green color
                            cv2.putText(frame, "Hand raise detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        else:
                            # Display "Hand is not raised" on the frame in red color
                            cv2.putText(frame, "Hand is not raised", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame with annotations in a window named 'frame'
    cv2.imshow('frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
