class ComplexSystem:

    def __init__(self):
        self.built = False
    def create(self):
        print('create it')

    def decorate(self):
        print('decorate it')

    def destroy(self):
        print('destroy it.')

    def repair(self):
        print('repair it.')

    def rent(self):
        print('give it for rent.')

    def empty(self):
        print('emptry it')

    def paint(self):
        print('paint it')

    def prepare(self):
        print('prepare it')

    def clean(self):
        print('clean it')


class Facade:

    def __init__(self, ):
        self.complex_system = ComplexSystem()

    def build(self):
        self.complex_system.prepare()
        self.complex_system.create()
        self.complex_system.paint()
        self.complex_system.decorate()
        self.complex_system.clean()
        self.complex_system.built = True
        print('it was built.')

    def rebuild(self):
        if self.complex_system.built:
            self.complex_system.empty()
            self.complex_system.prepare()
            self.complex_system.destroy()
            self.complex_system.built = True
        self.build()
        print('it was rebuilt')


if __name__ == '__main__':
    facade = Facade()
    facade.rebuild()
