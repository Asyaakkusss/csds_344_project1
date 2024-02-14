import pyglet


image = pyglet.resource.image('Typical-traffic-light-system-at-a-four-way-intersection.png')
window = pyglet.window.Window(width = image.width, height=image.height, caption='Traffic Simulation')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    # Draw your simulation here

def update(dt):
    # Update simulation state
    pass

# Schedule the update function to be called every 60th of a second
pyglet.clock.schedule_interval(update, 1/60.0)

pyglet.app.run()









