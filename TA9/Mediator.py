import tkinter as tk


class Mediator:
    def send(self, sender, message):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, root):
        self.root = root
        self.text_box = None
        self.button = None

    def send(self, sender, message):
        if sender == "text_box":
            self.button.config(text=message)
        elif sender == "button":
            self.text_box.insert(tk.END, message)


class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        pass


class TextBox(Colleague, tk.Text):
    def __init__(self, master, mediator):
        tk.Text.__init__(self, master)
        Colleague.__init__(self, mediator)
        self.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.get("1.0", tk.END).strip()
        self.mediator.send("text_box", message)


class Button(Colleague, tk.Button):
    def __init__(self, master, mediator, text):
        tk.Button.__init__(self, master, text=text, command=self.send_message)
        Colleague.__init__(self, mediator)

    def send_message(self):
        message = self["text"]
        self.mediator.send("button", message)


def main():
    root = tk.Tk()
    mediator = ConcreteMediator(root)
    text_box = TextBox(root, mediator)
    button = Button(root, mediator, "Click me")
    mediator.text_box = text_box
    mediator.button = button

    text_box.pack()
    button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
