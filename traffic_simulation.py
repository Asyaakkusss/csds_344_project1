import pyglet


image = pyglet.resource.image('Typical-traffic-light-system-at-a-four-way-intersection.png')
window = pyglet.window.Window(width = image.width, height=image.height, caption='Traffic Simulation')

green_light = pyglet.image.load('../resources/traffic_light_green.png')
#red_light = pyglet.image.load('/resources/traffic_light_yellow.png')
#yellow_light = pyglet.image.load('/resources/traffic_light_red.png')

green_sprite = pyglet.sprite.Sprite(green_light, x= 100, y =100)

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
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









