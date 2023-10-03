def upload_file(f):
    if type(f) != bool:
        with open("pool/" + f.name, "wb+") as file:
            for chunk in f.chunks():
                file.write(chunk)
    