import time

class CircuitBreaker:
    def __init__(self):
        self.failures = 0
        self.open = False

    def call(self, func):
        if self.open:
            return "Service unavailable"

        try:
            result = func()
            self.failures = 0
            return result
        except:
            self.failures += 1

            if self.failures >= 3:
                self.open = True

            return "Error"

def unstable_service():
    raise Exception("API down")

cb = CircuitBreaker()

for i in range(5):
    print(cb.call(unstable_service))
