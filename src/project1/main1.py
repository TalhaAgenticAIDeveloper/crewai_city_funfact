from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = "AIzaSyBADoh8sBZ008t25txcDB0WhYyhcWb4boQ"

class CITY(Flow):
    @start()
    def generate_city_name(self):
        
        result = completion(
            model = "gemini/gemini-1.5-flash",
            api_key= API_KEY,
            messages= [{"content":"Return any random city name from pakistan's kpk province.",
                        "role":"user"}]

        )

        city = result['choices'][0]['message']['content']
        print(city)
        return city # this is to pass result to next function

    @listen(generate_city_name)
    def generate_fun_fact(self, city_name):

        result = completion(
            model = "gemini/gemini-2.0-flash-exp",
            api_key= API_KEY,
            messages= [{"content":f"write a fun fact about {city_name}. The city of Pakistan.",
                        "role":"user"}]

        )

        fun_fact = result['choices'][0]['message']['content']
        print(fun_fact)
        # return fun_fact
        self.state["fun_fact"] = fun_fact # this is another way to pass value to next function
        # with this "self.state" method value will be accessed to any upcoming functions
        # with return method only very next function can access this value

    @listen(generate_fun_fact)
    def save_fun_fact(self,hello2):
        
        with open("fun_fact.md", "w") as file:
            file.write(self.state["fun_fact"])
            # file.write(hello2)
            return self.state["fun_fact"]
            # return hello2


def kickoff():
    obj = CITY()
    result = obj.kickoff()

    print(result)
    