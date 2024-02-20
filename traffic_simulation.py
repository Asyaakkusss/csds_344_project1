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


sprite_west = pyglet.sprite.Sprite(red_light, x= 100, y =125)
sprite_east = pyglet.sprite.Sprite(red_light, x= 285, y =250)
sprite_north = pyglet.sprite.Sprite(green_light, x= 140, y =325)
sprite_north.rotation += 90
sprite_south = pyglet.sprite.Sprite(green_light, x= 285, y =150)
sprite_south.rotation += 90

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


############# EW functions--not currently being used ###########################
def ew_red_update(dt):
    path2 = 'traffic_light_red.png'
    new_image = pyglet.resource.image(path2)
    sprite_east.image = new_image
    sprite_west.image = new_image

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


#this part of the code does the interval scheduling for the sprite manipulation 
def update_sequence(dt):
    ns_green_update(dt)
    pyglet.clock.schedule_once(ns_yellow_update, 5)
    pyglet.clock.schedule_once(ns_red_update, 10)
    pyglet.clock.schedule_once(update_sequence, 15)

    
pyglet.clock.schedule_once(update_sequence, 0)


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









