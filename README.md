Signature Verification Application

This Python-based GUI application verifies the similarity between two signatures using image processing techniques. 
It employs OpenCV and the Structural Similarity Index (SSIM) to compare signatures and determine their similarity percentage.

Features
Load two signature images for comparison.
Preprocess images using Gaussian blur and thresholding.
Resize and compare images using SSIM to calculate accuracy.
Display the verification result in a user-friendly interface.

Requirements
Ensure you have the following dependencies installed:
pip install opencv-python numpy pillow scikit-image

How to Run
Run the main.py script:
python main.py
Click "Load First Signature" to select the first image.
Click "Load Second Signature" to select the second image.
Click "Compare Signatures" to check the similarity.

Usage
If the similarity score is above 85%, the signature is considered verified.
Otherwise, the signatures are considered different.

Technologies Used
Python (Tkinter for GUI)
OpenCV (Image processing)
Pillow (Image handling)
Scikit-Image (SSIM calculation)

This project was majorly developed for the banks for checking the signatures of the customers for the secured transaction in the banks such that all the trasactions are secure and safe which help to verify the signature on the check leaf


![Screenshot (283)](https://github.com/user-attachments/assets/aa964028-f5b5-4801-bf68-380666b14647)


