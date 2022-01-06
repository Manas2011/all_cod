import pygame
#setting up the display of pygame .We are asking our pygame to create a display and set it to 1200x400 resolutino in screen
window = pygame.display.set_mode((1200, 400))
#Loading the image of track.
track = pygame.image.load('track6.png')
#Loading the image of our car
car = pygame.image.load('tesla.png')
#Here we are asking pygame to do some transformations i.e. change the scale of our car(dimentions) 
car = pygame.transform.scale(car, (30, 60))
#now we are defining initial position of our car in our cordinate plane i.e. 155,300 to bring ore car exactly on track
car_x = 155
car_y = 300
focal_dis = 25
#now we are creating a
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
#we are creating a clock that controlls the speed of our loop
clock = pygame.time.Clock()
while drive:

    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 20
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2
    window.blit(track, (0, 0))  # block image transfer here 0,0 is the x,y cordinate starting from top right corner
    window.blit(car, (car_x, car_y))
    #this is our imegnery camera 
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
