import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

def update(val):
    # Aggiorna il valore del threshold in base allo slider
    threshold_value = int(slider.val)
    
    # Applica il Canny Edge Detection con il nuovo valore di threshold
    edges = cv.Canny(img, threshold_value, 2 * threshold_value)

    # Aggiorna l'immagine con i nuovi bordi
    ax2.imshow(edges, cmap='gray')
    fig.canvas.draw_idle()

img = cv.imread('dambrosio.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# Crea una figura con due subplot
fig, (ax1, ax2) = plt.subplots(1, 2)

# Posiziona i subplot
ax1.set_title('Original Image')
ax1.imshow(img, cmap='gray')
ax1.axis('off')

ax2.set_title('Edge Image')
edges = cv.Canny(img, 100, 200)
edge_plot = ax2.imshow(edges, cmap='gray')
ax2.axis('off')

# Slider
ax_slider = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Threshold', 0, 100, valinit=100, valstep=1)

# Aggiorna immagine
slider.on_changed(update)

plt.show()
