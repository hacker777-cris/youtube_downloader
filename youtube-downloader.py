#if you are using dcoder this won't work unless you save the file locally and run it 
#because dcoder does not have a terminal hence we cannot install pytube
from pytube import YouTube
from sys import argv
import tkinter as tk
from tkinter import filedialog

link =argv[0]
print("\n                                         WELCOME TO THE YOUTUBE DOWNLOADER!!")
print("\n                                         created by H4CK3R_777")
print("\n                                  YOU CAN DO THE FOLLOWING ACTIONS ON YOUTUBE")
actions = ['1.CHECK TITLE','2.CHECK VIEWS','3.DOWNLOAD VIDEO']
#i print out the options

while True:

    for x in range(len(actions)):
        print(actions[x])

    action = input("WHAT DO YOU WANT TO DO?: ")

    #we make sure user enters a valid link
    while True:
        try :
            yt = YouTube(input("ENTER LINK HERE: "))
            
            break
        except :
            print("please enter a valid link")
        

    yd = YouTube.streams

    def title():
        print("TITLE: " + yt.title)
        return

    def views():
        print("VIEWS: " , yt.views)

        return
    

    def Download_high():
        # Create the root window
        root = tk.Tk()
        root.withdraw()

        # Ask the user to select a folder on the desktop
        folder_path = filedialog.askdirectory(initialdir='~/Desktop', title='Select a folder')

        # Print the selected folder path
        print(f"The selected folder is: {folder_path}")

        print("this may take time depending on length of video")   
        print("Downloading \n Please wait.......")
        yd = yt.streams.get_highest_resolution()
        yd.download(folder_path)
        print("your video has been downloaded")

        return
    def Download_low():
       
        # Create the root window
        root = tk.Tk()
        root.withdraw()

        # Ask the user to select a folder on the desktop
        folder_path = filedialog.askdirectory(initialdir='~/Desktop', title='Select a folder')

        # Print the selected folder path
        print(f"The selected folder is: {folder_path}")

        print("this may take time depending on length of video")   
        print("Downloading \n Please wait.......")
        yd = yt.streams.get_lowest_resolution()
        yd.download(folder_path)
        print("your video has been downloaded")
        
    if action == '1':
        title()

    elif action == '2':
        views()

    elif action == '3':
        resolution = input("Do you want your video in high or low resolution? (high/low): ").lower()
        
        if resolution == 'low':
            Download_low()
            
        elif resolution == 'high':
            Download_high()
    while True:
        return_to_menu = input("Return to main menu? (y/n): ")
        if return_to_menu == "y":
            break
        elif return_to_menu == "n":
            input("press enter to exit......")
            print("Exiting program...")
            quit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")



