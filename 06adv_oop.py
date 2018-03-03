# @property
class Student(object):
    # class attribute count
    count = 0

    def __init__(self, name, gender):
        self.__name = name
        if gender in ('male', 'female'):
            self.__gender = gender
            Student.count += 1

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('wrong gender type')

    def hit(self, name):
        print('%s hit %s' % (self.__name, name))

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    @property
    def grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        else:
            return 'C'

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = score


bart = Student('Bart', 'male')
simon = Student('Simon', 'male')
simon.score = 100

print(simon.score)
print(bart.gender)
print(simon.grade)


class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('width should be an integer')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError('height should be an integer')
        self.__height = height

    @property
    def resolution(self):
        self.__resolution = self.__height * self.__width
        return self.__resolution


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


Student2('Michael')
print(Student2('Michael'))


class Fib(object):
    """docstring for Fib"""
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)
f = Fib()
print(f[0:5])
print(f[:10])
