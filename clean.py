import sys
import os
import argparse
import shutil


def list_files(path):
    for path, dirs, files in os.walk(path):
      print (path)
      for f in files:
        print ('\t'+f)


def get_files_list(path):
    '''
    parameters:
    -----------
    path: string, root directory
    returns:
    --------
    directory: key filename, value list of directories containing filename
    '''
    response = dict()

    for path, dirs, files in os.walk(path):
        for f in files:
            if f in response:
                list_path = response[f]
            else:
                list_path = list()
                response[f] = list_path
            list_path.append(path)
    return response



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove dupplicate files.')
    parser.add_argument('--path',dest='path', help='source directory',required=True)
    args = parser.parse_args()
    d = get_files_list(args.path)
    for file,list_paths in d.items():
        print("\n\n")
        if len(list_paths) > 1:
            print("file:",file, "is duplicated", len(list_paths), " times")
            for path in list_paths:
                print("\t"+path)
            artiste = False
            for path in list_paths:
                if path.find('Artistes') !=-1:
                    artiste=True
            if artiste == False:
                rep = input("Copy to Artistes Folder ?")
                if rep == 'y':
                    name = input("Enter Artiste name: ")
                    try:
                        os.mkdir("/Users/djindjin/Music/Reggae/Artistes/"+name)
                    except FileExistsError:
                        pass
                    shutil.copyfile(path+"/"+file,"/Users/djindjin/Music/Reggae/Artistes/"+name+"/"+file)
            for path in list_paths:
                if path.find('Artistes') ==-1:
                    rep = input("\t remove -->: "+path + " ?")
                    if rep == "y":
                        os.remove(path+"/"+file)
