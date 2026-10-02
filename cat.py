def cat(file):
    out = sys.stdout.buffer
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        out.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
