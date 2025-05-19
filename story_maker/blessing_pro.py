# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:23:58 2018

@author: karja
"""

from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import tkinter.filedialog as fil
import tkinter.messagebox as mes
import webbrowser
from pathlib import Path
from textwrap import fill
from contextlib import chdir
try:
    from .story_archive import StoryFilesLoads, Choices
except:
    from story_archive import StoryFilesLoads, Choices


# Class that have no properties yet
class S_at:
    pass

# Class that generate Windows console and stories from Blessing_Story folder
class Bless(S_at):
    
    def __init__(self,root):
        super().__init__()
        self.asw = None
        self.cycle = 1
        self.root = root
        root.title("Blessing Project ✟ Story Reader and Maker")
        root.geometry("623x720+257+33")
        root.resizable(False,  False)
        
        # Binding short-cut for keyboard
        self.root.bind('<Control-d>', self.dele)
        self.root.bind('<Control-c>', self.copy)
        self.root.bind('<Control-s>', self.save_as)
        self.root.bind('<Control-x>', self.ex)
        self.root.bind('<Control-D>', self.dele)
        self.root.bind('<Control-C>', self.copy)
        self.root.bind('<Control-S>', self.save_as)
        self.root.bind('<Control-X>', self.ex)
        self.root.bind('<Control-f>', self.refresh)
        self.root.bind('<Control-F>', self.refresh)
        self.root.bind('<Control-P>', self.paste)
        self.root.bind('<Control-p>', self.paste)
        
        # Menu setting
        self.menu_bar = Menu(root)  # menu begins
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
        self.root.config(menu=self.menu_bar)  # menu ends
        
        # Help click to website
        self.about_menu = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_cascade(label = 'About', menu = self.about_menu)
        self.about_menu.add_command(label = 'Help',compound='left', 
                                    command=self.about)
        
        # File menu
        self.file_menu.add_command(label='Save as',  compound='left', 
                                   accelerator='Ctrl+S', command=self.save_as)
        self.file_menu.add_command(label='Refresh File',  compound='left', 
                                   accelerator='Ctrl+F', command=self.refresh)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', compound='left', 
                                   accelerator='Ctrl+X', command=self.ex)
        
        # Edit menu
        self.edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                                   compound='left', command=self.copy)
        self.edit_menu.add_command(label='Paste', accelerator='Ctrl+P',
                                   compound='left', command=self.paste)
        self.edit_menu.add_command(label='Delete', accelerator='Ctrl+D',
                                   compound='left', command=self.dele)
        
        
        # Variables to connect within widget.
        self.st1 = StringVar()
        
        # Checking the existence of the directory
        self.h_path = Path.home().joinpath("StoryMaker")
                    
        # Create frame, combobox, textbox, scrollbar, and radiobuttons
        self.combo = ttk.Combobox(root, width = 30)
        self.combo.pack(side = TOP, pady = 3)
        self.combo.bind("<<ComboboxSelected>>", self.start_story)
        self.combo["value"] = sorted([
            file.name.rpartition(".")[0] for file in self.h_path.iterdir() if ".zip" in file.name
        ])
        self.frame = Frame(root)
        self.frame.pack(side = BOTTOM, fill = BOTH, expand = True)
        self.scr = Scrollbar(self.frame)
        self.scr.pack(side = RIGHT, fill = BOTH, pady = 2, padx = 1)
        self.stbox = Text(self.frame, relief = 'sunken')
        self.stbox.pack(side = LEFT, fill = BOTH, expand = True,
                        padx = 2, pady = 2)
        self.scr.config(command=self.stbox.yview)
        self.stbox.config(yscrollcommand=self.scr.set)
        # self.bttr = Button(root, text = 'Dictionary', command = self.trans, 
        #                    relief = 'groove')
        # self.bttr.pack(side='left', padx = 3, pady = 2)
        self.rb1 = Radiobutton(root, text = 'A', variable=self.st1, 
                            value = 'A', compound='left', 
                            command = self.choice, tristatevalue = 0)
        self.rb1.pack(side='left', expand = True)
        self.rb2 = Radiobutton(root, text = 'B', variable=self.st1, 
                            value = 'B', compound=LEFT, 
                            command = self.choice, tristatevalue = 0)
        self.rb2.pack(side='left', expand = True)
        self.rb3 = Radiobutton(root, text = 'C', variable=self.st1, 
                            value = 'C', compound=LEFT, 
                            command = self.choice, tristatevalue = 0)
        self.rb3.pack(side='left', expand = True)
        self.rb1.config(state = 'disable')
        self.rb2.config(state = 'disable')
        self.rb3.config(state = 'disable')
    
    def text_conf(self, editable=False):
        if not editable:
            self.stbox.config(state="disabled")
        else:
            self.stbox.config(state="normal")

    # Choices function for choosing A/B/C    
    def choice(self, event = None):
        self.text_conf(True)
        self.asw = Choices(self.st1.get())
        match self.cycle:
            case 1:
                self.get_ans(self.asw, self.cycle)
                if self.asw != "C":
                    self.s_story2()
                    self.cycle += 1
                else:
                    self.cycle += 2
            case 2:
                self.get_ans(self.asw, self.cycle)
                if self.asw != "C":
                    self.s_story3()
                self.cycle += 1
        if self.cycle == 3:
            self.rb1.config(state = "disabled")
            self.rb2.config(state = "disabled")
            self.rb3.config(state = "disabled")
            self.cycle = 1
        self.text_conf()
                    
    # Answering function        
    def get_ans(self, ans=None, part=None):
        
        if part == 1:
            if ans == "A":
                self.stbox.insert(END, '\n' + 'Choose: ' + 'A\n')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansA)))
            elif ans == "B":
                self.stbox.insert(END, '\n' + 'Choose: ' + 'B\n')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansB)))
            elif ans == "C":
                self.stbox.insert(END, '\n' + 'Choose: ' + 'C\n')
                self.stbox.insert(END, '\n' + fill(str(self.q1_ansC)) + '\nThe End')
                
        elif part == 2:
            if ans == "A":
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'A\n')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansA)))
            elif ans == "B":
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'B\n')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansB)))
            elif ans == "C":
                self.stbox.insert(END, '\n')
                self.stbox.insert(END, '\n' + 'Choose: ' + 'C\n')
                self.stbox.insert(END, '\n' + fill(str(self.q2_ansC)) + '\nThe End')
                
    # Filling stories parts into 9 set of class properties    
    def story(self):
        
        self.docr = []
        with chdir(self.h_path):
            self.docr.extend(StoryFilesLoads(self.h_path).data_extract(self.combo.get()))


        # Setting up story to be run later on 
        S_at.pre = self.docr[0]["stories"]["begin"] + "\n"  
        S_at.q1 = [f"{k}. {v}" for k, v in self.docr[1]["choices"]["first"].items()]
        
        S_at.q2 = [f"{k}. {v}" for k, v in self.docr[1]["choices"]["second"].items()]
        
        S_at.q1_ansA = self.docr[0]["stories"]["first"]["A"] + "\n"
        
        S_at.q1_ansB = self.docr[0]["stories"]["first"]["B"] + "\n"
        
        S_at.q1_ansC = self.docr[0]["stories"]["first"]["C"] + "\n"
        
        S_at.q2_ansA = self.docr[0]["stories"]["second"]["A"] + "\n"
        
        S_at.q2_ansB = self.docr[0]["stories"]["second"]["B"] + "\n"
        
        S_at.q2_ansC = self.docr[0]["stories"]["second"]["C"] + "\n"
        
    # Starting first part of a story
    def s_story1(self):
        self.stbox.insert("1.0", str(fill(self.pre) + '\n'+'\n'))
        for i in self.q1:
            self.stbox.insert(END, i+'\n')

    # 2nd part of a story
    def s_story2(self):
        self.stbox.insert(END, '\n')
        for i in self.q2:
            self.stbox.insert(END, '\n' + i )
            self.st1.set(1)
     
    # 3rd of a story           
    def s_story3(self):
        if self.asw == "A":
            w = self.docr[2]["scriptures"]["A"] + "\n" 
            self.stbox.insert(END, '\n')
            self.stbox.insert(END, '\n' + str(fill(w.upper(),73)) )
        elif self.asw == "B":
            w = self.docr[2]["scriptures"]["B"] + "\n"
            self.stbox.insert(END, '\n')
            self.stbox.insert(END, '\n' + str(fill(w.upper(),73)) )
    
    # Clear function for starting new story afresh    
    def clear(self):
        self.docr = []
        self.fix_1=[]
        self.fix_2=[]
        self.text_conf(True)
        self.stbox.delete("1.0", "end")
        self.rb1.config(state = "normal")
        self.rb2.config(state = "normal")
        self.rb3.config(state = "normal")
        self.st1.set(1)

    # Start the story
    def start_story(self,event = None):
        self.clear()
        self.story()
        self.s_story1()
        self.text_conf()
    
    # Link to lWW Github page
    def about(self):
        webbrowser.open_new(r"https://github.com/kakkarja/BP")
    
    # Select all text content
    def select_all(self):
        self.stbox.tag_add('sel', '1.0', 'end')
            
    # Generate Copy Function
    def copy(self, event = None):
        self.root.clipboard_clear()
        self.select_all()
        self.stbox.event_generate("<<Copy>>")   
    
    def paste(self, event = None):
        self.text_conf(True)
        self.stbox.event_generate("<<Paste>>")
        self.text_conf()
            
    
    # Generate Delete Function
    def dele(self, event = None):
        self.text_conf(True)
        self.select_all()
        self.stbox.event_generate("<<Clear>>")
        self.text_conf()
    
    # Generate Exit Function
    def ex(self, event = None):
        self.root.destroy()
    
    # Writing to a .txt file (misc) 
    def write_to_file(self, file_name):
        try:
            sen = str(self.combo.selection_get())
            content = sen + '\n'+'\n' + self.stbox.get('1.0', 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except:
            content = self.stbox.get('1.0', 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
    
    # Generate Save as function dialog
    def save_as(self, event = None):
        input_file_name = fil.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        if input_file_name:
            self.write_to_file(input_file_name)
    
    # Refresh list of files in BP
    def refresh(self, event = None):
        pass

    # Dictionary Function
    def trans(self, event = None):
        pass

def main():
    pth = Path.home().joinpath("StoryMaker")
    begin = Tk()
    begin.withdraw()
    ans = mes.askyesno("Blessing Project", "Load story or Create story? (yes to load)")
    if pth.exists() and bool(list(pth.iterdir())) and ans:
        my_gui = Bless(begin)
        begin.deiconify()
        begin.mainloop()
    else:
        try:
            from .main_frame import story_maker
        except:
            from main_frame import story_maker
        if ans:
            print("No stories yet, please make one!")
            mes.showinfo("No Stories", "No stories exist yet, please make one!")
        begin.destroy()
        story_maker()
            
if __name__ == '__main__':
    main()
   