import cv2
import numpy as np
import sys
print(sys.path)

def measure_object(frame, contours, pixel_to_pixel_ratio):
    """
    Measure objects in the frame and draw their dimensions.
    :param frame: Input image
    :param contours: Detected contours
    :param pixel_to_pixel_ratio: Ratio of pixel dimensions to ArUco marker width
    :return: Updated frame
    """
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # Object dimensions in pixels
        object_width = w * pixel_to_pixel_ratio
        object_height = h * pixel_to_pixel_ratio

        # Detect specific object sizes (in pixels using the ratio)
        if (5.0 <= object_width <= 10.6 and 1.0 <= object_height <= 10.9) or \
           (1.0 <= object_width <= 5.0 and 3.0 <= object_height <= 6.0):
          cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
          cv2.putText(frame, f"Width:{object_width:.1f}cm Length: {object_height:.1f} cm", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    return frame

def main():
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
    parameters = cv2.aruco.DetectorParameters()
    aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'q' to exit.")

    pixel_to_pixel_ratio = None  # Ratio to use for measuring objects

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from webcam.")
            break

        # Convert the frame to grayscale (required for ArUco detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect ArUco markers in the frame using the ArucoDetector class
        corners, ids, rejectedImgPoints = aruco_detector.detectMarkers(frame)
        

        if ids is not None:
            # Draw detected markers and their IDs on the frame
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            for i, marker_id in enumerate(ids):
                # Get the center of the marker
                corner = corners[i][0]
                center_x = int(corner[:, 0].mean())
                center_y = int(corner[:, 1].mean())
                cv2.putText(frame, f"ID: {marker_id[0]}", (center_x, center_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Calculate the pixel-to-pixel ratio using the width of the detected ArUco marker
                if pixel_to_pixel_ratio is None:
                    marker_width = np.linalg.norm(corner[0] - corner[1])  # Distance between two corners
                    pixel_to_pixel_ratio = 1 / marker_width  # Using marker width as the base

        # Detect objects if the ArUco marker has been identified
        if pixel_to_pixel_ratio:
            # Preprocess the frame for contour detection
            #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            #edges = cv2.Canny(blurred, 100, 200)
            #contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = MyDetectionMethods.detect_contours_with_binarization(gray)

            # Measure objects and annotate the frame
            frame = measure_object(frame, contours, pixel_to_pixel_ratio)

        # Display the resulting frame
        cv2.imshow('ArUco Marker Detection and Object Measurement', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()



