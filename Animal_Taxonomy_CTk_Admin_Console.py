from customtkinter import *
from PIL import Image
import os 
from subprocess import call
import sqlite3

root = CTk()
root.geometry("1000x550")
root.title("Animal Taxonomy")
root.maxsize(width = 1000, height = 550)
root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")

con = sqlite3.connect("Animal_Taxonomy_Db.db")
cur = con.cursor()

global glb_top_position, \
    glb_crud_frame_width, glb_crud_frame_height, \
    glb_img_btn_height, glb_img_btn_width, \
    glb_menu_btn_ypos_space, glb_menu_btn_height, glb_menu_btn_width, glb_menu_btn_current_ypos, glb_menu_btn_font,\
    glb_home_btn_xpos, glb_img_btn_heights_space, \
    glb_fg_color_transparent,\
    border_line_size_2, glb_common_xpos, glb_current_working_directory

# get the current working directory
glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))
glb_top_position = 2
glb_crud_frame_height = 85
glb_crud_frame_width = 150
glb_img_btn_height, glb_img_btn_width = 10, 10
glb_menu_btn_ypos_space = 15
glb_menu_btn_xpos_space = 15
glb_menu_btn_height = 28
glb_menu_btn_width = 140
glb_menu_btn_current_ypos = 0
glb_menu_btn_font = ("Bradley Hand ITC" , 20, "italic", "bold" )
glb_fg_color_transparent = "transparent"
border_line_size_2 = 2
glb_common_xpos = 15

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=PAGES=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def createFrame(_frame, _border_color, _border_width, _fg_color, _xpos = 0, _ypos = 0 , _width = 100, _height = 100, _is_content_frame = False):
    global glb_top_position
    if _is_content_frame :
        tmp_frame = CTkFrame(_frame, border_color = _border_color,  border_width= _border_width, fg_color = _fg_color, width = 820, height = 520)#
        tmp_frame.place(x = 15, y = 15)
        glb_top_position = glb_top_position + _height + 5
    else:
        tmp_frame = CTkFrame(_frame, border_color = _border_color,  border_width= _border_width, fg_color = _fg_color, width = _width, height = _height)#
        tmp_frame.place(x = _xpos, y = _ypos)
        glb_top_position = glb_top_position + _height + 5
    return tmp_frame

def createRadioButton (_frame ,_text, _fg_color , _value , _command, _argument,  _xpos, _ypos ):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , fg_color = _fg_color, value = _value, command = lambda:(_command(_argument)))
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn

def createMenuButton (_frame, _text,  _command, _argument, _previous_control, _add_xpos = 0, _add_ypos = 0):
    global glb_menu_btn_font    
    tmp_btn = CTkButton(_frame,text = _text ,hover_color= "#c850c0", font = glb_menu_btn_font,
                         width=  glb_menu_btn_width, height= glb_menu_btn_height, command = lambda: (_command(_argument)))
    global glb_menu_btn_current_ypos 
    glb_menu_btn_current_ypos = glb_menu_btn_current_ypos + _previous_control._current_height + glb_menu_btn_ypos_space + _add_ypos
    tmp_btn.place(x = glb_menu_btn_xpos_space, y = glb_menu_btn_current_ypos)
    return tmp_btn

def createButton(_frame, _text, _corner_radius, _call_back_function, _xpos, _ypos):
    tmp_btn = CTkButton(_frame,text = _text,corner_radius = _corner_radius,hover_color = "#c850c0",
                         height= glb_img_btn_height, command = lambda: (_call_back_function()))
    tmp_btn.place(x = _xpos, y = _ypos)
    return tmp_btn

def createImageButton(_frame, _text, _image, _corner_radius, _call_back_function, _xpos, _ypos):
    img = Image.open(r"Images/" + _image)
    tmp_btn = CTkButton(_frame,text = _text, image = CTkImage(dark_image=img, light_image=img),corner_radius = _corner_radius,
                         width=  glb_img_btn_width, height= glb_img_btn_height, command = lambda: (_call_back_function()))
    tmp_btn.place(x = _xpos, y = _ypos)
    return tmp_btn

