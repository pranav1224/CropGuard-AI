"""
CropGuard 3D Visualization Engine.
Provides interactive WebGL 3D Leaf Topography, Matplotlib 3D Surface Plots,
and 3D Agronomic Yield Response Landscapes.
"""

import os
import json
import numpy as np
import cv2

# Set writable MPLCONFIGDIR to prevent warning
os.environ["MPLCONFIGDIR"] = os.path.join(os.path.dirname(__file__), ".mpl_cache")
os.makedirs(os.environ["MPLCONFIGDIR"], exist_ok=True)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_leaf_surface_plot(
    rgb_img: np.ndarray,
    disease_mask: np.ndarray,
    necrosis_mask: np.ndarray,
    rust_mask: np.ndarray
) -> plt.Figure:
    """Generates a scientific 3D surface elevation and contour plot of leaf pathology."""
    grid_size = 40
    small_img = cv2.resize(rgb_img, (grid_size, grid_size), interpolation=cv2.INTER_AREA)
    small_dis = cv2.resize(disease_mask, (grid_size, grid_size), interpolation=cv2.INTER_NEAREST)
    small_nec = cv2.resize(necrosis_mask, (grid_size, grid_size), interpolation=cv2.INTER_NEAREST)
    small_rst = cv2.resize(rust_mask, (grid_size, grid_size), interpolation=cv2.INTER_NEAREST)

    x = np.linspace(-2.2, 2.2, grid_size)
    y = np.linspace(-2.2, 2.2, grid_size)
    X, Y = np.meshgrid(x, y)

    # Base parabolic dome of natural leaf blade
    Z = np.clip(1.1 - 0.20 * (X**2 + Y**2), 0.1, 1.1)

    # Apply pathological elevation alterations
    # Necrotic craters dip down
    Z -= (small_nec.astype(np.float32) / 255.0) * 0.70
    # Rust pustules erupt upwards
    Z += (small_rst.astype(np.float32) / 255.0) * 0.80
    # General chlorosis slight depression
    Z -= (small_dis.astype(np.float32) / 255.0) * 0.15

    # Normalize colors for surface facecolors
    colors_face = small_img.astype(np.float32) / 255.0

    fig = plt.figure(figsize=(9, 5.5), facecolor="#0B1120", edgecolor="none")
    ax = fig.add_subplot(111, projection='3d', facecolor="#0B1120")

    surf = ax.plot_surface(
        X, Y, Z,
        facecolors=colors_face,
        rstride=1, cstride=1,
        linewidth=0,
        antialiased=True,
        shade=False
    )

    # 3D Aesthetic styling
    ax.view_init(elev=36, azim=-55)
    ax.set_title("3D Leaf Tissue Topography (Craters: Necrosis | Ridges: Rust)", fontsize=11, color="#E2E8F0", fontweight="bold", pad=10)
    ax.set_xlabel("Width (X)", fontsize=8, color="#94A3B8")
    ax.set_ylabel("Length (Y)", fontsize=8, color="#94A3B8")
    ax.set_zlabel("Elevation (Z)", fontsize=8, color="#94A3B8")

    # Dark theme grid lines
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1E293B')
    ax.yaxis.pane.set_edgecolor('#1E293B')
    ax.zaxis.pane.set_edgecolor('#1E293B')
    ax.tick_params(colors='#94A3B8', labelsize=7)

    plt.tight_layout()
    return fig

