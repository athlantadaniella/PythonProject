def delete_html_tags(html_file, result_file='cleaned.txt'):

    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    clean_text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            continue
        elif not inside_tag:
            clean_text += char

    lines = clean_text.split('\n')
    lines = [line.strip() for line in lines if line.strip() != '']
    clean_text = '\n'.join(lines)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(clean_text)

    print('File cleaned and saved as', result_file)


delete_html_tags('draft.html')