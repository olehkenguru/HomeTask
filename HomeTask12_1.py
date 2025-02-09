import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        clean_text = ''
        html_teg = False

        for char in html:
            if char == '<':
                html_teg = True
            elif char == '>':
                html_teg = False
                continue

            if not html_teg:
                clean_text += char

    with codecs.open(result_file, 'w', 'utf-8') as clean_file:
        for i in clean_text.split('\n'):
            if i.strip():
                clean_file.writelines(i.strip() + '\n')

    return


delete_html_tags('draft.html')