def generate_3d_yield_surface_plot(
    crop: str,
    base_n: float,
    base_k: float,
    predictor_fn,
    soil_ph: float = 6.5,
    oc_pct: float = 0.75
) -> plt.Figure:
    """Generates a 3D agronomic response surface: Nitrogen vs Potassium vs Yield."""
    n_vals = np.linspace(max(10, base_n * 0.4), base_n * 1.6, 22)
    k_vals = np.linspace(max(10, base_k * 0.4), base_k * 1.6, 22)
    N_grid, K_grid = np.meshgrid(n_vals, k_vals)
    Yield_grid = np.zeros_like(N_grid)

    for i in range(N_grid.shape[0]):
        for j in range(N_grid.shape[1]):
            res = predictor_fn(
                crop=crop,
                land_area_acres=1.0,
                nitrogen=float(N_grid[i, j]),
                phosphorus=50.0,
                potassium=float(K_grid[i, j]),
                soil_ph=soil_ph,
                organic_carbon_pct=oc_pct,
                irrigation_type="Precision Drip / Fertigation",
                avg_temp=25.0,
                disease_damage_pct=0.0,
                apply_growth_booster=True
            )
            Yield_grid[i, j] = res["boosted_yield_per_acre"]

    fig = plt.figure(figsize=(9, 5.5), facecolor="#0B1120")
    ax = fig.add_subplot(111, projection='3d', facecolor="#0B1120")

    surf = ax.plot_surface(
        N_grid, K_grid, Yield_grid,
        cmap="viridis",
        linewidth=0.2,
        alpha=0.92,
        antialiased=True
    )

    # Mark current farm point
    curr_res = predictor_fn(
        crop=crop,
        land_area_acres=1.0,
        nitrogen=base_n,
        phosphorus=50.0,
        potassium=base_k,
        soil_ph=soil_ph,
        organic_carbon_pct=oc_pct,
        irrigation_type="Precision Drip / Fertigation",
        avg_temp=25.0,
        disease_damage_pct=0.0,
        apply_growth_booster=True
    )
    curr_yield = curr_res["boosted_yield_per_acre"]
    ax.scatter([base_n], [base_k], [curr_yield], color="#EF4444", s=110, edgecolors="white", linewidth=2, label="Your Current Field Level")

    ax.view_init(elev=28, azim=130)
    ax.set_title(f"3D Yield Response Landscape: {crop}", fontsize=11, color="#E2E8F0", fontweight="bold", pad=10)
    ax.set_xlabel("Nitrogen N (kg/acre)", fontsize=8, color="#94A3B8")
    ax.set_ylabel("Potassium K (kg/acre)", fontsize=8, color="#94A3B8")
    ax.set_zlabel("Yield Rate", fontsize=8, color="#94A3B8")

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#1E293B')
    ax.yaxis.pane.set_edgecolor('#1E293B')
    ax.zaxis.pane.set_edgecolor('#1E293B')
    ax.tick_params(colors='#94A3B8', labelsize=7)
    ax.legend(facecolor="#1E293B", edgecolor="#475569", labelcolor="#F1F5F9", fontsize=8)

    plt.tight_layout()
    return fig

