#!/usr/bin/env python3
import pygame
import numpy as np
import math
import time
import argparse
import sys

SCREEN_W = 1280
SCREEN_H = 720
TEX_SIZE = 256

# Compact 8x8 ASCII Font (Characters 32 to 95)
font8x8 = [
    [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00], [0x18,0x3c,0x3c,0x18,0x18,0x00,0x18,0x00], [0x6c,0x6c,0x6c,0x00,0x00,0x00,0x00,0x00], [0x6c,0x6c,0xfe,0x6c,0xfe,0x6c,0x6c,0x00],
    [0x18,0x3e,0x60,0x3c,0x06,0x7c,0x18,0x00], [0x00,0xc6,0xcc,0x18,0x30,0x66,0xc6,0x00], [0x38,0x6c,0x6c,0x38,0x6d,0x66,0x3b,0x00], [0x18,0x18,0x18,0x00,0x00,0x00,0x00,0x00],
    [0x0c,0x18,0x30,0x30,0x30,0x18,0x0c,0x00], [0x30,0x18,0x0c,0x0c,0x0c,0x18,0x30,0x00], [0x00,0x66,0x3c,0xff,0x3c,0x66,0x00,0x00], [0x00,0x18,0x18,0x7e,0x18,0x18,0x00,0x00],
    [0x00,0x00,0x00,0x00,0x00,0x18,0x18,0x30], [0x00,0x00,0x00,0x7e,0x00,0x00,0x00,0x00], [0x00,0x00,0x00,0x00,0x00,0x18,0x18,0x00], [0x06,0x0c,0x18,0x30,0x60,0xc0,0x80,0x00],
    [0x3c,0x66,0x6e,0x76,0x66,0x66,0x3c,0x00], [0x18,0x38,0x58,0x18,0x18,0x18,0x7e,0x00], [0x3c,0x66,0x06,0x0c,0x30,0x60,0x7e,0x00], [0x3c,0x66,0x06,0x1c,0x06,0x66,0x3c,0x00],
    [0x0c,0x1c,0x3c,0x6c,0x7e,0x0c,0x0c,0x00], [0x7e,0x60,0x7c,0x06,0x06,0x66,0x3c,0x00], [0x3c,0x66,0x60,0x7c,0x66,0x66,0x3c,0x00], [0x7e,0x06,0x0c,0x18,0x30,0x30,0x30,0x00],
    [0x3c,0x66,0x66,0x3c,0x66,0x66,0x3c,0x00], [0x3c,0x66,0x66,0x3e,0x06,0x66,0x3c,0x00], [0x00,0x18,0x18,0x00,0x00,0x18,0x18,0x00], [0x00,0x18,0x18,0x00,0x00,0x18,0x18,0x30],
    [0x06,0x0c,0x18,0x30,0x18,0x0c,0x06,0x00], [0x00,0x00,0x7e,0x00,0x7e,0x00,0x00,0x00], [0x60,0x30,0x18,0x0c,0x18,0x30,0x60,0x00], [0x3c,0x66,0x06,0x0c,0x18,0x00,0x18,0x00],
    [0x3c,0x66,0x6e,0x6e,0x60,0x66,0x3c,0x00], [0x18,0x3c,0x66,0x66,0x7e,0x66,0x66,0x00], [0x7c,0x66,0x66,0x7c,0x66,0x66,0x7c,0x00], [0x3c,0x66,0x60,0x60,0x60,0x66,0x3c,0x00],
    [0x78,0x6c,0x66,0x66,0x66,0x6c,0x78,0x00], [0x7e,0x60,0x60,0x7c,0x60,0x60,0x7e,0x00], [0x7e,0x60,0x60,0x7c,0x60,0x60,0x60,0x00], [0x3c,0x66,0x60,0x6e,0x66,0x66,0x3e,0x00],
    [0x66,0x66,0x66,0x7e,0x66,0x66,0x66,0x00], [0x3c,0x18,0x18,0x18,0x18,0x18,0x3c,0x00], [0x06,0x06,0x06,0x06,0x06,0x66,0x3c,0x00], [0x66,0x6c,0x78,0x70,0x78,0x6c,0x66,0x00],
    [0x60,0x60,0x60,0x60,0x60,0x60,0x7e,0x00], [0x63,0x77,0x7f,0x6b,0x63,0x63,0x63,0x00], [0x66,0x76,0x7e,0x7e,0x6e,0x66,0x66,0x00], [0x3c,0x66,0x66,0x66,0x66,0x66,0x3c,0x00],
    [0x7c,0x66,0x66,0x7c,0x60,0x60,0x60,0x00], [0x3c,0x66,0x66,0x66,0x6a,0x6c,0x36,0x00], [0x7c,0x66,0x66,0x7c,0x6c,0x66,0x66,0x00], [0x3c,0x66,0x60,0x3c,0x06,0x66,0x3c,0x00],
    [0x7e,0x18,0x18,0x18,0x18,0x18,0x18,0x00], [0x66,0x66,0x66,0x66,0x66,0x66,0x3c,0x00], [0x66,0x66,0x66,0x66,0x66,0x3c,0x18,0x00], [0x63,0x63,0x63,0x6b,0x7f,0x77,0x63,0x00],
    [0x66,0x66,0x3c,0x18,0x3c,0x66,0x66,0x00], [0x66,0x66,0x66,0x3c,0x18,0x18,0x18,0x00], [0x7e,0x06,0x0c,0x18,0x30,0x60,0x7e,0x00], [0x3c,0x30,0x30,0x30,0x30,0x30,0x3c,0x00],
    [0x60,0x30,0x18,0x0c,0x06,0x03,0x01,0x00], [0x3c,0x0c,0x0c,0x0c,0x0c,0x0c,0x3c,0x00], [0x00,0x00,0x3c,0x66,0x00,0x00,0x00,0x00], [0x00,0x00,0x00,0x00,0x00,0x00,0xff,0x00]
]

