##class Point:
##    def __init__(self, x= 0.0, y = 0.0 ):
##        self.x = x
##        self.y = y
##
##    def __str__(self):
##        return '(' + str(self.x) + ',' + str(self.y) + ')'
##
##    def __add__(self, other):
##        new_x = self.x + other.x
##        new_y = self.y + other.y
##        return Point(new_x, new_y)
##
##    def __mul__(self, other):
##        return self.x * other.x + self.y* other.y
##
##    def __rmul__(self, other):
##        new_x = self.x * other
##        new_y = self.y *other
##        return Point(new_x, new_y)
##        
##    def dist_to_origin(self):
##        return (self.x**2 + self.y**2)**.5
##
##    def dist_to_point(self, other):
##        return ( (self.x - other.x)**2 + (self.y - other.y)**2)**.5
####
##class Line:
##    def __init__(self, pt1=Point(), pt2=Point()):
##        self.pt1 = pt1
##        self.pt2 = pt2
##
##    def __str__(self):
##        return str(self.pt1) + ','+ str(self.pt2)
##
##    def slope(self):
##        dy = self.pt1.y - self.pt2.y
##        dx = self.pt1.x - self.pt2.x
##        try:
##            m = float(dy)/dx
##            return m
##        except ZeroDivisionError:
##            print 'ZeroDivisionError'
##
##
##
##pt1 = Point(3,4)
##print pt1
##dist = pt1.dist_to_origin()
##print dist
##pt2 = Point(4,-2)
##print pt2
##print pt1 + pt2
##print pt1 * pt2  # (3,4) * (4,-2) = 4
##print 3* pt1  # 3 *(3,4) = (9,12)
##line1 = Line(pt1,pt2)
##print line1
##print line1.slope()
##print line1.pt1.dist_to_origin()
##print pt1.dist_to_point(pt2)
### use the Point class to calculate the distance between the two points of line1
##print line1.pt1.dist_to_point(line1.pt2)
##line2 = Line(Point(1,5),Point(4,9))
##print line2.pt1.dist_to_point(line2.pt2)
##
##
##
##from gasp import *
##
##SCREEN_WIDTH = 640
##SCREEN_HEIGHT = 480
##GRID_WIDTH = SCREEN_WIDTH/10 - 1
##GRID_HEIGHT = SCREEN_HEIGHT/10 - 1
##
##
##def place_player():
##    x = random.randint(0, GRID_WIDTH)
##    y = random.randint(0, GRID_HEIGHT)
##    return {'shape': Circle((10*x+5, 10*y+5), 5, filled=True), 'x': x, 'y': y}
##
##
##def move_player(player):
##    update_when('key_pressed')
##    if key_pressed('escape'):
##        return True
##    elif key_pressed('4'):
##        if player['x'] > 0: player['x'] -= 1
##    elif key_pressed('7'):
##        if player['x'] > 0: player['x'] -= 1
##        if player['y'] < GRID_HEIGHT: player['y'] += 1
##    elif key_pressed('8'):
##        if player['y'] < GRID_HEIGHT: player['y'] += 1
##    elif key_pressed('9'):
##        if player['x'] < GRID_WIDTH: player['x'] += 1
##        if player['y'] < GRID_HEIGHT: player['y'] += 1
##    elif key_pressed('6'):
##        if player['x'] < GRID_WIDTH: player['x'] += 1
##    elif key_pressed('3'):
##        if player['x'] < GRID_WIDTH: player['x'] += 1
##        if player['y'] > 0: player['y'] -= 1
##    elif key_pressed('2'):
##        if player['y'] > 0: player['y'] -= 1
##    elif key_pressed('1'):
##        if player['x'] > 0: player['x'] -= 1
##        if player['y'] > 0: player['y'] -= 1
##    else:
##        return False
##
##    move_to(player['shape'], (10*player['x']+5, 10*player['y']+5))
##
##    return False
##
##
##def play_game():
##    begin_graphics(SCREEN_WIDTH, SCREEN_HEIGHT, title="Robots")
##    player = place_player()
##    finished = False
##    while not finished:
##        finished = move_player(player)
##    end_graphics()
##
##
##if __name__ == '__main__':
##    play_game()


