# ----- required imports -----

import cv2
import numpy as np
import os

# ----- helper functions -----

def detect_panels(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    panels = []
    for cnt in contours:
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)
            panels.append((x, y, x+w, y+h))
    panels.sort(key=lambda rect: (rect[2]-rect[0])*(rect[3]-rect[1]), reverse=True)
    return image, panels

def main():
    image_path = input("Enter manga image path: ")
    original, panels = detect_panels(image_path)
    output_dir = 'wallpapers'
    MIN_AREA_PERCENTAGE = 0.02  # can tweak this later kek
    img_height, img_width = original.shape[:2]
    total_image_area = img_width * img_height
    min_valid_area = total_image_area * MIN_AREA_PERCENTAGE
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    saved_count = 0
    for i, (x1, y1, x2, y2) in enumerate(panels):
        panel_width = x2 - x1
        panel_height = y2 - y1
        panel_area = panel_width * panel_height
        if panel_area < min_valid_area:
            print(f"Skipping panel {i+1} (too small: {panel_area}px)")
            continue
        panel = original[y1:y2, x1:x2]
        filename = os.path.join(output_dir, f'panel_{i+1}.png')
        cv2.imwrite(filename, panel)
        print(f"Saved {filename} ({panel_area}px)")
        saved_count += 1
    print(f"\nDone! Saved {saved_count} valid panels out of {len(panels)} detected")

# ----- execution code -----

if __name__ == "__main__":
    main()