def draw_text_to_surface(surface, text, x, y, scale, color):
    """Burns the 8x8 bitmap font into a Pygame surface."""
    for i, char in enumerate(text):
        c = ord(char.upper()) if 'a' <= char <= 'z' else ord(char)
        c = 32 if c < 32 or c > 95 else c
        for row in range(8):
            glyph = font8x8[c - 32][row]
            for col in range(8):
                if glyph & (1 << (7 - col)):
                    pygame.draw.rect(surface, color, (x + (i*8 + col)*scale, y + row*scale, scale, scale))

def generate_roto_badge():
    """Generates the simple glassy checkerboard badge."""
    badge = pygame.Surface((TEX_SIZE, TEX_SIZE), pygame.SRCALPHA)
    
    X, Y = np.mgrid[-128:128, -128:128]
    dist_sq = X**2 + Y**2

    check = (((X + 128) >> 4) ^ ((Y + 128) >> 4)) & 1
    cr = np.where(check, 0x99, 0x33).astype(np.uint8)
    cg = np.where(check, 0x00, 0x00).astype(np.uint8)
    cb = np.where(check, 0x33, 0x11).astype(np.uint8)

    alpha = np.zeros_like(X, dtype=np.uint8)
    alpha[dist_sq <= 120**2] = 255

    pygame.surfarray.pixels_alpha(badge)[:] = alpha
    pixels3d = pygame.surfarray.pixels3d(badge)
    pixels3d[:, :, 0] = cr
    pixels3d[:, :, 1] = cg
    pixels3d[:, :, 2] = cb
    del pixels3d 

    text = "k ! M"
    scale = 3
    tx = (TEX_SIZE - (len(text) * 8 * scale)) // 2
    ty = (TEX_SIZE - (8 * scale)) // 2
    draw_text_to_surface(badge, text, tx+3, ty+3, scale, (0, 0, 0, 255))
    draw_text_to_surface(badge, text, tx, ty, scale, (0, 255, 255, 255))
    
    return badge

def render_boing_ball(t):
    """Generates a true 3D rotating Amiga Boing Ball using NumPy raycasting."""
    R = 50  # Radius of the ball
    size = R * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # 2D Grid
    X, Y = np.mgrid[-R:R, -R:R]
    r_sq = X**2 + Y**2
    mask = r_sq <= R**2
    
    # Calculate 3D Z-depth for the sphere (clip to prevent math domain errors)
    Z = np.sqrt(np.clip(R**2 - r_sq, 0, None))
    
    # Calculate spherical UV coordinates for texture wrapping
    U = np.arctan2(X, Z) 
    V = np.arcsin(Y / R)
    
    # Rotate the ball continuously over time
    rot_u = t * 2.5
    rot_v = math.sin(t * 1.5) * 0.5 
    
    # Generate the checkerboard pattern on the 3D surface
    tiles = 3.5
    check = (np.floor((U + rot_u) * tiles) + np.floor((V + rot_v) * tiles)) % 2
    
    # Colors: Amiga Red and Silver/Grey
    cr = np.where(check, 255, 190).astype(np.uint8)
    cg = np.where(check, 30, 190).astype(np.uint8)
    cb = np.where(check, 30, 190).astype(np.uint8)
    
    # Apply 3D volume shading (darker at the edges)
    shade = (Z / R)
    cr = (cr * shade).astype(np.uint8)
    cg = (cg * shade).astype(np.uint8)
    cb = (cb * shade).astype(np.uint8)
    
    alpha = np.zeros_like(X, dtype=np.uint8)
    alpha[mask] = 255
    
    # Push pixels to the Pygame surface
    pygame.surfarray.pixels_alpha(surface)[:] = alpha
    pixels3d = pygame.surfarray.pixels3d(surface)
    pixels3d[:, :, 0] = cr
    pixels3d[:, :, 1] = cg
    pixels3d[:, :, 2] = cb
    del pixels3d 
    
    return surface

