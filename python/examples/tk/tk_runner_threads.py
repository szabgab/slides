import tkinter as tk
import time
import threading
import queue
import ctypes

class MyStopButton(Exception):
    pass

class ThreadedJob(threading.Thread):
    def __init__(self, que):
        self.que = que
        threading.Thread.__init__(self)
    def run(self):
        thread = threading.current_thread()
        print("Start thread {}".format(thread.name))
        try:
            for i in range(10):
                print(i)
                self.que.put(str(i))
                time.sleep(1)
        except Exception as err:
            print(f"Exception in {thread.name}: {err}  {err.__class__.__name__}")



    def raise_exception(self):
        thread = threading.current_thread()
        print(f"Raise exception in {thread.name}")
        thread_id = self.native_id
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(MyStopButton))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
        print("DONE")

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
        print(self.job.name)
        self.job.raise_exception()
        #self.stop_process = True
        self.add_line('stop')


    def start(self):
        self.stop_process = False
        self.start_button['state'] = 'disabled'
        self.que = queue.Queue()
        self.job = ThreadedJob(self.que)
        self.job.start()
        self.master.after(100, self.process_queue)

    def process_queue(self):
        print("process " + str(time.time()))
        if not self.job.is_alive():
            self.job.join()
            self.job = None
            self.stop_process = True
            self.start_button['state'] = 'normal'
            print("finished")
            return

        try:
            msg = self.que.get(0)
            self.add_line(msg)
        except queue.Empty:
            pass
        finally:
            if not self.stop_process:
                self.master.after(100, self.process_queue)

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
