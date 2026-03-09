# Classes


class Cookie:
    def __init__(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour


cookie_one = Cookie("Green")
cookie_two = Cookie("Blue")

print("Cookie one is ", cookie_one.get_colour())
print("Cookie two is ", cookie_two.get_colour())

cookie_one.set_colour("Yellow")

print("\nCookie one is now ", cookie_one.get_colour())
print("Cookie two is still ", cookie_two.get_colour())
