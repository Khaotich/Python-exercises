class OpenFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with OpenFile("sample.txt", "w") as f:
    f.write("\nto jest sampl testowy")


from contextlib import contextmanager
@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    yield f
    f.close()

with open("sample2.txt", "w") as f:
    f.write("\nto jest sampl testowy 2")