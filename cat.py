'''
This program prints stdin (or the given files) to the screen while using only
constant memory.
'''
import sys

CHUNK_SIZE = 64 * 1024


def cat(file_obj):
    while True:
        chunk = file_obj.read(CHUNK_SIZE)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)















