import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []

        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        if num > len(self.contents):
            return self.contents

        balls_drawn = []

        for i in range(num):
            rand_choice = random.choice(self.contents)
            balls_drawn.append(rand_choice)
            self.contents.remove(rand_choice)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0

    for i in range(num_experiments):
        # make two copies of our original lists of expected balls and balls in hat
        # we are modifying our args every loop and need to be able to reset back to their original values everytime
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # compare each ball drawn to expected balls, if they exist, remove one from expected balls successful_draws
        for color in balls_drawn:
            if color in expected_balls_copy:
                expected_balls_copy[color] -= 1

        # if all the values in our expected balls list is 0 then we know we drew enough of each ball to be successful
        if all(values <= 0 for values in expected_balls_copy.values()):
            successful_draws += 1

    return successful_draws / num_experiments
