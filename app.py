class People:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    def name_is(self):
        return "{} {}".format(self.first_name, self.second_name)

mihai = People("Mihai", "Blebea")
print(mihai.name_is())
