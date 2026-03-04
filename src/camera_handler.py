"""
Camera handler for live video capture.
"""
import cv2  ## python module for Open Source Computre Vision Library. It helps computers see by processing images and video. It opens up the camera
import numpy as np
from typing import Optional


class CameraHandler:
    """Manages webcam video capture."""

    def __init__(self, camera_index: int = 0):
        # TODO: Store the camera_index parameter as an instance variable
        self.camera_index = camera_index   #is the index of the spefic capture you are using. To use cv2 you need an index to start up your camera. The index species which camera you are using.

        # TODO: Initialize capture to None (will be set when camera starts)
        self.capture = None #Is the thing that tells you if the computer webcam is actively capturing things

        # TODO: Initialize running state flag to False
        self.is_running = False   #lets you know if the camera is actively running




    def start(self) -> bool:   #function that starts the camera
        """
        Start the camera capture.

        Returns:
            bool: True if camera started successfully, False if failed
        """
    # If camera is already running, return success
        if self.capture is not None:
            return True

    # TODO: Initialize OpenCV VideoCapture with the camera_index
        self.capture = cv2.VideoCapture(self.camera_index)  #You computer is capturing stuff because you opened up the Cv2 library using your camera_index

    # TODO: Check if camera opened successfully using .isOpened() method
        if not self.capture.isOpened():
            # Failed - cleanup and return False
            self.capture = None
            return False

    # TODO: Set the is_running flag to True
        self.is_running = True  #question
        return True




    def stop(self):
        """
        Stop the camera capture and release resources.
        """
        # TODO: Set is_running flag to False
        self.is_running = False

        # Release camera resources if active
        if self.is_running is not None:
            # TODO: Call the release() method to free the camera
            self.capture.release()
            self.capture = None




    def read_frame(self) -> Optional[np.ndarray]:
        """
        Read a single frame from the camera.

        Returns:
            np.ndarray: BGR image (H x W x 3), or None if failed    def read_frame(self) -> Optional[np.ndarray]:  #is an array of numbers that make up pictures
        """

        # Check if camera is initialized and running
        if self.capture is None or not self.is_running:
            return None

        # TODO: Read frame using capture.read() method
        # This returns (success_flag, frame_array)
        ret, frame = self.capture.read()

        # Return frame if successful, otherwise None
        if ret:
            return frame
        return None




    def get_frame_size(self) -> tuple:
        """
        Get current frame dimensions.

        Returns:
            tuple: (width, height) in pixels
        """
        # Return default if not initialized
        if self.capture is None:
            return (640, 480)

        # TODO: Query camera properties using cv2.CAP_PROP_FRAME_WIDTH
        width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))  #double check

        # TODO: Query camera properties using cv2.CAP_PROP_FRAME_HEIGHT
        height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        return (width, height)


