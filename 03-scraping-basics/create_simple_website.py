import fileinput

tag = "p"
delete_empties = True

body = ""

for line in fileinput.input():
    line = line.strip()
    if delete_empties is True and line == "":
        continue
    body += f"\n    <{tag}>{line}</{tag}>"

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Untitled</title>
    <style>

    </style>
</head>
<body>
    {body}
</body>
</html>
"""

print(html)
