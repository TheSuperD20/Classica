class Classes:
    def __init__(self, settings):
        self.out_text_source = settings[1]
        self.in_classes = settings[2]
        self.__classes = {}
        self.__read()

    def __read(self):
        with open(self.in_classes) as file:
            f = str(file.read())
        pre_classes = f.split('#!')
        for class_m in pre_classes:
            class_name = ''
            for l in class_m:
                if l is not '(' and l is not ')':
                    class_name += l
                if l is ')':
                    break
            class_name = class_name.replace('\n', '')
            class_m = class_m.replace('(' + class_name + ')', '')
            in_variables = ''
            for l in class_m:
                if l is not '(' and l is not ')':
                    in_variables += l
                if l is ')':
                    break
            class_m = class_m.replace('(' + in_variables + ')', '')
            in_variables = in_variables.replace('\n', '')
            variables = in_variables.split('|')
            class_m = class_m[1:-1]
            if class_m[0:1] == '\n':
                class_m = class_m[1:]
            self.__classes[class_name] = [class_m, variables]

    def paste(self, filler):
        out_text = self.__classes[filler[0]][0]
        for v in self.__classes[filler[0]][1]:
            out_text = out_text.replace('#@'+v, filler[self.__classes[filler[0]][1].index(v) + 1])
        return out_text

    def out_text(self, in_filler):
        fillers = in_filler.get_fillers()
        strings = in_filler.get_strings()
        out = []
        for s in strings:
            out.append(s)
            if strings.index(s) < len(strings) - 1:
                out.append(self.paste(fillers[strings.index(s)]))
        return ''.join(out)

