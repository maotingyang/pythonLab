from fastapi import FastAPI
import threading
import time

app = FastAPI()

class HelloPrinter:
    def __init__(self):
        self.event = threading.Event()
        self.lock = threading.Lock()
        self.delay = 10
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True  # 設定為守護執行緒
        self.thread.start()
        self.last_called = time.time()

    def run(self):
        count = 0
        while True:
            count += 1
            print(f"第{count}次等待")
            self.event.wait()  # 等待事件被設置
            with self.lock:
                elapsed = time.time() - self.last_called
                remaining = self.delay - elapsed
                print("remaining:", remaining)

            if remaining <= 0:
                print("hello")
                with self.lock:
                    self.last_called = time.time()
                self.event.clear()  # 清除事件標誌
            else:
                # self.event.clear()  # 清除事件標誌
                time.sleep(1)

    def hello(self):
        with self.lock:
            self.last_called = time.time()
        self.event.set()  # 設置事件標誌，通知執行緒

hello_printer = HelloPrinter()

@app.get("/hello")
def call_hello():
    hello_printer.hello()
    return {"message": "Timer reset"}

# To run the application, use the command:
# uvicorn script_name:app --reload
# Replace `script_name` with the name of your script file without the .py extension.
