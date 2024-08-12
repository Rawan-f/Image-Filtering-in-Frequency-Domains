from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread('original image.jpg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Compute the Fourier Transform of the grayscale image
dft = np.fft.fft2(gray_image)
dft_shift = np.fft.fftshift(dft)

# Step 4: Create a high-pass filter in the frequency domain
rows, cols = gray_image.shape
crow, ccol = rows // 2 , cols // 2
radius = 30
mask = np.ones((rows, cols), np.uint8)
mask[crow - radius:crow + radius, ccol - radius:ccol + radius] = 0

# Step 5: Perform element-wise multiplication between the Fourier Transform and the high-pass filter
dft_shift_filtered = dft_shift * mask

# Step 6: Compute the Inverse Fourier Transform to obtain the filtered image
filtered_image = np.fft.ifftshift(dft_shift_filtered)
filtered_image = np.fft.ifft2(filtered_image)
filtered_image = np.abs(filtered_image)

# Step 7: Display the original image, the filtered image, and the high-pass filter
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image (High-pass)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(mask, cmap='gray')
plt.title('High-pass Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
