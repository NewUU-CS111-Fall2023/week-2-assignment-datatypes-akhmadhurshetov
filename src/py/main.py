# * Author: Axmad Xurshetov
# * Date: 25.10.2023

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SpawnPrediction:
    def __init__(self):
        self.coordinates = []

    def input_coordinates(self, N):
        for _ in range(N):
            x, y = map(int, input(f"Enter x and y for coordinate {_+1}: ").split())
            self.coordinates.append(Coordinate(x, y))

    def predict_death(self):
        next_x, next_y = map(int, input("Enter next coordinate (x y): ").split())
        next_coord = Coordinate(next_x, next_y)
        
        if 10 <= next_coord.x <= 20 and 10 <= next_coord.y <= 20:
            return "Character died."
        else:
            return "Character survived."

if __name__ == "__main__":
    N = int(input("Enter number of coordinates: "))
    prediction = SpawnPrediction()
    prediction.input_coordinates(N)
    result = prediction.predict_death()
    print(result)
