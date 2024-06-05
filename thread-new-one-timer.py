import threading

class HelloPrinter:
    def __init__(self):
        self.timer = None
        self.delay = 10

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = threading.Timer(self.delay, self.print_hello)
        self.timer.start()

    def print_hello(self):
        print("hello")
        self.timer = None

    def hello(self):
        self.reset_timer()

# Example usage
hello_printer = HelloPrinter()

# Calling the hello method multiple times
hello_printer.hello()
# Wait a few seconds and call again
# The timer will reset each time the hello method is called
