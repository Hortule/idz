from tkinter import *


class Zodiac:

    def __init__(self, name, surname, zodiac, dob):
        self.name = name
        self.surname = surname
        self.zodiac = zodiac
        self.dob = dob.split('.')


class Application(Frame):
    n = -1

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.name_label = Label(text="Введите имя:")
        self.surname_label = Label(text="Введите фамилию:")
        self.zodiac_label = Label(text="Введите зодиак:")
        self.dob_lable = Label(text="Введите дату рождения дд.мм.гггг:")

        self.name = StringVar()
        self.surname = StringVar()
        self.zodiac = StringVar()
        self.dob = StringVar()
        self.nameoutp = StringVar()
        self.filename = StringVar()

        self.name_outp_lable = Label(text="Введите имя:")
        self.name_outp_entry = Entry(textvariable=self.nameoutp)
        self.name_outp_button = Button(text="Output", command=self.outp)
        self.info_outp_lable = Label(text="")

        self.blank_lable = Label(text="")
        self.file_entry = Entry(textvariable=self.filename)
        self.save_button = Button(text="Save", command=self.save)

        self.name_entry = Entry(textvariable=self.name)
        self.surname_entry = Entry(textvariable=self.surname)
        self.zodiac_entry = Entry(textvariable=self.zodiac)
        self.dob_entry = Entry(textvariable=self.dob)
        self.input_button = Button(text="Input", command=self.increase)

        self.increase()

    def increase(self):

        global zod

        self.n += 1

        if self.n <= 8:
            self.name_label.grid(row=0, column=0, sticky="w")
            self.surname_label.grid(row=0, column=1, sticky="w")
            self.zodiac_label.grid(row=0, column=2, sticky="w")
            self.dob_lable.grid(row=0, column=3, sticky="w")

            self.name_entry.grid(row=1, column=0, padx=5, pady=5)
            self.surname_entry.grid(row=1, column=1, padx=5, pady=5)
            self.zodiac_entry.grid(row=1, column=2, padx=5, pady=5)
            self.dob_entry.grid(row=1, column=3, padx=5, pady=5)

            self.input_button.grid(row=2, column=3, padx=5, pady=5, sticky="e")
            self.write_down()

        else:
            self.name_label.grid_forget()
            self.surname_label.grid_forget()
            self.zodiac_label.grid_forget()
            self.dob_lable.grid_forget()

            self.name_entry.grid_forget()
            self.surname_entry.grid_forget()
            self.zodiac_entry.grid_forget()
            self.dob_entry.grid_forget()

            self.input_button.grid_forget()

            self.name_outp_lable.grid(row=3, column=0, sticky="w")
            self.name_outp_entry.grid(row=3, column=1, padx=5, pady=5)
            self.name_outp_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")
            self.info_outp_lable.grid(row=4, column=1, sticky="w")

            self.blank_lable.grid(row=4, column=0, sticky="w")
            self.file_entry.grid(row=5, column=0, padx=5, pady=5)
            self.save_button.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        if self.n == 8:
            self.sort()

    def write_down(self):
        global zod
        z = Zodiac(self.name.get(), self.surname.get(), self.zodiac.get(), self.dob.get())
        zod.append(z)

    def sort(self):
        global zod
        zn = []
        zod.pop(0)

        for i in range(8):
            zn.append(int(zod[i].dob[0]) + int(zod[i].dob[1]) * 30 + int(zod[i].dob[2]) * 365)
        for i in range(7):
            for j in range(i, 8):
                if zn[i] > zn[j]:
                    promzn = zn[i]
                    promzod = zod[i]
                    zn[i] = zn[j]
                    zod[i] = zod[j]
                    zn[j] = promzn
                    zod[j] = promzod

    def outp(self):
        (name, surname) = str(self.nameoutp.get()).split(' ')
        for i in range(8):
            if zod[i].name == name and zod[i].surname == surname:
                self.info_outp_lable = Label(text='{0} {1} {2} {3}.{4}.{5}'.format(zod[i].name, zod[i].surname,
                                                                                   zod[i].zodiac, zod[i].dob[0],
                                                                                   zod[i].dob[1], zod[i].dob[2]))
                self.info_outp_lable.grid(row=4, column=1, sticky="w")

    def save(self):
        name = self.filename.get()
        f = open(name+'.csv', 'w')
        out = ''
        for i in range(8):
            out += 'Имя;Фамилия;Зодиак;Дата рождения;\n'
            out += '{0};{1};{2};{3}.{4}.{5}\n'.format(zod[i].name, zod[i].surname,
                                                      zod[i].zodiac, zod[i].dob[0],
                                                      zod[i].dob[1], zod[i].dob[2])
        f.write(out);
        f.close()


# main
zod = []

root = Tk()
root.title("GUI")
app = Application(root)
root.mainloop()
