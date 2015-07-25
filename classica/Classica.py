import sys
from classical.Classes import Classes
from classical.Fillers import Fillers


def work(argv):
    fillers = Fillers(argv[0])
    classes = Classes(fillers.get_settings())
    f = open(classes.out_text_source, 'w+')
    f.write(classes.out_text(fillers))
    f.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == ' ':
            pass
        else:
            work(sys.argv[1:])
    else:
        print('Just write path to your file')