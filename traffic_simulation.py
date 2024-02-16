#for other users, remove my sys.path append. lmao 
import sys
sys.path.append(r'C:\Users\asyas\AppData\Local\Programs\Python\Python311\Lib\site-packages')
import pyglet


image = pyglet.resource.image('Typical-traffic-light-system-at-a-four-way-intersection.png')
window = pyglet.window.Window(width = image.width, height=image.height, caption='Traffic Simulation')

green_light = pyglet.image.load('traffic_light_green.png')
#red_light = pyglet.image.load('/resources/traffic_light_yellow.png')
#yellow_light = pyglet.image.load('/resources/traffic_light_red.png')

green_sprite_west = pyglet.sprite.Sprite(green_light, x= 100, y =125)
#green_sprite_west.rotation += 90
green_sprite_east = pyglet.sprite.Sprite(green_light, x= 285, y =250)
green_sprite_north = pyglet.sprite.Sprite(green_light, x= 140, y =325)
green_sprite_north.rotation += 90
green_sprite_south = pyglet.sprite.Sprite(green_light, x= 285, y =150)
green_sprite_south.rotation += 90

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    green_sprite_west.draw()
    green_sprite_east.draw()
    green_sprite_north.draw()
    green_sprite_south.draw()
    # Draw your simulation here

def update(dt):
    # Update simulation state
    pass

def ns_green_update(dt):
    green_sprite.draw()
    pass

# Schedule the update function to be called every 60th of a second
pyglet.clock.schedule_interval(update, 1/60.0)
#pyglet.clock.schedule_interval(ns_green_update, 1/60.0)

pyglet.app.run()









