import os
import shutil
import re

class filedestiny:
    def __init__(self, path: str, extencions: list):
        self.path = path
        self.extencions = extencions


def FolderSetup(clenerpath, ListOfDest):
    if not os.path.isdir(clenerpath):
        os.makedirs(clenerpath)
    for dest in ListOfDest:
        if not os.path.isdir(dest.path):
            os.makedirs(dest.path)


def extencionToString(extencions: list) -> str:
    exten = ""
    for ex in extencions:
        exten = exten+"|" + ex
    return exten


if __name__ == '__main__':
    path = "C://Users//jefte//Downloads"
    clenerpath = "C://Users//jefte//Documents//File_Clener"
    files = os.listdir(path)
    ListOfDest = [
        filedestiny(clenerpath + "//Documents", ["docx", "doc", "pdf", "xlsx", "ppt", "txt"]),
        filedestiny(clenerpath + "//Images", ["jpg", "svg", "gif", "png", "webm"]),
        filedestiny(clenerpath + "//folders", []),
        filedestiny(clenerpath + "//compressed files", ["zip", "rar","gz"]),
        filedestiny(clenerpath + "//installers", ["msi", "tar", "jar"]),
        filedestiny(clenerpath + "//videos", ["mp4", "mkv"]),
        filedestiny(clenerpath + "//apps", ["exe"]),
        filedestiny(clenerpath + "//code", ["json", "sql", "js", "xml", "csv", "log"]),
        filedestiny(clenerpath + "//3dFiles", ["fbx", "blend", "blend1", "hdr"])
    ]

    FolderSetup(clenerpath, ListOfDest)

    for dest in ListOfDest:


        for file in files:
            if re.search("^.*\.("+extencionToString(dest.extencions)+")$", file):
                print(dest.path +"----------------"+ file)
                print(path +"//"+ file)
                shutil.move(path+"//"+file, dest.path)
            if (extencionToString(dest.extencions) == ""):
                if os.path.isdir(path+"//"+file):
                    print(file)
                    shutil.move(path+"//"+file, dest.path)



