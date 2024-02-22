#for other users, remove my sys.path append. lmao 
import sys
#sys.path.append(r'C:\Users\asyas\AppData\Local\Programs\Python\Python311\Lib\site-packages')
import pyglet

#main image generated here 
image = pyglet.resource.image('Typical-traffic-light-system-at-a-four-way-intersection.png')
window = pyglet.window.Window(width = image.width, height=image.height, caption='Traffic Simulation')

#green and yellow light images generated here 
green_light = pyglet.image.load('traffic_light_green.png')
yellow_light = pyglet.image.load('traffic_light_yellow.png')
red_light = pyglet.image.load('traffic_light_red.png')

#pedestrian crossing signals (walking signs) images
pedestrian_green = pyglet.image.load('greenman.png')
pedestrian_red = pyglet.image.load('redman.png')

sprite_west = pyglet.sprite.Sprite(red_light, x= 100, y =125)
sprite_east = pyglet.sprite.Sprite(red_light, x= 285, y =250)
sprite_north = pyglet.sprite.Sprite(green_light, x= 140, y =325)
sprite_north.rotation += 90
sprite_south = pyglet.sprite.Sprite(green_light, x= 285, y =150)
sprite_south.rotation += 90

# Create sprite objects for pedestrian signals
pedestrian_sprite_north = pyglet.sprite.Sprite(pedestrian_red, x=140, y=250)
pedestrian_sprite_north.rotation += 270
pedestrian_sprite_north.scale = 0.2

pedestrian_sprite_south = pyglet.sprite.Sprite(pedestrian_red, x=315, y=150)
pedestrian_sprite_south.rotation += 90
pedestrian_sprite_south.scale = 0.2


pedestrian_sprite_west = pyglet.sprite.Sprite(pedestrian_red, x=130, y=90)
pedestrian_sprite_west.scale = 0.2

pedestrian_sprite_east = pyglet.sprite.Sprite(pedestrian_red, x=285, y=280)
pedestrian_sprite_east.scale = 0.2


#functions for updating the n/s traffic lights 
def ns_green_update(dt):
    print("north-south green")
    path = 'traffic_light_green.png'
    new_image = pyglet.resource.image(path)
    sprite_south.image = new_image
    sprite_north.image = new_image
    path2 = 'traffic_light_red.png'
    new_image2 = pyglet.resource.image(path2)
    sprite_east.image = new_image2
    sprite_west.image = new_image2

    #update_pedestrian_signals('green', 'red')
 
def ns_yellow_update(dt): 
    print("north-south yellow")
    path = 'traffic_light_yellow.png'
    new_image = pyglet.resource.image(path)
    sprite_south.image = new_image
    sprite_north.image = new_image
    path2 = 'traffic_light_red.png'
    new_image2 = pyglet.resource.image(path2)
    sprite_east.image = new_image2
    sprite_west.image = new_image2

def ns_red_update(dt): 
    print("north-south red")
    path = 'traffic_light_red.png'
    new_image = pyglet.resource.image(path)
    sprite_south.image = new_image
    sprite_north.image = new_image
    path2 = 'traffic_light_green.png'
    new_image2 = pyglet.resource.image(path2)
    sprite_east.image = new_image2
    sprite_west.image = new_image2

    # Schedule the yellow state transition for the west and east roads
    pyglet.clock.schedule_once(ew_yellow_update, 1)
    
    #Call pedestrian sign
    #update_pedestrian_signals('red', 'green')


# Update pedestrian signals based on traffic light state
"""
def update_pedestrian_signals(ns_traffic_light_state, ew_traffic_light_state):
    if ns_traffic_light_state == 'green':
        pedestrian_sprite_north.image = pedestrian_red
        pedestrian_sprite_south.image = pedestrian_red
        pedestrian_sprite_west.image = pedestrian_green
        pedestrian_sprite_east.image = pedestrian_green
    else:
        pedestrian_sprite_north.image = pedestrian_green
        pedestrian_sprite_south.image = pedestrian_green
        pedestrian_sprite_west.image = pedestrian_red
        pedestrian_sprite_east.image = pedestrian_red

"""
############# EW functions--not currently being used ###########################
def ew_red_update(dt):
    path2 = 'traffic_light_red.png'
    new_image = pyglet.resource.image(path2)
    sprite_east.image = new_image
    sprite_west.image = new_image
    update_pedestrian_signals('red')

def ew_yellow_update(dt):
    path2 = 'traffic_light_yellow.png'
    new_image = pyglet.resource.image(path2)
    sprite_east.image = new_image
    sprite_west.image = new_image

def ew_green_update(dt):
    path2 = 'traffic_light_green.png'
    new_image2 = pyglet.resource.image(path2)
    sprite_east.image = new_image2
    sprite_west.image = new_image2

    update_pedestrian_signals('red', 'green')


#this part of the code does the interval scheduling for the sprite manipulation 
def update_sequence(dt):
    ns_green_update(dt)
    pyglet.clock.schedule_once(ns_yellow_update, 5)
    pyglet.clock.schedule_once(ns_red_update, 10)
    pyglet.clock.schedule_once(update_sequence, 15)

pyglet.clock.schedule_once(update_sequence, 0)


# Schedule update_pedestrian_signals from ns_green_update and ew_green_update functions
pyglet.clock.schedule_once(ns_green_update, 10)
pyglet.clock.schedule_once(ew_green_update, 10)


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

    sprite_west.draw()
    sprite_east.draw()
    sprite_north.draw()
    sprite_south.draw()
    pedestrian_sprite_north.draw()
    pedestrian_sprite_south.draw()
    pedestrian_sprite_west.draw()
    pedestrian_sprite_east.draw()
    # Draw your simulation here

pyglet.app.run()









