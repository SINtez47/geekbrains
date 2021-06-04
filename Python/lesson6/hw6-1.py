from time import sleep
from datetime import datetime as dt


class TrafficLight:

    _states = {'red': 7, 'yellow': 2, 'green': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._color}' after" 
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
