"""
Generates high-definition sample leaf images with accurate pathological markers
for instantaneous 1-click testing in CropGuard.
"""

import os
import numpy as np
import cv2

def ensure_samples_dir():
    samples_dir = os.path.join(os.path.dirname(__file__), "samples")
    os.makedirs(samples_dir, exist_ok=True)
    return samples_dir

def create_leaf_base(w=512, h=512, leaf_type="broad", base_color=(45, 135, 55)):
    """Creates a realistic leaf shape with natural green chlorophyll gradients and veins."""
    img = np.zeros((h, w, 3), dtype=np.uint8)
    # Natural subtle soil/neutral warm background
    img[:] = (238, 235, 230)

    # Leaf mask
    mask = np.zeros((h, w), dtype=np.uint8)
    center = (w // 2, h // 2)

    if leaf_type == "broad":
        # Tomato / Potato / Pepper broad compound leaf
        pts = np.array([
            [w//2, 45],
            [w//2 + 130, 160],
            [w//2 + 180, 290],
            [w//2 + 120, 420],
            [w//2 + 15, 470],
            [w//2 - 15, 470],
            [w//2 - 120, 420],
            [w//2 - 180, 290],
            [w//2 - 130, 160],
        ], np.int32)
        cv2.fillPoly(mask, [pts], 255)
        mask = cv2.GaussianBlur(mask, (15, 15), 0)
        _, mask = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)
    elif leaf_type == "linear":
        # Corn / Wheat / Rice elongated blade
        pts = np.array([
            [w//2, 30],
            [w//2 + 65, 180],
            [w//2 + 75, 340],
            [w//2 + 50, 480],
            [w//2 - 50, 480],
            [w//2 - 75, 340],
            [w//2 - 65, 180],
        ], np.int32)
        cv2.fillPoly(mask, [pts], 255)
        mask = cv2.GaussianBlur(mask, (11, 11), 0)
        _, mask = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)

    # Base leaf color with radial gradient
    leaf_layer = np.zeros_like(img)
    leaf_layer[:] = base_color

    # Add cellular texture
    noise = np.random.normal(0, 10, (h, w, 3)).astype(np.int16)
    leaf_noisy = np.clip(leaf_layer.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    # Draw primary and secondary veins
    vein_color = (base_color[0] + 15, min(255, base_color[1] + 35), base_color[2] + 15)
    # Main midrib
    cv2.line(leaf_noisy, (w//2, 50), (w//2, 470), vein_color, 4)

    if leaf_type == "broad":
        for y in range(120, 430, 45):
            cv2.line(leaf_noisy, (w//2, y), (w//2 + 110, y - 35), vein_color, 2)
            cv2.line(leaf_noisy, (w//2, y), (w//2 - 110, y - 35), vein_color, 2)
    elif leaf_type == "linear":
        for x_off in [-30, -15, 15, 30]:
            cv2.line(leaf_noisy, (w//2 + x_off, 100), (w//2 + x_off, 470), vein_color, 1)

    # Smooth veins slightly
    leaf_noisy = cv2.GaussianBlur(leaf_noisy, (3, 3), 0)

    # Composite leaf onto background
    mask_3d = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) > 0
    img[mask_3d] = leaf_noisy[mask_3d]
    return img, mask

def generate_samples():
    samples_dir = ensure_samples_dir()

    # 1. Tomato Late Blight (Large dark brown water-soaked blotches with chlorotic rim)
    img, mask = create_leaf_base(leaf_type="broad", base_color=(40, 130, 45))
    # Blight blotches
    for cx, cy, rx, ry in [(210, 200, 55, 70), (310, 310, 65, 50), (230, 370, 45, 40)]:
        # Chlorotic border
        cv2.ellipse(img, (cx, cy), (rx + 15, ry + 15), 25, 0, 360, (50, 195, 210), -1)
        # Necrotic dead tissue center (dark purplish-brown)
        cv2.ellipse(img, (cx, cy), (rx, ry), 25, 0, 360, (25, 38, 55), -1)
    img = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imwrite(os.path.join(samples_dir, "tomato_late_blight.jpg"), img)

    # 2. Tomato Early Blight (Concentric bullseye rings)
    img, mask = create_leaf_base(leaf_type="broad", base_color=(45, 140, 50))
    for cx, cy in [(190, 220), (320, 270), (250, 360), (210, 140)]:
        # Yellow chlorosis ring
        cv2.circle(img, (cx, cy), 36, (55, 210, 225), -1)
        # Concentric dark rings
        for r, col in [(28, (30, 55, 75)), (21, (45, 80, 105)), (14, (25, 45, 65)), (7, (20, 35, 50))]:
            cv2.circle(img, (cx, cy), r, col, -1)
            cv2.circle(img, (cx, cy), r, (15, 25, 35), 1)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(os.path.join(samples_dir, "tomato_early_blight.jpg"), img)

    # 3. Potato Early Blight (Target spots on potato foliage)
    img, mask = create_leaf_base(leaf_type="broad", base_color=(50, 135, 50))
    for cx, cy in [(220, 180), (300, 240), (240, 320), (310, 380)]:
        cv2.circle(img, (cx, cy), 32, (60, 200, 215), -1)
        for r, col in [(24, (32, 60, 80)), (17, (48, 85, 110)), (10, (25, 45, 65))]:
            cv2.circle(img, (cx, cy), r, col, -1)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(os.path.join(samples_dir, "potato_early_blight.jpg"), img)

    # 4. Corn Common Rust (Cinnamon-orange powdery pustules across leaf blade)
    img, mask = create_leaf_base(leaf_type="linear", base_color=(50, 145, 60))
    np.random.seed(42)
    for _ in range(85):
        px = np.random.randint(220, 300)
        py = np.random.randint(90, 440)
        # Small elongated cinnamon-red rust pustule
        cv2.ellipse(img, (px, py), (4, 8), 0, 0, 360, (25, 105, 215), -1)
        cv2.circle(img, (px, py), 2, (15, 65, 160), -1)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(os.path.join(samples_dir, "corn_common_rust.jpg"), img)

    # 5. Rice Leaf Blast (Spindle / diamond shaped lesions with greyish center)
    img, mask = create_leaf_base(leaf_type="linear", base_color=(45, 138, 55))
    for cx, cy in [(256, 170), (240, 260), (265, 340), (250, 410)]:
        # Spindle diamond contour
        pts = np.array([
            [cx, cy - 35],
            [cx + 16, cy],
            [cx, cy + 35],
            [cx - 16, cy]
        ], np.int32)
        # Yellowish margin
        cv2.drawContours(img, [pts], -1, (65, 205, 220), 8)
        # Brown border
        cv2.drawContours(img, [pts], -1, (25, 50, 85), 4)
        # Pale grey/ash center
        cv2.fillPoly(img, [pts], (165, 170, 175))
    img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(os.path.join(samples_dir, "rice_leaf_blast.jpg"), img)

    # 6. Wheat Yellow Rust (Linear yellow stripes along veins)
    img, mask = create_leaf_base(leaf_type="linear", base_color=(48, 142, 58))
    for stripe_x in [240, 252, 268]:
        for y in range(120, 430, 8):
            cv2.ellipse(img, (stripe_x, y), (3, 5), 0, 0, 360, (30, 185, 245), -1)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    cv2.imwrite(os.path.join(samples_dir, "wheat_yellow_rust.jpg"), img)

    # 7. Healthy Tomato Leaf (Flawless lush green canopy)
    img, mask = create_leaf_base(leaf_type="broad", base_color=(40, 150, 50))
    cv2.imwrite(os.path.join(samples_dir, "healthy_tomato.jpg"), img)

    # 8. Healthy Wheat Blade (Pristine cereal blade)
    img, mask = create_leaf_base(leaf_type="linear", base_color=(45, 155, 55))
    cv2.imwrite(os.path.join(samples_dir, "healthy_wheat.jpg"), img)

    print("All 8 sample images generated successfully in:", samples_dir)

if __name__ == "__main__":
    generate_samples()
