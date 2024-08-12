from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the color image
image = cv2.imread('original image.jpg')
# Convert the color image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the size of the filter
filter_size = 31

# Create a high-pass filter (notch filter) in the frequency domain
high_pass_mask = np.ones_like(gray_image, dtype=np.complex64)
# Define the coordinates for the center of the filter
center = tuple(map(lambda x: (x - 1) // 2, high_pass_mask.shape))
# Set the radius of the central circle
radius = 10
# Create a circular notch in the center of the filter
for i in range(high_pass_mask.shape[0]):
    for j in range(high_pass_mask.shape[1]):
        if np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2) <= radius:
            high_pass_mask[i, j] = 0

# Apply the high-pass filter to the frequency domain representation of the image
dft_shift_filtered = np.fft.fftshift(np.fft.fft2(gray_image)) * high_pass_mask

# Compute the Inverse Discrete Fourier Transform (IDFT) to obtain the filtered image in the spatial domain
filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(dft_shift_filtered)))

# Display the original color image, grayscale image, high-pass filter, and filtered images
plt.figure(figsize=(12, 8))

# Original Color Image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Color Image')
plt.axis('off')

# Grayscale Image
plt.subplot(2, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# High-pass Filter (Frequency Domain)
plt.subplot(2, 3, 4)
plt.imshow(np.log(1 + np.abs(dft_shift_filtered)), cmap='gray')
plt.title('High-pass Filter (Frequency Domain)')
plt.axis('off')

# Filtered Image (Spatial Domain)
plt.subplot(2, 3, 5)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image (Spatial Domain)')
plt.axis('off')

plt.tight_layout()
plt.show()