class Garden:
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)
        self.plants_dict = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}

    def plants(self, name):
        index = self.students.index(name) * 2

        return [self.plants_dict[letter] for letter in (self.diagram[0][index:index+2] + self.diagram[1][index:index+2])]