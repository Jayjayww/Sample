class LABStudent:
    
    def __init__(self, name, age, major):
        self.name = name # Atribuutti 
        self.age = age # Atribuutti
        self.major = major # Atribuutti
   
    def Introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, majoring in {self.major}."
    
    def study(self):
        return f"{self.name} is studying {self.major}."