def createSearchByLabel(_frame):
    tmp_label = CTkLabel(_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#c850c0")
    tmp_label.place(x = glb_common_xpos, y = 70)
    return tmp_label

def createSearchResultLabel(_frame, _iskingdompage = False, _isafterclasspage = False):

    if _iskingdompage :
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
        tmp_label.place(x = 15, y = 130)
        return tmp_label
    elif _isafterclasspage:
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
        tmp_label.place(x = 15, y = 140)
        return tmp_label
    else :
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "dodgerblue3")
        tmp_label.place(x = 15, y = 160)
        return tmp_label

def createMainHeading(_frame, _text):
    tmp_heading = CTkLabel(_frame, text = _text,font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = "#c850c0")
    tmp_heading.place(x = 300, y = 5)
    return tmp_heading

def createSearchButton(_frame, _command, _ishomepage = False):
    if _ishomepage :
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = "dodgerblue3",hover_color = "#c850c0",corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 660, y = 130)
        return tmp_Search_Btn
    else:
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = "dodgerblue3",hover_color = "#c850c0",corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 660, y = 105)
        return tmp_Search_Btn

def createSearchEntry(_frame, _ishomepage = False):
    if _ishomepage :
        tmp_Entry = CTkEntry(_frame, width = 640, text_color = "#c850c0")
        tmp_Entry.place(x = 15, y = 130)
        return tmp_Entry
    else:
        tmp_Entry = CTkEntry(_frame, width = 640, text_color = "#c850c0")
        tmp_Entry.place(x = 15, y = 105)
        return tmp_Entry


def home_page():
    home_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(home_frame, "HOME")

    label = createSearchByLabel(home_frame)

    global radio_value
    def radio_value(value_before):
        if value_before == "":
            label = CTkLabel(home_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              fg_color = "transparent", fg = "red")
            label.place(x = 1, y = 470)
        else:
            global home_value
            home_value = value_before

    search_name_btn = createRadioButton (home_frame , "NAME", "darkgrey" , "NAME" , radio_value, "name", 10, 100 )

    search_kingdom_btn = createRadioButton (home_frame ,"KINGDOM", "darkgrey" , "NAME" , radio_value, "kingdom", 81, 100)

    search_phylum_btn = createRadioButton (home_frame ,"PHYLUM", "darkgrey" , "NAME" , radio_value, "phylum", 177, 100)

    search_class_btn = createRadioButton (home_frame ,"CLASS", "darkgrey" , "NAME" , radio_value, "class", 262, 100)

    search_order_btn = createRadioButton(home_frame ,"ORDER", "darkgrey" , "NAME" , radio_value, "naturalorder", 335, 100)

    search_family_btn = createRadioButton (home_frame ,"FAMILY", "darkgrey" , "NAME" , radio_value, "family", 415, 100)

    search_genus_btn = createRadioButton (home_frame ,"GENUS", "darkgrey" , "NAME" , radio_value, "genus", 495, 100)

    search_species_btn = createRadioButton (home_frame ,"SPECIES", "darkgrey" , "NAME" , radio_value, "species", 570, 100)

    def on_home_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            tosearch = tosearch

        if home_value == "name":
            for label in result_frame.winfo_children():
                label.destroy()
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  name = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 30, "italic" ), text_color = "aliceblue")
                label.place(x = 1, y = 10) 

        elif home_value == "kingdom":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "phylum":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "class":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "naturalorder":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "family":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "genus":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

        elif home_value == "species":
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10 
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

    result_frame = createFrame(home_frame,  "#c850c0",  2, "transparent", 15, 173, 790, 333)

    label = createSearchResultLabel(home_frame)

    search = createSearchEntry(home_frame, _ishomepage = True)
    global contents
    contents = StringVar()
    contents.set("Search As Per Your Option.")
    search["textvariable"] = contents

    search_btn = createSearchButton(home_frame, on_home_search_btn_click, _ishomepage = True)

