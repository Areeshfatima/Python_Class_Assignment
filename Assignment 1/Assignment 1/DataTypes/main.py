# Data Types:
# Data Type specifies the type of value a variable holds.
# The main data types are:

# 1. Sequence Types: String(str) , List(list) , Tuple(tuple) , Range(range).
# 2. Numeric Types: Integer(int) , Floating-Point(float) and Complex(complex).
# 3. Boolean Type: Boolean(bool).
# 4. Set Types: Set(set) , Frozen Set(frozenset).
# 5. Mapping Type: Dictionary(dict).
# 6. None Type : None(none).
# 7. Binary Types: Bytes(bytes) , Bytearray(bytearray) , MemoryView(memoryview).


# String:str textual form enclosed in quotes

text_greeting: str = 'Learning Python..!!'                #single quotes
city_name: str = "Karachi"                            #double quotes
about_city: str = '''City of Lights'''                # for multi-line string using triple quotes 
special_place: str = """Tomb of Quaid-e-Azam"""       # for multi-line string using triple quotes  

print("I am ", text_greeting , type(text_greeting)) 
print("I am from " , city_name ,type(city_name))
print(city_name , "is also called the" , about_city , type(about_city) )
print("There is also the famous place in Karachi which is the" , special_place , type(special_place) )


# List:list an ordered mutable(changeable) collection

players_name: list = ["Imran Khan" , "Younis Khan" , "Sarfraz Khan" , "Waseem Akram"]
players_name[3] = "Muhammad Amir"        #changing the last element
print(type(players_name),"Great players of Pakistan:" , players_name)

odd_numbers: list = [1 , 3 , 5 , 7 , 9 , 11 ]
print(type(odd_numbers) ,"first six odd numbers:" , odd_numbers)


#Tuple:tuple an ordered immutable(unchangeable) collection

traffic_lights: tuple = ("red" , "yellow" , "green")
# traffic_lights[1] = "black"   #immutable it raise am error
print(type(traffic_lights) , "The three signals of traffic lights:" , traffic_lights)


#Range:range sequence of numbers commonly used in loops
# range(start , stop , step)

numbers: range = range(2 , 20)
print(type(numbers) , numbers)
for i in numbers:
    print(i)

table_of_two: range = range(2,22,2)
print(type(table_of_two))
for i in table_of_two:
    print(i)



#Integer:int  whole numbers , positive or negative numbers not decimal

age: int = 21
print(type(age) , "given age is:" , age)


#Floating-Point:float numbers with decimal

zakat_rate: float = 2.5
print(type(zakat_rate) , "Zakat Rate:" , zakat_rate)

pi: float = 3.14
print(type(pi) , pi)

gravity: float = 9.81
print(type(gravity) , gravity)

#Complex:complex numbers with real and imaginary parts

num1: complex = 6 + 9j
num2: complex = 9 + 6j
sum_num: complex = num1 + num2
diff: complex = num1 - num2
multi: complex = num1 * num2
print(type(sum_num) , "Sum of the num1 + num2 =" , sum_num)
print(type(diff) , "Difference of the num1 - num2 =" , diff)
print(type(multi) , "Multiply of the num1 * num2 =" , multi)


# Boolean:bool represents True or False

is_passed: bool = True
print(type(is_passed), is_passed)

is_logged_in: bool = False
print(type(is_logged_in) , is_logged_in)


#Set:set an unordered , mutable(changeable) and contains unique elements

even_numbers: set = {2 , 4 , 6 , 8 ,8 , 10}    
even_numbers.add(12)   
print(type(even_numbers) , even_numbers)     #output will be {2 , 4 , 6 , 8 , 10 , 12},because it contains unique values


# Frozen Set:frozenset immutable version of set , unordered and unique elements

frozen_num = frozenset([24 , 6 , 45 , 8 , 8 , 10])
# frozen_num.add(4)   #throws an AttributeError because it is immutable but unique
print(type(frozen_num) , frozen_num)


#Dictionary:dict stores key:value pairs also immutable types

student_info: dict = {"name" : "Arisha", "age" : 22, "learning" : "Python" }
print(type(student_info) , student_info)


#None:none represents the absence of a value

value = None
print(type(value), value)


#Bytes:bytes immutable sequence of bytes , in range(0 , 255)

x = [10 , 20 , 30 , 40 , 50]   #list
y: bytes = bytes(x)    #list to bytes
print(type(x) , x[4])   #list type
print(type(y) , y[0])
print(type(y) , y[3])
print(type(y) , y[-3])

greeting: bytes = b"Hello"   #Literal syntax
print(type(greeting) , greeting)


#Bytearray:bytearray mutable sequence of bytes difference is we can modify the elements

m = [60, 70, 80, 90, 100]
n: bytearray = bytearray(m)     #convert list to bytearray
print(type(n) , n[2])
print(type(n) , n[-1])

#modify 3rd index value 
n[3] = 200
print(type(n), n)



#Memory View:memoryview



ramdan_vibes: memoryview = memoryview(b"Suhoor , Iftar , Taraweeh , Tahajjud , Quran Recitation")
print(type(ramdan_vibes), "Ramdan Vibes" ,ramdan_vibes)
print(bytes(ramdan_vibes[0:25]))
print(ramdan_vibes[26:30])      #if we don't caste it bytes it will show memory address











 






    