import tkinter as tk
import time

# TODO: async or threading to run long-running other processes


class RunnerApp(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()

        # Capture event when someone closes the window with the X on the top-right corner of the window
        parent.protocol("WM_DELETE_WINDOW", self.close_app)

        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.close_app
        self.QUIT.pack({"side": "left"})

        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start
        self.start_button.pack({"side": "left"})

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop
        self.stop_button.pack({"side": "left"})

        self.text = tk.Text(self, state='disabled')
        self.text.pack({"side": "bottom"})

        self.stop_process = False

    def close_app(self):
        print("close")
        self.stop_process = True
        self.quit()

    def stop(self):
        print("stop")
        self.stop_process = True
        self.add_line('stop')

    def start(self):
        self.stop_process = False
        for i in range(100):
            if self.stop_process:
                break
            self.add_line(str(i))
            time.sleep(0.1)

    def add_line(self, line):
        self.text['state'] = 'normal'  # allow editing of the Text widget
        self.text.insert('end', line + "\n")
        self.text['state'] = 'disabled'  # disable editing
        self.text.see('end')  # scroll to the end as we make progress
        self.update()  # update the content and allow other events (e.g. from stop and quit buttons) to take place


def main():
    tk_root = tk.Tk()
    app = RunnerApp(parent=tk_root)

    tk_root.lift()
    tk_root.call('wm', 'attributes', '.', '-topmost', True)
    tk_root.after_idle(tk_root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()


main()
