# infinite-3d-floor-python3

A personal challenge creating yet another demoscene'ish program in `Python3`, showing off classic Amiga demoscene-like "_infinite floor_" graphics effect, scrolling text with water drop-shadow and a bouncing Boing Ball, **On Linux** :P

Made with `Python3` using `PyGame` that implements a perspective checkered moving 3d floor, Rotozoomer, Boing Ball, "Copper" Raster Bars and "Copper" Raster scrolling text with water shimmering effect.

Should work on any Linux distribution that has `Python3` + `PyGame`.

Sound loop provided by [CallRoll](https://archive.org/details/free-chiptune-collection-for-game-usage).

## Required:
```bash
sudo apt-get install python3 python3-pygame python3-numpy
```

Usage:
```bash
$ ./infinite-3d-floor.py -f / --fullscreen /  -w 1280 -h 720 / --width 1280 --height 720
```

#### How:
- **Perspective Floor**: map the 2D screen pixels of the bottom half of the screen into 3D world space using a depth divisor (Distance $Z = \frac{\text{Camera Height}}{Y}$).
- **Rotozoomer Overlay**: A smaller, floating texture (like a logo or text) spinning and scaling smoothly across the screen, rendered directly into the pixel buffer on top of the 3D floor.
- **Boing Ball**: The "Boing Ball" is the ultimate crown jewel of the Amiga demoscene! To do it justice, we won’t just move a flat 2D sprite around. We will use NumPy to calculate a true 3D raycasted sphere with a wrapping checkerboard texture that dynamically rotates and depth-shades itself using volume lighting every single frame.
- **"Copper" Raster Text + Shimmering Water Reflection**: horizontal scrolling "copper" raster text, computing a second set of inverted pixels rendered below the text, then applying high-frequency trigonometry to create a shimmering water effect.
- **"Copper" Raster Bars**: classic Amiga "Copper" raster bar effect, we draw thick, horizontal gradients that sweep up and down the Y-axis using overlapping sine waves.

![infinite-3d-floor](images/infinite-3d-floor.png)
