#!/usr/bin/env python3
import pygame
import numpy as np
import math
import time

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

def render_scroller(surface, t, text):
    screen_h = SCREEN_H
    screen_w = SCREEN_W
    scale = 6.0  # Increased from 4.0 for 'Fat Text'
    base_y = screen_h - 120.0
    speed = 250.0
    
    length = len(text)
    char_width = 8.0 * scale
    total_width = length * char_width
    offset = screen_w - (t * speed % total_width)

    # Collect all rects before drawing so the shadow stays strictly in the background
    shadow_rects = []
    text_passes = [] 

    for row in range(8):
        # Amiga Copper Bar effect
        phase = row * 0.4 - t * 4.0
        cr = int((math.sin(phase + 0.0) + 1.0) * 127.5)
        cg = int((math.sin(phase + 2.0) + 1.0) * 127.5)
        cb = int((math.sin(phase + 4.0) + 1.0) * 127.5)
        color = (cr, cg, cb)
        
        row_rects = []
        for i in range(length * 2):
            char = text[i % length]
            c = ord(char.upper()) if 'a' <= char <= 'z' else ord(char)
            if c < 32 or c > 95: c = 32
            
            glyph_row = font8x8[c - 32][row]
            for col in range(8):
                if glyph_row & (1 << (7 - col)):
                    px = offset + (i * char_width) + (col * scale)
                    
                    # Slightly wider culling to prevent the wobbling shadow from popping in
                    if -scale - 20 < px < screen_w + 20: 
                        # Base wave for the main text
                        py = base_y + math.sin(px * 0.005 + t * 4.0) * 45.0 + (row * scale)
                        
                        # --- WATER DROP-SHADOW MATH ---
                        # Offset by 12px, then add high-frequency sine ripples dependent 
                        # on time and screen position to simulate underwater refraction
                        water_x = px + 12.0 + math.sin(py * 0.15 + t * 6.0) * 8.0
                        water_y = py + 12.0 + math.cos(px * 0.10 + t * 4.0) * 8.0
                        
                        shadow_rects.append(pygame.Rect(int(water_x), int(water_y), int(scale), int(scale)))
                        row_rects.append(pygame.Rect(int(px), int(py), int(scale), int(scale)))
        
        if row_rects:
            text_passes.append((color, row_rects))

    # --- SCROLLING TEXT w/WATER DROP-SHADOW --
    # 1. Draw the watery drop-shadow pass first (Deep Liquid Cyan/Blue)
    shadow_color = (15, 30, 60)
    for rect in shadow_rects:
        surface.fill(shadow_color, rect)

    # 2. Draw the main foreground text with Copper shading on top
    for color, rects in text_passes:
        for rect in rects:
            surface.fill(color, rect)

def main():
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Python Demoscene: Infinite 3D Floor")
    
    try:
        pygame.mixer.music.load("A.Cambian.Bitdream.mp3")
        pygame.mixer.music.play(-1) 
    except pygame.error as e:
        print(f"Warning: Could not load A.Cambian.Bitdream.mp3 - {e}")

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

        # 2. Generate the XOR Texture Pattern (Classic Amiga Floor style)
        u_int = u.astype(np.int32) >> 5
        v_int = v.astype(np.int32) >> 5
        tex_val = (u_int ^ v_int) & 1

        # 3. Colors (Neon Blue & Magenta grid)
        floor_r = np.where(tex_val, 0, 180).astype(np.uint8)
        floor_g = np.where(tex_val, 150, 0).astype(np.uint8)
        floor_b = np.where(tex_val, 255, 100).astype(np.uint8)

        # 4. Depth Shading (Fade to black at the horizon)
        # Y goes from 1 (horizon) to 300 (bottom).
        shade = np.clip(Y / (SCREEN_H // 2), 0.0, 1.0)
        floor_r = (floor_r * shade).astype(np.uint8)
        floor_g = (floor_g * shade).astype(np.uint8)
        floor_b = (floor_b * shade).astype(np.uint8)

        # 5. Write to Pygame Surface
        pixels3d = pygame.surfarray.pixels3d(screen)
        
        # Clear top half (sky) to pure black
        pixels3d[:, :SCREEN_H//2, :] = 0
        
        # Draw floor on the bottom half
        pixels3d[:, SCREEN_H//2:, 0] = floor_r
        pixels3d[:, SCREEN_H//2:, 1] = floor_g
        pixels3d[:, SCREEN_H//2:, 2] = floor_b
        
        del pixels3d # Must delete the lock to allow blitting on top!

        # --- ROTOZOOMER ---
        angle_deg = math.degrees(t * 1.5) 
        zoom = 1.0 + math.sin(t * 2.0) * 0.4
        
        rotated_badge = pygame.transform.rotozoom(badge, -angle_deg, zoom)
        
        center_x = (SCREEN_W / 2) + int(math.sin(t * 1.5) * 150.0)
        
        # Make the badge hover dynamically over the horizon line
        center_y = (SCREEN_H / 2) - 50 + int(math.sin(t * 2.2) * 80.0)
        
        rect = rotated_badge.get_rect(center=(center_x, center_y))
        screen.blit(rotated_badge, rect)

        # 6. Amiga Sine Wave Scroller (Two-pass with water drop shadow)
        render_scroller(screen, t, msg)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()