def get_webgl_leaf_3d_html(
    rgb_img: np.ndarray,
    disease_mask: np.ndarray,
    necrosis_mask: np.ndarray,
    rust_mask: np.ndarray
) -> str:
    """
    Produces a self-contained interactive WebGL 3D leaf model with orbit controls,
    lighting, depth elevation, and cratering. Runs 100% locally with zero external CDNs!
    """
    grid_res = 32
    small_rgb = cv2.resize(rgb_img, (grid_res, grid_res), interpolation=cv2.INTER_AREA)
    small_nec = cv2.resize(necrosis_mask, (grid_res, grid_res), interpolation=cv2.INTER_NEAREST)
    small_rst = cv2.resize(rust_mask, (grid_res, grid_res), interpolation=cv2.INTER_NEAREST)
    small_dis = cv2.resize(disease_mask, (grid_res, grid_res), interpolation=cv2.INTER_NEAREST)

    # Build vertex array: X, Y, Z, R, G, B
    vertices = []
    indices = []

    for y in range(grid_res):
        for x in range(grid_res):
            nx = (x / (grid_res - 1)) * 2.0 - 1.0
            ny = (y / (grid_res - 1)) * 2.0 - 1.0

            r_norm = np.sqrt(nx**2 + ny**2)
            nz = max(0.0, 0.45 * (1.0 - r_norm**1.4))

            nec_val = float(small_nec[y, x]) / 255.0
            rst_val = float(small_rst[y, x]) / 255.0
            dis_val = float(small_dis[y, x]) / 255.0

            nz -= nec_val * 0.35
            nz += rst_val * 0.45
            nz -= dis_val * 0.08

            r = float(small_rgb[y, x, 0]) / 255.0
            g = float(small_rgb[y, x, 1]) / 255.0
            b = float(small_rgb[y, x, 2]) / 255.0

            vertices.extend([round(nx, 3), round(ny, 3), round(nz, 3), round(r, 2), round(g, 2), round(b, 2)])

    for y in range(grid_res - 1):
        for x in range(grid_res - 1):
            top_left = y * grid_res + x
            top_right = top_left + 1
            bottom_left = (y + 1) * grid_res + x
            bottom_right = bottom_left + 1

            indices.extend([top_left, bottom_left, top_right])
            indices.extend([top_right, bottom_left, bottom_right])

    vertices_json = json.dumps(vertices)
    indices_json = json.dumps(indices)

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                margin: 0;
                padding: 0;
                background: #0B1120;
                overflow: hidden;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                user-select: none;
            }}
            #container {{
                width: 100%;
                height: 440px;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 14px;
                overflow: hidden;
                box-shadow: inset 0 0 20px rgba(0,0,0,0.6);
            }}
            canvas {{
                width: 100%;
                height: 100%;
                display: block;
                cursor: grab;
            }}
            canvas:active {{
                cursor: grabbing;
            }}
            .hud-overlay {{
                position: absolute;
                top: 14px;
                left: 14px;
                color: #A7F3D0;
                font-size: 11px;
                background: rgba(15, 23, 42, 0.82);
                backdrop-filter: blur(8px);
                border: 1px solid rgba(16, 185, 129, 0.35);
                padding: 10px 14px;
                border-radius: 10px;
                pointer-events: none;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
                line-height: 1.5;
            }}
            .hud-title {{
                font-weight: 700;
                color: #34D399;
                font-size: 12px;
                display: flex;
                align-items: center;
                gap: 6px;
                margin-bottom: 4px;
            }}
            .controls-panel {{
                position: absolute;
                bottom: 14px;
                right: 14px;
                display: flex;
                gap: 8px;
            }}
            .btn-3d {{
                background: rgba(30, 41, 59, 0.9);
                color: #F1F5F9;
                border: 1px solid #475569;
                font-size: 11px;
                font-weight: 600;
                padding: 7px 13px;
                border-radius: 8px;
                cursor: pointer;
                transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            }}
            .btn-3d:hover {{
                background: #059669;
                border-color: #34D399;
                color: white;
                transform: translateY(-1px);
                box-shadow: 0 6px 14px rgba(5, 150, 105, 0.4);
            }}
        </style>
    </head>
    <body>
        <div id="container">
            <canvas id="webglCanvas"></canvas>
            <div class="hud-overlay">
                <div class="hud-title">🌐 3D PATHOLOGY TOPOGRAPHY VIEWER</div>
                <span>• <b>Drag</b> to Orbit / Rotate in 3D</span><br/>
                <span>• <b>Scroll Wheel</b> to Zoom Depth</span><br/>
                <span>• <b>Depressions</b>: Necrotic Tissue Collapse</span><br/>
                <span>• <b>Peaks</b>: Fungal Spore Pustules</span>
            </div>
            <div class="controls-panel">
                <button class="btn-3d" id="resetBtn">🔄 Reset View</button>
                <button class="btn-3d" id="wireframeBtn">🕸️ Toggle Mesh</button>
                <button class="btn-3d" id="spinBtn">⏸️ Pause Spin</button>
            </div>
        </div>

        <script>
            const canvas = document.getElementById("webglCanvas");
            const gl = canvas.getContext("webgl", {{ antialias: true, alpha: false }});

            if (!gl) {{
                document.getElementById("container").innerHTML = "<div style='color:white;padding:20px;'>WebGL not supported on this browser.</div>";
            }}

            const vsSource = `
                attribute vec3 aPosition;
                attribute vec3 aColor;

                uniform mat4 uModelViewMatrix;
                uniform mat4 uProjectionMatrix;
                uniform vec3 uLightDirection;

                varying vec3 vColor;
                varying float vLighting;

                void main(void) {{
                    gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aPosition, 1.0);
                    vColor = aColor;

                    vec3 normal = normalize(vec3(aPosition.x * 0.5, aPosition.y * 0.5, 1.0));
                    float diffuse = max(dot(normal, normalize(uLightDirection)), 0.3);
                    vLighting = diffuse + 0.45;
                }}
            `;

            const fsSource = `
                precision mediump float;
                varying vec3 vColor;
                varying float vLighting;

                void main(void) {{
                    vec3 finalCol = vColor * min(vLighting, 1.25);
                    gl_FragColor = vec4(finalCol, 1.0);
                }}
            `;

            function createShader(gl, type, source) {{
                const shader = gl.createShader(type);
                gl.shaderSource(shader, source);
                gl.compileShader(shader);
                if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {{
                    console.error(gl.getShaderInfoLog(shader));
                    gl.deleteShader(shader);
                    return null;
                }}
                return shader;
            }}

            const vertexShader = createShader(gl, gl.VERTEX_SHADER, vsSource);
            const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fsSource);
            const program = gl.createProgram();
            gl.attachShader(program, vertexShader);
            gl.attachShader(program, fragmentShader);
            gl.linkProgram(program);
            gl.useProgram(program);

            const aPosition = gl.getAttribLocation(program, "aPosition");
            const aColor = gl.getAttribLocation(program, "aColor");
            const uModelViewMatrix = gl.getUniformLocation(program, "uModelViewMatrix");
            const uProjectionMatrix = gl.getUniformLocation(program, "uProjectionMatrix");
            const uLightDirection = gl.getUniformLocation(program, "uLightDirection");

            const rawVertices = {vertices_json};
            const rawIndices = {indices_json};

            const vertexBuffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
            gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(rawVertices), gl.STATIC_DRAW);

            const indexBuffer = gl.createBuffer();
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
            gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(rawIndices), gl.STATIC_DRAW);

            const FSIZE = Float32Array.BYTES_PER_ELEMENT;
            gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, FSIZE * 6, 0);
            gl.enableVertexAttribArray(aPosition);
            gl.vertexAttribPointer(aColor, 3, gl.FLOAT, false, FSIZE * 6, FSIZE * 3);
            gl.enableVertexAttribArray(aColor);

            gl.enable(gl.DEPTH_TEST);
            gl.clearColor(0.04, 0.07, 0.12, 1.0);

            function createPerspective(fovy, aspect, near, far) {{
                const f = 1.0 / Math.tan(fovy / 2);
                const nf = 1 / (near - far);
                return [
                    f / aspect, 0, 0, 0,
                    0, f, 0, 0,
                    0, 0, (far + near) * nf, -1,
                    0, 0, (2 * far * near) * nf, 0
                ];
            }}

            function multiplyMatrix(a, b) {{
                const out = new Array(16);
                for (let i = 0; i < 4; i++) {{
                    for (let j = 0; j < 4; j++) {{
                        out[i * 4 + j] = 
                            a[i * 4 + 0] * b[0 * 4 + j] +
                            a[i * 4 + 1] * b[1 * 4 + j] +
                            a[i * 4 + 2] * b[2 * 4 + j] +
                            a[i * 4 + 3] * b[3 * 4 + j];
                    }}
                }}
                return out;
            }}

            function rotateXMatrix(rad) {{
                const c = Math.cos(rad), s = Math.sin(rad);
                return [
                    1, 0, 0, 0,
                    0, c, s, 0,
                    0, -s, c, 0,
                    0, 0, 0, 1
                ];
            }}

            function rotateYMatrix(rad) {{
                const c = Math.cos(rad), s = Math.sin(rad);
                return [
                    c, 0, -s, 0,
                    0, 1, 0, 0,
                    s, 0, c, 0,
                    0, 0, 0, 1
                ];
            }}

            function translateMatrix(tx, ty, tz) {{
                return [
                    1, 0, 0, 0,
                    0, 1, 0, 0,
                    0, 0, 1, 0,
                    tx, ty, tz, 1
                ];
            }}

            let rotX = -0.75;
            let rotY = 0.45;
            let zoom = -3.2;
            let isDragging = false;
            let lastMouseX = 0, lastMouseY = 0;
            let autoSpin = true;
            let isWireframe = false;

            function resize() {{
                const width = canvas.clientWidth;
                const height = canvas.clientHeight;
                if (canvas.width !== width || canvas.height !== height) {{
                    canvas.width = width;
                    canvas.height = height;
                    gl.viewport(0, 0, width, height);
                }}
            }}

            canvas.addEventListener('mousedown', (e) => {{
                isDragging = true;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;
                autoSpin = false;
            }});

            window.addEventListener('mouseup', () => isDragging = false);

            canvas.addEventListener('mousemove', (e) => {{
                if (!isDragging) return;
                const dx = e.clientX - lastMouseX;
                const dy = e.clientY - lastMouseY;
                rotY += dx * 0.012;
                rotX += dy * 0.012;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;
            }});

            canvas.addEventListener('wheel', (e) => {{
                e.preventDefault();
                zoom += e.deltaY * -0.0025;
                zoom = Math.min(-1.5, Math.max(-6.0, zoom));
            }});

            document.getElementById("resetBtn").onclick = () => {{
                rotX = -0.75; rotY = 0.45; zoom = -3.2; autoSpin = false;
            }};
            document.getElementById("wireframeBtn").onclick = () => {{
                isWireframe = !isWireframe;
            }};
            const spinBtn = document.getElementById("spinBtn");
            spinBtn.onclick = () => {{
                autoSpin = !autoSpin;
                spinBtn.innerText = autoSpin ? "⏸️ Pause Spin" : "▶️ Resume Spin";
            }};

            function render() {{
                resize();

                if (autoSpin) {{
                    rotY += 0.006;
                }}

                gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

                const aspect = canvas.width / canvas.height;
                const projMat = createPerspective(Math.PI / 4, aspect, 0.1, 100.0);

                let mvMat = translateMatrix(0, 0, zoom);
                mvMat = multiplyMatrix(mvMat, rotateXMatrix(rotX));
                mvMat = multiplyMatrix(mvMat, rotateYMatrix(rotY));

                gl.uniformMatrix4fv(uProjectionMatrix, false, new Float32Array(projMat));
                gl.uniformMatrix4fv(uModelViewMatrix, false, new Float32Array(mvMat));
                gl.uniform3f(uLightDirection, 0.5, 0.8, 1.2);

                const mode = isWireframe ? gl.LINES : gl.TRIANGLES;
                gl.drawElements(mode, rawIndices.length, gl.UNSIGNED_SHORT, 0);

                requestAnimationFrame(render);
            }}

            requestAnimationFrame(render);
        </script>
    </body>
    </html>
    """
    return html_code
