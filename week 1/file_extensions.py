aa = input("File name: ")

aaa = aa.lower()

if ".gif" in aaa:
    print("image/gif")
elif ".jpg" in aaa:
    print("image/jpeg")
elif ".jpeg" in aaa:
    print("image/jpeg")
elif ".png" in aaa:
    print("image/png")
elif ".pdf" in aaa:
    print("application/pdf")
elif ".txt" in aaa:
    print("text/plain")
elif ".zip" in aaa:
    print("application/zip")
else:
    print("application/octet-stream")