import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  
        plt.imshow(image, cmap='gray')
    else:  
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #color

    plt.title(title)
    plt.axis('off')
    plt.show()


def detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error")
        return
  
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display("Original", gray_image)
 
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. lap Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")
    while True:
        choice = input("Enter choice (1-6): ")
        if choice == "1":
            sobelx = cv2.Sobel(1, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display("Sobel Edge", combined_sobel)

        elif choice == "2":
            print("Adjust thresholds for Canny ")
            low = int(input("Enter lower threshold: "))
            up = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, low, up)
            display("Canny Edge ", edges)

        elif choice == "3":
            lap = cv2.lap(gray_image, cv2.CV_64F)
            display("lap Edge", np.abs(lap).astype(np.uint8))

        elif choice == "4":
            print(" Gaussian blur (must be odd, default: 5)")
            s = int(input("Enter kernel size (odd-no.): "))
            blurred = cv2.GaussianBlur(image, (s, s), 0)
            display("Gaussian Smoothed", blurred)

        elif choice == "5":
            print("Median filtering (must be odd, default: 5)")
            s = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(image, s)
            display("Median Filtered ", median_filtered)

        elif choice == "6":
            print("Exit..")
            break
        else:
            print("Invalid choice")

detection('dog1.jpeg')
