def read_file_line_by_line(filename):
    with open('largefile.txt', "r") as file:
        for line in file:
            yield line.strip()

#for line in read_file_line_by_line(r"C:\Users\hp\Desktop\mca\python\python-practice\largefile.txt"):
   # print(line)
class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        import time
        self.start_time = time.time()
        print("Timer started.")
    def stop(self):
        import time
        self.end_time = time.time()
        print("Timer stopped.")
    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError("Timer has not been started and stopped properly.")
        return self.end_time - self.start_time