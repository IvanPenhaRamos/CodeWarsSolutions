from re import findall  

def domain_name(url):

    result = findall(r'(?:https?://)?(?:www\.)?([^./]+)',url)   

    return result [0]

'''
https? porque la 's' es opcional
Se usa la \ tras el punto en www\. para escapar el punto
([^./]+)  El + para que devuelva uno o más caracteres que sigan a . ó /
'''


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("https://123.net")) 
print(domain_name("https://hyphen-site.org"))
print(domain_name("http://codewars.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("icann.org"))


'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet""
'''