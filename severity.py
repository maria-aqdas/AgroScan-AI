import cv2
import numpy as np

def verify_and_analyze_leaf(image_bgr):
    """
    1. Input Validation: Verifies if the image actually contains plant foliage.
    2. HSV Leaf Extraction & Lesion Detection.
    3. Severity Calculation.
    """
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    h, w = image_bgr.shape[:2]
    total_image_pixels = h * w

    # Plant Foliage Color Spectrum (Green to Olive/Yellowish hues)
    lower_plant = np.array([18, 25, 25])
    upper_plant = np.array([88, 255, 255])
    leaf_mask = cv2.inRange(hsv, lower_plant, upper_plant)

    # Clean morphological noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel)
    leaf_pixels = cv2.countNonZero(leaf_mask)

    # 1. Critical Input Validation: Must contain at least 6% plant area
    plant_ratio = (leaf_pixels / float(total_image_pixels)) * 100.0
    if plant_ratio < 6.0:
        return False, 0.0, None, None, None

    # 2. Lesion Extraction (Necrotic / Brown / Damaged tissue within the leaf)
    lower_lesion = np.array([8, 50, 20])
    upper_lesion = np.array([28, 255, 200])
    lesion_mask_raw = cv2.inRange(hsv, lower_lesion, upper_lesion)
    
    # Restrict lesions to leaf area only
    lesion_mask = cv2.bitwise_and(lesion_mask_raw, leaf_mask)
    lesion_pixels = cv2.countNonZero(lesion_mask)

    # Calculate Severity Percentage
    severity_pct = (lesion_pixels / float(leaf_pixels)) * 100.0
    severity_pct = min(100.0, max(0.0, round(severity_pct, 2)))

    # 3. Visual Overlay (Yellow border + Red lesion fill)
    overlay = image_bgr.copy()
    red_marker = np.zeros_like(image_bgr)
    red_marker[lesion_mask > 0] = [0, 0, 220]  # Red in BGR

    overlay = cv2.addWeighted(overlay, 0.72, red_marker, 0.28, 0)
    contours, _ = cv2.findContours(lesion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(overlay, contours, -1, (0, 255, 255), 1)

    return True, severity_pct, leaf_mask, lesion_mask, overlay