def render_scroller(surface, t, text):
    screen_h = SCREEN_H
    screen_w = SCREEN_W
    
    scale = 8.0  # Increased for a bigger 'Fat Text' font
    base_y = screen_h - 180.0  # Moved up slightly to leave room for the reflection beneath it
    speed = 240.0  # Slowed down for readability
    
    length = len(text)
    char_width = 8.0 * scale
    total_width = length * char_width
    offset = screen_w - (t * speed % total_width)

    main_text_passes = []
    reflection_passes = [] 

    for row in range(8):
        # --- 1. MAIN TEXT (Copper Bar Shading) ---
        phase = row * 0.4 - t * 4.0
        cr = int((math.sin(phase + 0.0) + 1.0) * 127.5)
        cg = int((math.sin(phase + 2.0) + 1.0) * 127.5)
        cb = int((math.sin(phase + 4.0) + 1.0) * 127.5)
        main_color = (cr, cg, cb)
        
        # --- 2. WATER REFLECTION (Deep Cyan fading to black) ---
        # row 7 (bottom of text) becomes the top of the reflection (brightest)
        # row 0 (top of text) becomes the bottom of the reflection (darkest)
        fade = (row + 1) / 8.0 
        ref_color = (int(15 * fade), int(60 * fade), int(120 * fade))
        
        main_row_rects = []
        ref_row_rects = []
        
        for i in range(length * 2):
            char = text[i % length]
            c = ord(char.upper()) if 'a' <= char <= 'z' else ord(char)
            if c < 32 or c > 95: c = 32
            
            glyph_row = font8x8[c - 32][row]
            for col in range(8):
                if glyph_row & (1 << (7 - col)):
                    px = offset + (i * char_width) + (col * scale)
                    
                    # Wider culling check so rippling reflection pixels don't pop-in suddenly
                    if -scale - 40 < px < screen_w + 40: 
                        
                        # --- NORMAL SCROLLING TEXT ---
                        py = base_y + (row * scale)
                        if -scale < px < screen_w:
                            main_row_rects.append(pygame.Rect(int(px), int(py), int(scale), int(scale)))
                        
                        # --- MIRRORED WATER RIPPLES ---
                        reflected_row = 7 - row
                        gap = 4.0 # Small gap between the text and the water surface
                        ref_py_base = base_y + (8 * scale) + gap + (reflected_row * scale)
                        
                        # Ripple intensity increases as the reflection goes deeper
                        ripple_amp_x = (reflected_row + 1) * 3.0
                        ripple_amp_y = (reflected_row + 1) * 1.5
                        
                        # Apply waves based on screen position and time to warp the reflection
                        water_x = px + math.sin(ref_py_base * 0.05 + t * 5.0) * ripple_amp_x
                        water_y = ref_py_base + math.cos(px * 0.05 + t * 4.0) * ripple_amp_y
                        
                        ref_row_rects.append(pygame.Rect(int(water_x), int(water_y), int(scale), int(scale)))
        
        if main_row_rects:
            main_text_passes.append((main_color, main_row_rects))
        if ref_row_rects:
            reflection_passes.append((ref_color, ref_row_rects))

    # --- RENDER PASSES ---
    
    # 1. Draw the water reflection pass first (50% Translucent)
    for color, rects in reflection_passes:
        # Create a single translucent tile for this specific row's reflection color
        # We append 128 (50% opacity) to the RGB color tuple
        ref_tile = pygame.Surface((int(scale), int(scale)), pygame.SRCALPHA)
        ref_tile.fill((color[0], color[1], color[2], 128))
        
        # Use Pygame's hardware-accelerated batch blitting to draw this row instantly
        surface.blits([(ref_tile, rect) for rect in rects])

    # 2. Draw the main foreground text with Copper shading on top
    for color, rects in main_text_passes:
        for rect in rects:
            surface.fill(color, rect)

