import cv2
import numpy as np
import os

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

def resize_for_device(image, device):
    device_resolutions = {
        'phone': (1080, 1920),
        'laptop': (1366, 768),
        'ipad': (2048, 2732),
        'desktop': (3840, 2160)
    }
    target_w, target_h = device_resolutions[device]
    h, w = image.shape[:2]
    scale = min(target_w/w, target_h/h)
    resized = cv2.resize(image, (int(w*scale), int(h*scale)))
    delta_w = target_w - resized.shape[1]
    delta_h = target_h - resized.shape[0]
    return cv2.copyMakeBorder(resized, 0, delta_h, 0, delta_w, 
                             cv2.BORDER_CONSTANT, value=(0,0,0))

def main():
    image_path = input("Enter manga image path: ")
    original, panels = detect_panels(image_path)
    if not os.path.exists('wallpapers'):
        os.makedirs('wallpapers')
    for i, (x1, y1, x2, y2) in enumerate(panels):
        panel = original[y1:y2, x1:x2]
        cv2.imshow(f'Panel {i+1}', panel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        choice = input(f"Save Panel {i+1}? (y/n): ").lower()
        if choice == 'y':
            devices = input("Enter devices (comma separated): ").lower().split(',')
            for device in devices:
                device = device.strip()
                resized = resize_for_device(panel, device)
                filename = f'wallpapers/panel_{i+1}_{device}.png'
                cv2.imwrite(filename, resized)
                print(f"Saved {filename}")

if __name__ == "__main__":
    main()