def kingdom_page():

    kingdom_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(kingdom_frame, "KINGDOM")

    label = createSearchByLabel(kingdom_frame)

    result_frame = createFrame(kingdom_frame,  "#c850c0",  2, "transparent", 15, 143, 790, 363)

    def on_search_animal_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Animalia:"
        ypos = 10 
        tmp_qry = "SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' AND active = 1"
        record_set = cur.execute(tmp_qry)
        print(record_set.rowcount)
        for row in record_set:
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos)
            ypos = ypos + 27 

    search_animal_btn = CTkButton(kingdom_frame, text = "ANIMALS", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                  command = lambda:(on_search_animal_btn_click()))
    search_animal_btn.place(x = 10, y = 98)


    def on_search_plant_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Plantae:"
        ypos = 11 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_plant_btn = CTkButton(kingdom_frame, text = "PLANT", fg_color = "dodgerblue3",hover_color = "#c850c0",  corner_radius = 40,
                                 command = lambda:(on_search_plant_btn_click()))
    search_plant_btn.place(x = 158, y = 98)


    def on_search_fungi_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Fungi:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_fungi_btn = CTkButton(kingdom_frame, text = "FUNGI", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                     command = lambda:(on_search_fungi_btn_click()))
    search_fungi_btn.place(x = 305, y = 98)


    def on_search_protista_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Protista:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 
    
    search_protista_btn = CTkButton(kingdom_frame, text = "PROTISTA", fg_color = "dodgerblue3",hover_color = "#c850c0", corner_radius = 40,
                                     command = lambda:(on_search_protista_btn_click()))
    search_protista_btn.place(x = 453, y = 98)


    def on_search_monera_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Monera:"
        ypos = 10 
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 15, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
            label.place(x = 10, y = ypos) 
            ypos = ypos + 27 

    search_monera_btn = CTkButton(kingdom_frame, text = "MONERA", fg_color = "dodgerblue3",hover_color = "#c850c0",  corner_radius = 40,
                                     command = lambda:(on_search_monera_btn_click()))
    search_monera_btn.place(x = 600, y = 98)

    label =createSearchResultLabel(kingdom_frame, _iskingdompage = True)

