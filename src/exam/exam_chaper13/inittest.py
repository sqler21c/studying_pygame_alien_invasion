class Sqler:

    def __init__(self, name='날뫼'):
        self.name = name
    
    def print_name(self):
        print(f'내 이름은 {self.name}입니다.')

if __name__ == '__main__':
    sqler = Sqler()
    sqler.print_name()
    