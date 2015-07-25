class Fillers:
    def __init__(self, sours):
        self.__fillers = []
        self.__strings = []
        self.__source = sours
        self.__read()

    def __read(self):
        with open(self.__source) as file:
            f = str(file.read())
        all_sources = f.split('#!')
        pre_fillers = []
        for a in all_sources:
            if all_sources.index(a) % 2 == 0:
                self.__strings.append(a)
            else:
                pre_fillers.append(a)
        for filler in pre_fillers:
            filler_name = ''
            for l in filler:
                if l != '(' and l != ')':
                    filler_name += l
                if l is ')':
                    break
            self.__fillers.append([filler_name] + filler.replace('(' + filler_name + ')', '').split('|'))
        print(self.__fillers)
        self.__strings[0] = ''.join([self.__strings[0], self.__strings[1][1:]])
        del self.__strings[1]

    def get_settings(self):
        return self.__fillers[0]

    def get_source(self):
        return self.__source

    def get_fillers(self):
        return self.__fillers[1:]

    def get_strings(self):
        return self.__strings

    def create_filler(self, filler):
        if len(filler) > 1:
            self.__fillers.append(filler)