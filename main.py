print("For Relative Links")
url = input("Enter the URL you would like to tokenize: ")
path = url.replace('https://www.','')
print('[@T[link:<relative path="' + str(path) + '"/>]@T]')


    def url(u):
        s = print u.replace('https://www.','')
        r = str('[@T[link:<relative path="')
        t = str('"/>]@T])')
        x = r + s + t
        return f"<h1>{x}</h1>"


    def url(u):
        u = str(u)
        s = u.replace('https://www.','')
        r = str('([@T[link:&lt;relative path="')
        t = str('"/&gt;]@T])')
        x = r + s + t
        return f"<h1>{x}</h1>"