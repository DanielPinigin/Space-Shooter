"""
spaceshooter.py
Author: Daniel Pinigin
Credit: Tutorial4.py, Mr. Dennison, Brendan

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        
        self.rotation = 4.712
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keyup", "d", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self):
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
            
        
    def thrustOn(self, event):
        self.thrust = 1
    def wKey(self,event):
        self.y-=5
    def sKey(self,event):
        self.y+=5
    def dKey(self,event):
        self.x+=5
        self.thrust = 1
    def aKey(self,event):
        self.x-=5
    def thrustOff(self, event):
        self.thrust = 0
    
    
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("images/starfield.jpg")
        for x in range(self.width//512 + 1):
            for y in range(self.height//512 + 1):
                Sprite(asset,(x*512, y*512))
        SpaceShip((100,500))
        SpaceShip((100,400))
        SpaceShip((100,600))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()




