from fastapi import FastAPI
import asyncio

app = FastAPI()

class HelloPrinter:
    def __init__(self):
        self.delay = 10
        self.last_called = None
        self.task = None

    async def run(self):
        while True:
            await asyncio.sleep(self.delay)
            now = asyncio.get_event_loop().time()
            if self.last_called and now - self.last_called >= self.delay:
                print("hello")
                self.last_called = None

    async def hello(self):
        self.last_called = asyncio.get_event_loop().time()
        if self.task is None or self.task.done():
            self.task = asyncio.create_task(self.run())

hello_printer = HelloPrinter()

@app.get("/hello")
async def call_hello():
    await hello_printer.hello()
    return {"message": "Timer reset"}

# To run the application, use the command:
# uvicorn script_name:app --reload
# Replace `script_name` with the name of your script file without the .py extension.
