# Image Filtering in Frequency Domains

## Overview

This project explores image filtering techniques in the frequency domain using Python. It includes three tasks demonstrating different methods for applying high-pass filters to grayscale images and comparing the performance of spatial versus frequency domain filtering.

## Project Structure

- `task1_frequency_filtering.py`: Applies a high-pass filter to an image in the frequency domain.
- `task2_notch_filtering.py`: Uses a notch filter to filter an image in the frequency domain.
- `task3_comparison.py`: Compares the performance of spatial and frequency domain filtering methods.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install opencv-python-headless numpy matplotlib
```

## Usage

### 1. High-pass Filtering in Frequency Domain

**File:** `task1_frequency_filtering.py`

**How to Run:**

1. Ensure `original_image.jpg` is in the same directory as the script.
2. Run the script using Python:

    ```bash
    python task1_frequency_filtering.py
    ```

**What the Code Does:**

- Reads and converts the image to grayscale.
- Computes the Fourier Transform and applies a high-pass filter.
- Displays the original image, the high-pass filtered image, and the high-pass filter.

### 2. Notch Filtering in Frequency Domain

**File:** `task2_notch_filtering.py`

**How to Run:**

1. Ensure `original_image.jpg` is in the same directory as the script.
2. Run the script using Python:

    ```bash
    python task2_notch_filtering.py
    ```

**What the Code Does:**

- Reads and converts the image to grayscale.
- Creates a notch filter in the frequency domain and applies it.
- Displays the original image, grayscale image, notch filter, and the filtered image.

### 3. Performance Comparison

**File:** `task3_comparison.py`

**How to Run:**

1. Ensure `original_image.jpg` is in the same directory as the script.
2. Run the script using Python:

    ```bash
    python task3_comparison.py
    ```

**What the Code Does:**

- Applies spatial domain filtering using Gaussian blur.
- Applies frequency domain filtering using a high-pass filter.
- Compares the execution time of both methods and displays the results.

## Code Details

### High-pass Filtering

- **Computes** the Fourier Transform of the image.
- **Applies** a high-pass filter.
- **Displays** the filtered image and the filter mask.

### Notch Filtering

- **Creates** a notch filter in the frequency domain.
- **Applies** the notch filter to the image.
- **Displays** the filtered image and the frequency domain representation of the filter.

### Performance Comparison

- **Compares** spatial and frequency domain filtering times.
- **Displays** the original image, filtered images, and performance metrics.
