import dropbox

link = dropbox.files.SharedLink(url="https://www.dropbox.com/sh/b26ffjxwong7txd/AADGXFyDZm31imIgje-JqS5Ka?dl=0")

dpx = dropbox.Dropbox("vB-DnYL1qTgAAAAAAAAYO1LxBNIZZpbqbPAYRqvj4vqRb6izYDwe41k6sEY4acgf")
resultset = dpx.files_list_folder(path='', shared_link=link)
for file in resultset.entries:
    name = file.name.strip().replace(' ','')
    with open("sounds/"+name, "wb") as f:
        metadata, res = dpx.sharing_get_shared_link_file(url="https://www.dropbox.com/sh/b26ffjxwong7txd/AADGXFyDZm31imIgje-JqS5Ka?dl=0", path="/"+file.name)
        f.write(res.content)
