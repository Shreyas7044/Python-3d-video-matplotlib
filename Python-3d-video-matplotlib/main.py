import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Create output directory
if not os.path.exists("3d"):
    os.makedirs("3d")

# ---- Create 3D Data ---- #
x = np.linspace(-10, 10, 100)
y = np.linspace(-15, 15, 100)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# ---- Generate Rotating Frames ---- #
print("Generating 3D frames...")

for angle in range(0, 360, 2):
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(projection='3d')

    ax._axis3don = False
    
    ax.contour3D(X, Y, Z, 200, cmap='viridis')

    ax.xaxis.set_pane_color((1,1,1,0))
    ax.yaxis.set_pane_color((1,1,1,0))
    ax.zaxis.set_pane_color((1,1,1,0))

    ax.xaxis._axinfo['grid']['color'] = (1,1,1,0)
    ax.yaxis._axinfo['grid']['color'] = (1,1,1,0)
    ax.zaxis._axinfo['grid']['color'] = (1,1,1,0)

    ax.view_init(60, angle)

    filename = f"3d/3d_vis_{angle}.png"
    plt.savefig(filename, dpi=80)
    plt.close()

print("Frames generated successfully!")


# ---- Convert Images to GIF ---- #
print("Creating GIF...")

png_count = 180
files = []

for i in range(png_count):
    seq = str(i * 2)
    file_name = f"3d_vis_{seq}.png"
    files.append(file_name)

frames = []

for file in files:
    img_path = os.path.join("3d", file)
    image = Image.open(img_path)
    frames.append(image)

frames[0].save("3d_video.gif",
               format="GIF",
               append_images=frames[1:],
               save_all=True,
               duration=40,
               loop=0)

print("GIF Created Successfully -> 3d_video.gif")