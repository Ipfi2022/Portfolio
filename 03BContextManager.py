class FileCtxtManager:
    def __init__(hours, filename, mode):
        hours.filename = filename
        hours.mode = mode
        hours.file = None

    def __enter__(hours):
        hours.file = open(hours.filename, hours.mode)
        return hours.file

    def __exit__(hours, exc_type, exc_value, traceback):
        if hours.file:
            hours.file.close()
        return False  # Propagate exceptions, if any

with FileCtxtManager('DS4Class.txt', 'a') as f:
    f.write("\nProf")

with FileCtxtManager('DS4Class.txt', 'r') as g:
    content = g.read()
    print(content)

with FileCtxtManager('RM4Class.txt', 'r') as h:
    content = h.read()
    print(content)
