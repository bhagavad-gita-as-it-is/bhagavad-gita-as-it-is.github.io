import os

input_folder = 'jpg'
html_filename = 'jpg-page.md'

all_data = []
sorted_filenames = sorted(os.listdir(input_folder), key=lambda x: int(x[x.rfind('-')+1:x.index('.')]))
for filename in sorted_filenames:
    link = f"https://bhagavad-gita-as-it-is.vercel.app/jpg/{filename}"
    text = f"<img src=\"{link}\" alt=\"{filename}\" loading=\"lazy\">\n"
    all_data.append(text)

with open(html_filename, 'w') as file:
    for text in all_data:
        file.write(text)


