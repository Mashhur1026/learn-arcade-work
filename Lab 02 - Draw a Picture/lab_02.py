import arcade

# Open the window
arcade.open_window(800, 600, "Different Picture Example")

# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)

# Get ready to draw
arcade.start_render()

arcade.draw_rectangle_filled(700, 500, 500, 500, arcade.color.DARK_BLUE)

arcade.draw_rectangle_filled(500, 470, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(510, 480, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(530, 520, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(550, 490, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(570, 460, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(540, 500, 5, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(550, 480, 5, 5, arcade.color.WHITE)

# Draw the moon
arcade.draw_circle_filled(700, 500, 80, (255, 255, 224))  # RGB for Pale Yellow

# Draw the mountains
arcade.draw_triangle_filled(-6000, 100, 800, 400, 900, 0, arcade.color.DARK_GREEN)

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

# Draw a house
arcade.draw_rectangle_filled(400, 230, 200, 200, arcade.color.BROWN)
arcade.draw_triangle_filled(300, 330, 500, 330, 400, 480, arcade.color.RED)

# Man
arcade.draw_circle_filled(700, 150, 20, (0, 0, 0))
arcade.draw_rectangle_filled(700, 105, 15, 70, (0, 0, 0))
arcade.draw_rectangle_filled(720, 125, 40, 7, (0, 0, 0))
arcade.draw_rectangle_filled(680, 125, 40, 7, (0, 0, 0))

# Draw the sun
arcade.draw_arc_filled(100, 370, 150, 150, arcade.color.YELLOW, 0, 180)

# Draw a tree
arcade.draw_rectangle_filled(600, 100, 20, 100, arcade.color.BROWN)
arcade.draw_circle_filled(600, 150, 40, arcade.color.DARK_GREEN)

# Draw a tree
arcade.draw_rectangle_filled(100, 100, 20, 100, arcade.color.BROWN)
arcade.draw_circle_filled(100, 150, 40, arcade.color.DARK_GREEN)

# Draw a tree
arcade.draw_rectangle_filled(150, 100, 20, 100, arcade.color.BROWN)
arcade.draw_circle_filled(150, 150, 40, arcade.color.DARK_GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()