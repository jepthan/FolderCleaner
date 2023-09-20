import os
import shutil
import re
import json


def FolderSetup(clenerpath, ListOfDest):
    if not os.path.isdir(clenerpath):
        os.makedirs(clenerpath)
    for dest in ListOfDest:
        if not os.path.isdir(dest.path):
            os.makedirs(dest.path)


def extencionToString(extencions: list) -> str:
    exten = ""
    for ex in extencions:
        exten = exten + "|" + ex
    return exten


if __name__ == '__main__':
    path = "C://Users//jefte//Downloads"
    clenerpath = "C://Users//jefte//Documents//File_Clener"
    files = os.listdir(path)
    ListOfDest = [
        {"path": clenerpath + "//Documents", "ext": ["docx", "doc", "pdf", "xlsx", "ppt", "txt"]},
        {"path": clenerpath + "//Images", "ext": ["jpg", "svg", "gif", "png", "webm"]},
        {"path": clenerpath + "//folders", "ext": []},
        {"path": clenerpath + "//compressed files", "ext": ["zip", "rar", "gz"]},
        {"path": clenerpath + "//installers", "ext": ["msi", "tar", "jar"]},
        {"path": clenerpath + "//videos", "ext": ["mp4", "mkv"]},
        {"path": clenerpath + "//apps", "ext": ["exe"]},
        {"path": clenerpath + "//code", "ext": ["json", "sql", "js", "xml", "csv", "log"]},
        {"path": clenerpath + "//3dFiles", "ext": ["fbx", "blend", "blend1", "hdr"]}
    ]

    f = open("FileExtencionData.json", "w")
    f.write(json.dumps(ListOfDest))
    print(json.dumps(ListOfDest))

    # FolderSetup(clenerpath, ListOfDest)

    # for dest in ListOfDest:
    #     for file in files:
    #         if re.search("^.*\.("+extencionToString(dest.extencions)+")$", file):
    #             print(dest.path +"----------------"+ file)
    #             print(path +"//"+ file)
    #             shutil.move(path+"//"+file, dest.path)
    #         if (extencionToString(dest.extencions) == ""):
    #             if os.path.isdir(path+"//"+file):
    #                 print(file)
    #                 shutil.move(path+"//"+file, dest.path)
