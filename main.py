class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
        
    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


files = ['names.txt', 'emails.txt', 'file_names.txt', 'color.txt']


def MainFunc():
    while 1:
        command = input("pick a number 1~4, 5 for exit")

        with open('MOCK_DATA.txt','r') as file:
            for i in file:
                file_list = i.split()
                file_list[0] += ' ' + file_list.pop(1)
                if len(file_list) > 4:
                    file_list[0] += ' ' + file_list.pop(1)
                info = Data(*file_list)
                if command == '1':
                    with open(files[0], 'a') as fullN:
                        fullN.write(info.full_name)
                        fullN.write('\r')
                elif command == '2':
                    with open(files[1], 'a') as emailN:
                        emailN.write(info.email)
                        emailN.write('\r')
                elif command == '3':
                    with open(files[2], 'a') as fileN:
                        fileN.write(info.file_name)
                        fileN.write('\r')
                elif command == '4':
                    with open(files[3], 'a') as colorN:
                        colorN.write(info.color)
                        colorN.write('\r')
                elif command == '5':
                    break
                else:
                    print('wrong number')
MainFunc()

def RemList():
    file = open('names.txt', 'w')
    file.close()

    file = open('emails.txt', 'w')
    file.close()

    file = open('file_names.txt', 'w')
    file.close()

    file = open('color.txt', 'w')
    file.close()
MainFunc()