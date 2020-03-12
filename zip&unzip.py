import os
import tkinter as tk
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox, filedialog

def CreateWidgets():
	selectlabel = Label(root, text="Files to Zip : " , bg="steelblue")
	selectlabel.grid(row=0,column=0,padx=5,pady=5)

	root.zipFilesEntry = Text(root,height=4,width=39)
	root.zipFilesEntry.grid(row=0,column=1,columnspan=2,padx=5,pady=5)

	zipBrowseButton = Button(root,text="BrowseFile",width=15,height=1,command=ZipFileBrowse)
	zipBrowseButton.grid(row=0,column=3,padx=5,pady=5)

	zipNamelabel = Label(root,text="Zipped Location : ", bg="steelblue")
	zipNamelabel.grid(row=1,column=0,padx=5,pady=5)

	root.zipFolderEntry = Entry(root,width=30,textvariable = zipFileName)
	root.zipFolderEntry.grid(row=1,column=1,columnspan=2,padx=5,pady=5)

	zipSaveBrowse = Button(root,text="Browse", width=15,height=1,command=ZipSaveBrowse)
	zipSaveBrowse.grid(row=1,column=3,padx=5,pady=5)

	ZipButton=Button(root,text="Zip",width=20,command=ZipFiles)
	ZipButton.grid(row=2,column=1,columnspan=2,padx=5,pady=5)

	unzipFilelabel  = Label(root,text="Files to Unzip : "  , bg ="steelblue")
	unzipFilelabel.grid(row=3,column=0,padx=5,pady=5)

	root.unzipFilesEntry = Text(root,height=4,width=39)
	root.unzipFilesEntry.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

	unZipBrowsebutton = Button(root,text="Browse",width=15,command=unZipFileBrowse)
	unZipBrowsebutton.grid(row=3,column=3,padx=5,pady=5)

	unzipFileNamelabel = Label(root,text = "Unzipped Location", bg = "steelblue")
	unzipFileNamelabel = Label(root,text = "Unzipped Location", bg = "steelblue")

	root.unzipFolderEntry = Entry(root,width=30,textvariable=unzipFolderName)
	root.unzipFolderEntry.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

	unzipSavebrowse = Button(root,text="Browse",width=15,command=unZipSaveBrowse)
	unzipSavebrowse.grid(row=4,column=3,padx=5,pady=5)

	unZipButton = Button(root,text="UnZip",width=15,command=unZipFiles)
	unZipButton.grid(row=5,column=1,columnspan=2,padx=5,pady=5)


def ZipFileBrowse():
	root.zipFileSelection = filedialog.askopenfilenames(initialdir = "YOUR PATH")

	for files in root.zipFileSelection:
		root.files=os.path.basename(files)
		root.zipFilesEntry.insert('2.0' , root.files+"\n")
	root.zipFilesEntry.config(state=DISABLED)

def unZipFileBrowse():
	root.unzipFileSelection = filedialog.askopenfilename(initialdir = "YOUR PATH")

	root.files=os.path.basename(root.unzipFileSelection)
	root.unzipFilesEntry.insert('1.0',root.files+"\n")
	root.unzipFilesEntry.config(state=DISABLED)

def ZipSaveBrowse():
	zipSaveDestination = filedialog.asksaveasfilename(initialdir = "YOUR PATH")
	zipFileName.set(zipSaveDestination)
	root.zipFolderEntry.config(text=zipSaveDestination)

def unZipSaveBrowse():
	unZipSaveDestination = filedialog.asksaveasfilename(initialdir="YOUR PATH")
	unzipFolderName.set(unZipSaveDestination)
	root.unzipFolderEntry.config(text = unZipSaveDestination)


def ZipFiles():
	with ZipFile(zipFileName.get(),'w') as zip_file:
		for file in root.zipFileSelection:
			zip_file.write(file,os.path.basename(file))

	messagebox.showinfo("Success","Files Zipped Successfully")

def unZipFiles():
	os.makedirs(unzipFolderName.get())

	with ZipFile(root.unzipFileSelection,'r') as unzip_file:
		unzip_file.extractall(unzipFolderName.get())

	messagebox.showinfo("Success", "Files Unziped Successfully")


root = tk.Tk()

root.title("Zip&UnZip")
root.config(background  = "steelblue")

zipFileName = StringVar()
unzipFolderName = StringVar()

CreateWidgets()

root.mainloop()