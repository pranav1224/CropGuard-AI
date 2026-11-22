"""
Generate a beautiful local banner image for CropGuard sidebar.
"""

import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def generate_banner():
    width = 600
    height = 320

    # Create gradient background
    img = Image.new("RGB", (width, height), "#022c22")
    draw = ImageDraw.Draw(img)

    for y in range(height):
        ratio = y / height
        # Gradient from #064e3b (6, 78, 59) to #022c22 (2, 44, 34)
        r = int(6 * (1 - ratio) + 2 * ratio)
        g = int(78 * (1 - ratio) + 44 * ratio)
        b = int(59 * (1 - ratio) + 34 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Draw geometric glowing aura circles
    for i in range(4):
        radius = 160 + i * 25
        alpha_color = (16, 185, 129)
        draw.ellipse([width - radius, height//2 - radius, width + radius, height//2 + radius], outline=(16, 185, 129), width=2)

    # Draw stylized central leaf shape
    leaf_pts = [
        (300, 60),
        (380, 130),
        (400, 200),
        (350, 260),
        (300, 275),
        (250, 260),
        (200, 200),
        (220, 130)
    ]
    draw.polygon(leaf_pts, fill=(5, 150, 105), outline=(52, 211, 153))

    # Leaf midrib & veins
    draw.line([(300, 70), (300, 265)], fill=(167, 243, 208), width=3)
    for y_v in range(110, 240, 28):
        draw.line([(300, y_v), (360, y_v - 20)], fill=(167, 243, 208), width=2)
        draw.line([(300, y_v), (240, y_v - 20)], fill=(167, 243, 208), width=2)

    # Accent glow badge
    draw.rounded_rectangle([40, 40, 200, 70], radius=15, fill=(6, 95, 70), outline=(16, 185, 129))
    draw.text((60, 48), "🌿 CROP黠UARD", fill=(255, 255, 255))

    # Banner Title text
    draw.text((40, 230), "CropGuard AI Precision", fill=(255, 255, 255))
    draw.text((40, 260), "3D Pathology & Yield Optimizer", fill=(167, 243, 208))

    save_path = os.path.join(os.path.dirname(__file__), "assets", "cropguard_banner.png")
    img.save(save_path, "PNG")
    print("Banner generated successfully at:", save_path)

if __name__ == "__main__":
    generate_banner()
