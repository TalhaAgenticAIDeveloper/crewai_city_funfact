from crewai.flow.flow import Flow, start, listen
from litellm import completion



class SimpleFlow(Flow):
    
    

    @start()
    def func2(self):
        print("Hello from Func2!")

    @listen(func2)
    def func1(self):
        print("Hello from Func1!")

    @listen(func1)
    def func3(self):
        print("Hello from Func3!")    

def kickoff():
    print("Hello from Talha!")

    obj1 = SimpleFlow()
    obj1.kickoff() # inherited method from Flow