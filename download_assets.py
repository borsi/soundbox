import dropbox

link = dropbox.files.SharedLink(url="")

dpx = dropbox.Dropbox("")
resultset = dpx.files_list_folder(path='', shared_link=link)
for file in resultset.entries:
    name = file.name.strip().replace(' ','')
    with open("sounds/"+name, "wb") as f:
        metadata, res = dpx.sharing_get_shared_link_file(url="", path="/"+file.name)
        f.write(res.content)
