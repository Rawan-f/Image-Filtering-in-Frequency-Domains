from google.colab import files
uploaded = files.upload()

import cv2
import numpy as np
import time
from google.colab.patches import cv2_imshow

# Step 1: Choose specific filters and image sizes
image_path = 'original image.jpg'
filter_size = 3  # Kernel size for spatial domain filtering
image_dimensions = (512, 512)  # Dimensions of the input image

# Step 2: Implement both approaches
def spatial_domain_filtering(image, kernel_size):
    start_time = time.time()
    filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    end_time = time.time()
    return filtered_image, end_time - start_time

def frequency_domain_filtering(image):
    start_time = time.time()
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    radius = 30
    mask = np.ones((rows, cols), np.uint8)
    mask[crow - radius:crow + radius, ccol - radius:ccol + radius] = 0
    dft_shift_filtered = dft_shift * mask
    filtered_image = np.fft.ifftshift(dft_shift_filtered)
    filtered_image = np.fft.ifft2(filtered_image)
    filtered_image = np.abs(filtered_image)
    end_time = time.time()
    return filtered_image, end_time - start_time

# Step 3: Load the image
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
original_image = cv2.resize(original_image, image_dimensions)

# Step 4: Measure execution time for both approaches
filtered_image_spatial, time_spatial = spatial_domain_filtering(original_image, filter_size)
filtered_image_frequency, time_frequency = frequency_domain_filtering(original_image)

# Step 5: Calculate performance ratio
performance_ratio = time_spatial / time_frequency

# Step 6: Analyze results
print("Time taken for spatial domain filtering:", time_spatial, "seconds")
print("Time taken for frequency domain filtering:", time_frequency, "seconds")
print("Performance ratio (spatial / frequency):", performance_ratio)

# Step 7: Display the original and filtered images
cv2_imshow(original_image)
cv2_imshow(filtered_image_spatial)
cv2_imshow(filtered_image_frequency)
