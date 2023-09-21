import os
import shutil
import re
import json
import sys


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


def loadJson(clenerpath) ->list:
    f = open("FileExtencionData.json", "r")
    fr = f.read()
    print("LOADING JSON FILE" )
    ListOfDest = json.loads(fr)
    return ListOfDest
def CreateDefaultJSON(clenerpath) -> list:
    print("CREATING DEFAULT JSON FILE")
    ListOfDest = [
        {"path": clenerpath + "//Documents", "ext": ["docx", "doc", "pdf", "xlsx", "ppt", "txt"]},
        {"path": clenerpath + "//Images", "ext": ["jpg","jpeg", "svg", "gif", "png", "webm"]},
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
    return ListOfDest

def main():
    path = "C://Users//jefte//Downloads"
    clenerpath = "C://Users//jefte//Documents//File_Clener"
    files = os.listdir(path)
    ListOfDest = loadJson(clenerpath)
    if not os.path.isfile("FileExtencionData.json"):
        ListOfDest = CreateDefaultJSON(clenerpath)

    for item in ListOfDest:
        print(item["path"] + "       " + extencionToString(item["ext"]))
    comfirm = input("Are you sure you want to move the files (Y/N)")

    if (comfirm != "Y"):
        print("Bye then")
        return 0

    # FolderSetup(clenerpath, ListOfDest)

    for dest in ListOfDest:
        for file in files:
            if re.search("^.*\.("+extencionToString(dest["ext"])+")$", file):
                print("archivo:"+ file+" Movido a")
                shutil.move(path+"//"+file, dest["path"])
            if (extencionToString(dest["ext"]) == ""):
                if os.path.isdir(path+"//"+file):
                    print(file)
                    shutil.move(path+"//"+file, dest["path"])

if __name__ == '__main__':
    main()
