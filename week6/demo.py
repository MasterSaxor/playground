movie = "transfomer"

def review():
    print(movie)
    def inner():
        print(movie)
    
    inner()

review()