def main():
    global SCREEN_W, SCREEN_H
    
    # --- COMMAND LINE ARGUMENTS ---
    parser = argparse.ArgumentParser(description="Python Demoscene: Infinite 3D Floor", add_help=False)
    parser.add_argument("-w", type=int, default=1280, help="Screen width")
    parser.add_argument("-h", type=int, default=720, help="Screen height")
    parser.add_argument("-f", "--fullscreen", action="store_true", help="Enable fullscreen")
    parser.add_argument("--help", action="help", help="Show this help message and exit")
    
    args = parser.parse_args()
    SCREEN_W = args.w
    SCREEN_H = args.h
    fullscreen = args.fullscreen

    # --- INITIALIZE PYGAME ---
    pygame.init()
    pygame.mixer.init()
    
    flags = pygame.FULLSCREEN | pygame.SCALED if fullscreen else 0
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), flags)
    pygame.display.set_caption("Python Demoscene: Infinite 3D Floor")
    
    # If fullscreen, dynamically update variables to the actual desktop resolution
    if fullscreen:
        SCREEN_W, SCREEN_H = screen.get_size()
    
    try:
        pygame.mixer.music.load("i3df.mp3")
        pygame.mixer.music.play(-1) 
    except pygame.error as e:
        print(f"Warning: Could not load i3df.mp3 - {e}")

    badge = generate_roto_badge()
    badge.set_alpha(128) 

    clock = pygame.time.Clock()
    start_time = time.time()
    running = True
    msg = " *** AMIGA DEMOSCENE RULES *** THE PIXELS ARE BENDING *** HARDWARE ACCELERATED IN PYTHON AND PYGAME *** DRONING IS LOOPING *** THE FLOOR IS INFINITE *** OUR FATHER *** WHO ART IN SBIN *** INIT IS THY NAME *** THY PID IS 1 *** THY CHILDREN RUN IN USER SPACE *** GIVE US THIS DAY OUR DAILY RAM *** AND FORGIVE US OUR BAD CODE *** AS WE FORGIVE THOSE WHO FORK OUR CODE *** LEAD US NOT INTO SEGMENTATION FAULT *** BUT DELIVER US FROM SIGKILL *** SUDO *** "

    # --- PRE-CALCULATE FLOOR MATRICES ---
    # We only compute math for the bottom half of the screen (Y from 1 to 300)
    # X goes from -400 to 399
    X, Y = np.mgrid[-SCREEN_W//2 : SCREEN_W//2, 1 : SCREEN_H//2 + 1]
    
    # Perspective division: Z gets smaller as Y gets larger (moving towards the bottom of screen)
    camera_height = 8000.0
    Z = camera_height / Y 
    
    # World Coordinates before rotation
    WX = X * Z / 250.0
    WY = Z

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        t = time.time() - start_time

        # --- 3D PERSPECTIVE FLOOR GENERATOR ---
        # 1. Rotate the camera (Yaw) and move forward
        angle = t * 0.4
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        scroll_speed = t * 300.0
        
        # Apply affine rotation and translation to the 3D world coordinates
        u = (WX * cos_a - WY * sin_a) + scroll_speed
        v = (WX * sin_a + WY * cos_a) + scroll_speed

        # Generate the XOR Texture Pattern (Classic Amiga Floor style)
        u_int = u.astype(np.int32) >> 5
        v_int = v.astype(np.int32) >> 5
        tex_val = (u_int ^ v_int) & 1

        # Colors (Neon Blue & Magenta grid)
        floor_r = np.where(tex_val, 0, 180).astype(np.uint8)
        floor_g = np.where(tex_val, 150, 0).astype(np.uint8)
        floor_b = np.where(tex_val, 255, 100).astype(np.uint8)

        # Depth Shading (Fade to black at the horizon)
        # Y goes from 1 (horizon) to 300 (bottom).
        shade = np.clip(Y / (SCREEN_H // 2), 0.0, 1.0)
        floor_r = (floor_r * shade).astype(np.uint8)
        floor_g = (floor_g * shade).astype(np.uint8)
        floor_b = (floor_b * shade).astype(np.uint8)

        # Write to Pygame Surface
        pixels3d = pygame.surfarray.pixels3d(screen)
        
        # Clear top half (sky) to pure black
        pixels3d[:, :SCREEN_H//2, :] = 0
        
        # Draw floor on the bottom half
        pixels3d[:, SCREEN_H//2:, 0] = floor_r
        pixels3d[:, SCREEN_H//2:, 1] = floor_g
        pixels3d[:, SCREEN_H//2:, 2] = floor_b
        
        del pixels3d # Must delete the lock to allow blitting on top!

        # --- CLASSIC AMIGA RASTER BARS (COPPER BARS) ---
        sky_h = SCREEN_H // 2
        
        # Create 3 independent chasing bars
        for i in range(3):  
            # Oscillate the center of each bar up and down the sky
            bar_center = (sky_h // 2) + math.sin(t * 1.5 + i * 2.0) * (sky_h * 0.4)
            bar_thickness = 30
            
            # Draw the bar using horizontal 2-pixel high strips to create a smooth gradient
            for line in range(-bar_thickness, bar_thickness, 2):
                y_pos = int(bar_center + line)
                
                # Clip the rendering so the bars never overlap the 3D floor
                if 0 <= y_pos < sky_h:
                    # The center of the bar is brightest (1.0), fading to 0.0 at the edges
                    intensity = 1.0 - (abs(line) / bar_thickness)
                    
                    # Cycle colors: 0 = Deep Blue, 1 = Hot Pink, 2 = Cyan
                    if i == 0:
                        r, g, b = 0, int(120 * intensity), int(255 * intensity)
                    elif i == 1:
                        r, g, b = int(255 * intensity), 0, int(180 * intensity)
                    else:
                        r, g, b = 0, int(255 * intensity), int(150 * intensity)
                        
                    # Draw the horizontal raster line across the entire screen
                    pygame.draw.rect(screen, (r, g, b), (0, y_pos, SCREEN_W, 2))

        # --- AMIGA BOING BALL W/ MOTION BLUR ---
        ball_radius = 50
        num_ghosts = 5  # Number of trail echoes
        
        # Draw the floor shadow based on the current actual time (t)
        floor_z = (SCREEN_H // 2) + 120 + math.sin(t * 0.8) * 80.0
        ball_x = (SCREEN_W / 2) + math.sin(t * 1.3) * math.cos(t * 0.7) * (SCREEN_W * 0.4)
        
        shadow_surface = pygame.Surface((120, 60), pygame.SRCALPHA)
        shadow_w = 40 + abs(math.sin(t * 3.5)) * 40
        shadow_h = 15 + abs(math.sin(t * 3.5)) * 15
        shadow_rect = pygame.Rect((120 - shadow_w)//2, (60 - shadow_h)//2, shadow_w, shadow_h)
        shadow_alpha = int(180 - abs(math.sin(t * 3.5)) * 140)
        pygame.draw.ellipse(shadow_surface, (10, 5, 15, shadow_alpha), shadow_rect)
        screen.blit(shadow_surface, (int(ball_x - 60), int(floor_z - 30)))
        
        # Render the motion blur trail (oldest ghost first, newest frame last)
        for i in range(num_ghosts, -1, -1):
            # Go backward in time 0.04 seconds per ghost
            trail_t = t - (i * 0.04) 
            
            # Recalculate physics position for this exact historical millisecond
            t_floor_z = (SCREEN_H // 2) + 120 + math.sin(trail_t * 0.8) * 80.0
            t_ball_x = (SCREEN_W / 2) + math.sin(trail_t * 1.3) * math.cos(trail_t * 0.7) * (SCREEN_W * 0.4)
            t_bounce = 120.0 + math.sin(trail_t * 1.1) * 40.0
            t_ball_y = t_floor_z - abs(math.sin(trail_t * 3.5)) * t_bounce - ball_radius
            
            # Generate the ball at its historical 3D rotation
            boing_surf = render_boing_ball(trail_t)
            
            if i > 0:
                # Fade out older ghosts (255 is solid, 0 is invisible)
                boing_surf.set_alpha(255 - (i * 45))
                
            screen.blit(boing_surf, (int(t_ball_x - ball_radius), int(t_ball_y - ball_radius)))

        # --- ROTOZOOMER ---
        angle_deg = math.degrees(t * 1.5) 
        zoom = 1.0 + math.sin(t * 2.0) * 0.4
        
        rotated_badge = pygame.transform.rotozoom(badge, -angle_deg, zoom)
        
        center_x = (SCREEN_W / 2) + int(math.sin(t * 1.5) * 150.0)
        
        # Make the badge hover dynamically over the horizon line
        center_y = (SCREEN_H / 2) - 50 + int(math.sin(t * 2.2) * 80.0)
        
        rect = rotated_badge.get_rect(center=(center_x, center_y))
        screen.blit(rotated_badge, rect)

        # Amiga Copper Bar Scroller (Two-pass with water ripple shadow)
        render_scroller(screen, t, msg)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()