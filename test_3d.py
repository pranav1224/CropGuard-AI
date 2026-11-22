"""
Test 3D Visualizer Engine
"""
import numpy as np
from engine.visualizer_3d import generate_3d_leaf_surface_plot, generate_3d_yield_surface_plot, get_webgl_leaf_3d_html
from engine.yield_predictor import CropYieldPredictor

def test_3d():
    dummy_img = np.ones((128, 128, 3), dtype=np.uint8) * 100
    dummy_mask = np.zeros((128, 128), dtype=np.uint8)
    dummy_mask[40:80, 40:80] = 255

    # 1. Test 3D leaf surface plot
    fig1 = generate_3d_leaf_surface_plot(dummy_img, dummy_mask, dummy_mask, np.zeros_like(dummy_mask))
    print("3D Leaf Surface Figure created successfully:", fig1)

    # 2. Test 3D yield surface plot
    yp = CropYieldPredictor()
    fig2 = generate_3d_yield_surface_plot("Tomato", 100.0, 100.0, yp.predict_yield)
    print("3D Yield Surface Figure created successfully:", fig2)

    # 3. Test WebGL HTML generator
    html_str = get_webgl_leaf_3d_html(dummy_img, dummy_mask, dummy_mask, np.zeros_like(dummy_mask))
    print("WebGL HTML generated, length:", len(html_str))

if __name__ == "__main__":
    test_3d()
