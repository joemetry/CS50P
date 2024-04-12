# extensions.py

def main():
    filename = input("Enter the name of a file: ").lower()
    media_type = get_media_type(filename)
    print(media_type)

def get_media_type(filename):
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