def phylum_page():
    global search_result_ypos 
    search_result_ypos = 160

    phylum_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(phylum_frame, "PHYLUM")

    label = createSearchByLabel(phylum_frame)


    def radio_value(value_before):
        if value_before == "":
            label = CTkLabel(phylum_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              fg_color = "darkgrey", fg = "red")
            label.place(x = 10, y = 470)
        else:
            global phylum_value
            phylum_value = value_before
        
            if phylum_value == "Animalia":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Chordate", 
                "Arthrpod", 
                "Molusc", 
                "Echinoderm", 
                "Annalid"
                ] 
                combo.set("Animalia")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Plantae":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [  
                "Bryophyta", 
                "Cycadophyta", 
                "Ginkgophyta", 
                "Chlorophyta", 
                "Lycophyta"
                ]
                combo.set("Plantae")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Fungi":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Ascomycota", 
                "Basidiomycota", 
                "Zygomycota",
                "Microsporidia",  
                "Bigyra",
                "Aphelida",
                "Mycetozoa"
                ]
                combo.set("Fungi")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Protista":
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Dinoflagellates", 
                "Amoebozoa", 
                "Rhodophyta",
                "Ciliates"  
                ] 
                combo.set("Protista")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Monera": 
                combo = CTkComboBox(phylum_frame, width = 200)
                combo["values"] = [ 
                "Archaebacteria", 
                "Schizopyta", 
                "Cyanophyta",
                "Prochlorophyta"  
                ] 
                combo.set("Monera")
                #combo.current()
                combo.place(x = 10, y = 130)

    search_phylum_animal_menu =createRadioButton (phylum_frame ,"Animal", "darkgrey" , "NAME" , radio_value, "Animalia", 10, 100)

    search_phylum_plant_menu =createRadioButton (phylum_frame ,"Plant", "darkgrey" , "NAME" , radio_value, "Plantae", 85, 100)

    search_phylum_fungi_menu =createRadioButton (phylum_frame ,"Fungi", "darkgrey" , "NAME" , radio_value, "Fungi", 150, 100)

    search_phylum_protista_menu =createRadioButton (phylum_frame ,"Protista", "darkgrey" , "NAME" , radio_value, "Protista", 215, 100)

    search_phylum_monera_menu =createRadioButton (phylum_frame ,"Monera", "darkgrey" , "Monera" , radio_value, "Animalia", 295, 100)

    result_frame = createFrame(phylum_frame,  "#c850c0",  2, "transparent", 15, 173, 790, 333)

    label = createSearchResultLabel(phylum_frame)
    
    combo = CTkComboBox(phylum_frame, width = 200)
    combo["values"] = ("Choose", "An", "Option!")
    combo.set("Please Choose An Option!")
    #combo.current()
    contents = StringVar()
    combo["textvariable"] = contents
    combo.place(x = 10, y = 130)
    
    def on_pylum_search_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        ypos = 10 
        tosearch = combo.get()
        tosearch = tosearch.title() + ":"
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum = '"+tosearch+"' "):
            label = CTkLabel(result_frame, text = row,font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
            label.place(x = 1, y = ypos)
            ypos = ypos + 27


    global search_btn
    search_btn = CTkButton(phylum_frame, text = "SEARCH", fg_color = "dodgerblue3", hover_color = "#c850c0", corner_radius = 40, 
                           command = on_pylum_search_btn_click())
    search_btn.place(x = 230, y = 130)

def class_page():

    class_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(class_frame, "CLASS")
    label = createSearchByLabel(class_frame)

    result_frame = createFrame(class_frame,  "#c850c0",  2, "transparent", 15, 153, 790, 353)

    search = createSearchEntry(class_frame)
    global contents
    contents = StringVar()
    contents.set("Search For Classes.")
    search["textvariable"] = contents

    def on_class_search_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
        else:
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
 
    search_btn = createSearchButton(class_frame, on_class_search_click)

    label = createSearchResultLabel(class_frame, _isafterclasspage = True)

def order_page():

    order_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(order_frame, "ORDER")

    label = createSearchByLabel(order_frame)

    result_frame = createFrame(order_frame,  "#c850c0",  2, "transparent", 15, 153, 790, 353)

    search = createSearchEntry(order_frame)
    contents = StringVar()
    contents.set("Search For Orders")
    search["textvariable"] = contents

    def on_order_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
        else:
            for label in result_frame.winfo_children():
                label.destroy()
            ypos = 10
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder = '"+tosearch+"' "):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27
 
    search_btn = createSearchButton(order_frame, on_order_page_search_btn_click)

    label = createSearchResultLabel(order_frame, _isafterclasspage = True)

def family_page():

    family_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(family_frame, "FAMILY")

    label = createSearchByLabel(family_frame)

    search = createSearchEntry(family_frame)
    contents = StringVar()
    contents.set("Search For Family.")
    search["textvariable"] = contents

    def on_family_page_search_btn_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            ypos = 170
            for label in result_frame.winfo_children():
                #label.destroy()
                pass
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family = '"+tosearch+"' "):
                label = CTkLabel(family_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

    result_frame = createFrame(family_frame,  "#c850c0",  2, "transparent", 15, 153, 790, 353)
    
    search_btn =createSearchButton(family_frame, on_family_page_search_btn_click)
    label = createSearchResultLabel(family_frame, _isafterclasspage = True)

def genus_page():

    genus_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(genus_frame, "GENUS")

    label = createSearchByLabel(genus_frame)

    def on_genus_search_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            ypos = 170
            for label in result_frame.winfo_children():
                #label.destroy()
                pass
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus = '"+tosearch+"' "):
                label = CTkLabel(genus_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

    search = createSearchEntry(genus_frame)
    contents = StringVar()
    contents.set("Search For Genus.")
    search["textvariable"] = contents
    
    result_frame = createFrame(genus_frame,  "#c850c0",  2, "transparent", 15, 153, 790, 353)

    search_btn = createSearchButton(genus_frame, on_genus_search_click)

    label = createSearchResultLabel(genus_frame, _isafterclasspage = True)

def species_page():
    species_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(species_frame, "SPEICES")

    label = createSearchByLabel(species_frame)

    def on_species_search_click():
        tosearch = ((contents.get())).title()
        if tosearch[-1]!= ":":
            tosearch = ((contents.get())).title() + ":"
        else:
            ypos = 170
            for label in result_frame.winfo_children():
                #label.destroy()
                pass
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species = '"+tosearch+"' "):
                label = CTkLabel(species_frame, text = row, font = ("Arial" , 10, "italic" ), fg_color = "darkgrey")
                label.place(x = 1, y = ypos)
                ypos = ypos + 27

    search = createSearchEntry(species_frame)
    contents = StringVar()
    contents.set("Search For Species.")
    search["textvariable"] = contents
    
    result_frame = createFrame(species_frame,  "#c850c0",  2, "transparent", 15, 153, 790, 353)

    search_btn =createSearchButton(species_frame, on_species_search_click)
    label = createSearchResultLabel(species_frame, _isafterclasspage = True)

def about_page():
    about_frame = createFrame(main_frame,  "dodgerblue3",  2, "transparent", _is_content_frame = True)

    label = createMainHeading(about_frame, "ABOUT")

    frame = createFrame(about_frame,  "#c850c0",  2, "transparent", 15, 70, 790, 436)

    label = CTkLabel(frame, text = "\
We are a group of students studying in XI std,\n\
<--CREDITS-->\n\
Ideaology --> Hari Dhejus V.S.\n\
Cheif Devoloper --> Hari Dhejus V.S.\n\
Co-Devoloper --> Anandha Krishnan\n\
Chief Biologist --> Pranav Krishna Prathap\n\
Co-Biologist-1-->Adharsh S.M.\n\
Co-Biologist2-->Akshay Ram R.F\n\
\n\
Contact us --> +91 948 668 3398\n\
\n\
        Thank you for using this program © AnimalTaxonaomy HAPAA™", 
                        font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = "#FFCC70")
    label.place(x = 120, y = 80)


#=-=-=-=-=-=-=-EXTRA-=-=-=-=-=-=-=#

def indicate(page):
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def insert():
    insert_root = CTk()
    insert_root.iconbitmap(r"icon/favicon6.ico")
    insert_root.geometry("400x300")
    insert_root.title("Insert")
    insert_root.maxsize(width = 400, height = 300)

    insert_frame = CTkFrame(insert_root, border_color = "#FFCC70", border_width = 2, width = 400, height = 300)
    insert_frame.pack()

    name_label = CTkLabel(insert_frame, text = "Name :-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    name_label.place(x = 5, y = 5)

    name_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    name_entry.place(x = 170, y = 5)

    kingdom_label = CTkLabel(insert_frame, text = "Kingdom:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    kingdom_label.place(x = 5, y = 35)

    kingdom_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    kingdom_entry.place(x = 170, y = 35)

    phylum_label = CTkLabel(insert_frame, text = "Phylum:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    phylum_label.place(x = 5, y = 65)

    phylum_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    phylum_entry.place(x = 170, y = 65)

    class_label = CTkLabel(insert_frame, text = "Class:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    class_label.place(x = 5, y = 95)

    class_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    class_entry.place(x = 170, y = 95)

    order_label = CTkLabel(insert_frame, text = "Order:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    order_label.place(x = 5, y = 125)

    order_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    order_entry.place(x = 170, y = 125)

    family_label = CTkLabel(insert_frame, text = "Family:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    family_label.place(x = 5, y = 155)

    family_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    family_entry.place(x = 170, y = 155)

    genus_label = CTkLabel(insert_frame, text = "Genus:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    genus_label.place(x = 5, y = 185)

    genus_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    genus_entry.place(x = 170, y = 185)

    species_label = CTkLabel(insert_frame, text = "Species:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    species_label.place(x = 5, y = 215)

    species_entry = CTkEntry(insert_frame, text_color = "#c850c0")
    species_entry.place(x = 170, y = 215)
    
    def insert():
        _name = name_entry.get()
        _kingdom = kingdom_entry.get()
        _phylum = phylum_entry.get()
        _class = class_entry.get()
        _order = order_entry.get()
        _family = family_entry.get()
        _genus = genus_entry.get()
        _species = species_entry.get()

        cur.execute("INSERT INTO animal_details (name, kingdom, phylum, class, naturalorder, family, genus, species) VALUES (?,?,?,?,?,?,?,?)",
                    (_name, _kingdom, _phylum, _class, _order, _family, _genus, _species))
        con.commit()

    insert_btn = createButton(insert_frame, "Insert", 40, insert, 40, 255)

    def back_to_admin_console():
        insert_root.destroy()

    back_btn = createButton(insert_frame, "Back", 40, back_to_admin_console, 210, 255)

    insert_root.mainloop()

def update():
    pass

def delete():
    delete_root = CTk()
    delete_root.iconbitmap(r"icon/favicon6.ico")
    delete_root.geometry("400x70")
    delete_root.title("Delete")
    delete_root.maxsize(width = 400, height = 70)

    delete_frame = CTkFrame(delete_root, border_color = "#FFCC70", border_width = 2, width = 400, height = 70)
    delete_frame.pack()

    name_label = CTkLabel(delete_frame, text = "Name :-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = "dodgerblue3")
    name_label.place(x = 5, y = 5)

    name_entry = CTkEntry(delete_frame, text_color = "#c850c0")
    name_entry.place(x = 170, y = 5)
    
    def delete():
        _name = name_entry.get()

        cur.execute("UPDATE animal_details set active = 0 WHERE name = '"+_name+"'")
        con.commit()
    
    insert_btn = createButton(delete_frame, "Delete", 40, delete, 40, 40)


    def back_to_admin_console():
        delete_root.destroy()

    back_btn = createButton(delete_frame, "Back", 40, back_to_admin_console, 210, 40)

    delete_root.mainloop()

    root.destroy()


def back_to_main_console():
    root.destroy()
    call(["python", glb_current_working_directory + "/Animal_Taxonamy_Ctk_Main.py"])


menu_frame = CTkFrame(root, fg_color = "transparent")

crud_frame = createFrame(menu_frame, "dodgerblue3",  border_line_size_2, glb_fg_color_transparent , 5, 5, 150, glb_crud_frame_height)


insert_btn = createImageButton(crud_frame, "", "add.png", 100, insert, 25, 8)

edit_btn = createImageButton(crud_frame, "", "edit_blue.png", 100, update, 85, 8)

delete_btn = createImageButton(crud_frame, "", "delete.png", 100, delete, 25, 48)

back_btn = createImageButton(crud_frame, "", "previous.png", 100, back_to_main_console, 85, 48)

home_btn = createMenuButton(menu_frame, "Home", indicate, home_page, crud_frame)

kingdom_btn = createMenuButton(menu_frame, "Kingdom", indicate, kingdom_page, home_btn)

phylum_btn =  createMenuButton(menu_frame, "Phylum-\n-Division", indicate, phylum_page, kingdom_btn)

class_btn =  createMenuButton(menu_frame, "Class", indicate, class_page, phylum_btn, _add_ypos = 25)

order_btn =  createMenuButton(menu_frame, "Order", indicate, order_page, class_btn)

family_btn = createMenuButton(menu_frame, "Family", indicate, family_page, order_btn)

genus_btn = createMenuButton(menu_frame, "Genus", indicate, genus_page, family_btn)

species_btn = createMenuButton(menu_frame, "Species", indicate, species_page, genus_btn)

about_btn = createMenuButton(menu_frame, "About", indicate, about_page, species_btn)

menu_frame.pack(side = "left")
menu_frame.pack_propagate(False)
menu_frame.configure(width = 150, height = 550)

main_frame = createFrame(root,  "#FFCC70",  3, "transparent", 0 , 0, 950, 550)
main_frame.pack(side = "left")
main_frame.pack_propagate(False)

root.mainloop()