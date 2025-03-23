# <body>
# <center>
# <h1> The Little Boat </h1>
# </center>
# <p> The storm tossed the little
# boat like a cheap sneaker in an
# old washing machine. The three
# drunken fishermen were used to
# such treatment, of course, but
# not the tree salesman, who even as
# a stowaway now felt that he
# had overpaid for the voyage. </p>
# <ol>
# <li> Will the salesman die? </li>
# <li> What color is the boat? </li>
# <li> And what about Naomi? </li>
# </ol>
# </body>

def check_html_tags(html_content):
    html_content = html_content.strip()
    tags = []
    i = 0
    while i < len(html_content):
        if html_content[i] == '<':  # Start of a tag
            j = i + 1
            while j < len(html_content) and html_content[j] != '>':
                j += 1
            if j == len(html_content):  # Incomplete tag
                return False
            tag = html_content[i + 1:j]
            print(tag)
            # Handle closing tags
            if tag.startswith('/'):
                if not tags or tags[-1] != tag[1:]:
                    return False
                tags.pop()
            else:  # Opening tag
                tags.append(tag)
            i = j
        i += 1
    
    return not tags  # Valid if stack is empty

# Test case
html_content = """
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
"""

# Validate the HTML content
print(check_html_tags(html_content))  # Output: True
