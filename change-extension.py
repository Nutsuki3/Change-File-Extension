import os
import webbrowser as wb
import platform as pf


def change_extension(file_path, new_ets) -> None:
    file_name, old_ets = os.path.splitext(file_path)
    path = file_name + "." + new_ets
    os.rename(file_path, path)

def change_extensions_folder(folder_path, old_ets, new_ets) -> None:
    for file_name in os.listdir(folder_path):
        if file_name.endswith(old_ets):
            file_path = os.path.join(folder_path, file_name)
            change_extension(file_path, new_ets)

def main() -> None:
    while True:
        choice = input(">>> ")
        if choice[0:4] == "-ets":
            if os.path.isfile(choice[5:]) or os.path.isdir(choice[5:]) :
                path = choice[5:]
                if os.path.isfile(path) and os.path.exists(path):
                    extension = os.path.splitext(path)[1]
                    print(f"{path}\033[96m is > {extension}\033[0m")
                elif os.path.isdir(path) and os.path.exists(path):      
                    file_ets = os.listdir(path)
                    for ets in file_ets:
                        extension = os.path.splitext(ets)[1]
                        if extension:
                            print(f"{ets}\033[96m is > {extension}\033[0m")
                        else :
                            print(f"{ets}\033[31m > has no extension\033[0m")
                else:
                    print("\033[31mFolder or file not found\033[0m")
            else :
                print("\033[31m-help for commands detials\033[0m")
        elif choice[0:3] == "-ch":
            if os.path.isfile(choice[4:]) or os.path.isdir(choice[4:]) :
                path = choice[4:]
                try:
                    if os.path.isfile(path) and os.path.exists(path):
                        old_ets = os.path.splitext(path)[1]
                        new_ets = input("Enter the new file extension >>> ")
                        change_extension(path, new_ets)
                        print(f"\033[32mFile extension changed from {old_ets} to {new_ets}.\033[0m")
                    elif os.path.isdir(path) and os.path.exists(path):
                        old_ets = input("Enter the old file extension >>> ")
                        new_ets = input("Enter the new file extension >>> ")
                        change_extensions_folder(path, old_ets, new_ets)
                        print(f"\033[32mAll files with extension {old_ets} in {path} have been changed to {new_ets}\033[0m")
                    else:
                        print("\033[31mFolder or file not found\033[0m")
                except FileNotFoundError:
                    print("\033[31mFolder or File not found.\033[0m")
            else :
                print("\033[31m-help for commands detials\033[0m")
        elif choice[0:4] == "-ext":
            print("\033[33mThank for using program\033[0m")
            print("\033[33mIf you like it, please give stars to my repo, thanks :>\033[0m")
            ops = pf.system()
            url = "https://github.com/Nutsuki3/Change-File-Extension"
            if ops == "Windows":
                wb.open_new_tab(url, new=2)
            elif ops == "Linux":
                wb.get("xdg-open").open_new_tab(url)
            elif ops == "Darwin":
                wb.get("safari").open_new_tab(url)
            elif ops == "Android":
                wb.get("android").open_new_tab(url)
            elif ops == "iOS":
                wb.get("safari").open_new_tab(url)
            break

        elif choice[0:5] == "-help":
            print("\033[33m-ets for check the extension file\033[0m")
            print("\033[33m-ch for change the extension file\033[0m")
            print("\033[33m-exp for commands example\033[0m")
            print("\033[33m-ext for exit the program\033[0m")
        elif choice[0:4] == "-exp":
            print("\033[33m-ets <file or folder path>\033[0m")
            print("\033[33m-ch <file path> -n <new extension>\033[0m")
            print("\033[33m-ch <folder path> -o <old extension> -n <new extension>\033[0m")
        else:
            print("\033[31m-help for commands detials\033[0m")

if __name__ == "__main__" : 
    main()