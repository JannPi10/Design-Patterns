import math

class RoundHole:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius



class SquarePeg:
    def __init__(self, width):
        self._width = width

    def get_width(self):
        return self._width



class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg):
        self._square_peg = square_peg

    def get_radius(self):

        return self._square_peg.get_width() * math.sqrt(2) / 2



if __name__ == "__main__":
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    print(hole.fits(rpeg))  

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)

 

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    print(hole.fits(small_sqpeg_adapter))  
    print(hole.fits(large_sqpeg_adapter))  
