def checking_tags(content):
    content = content.strip()
    tags, i = [], 0
    while i < len(content):
        if content[i] == '<':
            j = i + 1
            while j < len(content) and content[j] != '>':
                j += 1
            if j == len(content):
                return False
            tag = content[i+1:j]
            
            if tag.startswith('/'):
                if not tags or tags[-1] != tag[1:]:
                    return False
                tags.pop()
            else:
                tags.append(tag)
            i = j
        i += 1
        
    return not tags
            
            
            
def checking_tags(content):
    content = content.strip()
    tags, i = [], 0
    while i < len(content):
        if content[i] == '<':
            j = i + 1
            while j < len(content) and content[j] == '>':
                j += 1
            if j == len(content):
                return False
            tag = content[i + 1:j]
            if tag.startswith('/'):
                if not tags or tags[-1] != tag[1:]:
                    return False
                tags.pop()
            else:
                tags.append(tag)
            i = j
        i += 1
        
    return not tags            

            
            