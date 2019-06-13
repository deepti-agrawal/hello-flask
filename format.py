markup = """
<!doctype html>
<html>
    <head>
    <title>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""
newmarkup = """
<!doctype html>
<html>
    <head>
    <title>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""
#this is index way of formatting
markup = markup.format("My page title","Page Heading")
print(markup)
#this is named way of formatting
newmarkup = newmarkup.format(title="My page title",heading="Page Heading")
print(newmarkup)