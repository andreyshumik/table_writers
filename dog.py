class Dog:
    def __init__(self, height, weight, name, age, master):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

        self.master = master

    def jump(self):
        print('jump')
    def run(self):
        print('run')
    def bark(self):
        print('bark')
    def change_name(self, new_name):
        self.name = new_name
        print(new_name)

    def get_master(self):
        print(master)


dog1 = Dog(name = 'Tuzik', age = 100, height = 150, weight = 180, master = 'andrey')
dog2 = Dog(name = 'Bobik', age = 15, height = 40, weight = 250, master = 'pavel')
print(dog2.name)
dog2.change_name('sharik')
print(dog2.name)
print(Dog.get_master)
Dog.get_master()