from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
MAX = 360 + SIZE
MIN = 360 - SIZE

# if you make this larger, the game will go slower
DELAY = 0.01 

def handle_key(canvas, snake):
    key = canvas.get_last_key_press()
    if key == 'ArrowLeft':
        print('left arrow pressed!')
        canvas.move(snake, -20, 0)
    if key == 'ArrowRight':
        print('right arrow pressed!')
        canvas.move(snake, 20, 0) 
    if key == 'ArrowUp':
        print('up arrow pressed!')
        canvas.move(snake, 0, -20) 
    if key == 'ArrowDown':
        print('down arrow pressed!')
        canvas.move(snake, 0, 20)
        
def eat(canvas, snake, food, SIZE):
    left_x = canvas.get_left_x(snake)
    top_y = canvas.get_top_y(snake)
    
    if left_x == 360 and top_y == 360:
        canvas.delete(food)
        print('Bite')
        canvas.delete(snake)
        snake = canvas.create_rectangle(left_x, top_y, MAX, MAX+20, 'green')
        while True:
            handle_key(canvas, snake)
    #return blue_rect

        
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    snake = canvas.create_rectangle(20, 20, SIZE+20, SIZE+20, 'green')
    food = canvas.create_rectangle(360, 360, MAX, MAX, 'salmon')
    
    while True:
        handle_key(canvas, snake)
        left_x = canvas.get_left_x(snake)
        top_y = canvas.get_top_y(snake)
        
        if  left_x == 400-SIZE or top_y == 400-SIZE or left_x == 0 or top_y == 0:
            print("GAME OVER")
            break
        
        eat(canvas, snake, food, SIZE)
        time.sleep(DELAY)
        
if __name__ == '__main__':
    main()
