import cv2
import matplotlib.pyplot as plt

def image_pre_processing(image_path):
    image = cv2.imread(f"{image_path}")
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 3. Apply adaptive thresholding to binarize the image
    binary_image = cv2.adaptiveThreshold(blurred_image, 255,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

    # 4. Use morphology to remove noise and improve text structure
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morphed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    plt.imshow(morphed_image, cmap='gray')
    plt.savefig(f'{image_path}')
