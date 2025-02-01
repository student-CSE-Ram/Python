def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Server Error!"
        case 500:
            return "internal server not found"
        case _:
            return "unknown error"
        
# this is like switch case in python 
print(http_status(404))


# with 

with(
    open("file1.txt")as f1,
    open("file2.txt","w") as f2
) :
    content = "Hello Mr. this is a file that is opened with another file at a same time"
    f2.write(content)
    print(content)