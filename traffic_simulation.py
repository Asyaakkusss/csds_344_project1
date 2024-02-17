#for other users, remove my sys.path append. lmao 
import sys
sys.path.append(r'C:\Users\asyas\AppData\Local\Programs\Python\Python311\Lib\site-packages')
import pyglet

#main image generated here 
image = pyglet.resource.image('Typical-traffic-light-system-at-a-four-way-intersection.png')
window = pyglet.window.Window(width = image.width, height=image.height, caption='Traffic Simulation')

#green and yellow light images generated here 
green_light = pyglet.image.load('traffic_light_green.png')
yellow_light = pyglet.image.load('traffic_light_yellow.png')
red_light = pyglet.image.load('traffic_light_red.png')


sprite_west = pyglet.sprite.Sprite(green_light, x= 100, y =125)
sprite_east = pyglet.sprite.Sprite(green_light, x= 285, y =250)
sprite_north = pyglet.sprite.Sprite(green_light, x= 140, y =325)
sprite_north.rotation += 90
sprite_south = pyglet.sprite.Sprite(green_light, x= 285, y =150)
sprite_south.rotation += 90


def ns_green_update(dt):
    green_light = True 
    path = 'traffic_light_green.png'
    if green_light:
        path = 'traffic_light_yellow.png'

    new_image = pyglet.resource.image(path)
    sprite_south.image = new_image

def ns_yellow_update(dt): 
    yellow_light = True
    path = 'traffic_light_yellow.png'
    if yellow_light: 
        path = 'traffic_light_red.png'
    new_image = pyglet.resource.image(path)
    sprite_south.image = new_image
    
# Schedule the update function to be called every 60th of a second
pyglet.clock.schedule_interval(ns_green_update, 3)
pyglet.clock.schedule_interval(ns_yellow_update, 3)
#pyglet.clock.schedule_interval(ns_green_update, 1/60.0)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

    sprite_west.draw()
    sprite_east.draw()
    sprite_north.draw()
    sprite_south.draw()
    # Draw your simulation here

pyglet.app.run()









