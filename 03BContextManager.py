class FileCtxtManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False  # Propagate exceptions, if any

with FileCtxtManager('DS4Class.txt', 'a') as f:
    f.write("\nProf")

with FileCtxtManager('DS4Class.txt', 'r') as g:
    content = g.read()
    print(content)

with FileCtxtManager('RM4Class.txt', 'r') as h:
    content = h.read()
    print(content)
