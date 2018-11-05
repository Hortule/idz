from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """ инит Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ объекты на форме """
        # create instruction label
        Label(self,
              text="Введи информацию для новой истории"
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # create a label and text entry for the name of a person
        Label(self,
              text="Человек: "
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # create a label and text entry for a plural noun
        Label(self,
              text="Существительное мн. ч.:"
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        # create a label and text entry for a verb
        Label(self,
              text="Глагол:"
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        # create a label for adjectives check buttons
        Label(self,
              text="Прилагательное(ые):"
              ).grid(row=4, column=0, sticky=W)

        # create itchy check button
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text="нетерпиливый",
                    variable=self.is_itchy
                    ).grid(row=4, column=1, sticky=W)

        # create joyous check button
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="радостный",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)

        # create electric check button
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="пронизывающий",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)

        # create a label for body parts radio buttons
        Label(self,
              text="Часть тела:"
              ).grid(row=5, column=0, sticky=W)

        # create variable for single, body part
        self.body_part = StringVar()
        self.body_part.set(None)

        # create body part radio buttons
        body_parts = ["пупок", "большой палец", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part
                        ).grid(row=5, column=column, sticky=W)
            column += 1

        # create a submit button
        Button(self,
               text="Получение истории",
               command=self.tell_story
               ).grid(row=6, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyous.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "пронизывающее, "
        body_part = self.body_part.get()

        # create the story
        story = "Изветсный исследователь "
        story += person
        story += " уже отчаялся завершить дело своей жизни - поиск затерянного города "
        story += noun.title()
        story += " пока в один день "
        story += noun
        story += " не нашел "
        story += person + ". "
        story += "Мощное "
        story += adjectives
        story += "ни с чем не сравнимое чувство. "
        story += "После стольких лет поиска цель наконец была достигнута "
        story += person
        story += ' ощутил как на его ' + body_part + " скатилась слеза. "
        story += " Затем "
        story += noun
        story += " перешли в атаку "
        story += person + ". "
        story += " Мораль истории? Если задумали"
        story += verb
        story += " будьте осторожны."

        # display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()