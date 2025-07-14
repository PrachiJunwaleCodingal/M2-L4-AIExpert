import cv2
import numpy as np
import matplotlib.pyplot as plt
def display_image(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  
        plt.imshow(image, cmap='gray')
    else: 
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if method == "sobel":
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        return cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))

    elif method == "canny":
        return cv2.Canny(gray_image, threshold1, threshold2)
  
    elif method == "laplacian":
        return cv2.Laplacian(gray_image, cv2.CV_64F).astype(np.uint8)

def apply_filter(image, filter_type="gaussian", ksize=5):
    if filter_type == "gaussian":
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif filter_type == "median":
        return cv2.medianBlur(image, ksize)

def detect(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error")
        return
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            ksize = int(input("Enter kernel size for Sobel: "))
            result = apply_edge_detection(image, method="sobel", ksize=ksize)
            display_image("Sobel Edge ", result)

        elif choice == "2":
            threshold1 = int(input("Enter lower threshold for Canny: "))
            threshold2 = int(input("Enter upper threshold for Canny: "))
            result = apply_edge_detection(image, method="canny", threshold1=threshold1, threshold2=threshold2)
            display_image("Canny Edge", result)

        elif choice == "3":
            result = apply_edge_detection(image, method="laplacian")
            display_image("Laplacian Edge", result)
        elif choice == "4":
            ksize = int(input(" Gaussian smoothing (odd number): "))
            result = apply_filter(image, filter_type="gaussian", ksize=ksize)
            display_image("Gaussian Smoothed ", result)
        elif choice == "5":
            ksize = int(input(" Median filtering (odd number): "))
            result = apply_filter(image, filter_type="median", ksize=ksize)
            display_image("Median Filtered ", result)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

detect('bird1.jpg')