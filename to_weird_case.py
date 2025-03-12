def to_weird_case(words):
    
    n = 2

    result = ""

    for i in words:
        
        result += str.upper(i) if n % 2 == 0 else str.lower(i)
        n += i != ' '

    return print (result)

to_weird_case("This is an example")
to_weird_case("This")
to_weird_case("iS")
to_weird_case("rANdoM")