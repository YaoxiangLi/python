# Encapsulation
class Student(object):
    # class attribute: count
    count = 0

    def __init__(self, name, gender):
        self.__name = name
        if gender in ('male', 'female'):
            self.__gender = gender
            Student.count += 1

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('wrong gender type')

    def hit(self, name):
        print('%s hit %s' % (self.__name, name))

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score


bart = Student('Bart', 'male')
simon = Student('Simon', 'male')
print(Student.count)


# Inheritance Polymorphism
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        super().run()
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(x):
    x.run()
    x.run()


class MyDog(object):
    def __len__(self):
        return 100


husky = Dog()
husky.run()
# print(len(husky), husky.__len__())
