import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os   #despues borrar
import time #despues borrar 
############################################################## 

Symbols = ["1","2","3","/","4","5","6","X","7","8","9","+","C","0","=","-"]
operators = ["X","+","-","/"]
pressedd=[]
numeros = []
nums = ""
result = 0
x = 0 
class My_Grid(GridLayout):
    def __init__(self,**kwargs):
        super(My_Grid,self).__init__(**kwargs)
        self.top_grid = GridLayout()
        main_layout= BoxLayout(orientation="vertical")
        self.solution=TextInput(background_color="black",
            foreground_color="white",multiline=False,halign="right",
            font_size=50,readonly=False,size_hint_y = None,height=175
            )
        self.add_widget(self.solution)   
        self.add_widget(self.top_grid)
        self.top_grid.cols = 4

        self.cols = 1
        
        for i in Symbols:
            self.i = Button(text=i,font_size = 30,)
            self.top_grid.add_widget(self.i)
            self.i.bind(on_press = self.on_button_press)      
    def on_button_press(self,instance):   
        global pressedd
        global numeros
        global nums 
        global result
        global x 
        current = self.solution.text
        button_text = instance.text
        if button_text !="C" and button_text!= "=" and button_text not in operators:
            pressedd.append(button_text)
            self.solution.text = current + button_text
        elif button_text == "C":
            pressedd = []
            numeros  = []
            nums = ""
            self.solution.text=""
            result = 0
            x = 0
        elif button_text in operators:
            self.solution.text= ""
            pressedd.append(button_text)
        elif button_text == "=": 
            if x == 0 : 
                nums = ""
                for i in pressedd:
                    if i not in operators:
                        nums = nums+"".join(str(i))
                        
                    elif i in operators:
                        operator = i
                        numeros.append(nums) 
                        nums = ""
                pressedd = []  
                nums = int(nums)
                numeros.append(nums)
                match operator:
                    case  "+":
                        result = result +(int(numeros[0]) + int(numeros[1]))
                        self.solution.text= str(result)
                    case  "-":
                        result = result +(int(numeros[0]) - int(numeros[1]))
                        self.solution.text= str(result)
                    case "X":
                        result = result +(int(numeros[0]) * int(numeros[1]))   
                        self.solution.text= str(result)
                    case "/":
                        result = result +(int(numeros[0]) / int(numeros[1]))
                        self.solution.text= str(result)       
                x = 1
                pressedd = []
            elif x == 1: 
                nums = ""
                for i in pressedd:
                    if i not in operators:
                        nums = nums+"".join(str(i))
                        
                    elif i in operators:
                        operator = i
                pressedd = []
                match operator:
                    case "+":
                        result = result + int(nums)
                        self.solution.text= str(result)  
                    case "-":
                        result = result - int(nums)
                        self.solution.text= str(result) 
                    case "X":
                        result = result * int(nums)
                        self.solution.text= str(result) 
                    case "/":
                        result = result / int(nums)
                        self.solution.text= str(result) 
        os.system("cls")  
        print ("el resultyado es:",result)
        print("lista de numeros presionados",(pressedd))
        print("el boton precionado:",button_text)
        print("lista de numeros para operar:", (numeros))
###############################################################
class Polynomial_Calculator(App):
    def build(self):
        self.title="Calculator "
        self.icon = "calculadora.png"
        return My_Grid()
###############################################################
if __name__ == "__main__":
    Polynomial_Calculator().run()


