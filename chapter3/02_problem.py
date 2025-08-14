letter='''
Dear <|name|>,
    you are selected!
    <|date|>'''

print(letter.replace("<|name|>", "mohiz").replace("<|date|>", "07/09/2050"))