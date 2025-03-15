import pygame, sys, time

def main():
    # Initialize Pygame and its modules
    pygame.init()
    
    # Set up the drawing window
    screen_width, screen_height = 1440, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paint")
    
    """ Create a canvas surface to accumulate drawings.
    We use a separate surface so that temporary previews (for shapes) can be drawn 
    without affecting the finished artwork. """
    canvas = pygame.Surface((screen_width, screen_height))
    canvas = canvas.convert()
    canvas.fill((255, 255, 255))  # Fill canvas with white background
    
    clock = pygame.time.Clock()
    
    # ---------------------------------------------------
    # Initialize Drawing Variables and Default Settings
    # ---------------------------------------------------
    # Current tool options: "pencil", "rectangle", "circle", "eraser",
    # "square", "right_triangle", "equilateral_triangle", "rhombus"
    current_tool = "pencil"
    # Default drawing color (blue)
    current_color = (0, 0, 255)
    # Brush (or pen) thickness; also used as the outline width for shapes
    brush_radius = 15
    # Flags and positions used during drawing
    drawing = False         # True when mouse button is held down
    start_pos = None        # Starting point for shape drawing
    last_pos = None         # Last recorded position for continuous free drawing
    
    # ---------------------------------------------------
    # Main Event Loop
    # ---------------------------------------------------
    while True:
        # Get the current state of all keys (used for detecting held keys if needed)
        pressed_keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            # Handle window close event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # -----------------------------
            # Keyboard Event Handling
            # -----------------------------
            if event.type == pygame.KEYDOWN:
                # Tool Selection via number keys:
                #   1: Pencil, 2: Rectangle, 3: Circle, 4: Eraser,
                #   5: Square, 6: Right Triangle, 7: Equilateral Triangle, 8: Rhombus
                if event.key == pygame.K_1:
                    current_tool = "pencil"
                elif event.key == pygame.K_2:
                    current_tool = "rectangle"
                elif event.key == pygame.K_3:
                    current_tool = "circle"
                elif event.key == pygame.K_4:
                    current_tool = "eraser"
                elif event.key == pygame.K_5:
                    current_tool = "square"
                elif event.key == pygame.K_6:
                    current_tool = "right_triangle"
                elif event.key == pygame.K_7:
                    current_tool = "equilateral_triangle"
                elif event.key == pygame.K_8:
                    current_tool = "rhombus"
                    
                # Color Selection via letter keys:
                #   R for red, G for green, B for blue, Y for yellow,
                #   C for cyan, M for magenta.
                if event.key == pygame.K_r:
                    current_color = (255, 0, 0)    # Red
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)    # Green
                elif event.key == pygame.K_b:
                    current_color = (0, 0, 255)    # Blue
                elif event.key == pygame.K_y:
                    current_color = (255, 255, 0)  # Yellow
                elif event.key == pygame.K_c:
                    current_color = (0, 255, 255)  # Cyan
                elif event.key == pygame.K_m:
                    current_color = (255, 0, 255)  # Magenta
                    
            # -----------------------------
            # Mouse Button Events for Brush Size Adjustment
            # -----------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left click increases brush size; right click decreases it.
                if event.button == 1:
                    brush_radius = min(200, brush_radius + 1)
                elif event.button == 3:
                    brush_radius = max(1, brush_radius - 1)
                    
            # -----------------------------
            # Mouse Events: Start and End Drawing
            # -----------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Begin drawing on left mouse button press
                    drawing = True
                    start_pos = event.pos  # Record the starting point for shapes
                    last_pos = event.pos   # For free drawing, track the last position
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # For shape tools, commit the shape onto the canvas
                    if drawing:
                        end_pos = event.pos
                        x, y = start_pos
                        ex, ey = end_pos
                        # Draw based on the current tool
                        if current_tool == "rectangle":
                            # Calculate rectangle parameters from start and end positions
                            rect = pygame.Rect(min(x, ex), min(y, ey), abs(ex - x), abs(ey - y))
                            pygame.draw.rect(canvas, current_color, rect, brush_radius)
                        elif current_tool == "circle":
                            # Determine radius based on the distance between start and end positions
                            radius_shape = int(((ex - x) ** 2 + (ey - y) ** 2) ** 0.5)
                            pygame.draw.circle(canvas, current_color, start_pos, radius_shape, brush_radius)
                        elif current_tool == "square":
                            # Force a square by taking the minimum side length
                            side = min(abs(ex - x), abs(ey - y))
                            # Determine the top-left corner based on drag direction
                            new_x = x if ex >= x else x - side
                            new_y = y if ey >= y else y - side
                            rect = pygame.Rect(new_x, new_y, side, side)
                            pygame.draw.rect(canvas, current_color, rect, brush_radius)
                        elif current_tool == "right_triangle":
                            # Right triangle with right angle at the starting point
                            points = [start_pos, (x, ey), (ex, y)]
                            pygame.draw.polygon(canvas, current_color, points, brush_radius)
                        elif current_tool == "equilateral_triangle":
                            # Equilateral triangle: use horizontal distance as base
                            side = abs(ex - x)
                            # Determine base start (leftmost) and orientation based on vertical drag
                            if ex >= x:
                                base_start = (x, y)
                            else:
                                base_start = (ex, y)
                            # Decide orientation: upward if end y is less than start y, else downward
                            if ey < y:
                                third_point = (base_start[0] + side // 2, y - int(side * (3 ** 0.5) / 2))
                            else:
                                third_point = (base_start[0] + side // 2, y + int(side * (3 ** 0.5) / 2))
                            points = [base_start, (base_start[0] + side, y), third_point]
                            pygame.draw.polygon(canvas, current_color, points, brush_radius)
                        elif current_tool == "rhombus":
                            # Rhombus drawn by connecting midpoints of the bounding rectangle
                            mid_x = (x + ex) // 2
                            mid_y = (y + ey) // 2
                            points = [(mid_x, y), (ex, mid_y), (mid_x, ey), (x, mid_y)]
                            pygame.draw.polygon(canvas, current_color, points, brush_radius)
                        # For pencil and eraser, drawing is handled continuously during mouse motion.
                    drawing = False
                    start_pos = None
                    last_pos = None
                    
            # -----------------------------
            # Mouse Motion: Free Drawing for Pencil/Eraser
            # -----------------------------
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if current_tool == "pencil":
                        pygame.draw.line(canvas, current_color, last_pos, event.pos, brush_radius)
                        last_pos = event.pos
                    elif current_tool == "eraser":
                        pygame.draw.line(canvas, (255, 255, 255), last_pos, event.pos, brush_radius)
                        last_pos = event.pos

        # -----------------------------------------
        # Preview for Shape Tools (Rectangle/Circle/Square/Triangles/Rhombus)
        # -----------------------------------------
        preview = canvas.copy()
        if drawing and current_tool in ["rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
            current_pos = pygame.mouse.get_pos()
            x, y = start_pos
            ex, ey = current_pos
            if current_tool == "rectangle":
                rect = pygame.Rect(min(x, ex), min(y, ey), abs(ex - x), abs(ey - y))
                pygame.draw.rect(preview, current_color, rect, brush_radius)
            elif current_tool == "circle":
                radius_shape = int(((ex - x) ** 2 + (ey - y) ** 2) ** 0.5)
                pygame.draw.circle(preview, current_color, start_pos, radius_shape, brush_radius)
            elif current_tool == "square":
                side = min(abs(ex - x), abs(ey - y))
                new_x = x if ex >= x else x - side
                new_y = y if ey >= y else y - side
                rect = pygame.Rect(new_x, new_y, side, side)
                pygame.draw.rect(preview, current_color, rect, brush_radius)
            elif current_tool == "right_triangle":
                points = [start_pos, (x, ey), (ex, y)]
                pygame.draw.polygon(preview, current_color, points, brush_radius)
            elif current_tool == "equilateral_triangle":
                side = abs(ex - x)
                if ex >= x:
                    base_start = (x, y)
                else:
                    base_start = (ex, y)
                if ey < y:
                    third_point = (base_start[0] + side // 2, y - int(side * (3 ** 0.5) / 2))
                else:
                    third_point = (base_start[0] + side // 2, y + int(side * (3 ** 0.5) / 2))
                points = [base_start, (base_start[0] + side, y), third_point]
                pygame.draw.polygon(preview, current_color, points, brush_radius)
            elif current_tool == "rhombus":
                mid_x = (x + ex) // 2
                mid_y = (y + ey) // 2
                points = [(mid_x, y), (ex, mid_y), (mid_x, ey), (x, mid_y)]
                pygame.draw.polygon(preview, current_color, points, brush_radius)
        
        # -----------------------------
        # Render the Combined Display
        # -----------------------------
        screen.blit(preview, (0, 0))
        
        # Optionally, display current tool and color information for user reference.
        info_font = pygame.font.SysFont(None, 24)
        tool_text = info_font.render("Tool: " + current_tool, True, (0, 0, 0))
        color_text = info_font.render("Color: " + str(current_color), True, (0, 0, 0))
        screen.blit(tool_text, (10, 10))
        screen.blit(color_text, (10, 30))
        
        pygame.display.flip()
        clock.tick(60)

main()