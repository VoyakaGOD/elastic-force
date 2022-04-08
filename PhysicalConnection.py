from PhysicalBody import *

class PhysicalConnection:
    def __init__(self, firstBody, secondBody, rigidity):
        self.firstBody = firstBody
        self.secondBody = secondBody
        self.length = (firstBody.position - secondBody.position).length()
        self.rigidity = rigidity

    def Update(self, dt):
        delta = self.secondBody.position - self.firstBody.position
        force = delta.normalize() * (delta.length() - self.length) * self.rigidity
        self.firstBody.AddForce(force, dt)
        self.secondBody.AddForce(-force, dt)

    def Draw(self, screen):
        pg.draw.line(screen, OBJECT_COLOR, WorldToScreen(self.firstBody.position), WorldToScreen(self.secondBody.position), PHYSICAL_CONNECTION_WIDTH)

    def ContainsPoint(self, point):
        halfWidth = 0.5*PHYSICAL_CONNECTION_WIDTH
        p1 = self.firstBody.position
        p2 = self.secondBody.position
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        numerator = dy*point.x - dx*point.y + p2.x*p1.y - p1.x*p2.y
        if numerator*numerator / (dx*dx + dy*dy) < halfWidth*halfWidth:
            return ((min(p1.x,p2.x) - halfWidth) < point.x) and ((max(p1.x,p2.x) + halfWidth) > point.x) and ((min(p1.y,p2.y) - halfWidth) < point.y) and ((max(p1.y,p2.y) + halfWidth) > point.y)
        return False

    def DependsOn(self, body):
        return (self.firstBody == body) or (self.secondBody == body)

    def __eq__(self, other):
        if not isinstance(other, PhysicalConnection):
            return False
        return ((self.firstBody == other.firstBody) and (self.secondBody == other.secondBody)) or ((self.firstBody == other.secondBody) and (self.secondBody == other.firstBody))
