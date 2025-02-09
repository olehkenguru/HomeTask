import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = []
    html_tag = False

    for char in html:
        if char == '<':
            html_tag = True
        elif char == '>':
            html_tag = False
            continue
        if not html_tag:
            clean_text.append(char)

    clean_text = ''.join(clean_text)
    lines = [line.strip() for line in clean_text.splitlines() if line.strip()]

    with open(result_file, 'w', encoding='utf-8') as clean_file:
        clean_file.write('\n'.join(lines) + '\n')


delete_html_tags('draft.html')