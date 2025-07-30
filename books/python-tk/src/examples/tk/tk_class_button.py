import tkinter as tk

class MyApp():
    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Class Based example')

        self.add_label()
        self.add_action_button()
        self.add_exit__button()

    def run(self):
        self.app.mainloop()

    def add_label(self):
        self.label = tk.Label(self.app,
                    text='Class Based example',
                    font=("Courier", 24),
                    fg="#0000FF",
                    bg="yellow",
                )
        self.label.pack()

    def add_exit__button(self):
        self.exit_button = tk.Button(self.app,
            text='Close',
            width=25,
            command=self.app.destroy,
            bg='lightblue',
        )
        self.exit_button.pack()

    def add_action_button(self):
        self.action_button = tk.Button(self.app,
                        text='Action',
                        width=25,
                        command=self.run_action)
        self.action_button.pack()

    def run_action(self):
        print(self) # MyApp object
        print("action")
        self.label['text'] = 'Action pressed'

MyApp().run()

