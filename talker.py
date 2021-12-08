import abc


class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Talker(Person):
    def __init__(self, first_name: str, last_name: str, age: int):
        Person.__init__(self, first_name, last_name, age)

    @abc.abstractmethod
    def talk(self, text: str):
        pass


class HappyTalker(Talker):
    # def __init__(self, first_name: str, last_name: str, age: int):
    #     Talker.__init__(self, first_name, last_name, age)

    def talk(self, text: str):
        return text + "!!!"


class SlowTalker(Talker):
    # def __init__(self, first_name: str, last_name: str, age: int):
    #     Talker.__init__(self, first_name, last_name, age)

    def talk(self, text: str):
        ch_list = []
        ch_list[:] = text
        return " ".join(ch_list)


class StutterTalker(Talker):
    # def __init__(self, first_name: str, last_name: str, age: int):
    #     Talker.__init__(self, first_name, last_name, age)

    def talk(self, text: str):
        new_txt_list = []
        txt_list = text.split(" ")
        for word in txt_list:
            ch_list = []
            ch_list[:] = word
            ch_list.insert(0, ch_list[0])
            ch_list.insert(0, ch_list[0])
            new_txt_list.append("".join(ch_list))
        return " ".join(new_txt_list)

