################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Minigame screens
################################################################################

# define for better performance.
define total_health = 5
default health = 5
default position = 1
default fruit = "grape"  # kana=apple, aiko=blueberry, sumi=grape, hana=banana
default win = False
default minigame_mode = False
default toffset = 1.0  # Time offset
define app_time = 1.0  # Approach time

transform t_bowl(x_to):  # transform bowl
    subpixel True
    
    on show:
        xpos 1002+(269*position)
    on update, replaced:
        easein_quad 0.125 xpos x_to
        
transform ds_in(t=0.5):  # Dissolve in
    alpha 0.0
    linear t alpha 1.0
    
    on hide:
        linear t alpha 0.0

# 128x128px fruit
transform fall(x_from, dur):
    crop_relative True ycenter 1.0
    xpos x_from ypos 62 crop(0, 1.0, 1.0, 1.0) alpha 0.0  # -50+112
    parallel:
        linear dur ypos 814  #750+int(128*0.5)
    parallel:
        linear dur*7/47 crop(0, 0.0, 1.0, 1.0) alpha 1.0  # dur*8/47
    pass
    parallel:
        linear dur*157/376 ypos 1128  #1000+128  # dur*5/16
    parallel:
        pause (dur*93/376)/1.45
        linear dur*4/47 crop(0, 0.0, 1.0, 0.0) alpha 0.0  # dur*8/47
        
    on hide:
        linear 0.5 alpha 0.0

# Lane 1
screen lane_1(dur):
    add "gui/minigame/"+fruit+".png" at fall(1033, dur)
    timer dur action If(position == 0, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_1")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_1")
screen lane_11(dur):
    add "gui/minigame/"+fruit+".png" at fall(1033, dur)
    timer dur action If(position == 0, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_11")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_11")
screen lane_12(dur):
    add "gui/minigame/"+fruit+".png" at fall(1033, dur)
    timer dur action If(position == 0, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_12")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_12")
screen lane_13(dur):
    add "gui/minigame/"+fruit+".png" at fall(1033, dur)
    timer dur action If(position == 0, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_13")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_13")
    
# Lane 2
screen lane_2(dur):
    add "gui/minigame/"+fruit+".png" at fall(1304, dur)
    timer dur action If(position == 1, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_2")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_2")
screen lane_21(dur):
    add "gui/minigame/"+fruit+".png" at fall(1304, dur)
    timer dur action If(position == 1, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_21")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_21")
screen lane_22(dur):
    add "gui/minigame/"+fruit+".png" at fall(1304, dur)
    timer dur action If(position == 1, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_22")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_22")
screen lane_23(dur):
    add "gui/minigame/"+fruit+".png" at fall(1304, dur)
    timer dur action If(position == 1, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_23")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_23")
    
# Lane 3
screen lane_3(dur):
    add "gui/minigame/"+fruit+".png" at fall(1573, dur)
    timer dur action If(position == 2, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_3")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_3")
screen lane_31(dur):
    add "gui/minigame/"+fruit+".png" at fall(1573, dur)
    timer dur action If(position == 2, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_31")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_31")
screen lane_32(dur):
    add "gui/minigame/"+fruit+".png" at fall(1573, dur)
    timer dur action If(position == 2, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_32")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_32")
screen lane_33(dur):
    add "gui/minigame/"+fruit+".png" at fall(1573, dur)
    timer dur action If(position == 2, true=(Play("sound", "soft_hitclap.wav"), Hide("lane_33")), false=(SetVariable("health", health-1)))
    timer dur+(dur*157.0/376.0) action Hide("lane_33")

screen msg(txt="None", t=2):
    add "gui/minigame/message.png" at ds_in(0.325):
        align(0.1, 0.95)
        
    text "[txt]" at ds_in(0.325):
        xsize 650
        color "#44527C"
        font "roboto_reg.ttf"
        size 42
        pos(180, 820)
        justify True
        
    timer t action Hide("msg")

screen minigame(level=1): # Level 1 = tutorial; Level 2-3 = Aiko; Level 4-5 = Sumi; Level 6-7 = Hana
    
    modal True
    
    add "gui/ui/bg.jpg"
    
    add "gui/minigame/bg.png":
        align(0.9125, 0.5)
        
    add "gui/minigame/inner_bg_pink.png":
        align(0.9, 0.5)
        
    add "gui/minigame/inner_line.png":
        align(0.9, 0.5)
    
    # If check fruit
    if level == 1:
        add "mkana_a":
            align(0.175, -0.25)
    elif level == 2:
        add "maiko_a":
            align(0.1125, -0.25)
    elif level == 3:
        add "maiko_b":
            align(0.1125, -0.25)
    elif level == 4:
        add "msumi_a":
            align(0.125, -0.25)
    elif level == 5:
        add "msumi_b":
            align(0.125, -0.25)
    elif level == 6:
        add "mhana_a":
            align(0.125, -0.25)
    elif level == 7:
        add "mhana_b":
            align(0.125, -0.25)
        
    # Health
    hbox:
        pos(335, 30)
        spacing 20
        
        for i in range(total_health):
            add "gui/ui/no_heart.png":
                zoom 0.67
    hbox:
        pos(335, 30)
        spacing 20
        
        for i in range(health):
            add "gui/ui/heart.png":
                zoom 0.67
                
    # 269px per lane
    add "gui/minigame/bowl.png" at t_bowl(1002+(269*position)):
        ypos 790
    
    if health > 0:
        
        if win:
        
            add "gui/overlay/confirm.png" at ds_in(1.0):
                alpha 0.75
             
            add "gui/minigame/win.png" at ds_in(1.0):
                align(0.5, 0.5)
            
            text "You win!" at ds_in(1.0):
                size 84
                yoffset 10
                color "#04C85C"
                align(0.5, 0.5)
                
            if level == 1:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level1")
            elif level == 2:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level2")
            elif level == 3:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level3")
            elif level == 4:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level4")
            elif level == 5:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level5")
            elif level == 6:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level6")
            elif level == 7:
                timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level7")
                
        else:
            
            # Control
            if position > 0:
                button:
                    area(0,0,0,0)
                    keysym "K_LEFT", "z"
                    
                    action SetVariable("position", position-1)
            if position < 2:
                button:
                    area(0,0,0,0)
                    keysym "K_RIGHT", "x"
                    
                    action SetVariable("position", position+1)
        
        # Gameplay
        
        if level == 1:
        
            timer 2.0 action Show("msg", txt="First things first, that <BOWL> down there, that is you.", t=4)
            timer 7.0 action Show("msg", txt="You can move your bowl to other lanes by using arrow keys or 'Z' or 'X' key.", t=4)
            timer 12.0 action Show("msg", txt="There will be falling <FRUITS> from above, your objective is to catch them.", t=4)
            timer 17.0 action Show("msg", txt="Careful though, if you miss a fruit, your <LIFE POINT> will decrease by 1.", t=4)
            timer 22.0 action Show("msg", txt="Don't miss up to 5 hearts or you'll fail.", t=3)
            timer 26.0 action Show("msg", txt="Alright, now give it a try yourself!", t=2)
            
            timer toffset action Play("music", "game_short.mp3", loop=False)
            
            timer 12.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 15.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 18.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 21.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 24.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 25.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 27.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 28.86+toffset-app_time action Show("lane_1", dur=app_time)
            timer 30.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 33.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 34.86+toffset-app_time action Show("lane_2", dur=app_time)
            timer 36.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 37.11+toffset-app_time action Show("lane_2", dur=app_time)
            timer 37.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 39.36+toffset-app_time action Show("lane_31", dur=app_time)
            timer 40.11+toffset-app_time action Show("lane_2", dur=app_time)
            timer 40.86+toffset-app_time action Show("lane_1", dur=app_time)
            timer 42.36+toffset-app_time action Show("lane_11", dur=app_time)
            timer 45.36+toffset-app_time action Show("lane_12", dur=app_time)
            timer 46.86+toffset-app_time action Show("lane_2", dur=app_time)
            timer 49.11+toffset-app_time action Show("lane_3", dur=app_time)
            timer 49.86+toffset-app_time action Show("lane_2", dur=app_time)
            timer 50.61+toffset-app_time action Show("lane_1", dur=app_time)
            timer 51.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 52.11+toffset-app_time action Show("lane_1", dur=app_time)
            timer 52.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 53.61+toffset-app_time action Show("lane_2", dur=app_time)
            timer 54.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 55.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 56.61+toffset-app_time action Show("lane_2", dur=app_time)
            timer 57.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 60.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 61.11+toffset-app_time action Show("lane_1", dur=app_time)
            timer 61.86+toffset-app_time action Show("lane_11", dur=app_time)
            timer 62.61+toffset-app_time action Show("lane_3", dur=app_time)
            timer 63.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 63.922+toffset-app_time action Show("lane_3", dur=app_time)
            timer 66.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 67.11+toffset-app_time action Show("lane_1", dur=app_time)
            timer 67.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 68.61+toffset-app_time action Show("lane_2", dur=app_time)
            timer 69.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 70.11+toffset-app_time action Show("lane_3", dur=app_time)
            timer 72.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 73.11+toffset-app_time action Show("lane_1", dur=app_time)
            timer 73.86+toffset-app_time action Show("lane_3", dur=app_time)
            timer 74.61+toffset-app_time action Show("lane_2", dur=app_time)
            timer 75.36+toffset-app_time action Show("lane_1", dur=app_time)
            timer 76.11+toffset-app_time action Show("lane_2", dur=app_time)
            timer 76.86+toffset-app_time action Show("lane_1", dur=app_time)
            timer 78.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 79.11+toffset-app_time action Show("lane_3", dur=app_time)
            timer 79.86+toffset-app_time action Show("lane_1", dur=app_time)
            timer 80.61+toffset-app_time action Show("lane_11", dur=app_time)
            timer 81.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 82.11+toffset-app_time action Show("lane_2", dur=app_time)
            timer 84.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 87.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 90.36+toffset-app_time action Show("lane_3", dur=app_time)
            timer 93.36+toffset-app_time action Show("lane_2", dur=app_time)
            timer 96.36+toffset-app_time action Show("lane_2", dur=app_time)
            
            timer 102.36+toffset action SetVariable("win", True)
        
        elif level == 2:
            
            timer toffset action Play("music", "wind.mp3", loop=False)
            
            timer 13.916+toffset-app_time action Show("lane_1", dur=app_time)
            timer 15.594+toffset-app_time action Show("lane_2", dur=app_time)
            timer 17.273+toffset-app_time action Show("lane_3", dur=app_time)
            timer 18.951+toffset-app_time action Show("lane_1", dur=app_time)
            timer 20.629+toffset-app_time action Show("lane_2", dur=app_time)
            timer 22.308+toffset-app_time action Show("lane_1", dur=app_time)
            timer 23.986+toffset-app_time action Show("lane_2", dur=app_time)
            timer 27.343+toffset-app_time action Show("lane_2", dur=app_time)
            timer 28.182+toffset-app_time action Show("lane_21", dur=app_time)
            timer 29.021+toffset-app_time action Show("lane_3", dur=app_time)
            timer 30.699+toffset-app_time action Show("lane_3", dur=app_time)
            timer 31.538+toffset-app_time action Show("lane_2", dur=app_time)
            timer 32.378+toffset-app_time action Show("lane_1", dur=app_time)
            timer 34.056+toffset-app_time action Show("lane_2", dur=app_time)
            timer 34.895+toffset-app_time action Show("lane_1", dur=app_time)
            timer 35.734+toffset-app_time action Show("lane_2", dur=app_time)
            timer 37.413+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.769+toffset-app_time action Show("lane_1", dur=app_time)
            timer 42.448+toffset-app_time action Show("lane_2", dur=app_time)
            timer 44.126+toffset-app_time action Show("lane_3", dur=app_time)
            timer 45.804+toffset-app_time action Show("lane_31", dur=app_time)
            timer 47.483+toffset-app_time action Show("lane_1", dur=app_time)
            timer 49.161+toffset-app_time action Show("lane_2", dur=app_time)
            timer 50.839+toffset-app_time action Show("lane_3", dur=app_time)
            timer 52.517+toffset-app_time action Show("lane_2", dur=app_time)
            timer 54.196+toffset-app_time action Show("lane_3", dur=app_time)
            timer 55.664+toffset-app_time action Show("lane_2", dur=app_time)
            timer 56.294+toffset-app_time action Show("lane_1", dur=app_time)
            timer 56.713+toffset-app_time action Show("lane_11", dur=app_time)
            timer 57.133+toffset-app_time action Show("lane_2", dur=app_time)
            timer 57.552+toffset-app_time action Show("lane_21", dur=app_time)
            timer 58.182+toffset-app_time action Show("lane_3", dur=app_time)
            timer 59.231+toffset-app_time action Show("lane_1", dur=app_time)
            timer 59.860+toffset-app_time action Show("lane_11", dur=app_time)
            timer 60.909+toffset-app_time action Show("lane_2", dur=app_time)
            timer 62.587+toffset-app_time action Show("lane_3", dur=app_time)
            timer 64.266+toffset-app_time action Show("lane_2", dur=app_time)
            timer 65.944+toffset-app_time action Show("lane_21", dur=app_time)
            timer 67.622+toffset-app_time action Show("lane_1", dur=app_time)
            timer 69.091+toffset-app_time action Show("lane_3", dur=app_time)
            timer 69.720+toffset-app_time action Show("lane_2", dur=app_time)
            timer 70.140+toffset-app_time action Show("lane_1", dur=app_time)
            timer 70.559+toffset-app_time action Show("lane_21", dur=app_time)
            timer 70.979+toffset-app_time action Show("lane_3", dur=app_time)
            timer 71.399+toffset-app_time action Show("lane_31", dur=app_time)
            timer 71.608+toffset-app_time action Show("lane_32", dur=app_time)
            timer 72.238+toffset-app_time action Show("lane_2", dur=app_time)
            timer 72.657+toffset-app_time action Show("lane_21", dur=app_time)
            timer 73.287+toffset-app_time action Show("lane_1", dur=app_time)
            timer 74.336+toffset-app_time action Show("lane_2", dur=app_time)
            timer 75.175+toffset-app_time action Show("lane_1", dur=app_time)
            timer 76.014+toffset-app_time action Show("lane_3", dur=app_time)
            timer 76.853+toffset-app_time action Show("lane_1", dur=app_time)
            timer 77.692+toffset-app_time action Show("lane_2", dur=app_time)
            timer 78.531+toffset-app_time action Show("lane_1", dur=app_time)
            timer 80.210+toffset-app_time action Show("lane_11", dur=app_time)
            timer 81.049+toffset-app_time action Show("lane_2", dur=app_time)
            timer 82.517+toffset-app_time action Show("lane_1", dur=app_time)
            timer 84.406+toffset-app_time action Show("lane_2", dur=app_time)
            timer 86.084+toffset-app_time action Show("lane_3", dur=app_time)
            timer 87.762+toffset-app_time action Show("lane_2", dur=app_time)
            timer 89.441+toffset-app_time action Show("lane_3", dur=app_time)
            timer 91.119+toffset-app_time action Show("lane_2", dur=app_time)
            timer 92.587+toffset-app_time action Show("lane_1", dur=app_time)
            
            timer 97.832+toffset action SetVariable("win", True)
            
        elif level == 3:
            
            timer toffset action Play("music", "yutori_adv_short.mp3", loop=False)
            
            timer 06.147+toffset-app_time action Show("lane_2", dur=app_time)
            timer 06.821+toffset-app_time action Show("lane_21", dur=app_time)
            timer 07.495+toffset-app_time action Show("lane_22", dur=app_time)
            timer 08.169+toffset-app_time action Show("lane_23", dur=app_time)
            timer 08.506+toffset-app_time action Show("lane_3", dur=app_time)
            timer 08.844+toffset-app_time action Show("lane_2", dur=app_time)
            timer 09.518+toffset-app_time action Show("lane_21", dur=app_time)
            timer 10.192+toffset-app_time action Show("lane_22", dur=app_time)
            timer 10.866+toffset-app_time action Show("lane_23", dur=app_time)
            timer 11.203+toffset-app_time action Show("lane_1", dur=app_time)
            timer 11.540+toffset-app_time action Show("lane_2", dur=app_time)
            timer 11.877+toffset-app_time action Show("lane_21", dur=app_time)
            timer 12.383+toffset-app_time action Show("lane_3", dur=app_time)
            timer 12.888+toffset-app_time action Show("lane_2", dur=app_time)
            timer 13.226+toffset-app_time action Show("lane_1", dur=app_time)
            timer 13.563+toffset-app_time action Show("lane_21", dur=app_time)
            timer 13.900+toffset-app_time action Show("lane_3", dur=app_time)
            timer 14.405+toffset-app_time action Show("lane_31", dur=app_time)
            timer 14.911+toffset-app_time action Show("lane_2", dur=app_time)
            timer 15.754+toffset-app_time action Show("lane_1", dur=app_time)
            timer 16.259+toffset-app_time action Show("lane_11", dur=app_time)
            timer 16.596+toffset-app_time action Show("lane_2", dur=app_time)
            timer 17.776+toffset-app_time action Show("lane_21", dur=app_time)
            timer 18.282+toffset-app_time action Show("lane_3", dur=app_time)
            timer 18.619+toffset-app_time action Show("lane_22", dur=app_time)
            timer 19.293+toffset-app_time action Show("lane_23", dur=app_time)
            timer 19.799+toffset-app_time action Show("lane_1", dur=app_time)
            timer 21.821+toffset-app_time action Show("lane_1", dur=app_time)
            timer 22.327+toffset-app_time action Show("lane_2", dur=app_time)
            timer 22.664+toffset-app_time action Show("lane_21", dur=app_time)
            timer 23.169+toffset-app_time action Show("lane_3", dur=app_time)
            timer 23.675+toffset-app_time action Show("lane_22", dur=app_time)
            timer 24.012+toffset-app_time action Show("lane_1", dur=app_time)
            timer 24.349+toffset-app_time action Show("lane_23", dur=app_time)
            timer 24.686+toffset-app_time action Show("lane_3", dur=app_time)
            timer 25.192+toffset-app_time action Show("lane_31", dur=app_time)
            timer 25.697+toffset-app_time action Show("lane_2", dur=app_time)
            timer 26.540+toffset-app_time action Show("lane_21", dur=app_time)
            timer 27.046+toffset-app_time action Show("lane_22", dur=app_time)
            timer 27.383+toffset-app_time action Show("lane_3", dur=app_time)
            timer 28.563+toffset-app_time action Show("lane_2", dur=app_time)
            timer 29.068+toffset-app_time action Show("lane_3", dur=app_time)
            timer 29.405+toffset-app_time action Show("lane_21", dur=app_time)
            timer 30.080+toffset-app_time action Show("lane_3", dur=app_time)
            timer 30.585+toffset-app_time action Show("lane_2", dur=app_time)
            timer 32.608+toffset-app_time action Show("lane_2", dur=app_time)
            timer 33.956+toffset-app_time action Show("lane_1", dur=app_time)
            timer 35.304+toffset-app_time action Show("lane_2", dur=app_time)
            timer 36.653+toffset-app_time action Show("lane_1", dur=app_time)
            timer 38.169+toffset-app_time action Show("lane_2", dur=app_time)
            timer 39.349+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.697+toffset-app_time action Show("lane_2", dur=app_time)
            timer 42.214+toffset-app_time action Show("lane_3", dur=app_time)
            timer 43.394+toffset-app_time action Show("lane_1", dur=app_time)
            timer 44.068+toffset-app_time action Show("lane_3", dur=app_time)
            timer 44.742+toffset-app_time action Show("lane_2", dur=app_time)
            timer 45.417+toffset-app_time action Show("lane_1", dur=app_time)
            timer 46.091+toffset-app_time action Show("lane_3", dur=app_time)
            timer 46.765+toffset-app_time action Show("lane_2", dur=app_time)
            timer 47.439+toffset-app_time action Show("lane_1", dur=app_time)
            timer 50.136+toffset-app_time action Show("lane_2", dur=app_time)
            timer 50.978+toffset-app_time action Show("lane_1", dur=app_time)
            timer 51.653+toffset-app_time action Show("lane_2", dur=app_time)
            timer 52.327+toffset-app_time action Show("lane_21", dur=app_time)
            timer 53.001+toffset-app_time action Show("lane_3", dur=app_time)
            timer 53.675+toffset-app_time action Show("lane_2", dur=app_time)
            timer 54.349+toffset-app_time action Show("lane_3", dur=app_time)
            timer 55.023+toffset-app_time action Show("lane_1", dur=app_time)
            timer 55.529+toffset-app_time action Show("lane_11", dur=app_time)
            timer 56.372+toffset-app_time action Show("lane_2", dur=app_time)
            timer 57.046+toffset-app_time action Show("lane_3", dur=app_time)
            timer 57.720+toffset-app_time action Show("lane_2", dur=app_time)
            timer 58.394+toffset-app_time action Show("lane_1", dur=app_time)
            timer 59.068+toffset-app_time action Show("lane_2", dur=app_time)
            timer 59.742+toffset-app_time action Show("lane_1", dur=app_time)
            timer 60.417+toffset-app_time action Show("lane_2", dur=app_time)
            timer 60.922+toffset-app_time action Show("lane_3", dur=app_time)
            timer 61.765+toffset-app_time action Show("lane_2", dur=app_time)
            timer 62.439+toffset-app_time action Show("lane_3", dur=app_time)
            timer 63.113+toffset-app_time action Show("lane_2", dur=app_time)
            timer 63.787+toffset-app_time action Show("lane_1", dur=app_time)
            timer 64.462+toffset-app_time action Show("lane_2", dur=app_time)
            timer 65.136+toffset-app_time action Show("lane_3", dur=app_time)
            timer 65.810+toffset-app_time action Show("lane_31", dur=app_time)
            timer 66.315+toffset-app_time action Show("lane_1", dur=app_time)
            timer 67.158+toffset-app_time action Show("lane_11", dur=app_time)
            timer 67.832+toffset-app_time action Show("lane_3", dur=app_time)
            timer 68.506+toffset-app_time action Show("lane_2", dur=app_time)
            timer 69.181+toffset-app_time action Show("lane_1", dur=app_time)
            timer 69.855+toffset-app_time action Show("lane_3", dur=app_time)
            timer 70.529+toffset-app_time action Show("lane_1", dur=app_time)
            timer 71.203+toffset-app_time action Show("lane_2", dur=app_time)
            timer 72.214+toffset-app_time action Show("lane_21", dur=app_time)
            timer 72.888+toffset-app_time action Show("lane_22", dur=app_time)
            timer 73.563+toffset-app_time action Show("lane_23", dur=app_time)
            timer 74.237+toffset-app_time action Show("lane_2", dur=app_time)
            timer 74.574+toffset-app_time action Show("lane_3", dur=app_time)
            timer 74.911+toffset-app_time action Show("lane_21", dur=app_time)
            timer 75.585+toffset-app_time action Show("lane_22", dur=app_time)
            timer 76.259+toffset-app_time action Show("lane_23", dur=app_time)
            timer 76.933+toffset-app_time action Show("lane_2", dur=app_time)
            timer 77.271+toffset-app_time action Show("lane_1", dur=app_time)
            timer 77.608+toffset-app_time action Show("lane_21", dur=app_time)
            timer 78.282+toffset-app_time action Show("lane_22", dur=app_time)
            timer 78.956+toffset-app_time action Show("lane_23", dur=app_time)
            timer 79.630+toffset-app_time action Show("lane_2", dur=app_time)
            timer 79.967+toffset-app_time action Show("lane_3", dur=app_time)
            timer 80.304+toffset-app_time action Show("lane_21", dur=app_time)
            timer 80.978+toffset-app_time action Show("lane_22", dur=app_time)
            timer 81.653+toffset-app_time action Show("lane_23", dur=app_time)
            timer 81.990+toffset-app_time action Show("lane_2", dur=app_time)
            timer 82.495+toffset-app_time action Show("lane_1", dur=app_time)
            
            timer 86.372+toffset action SetVariable("win", True)
            
        elif level == 7:  # Was 4
            
            timer toffset action Play("music", "daybreak.mp3", loop=False)
            
            timer 12.864+toffset-app_time action Show("lane_1", dur=app_time)
            timer 13.221+toffset-app_time action Show("lane_2", dur=app_time)
            timer 13.578+toffset-app_time action Show("lane_3", dur=app_time)
            timer 14.114+toffset-app_time action Show("lane_31", dur=app_time)
            timer 14.650+toffset-app_time action Show("lane_2", dur=app_time)
            timer 15.007+toffset-app_time action Show("lane_1", dur=app_time)
            timer 15.721+toffset-app_time action Show("lane_2", dur=app_time)
            timer 16.078+toffset-app_time action Show("lane_1", dur=app_time)
            timer 18.578+toffset-app_time action Show("lane_1", dur=app_time)
            timer 18.935+toffset-app_time action Show("lane_2", dur=app_time)
            timer 19.292+toffset-app_time action Show("lane_3", dur=app_time)
            timer 19.828+toffset-app_time action Show("lane_31", dur=app_time)
            timer 20.364+toffset-app_time action Show("lane_2", dur=app_time)
            timer 20.721+toffset-app_time action Show("lane_21", dur=app_time)
            timer 21.435+toffset-app_time action Show("lane_1", dur=app_time)
            timer 21.792+toffset-app_time action Show("lane_11", dur=app_time)
            timer 24.292+toffset-app_time action Show("lane_3", dur=app_time)
            timer 24.650+toffset-app_time action Show("lane_2", dur=app_time)
            timer 25.721+toffset-app_time action Show("lane_2", dur=app_time)
            timer 26.078+toffset-app_time action Show("lane_1", dur=app_time)
            timer 27.149+toffset-app_time action Show("lane_1", dur=app_time)
            timer 27.507+toffset-app_time action Show("lane_2", dur=app_time)
            timer 28.578+toffset-app_time action Show("lane_1", dur=app_time)
            timer 28.935+toffset-app_time action Show("lane_3", dur=app_time)
            timer 30.007+toffset-app_time action Show("lane_2", dur=app_time)
            timer 30.364+toffset-app_time action Show("lane_1", dur=app_time)
            timer 31.792+toffset-app_time action Show("lane_2", dur=app_time)
            timer 32.149+toffset-app_time action Show("lane_3", dur=app_time)
            timer 33.221+toffset-app_time action Show("lane_2", dur=app_time)
            timer 37.149+toffset-app_time action Show("lane_1", dur=app_time)
            timer 37.507+toffset-app_time action Show("lane_2", dur=app_time)
            timer 37.864+toffset-app_time action Show("lane_3", dur=app_time)
            timer 38.578+toffset-app_time action Show("lane_2", dur=app_time)
            timer 38.935+toffset-app_time action Show("lane_1", dur=app_time)
            timer 39.649+toffset-app_time action Show("lane_11", dur=app_time)
            timer 40.364+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.721+toffset-app_time action Show("lane_31", dur=app_time)
            timer 41.435+toffset-app_time action Show("lane_2", dur=app_time)
            timer 41.792+toffset-app_time action Show("lane_1", dur=app_time)
            timer 42.507+toffset-app_time action Show("lane_3", dur=app_time)
            timer 42.864+toffset-app_time action Show("lane_2", dur=app_time)
            timer 43.221+toffset-app_time action Show("lane_1", dur=app_time)
            timer 44.292+toffset-app_time action Show("lane_1", dur=app_time)
            timer 44.649+toffset-app_time action Show("lane_2", dur=app_time)
            timer 45.007+toffset-app_time action Show("lane_3", dur=app_time)
            timer 45.364+toffset-app_time action Show("lane_21", dur=app_time)
            timer 45.721+toffset-app_time action Show("lane_11", dur=app_time)
            timer 46.078+toffset-app_time action Show("lane_22", dur=app_time)
            timer 46.435+toffset-app_time action Show("lane_12", dur=app_time)
            timer 49.292+toffset-app_time action Show("lane_3", dur=app_time)
            timer 50.007+toffset-app_time action Show("lane_2", dur=app_time)
            timer 50.364+toffset-app_time action Show("lane_1", dur=app_time)
            timer 51.078+toffset-app_time action Show("lane_11", dur=app_time)
            timer 51.792+toffset-app_time action Show("lane_3", dur=app_time)
            timer 52.149+toffset-app_time action Show("lane_31", dur=app_time)
            timer 52.864+toffset-app_time action Show("lane_2", dur=app_time)
            timer 53.221+toffset-app_time action Show("lane_1", dur=app_time)
            timer 53.935+toffset-app_time action Show("lane_3", dur=app_time)
            timer 54.292+toffset-app_time action Show("lane_2", dur=app_time)
            timer 54.649+toffset-app_time action Show("lane_1", dur=app_time)
            timer 55.721+toffset-app_time action Show("lane_1", dur=app_time)
            timer 56.078+toffset-app_time action Show("lane_2", dur=app_time)
            timer 56.435+toffset-app_time action Show("lane_3", dur=app_time)
            timer 56.792+toffset-app_time action Show("lane_21", dur=app_time)
            timer 57.149+toffset-app_time action Show("lane_1", dur=app_time)
            timer 57.507+toffset-app_time action Show("lane_2", dur=app_time)
            timer 57.864+toffset-app_time action Show("lane_11", dur=app_time)
            # Break
            timer 65.444+toffset-app_time action Show("lane_1", dur=app_time)
            timer 65.801+toffset-app_time action Show("lane_2", dur=app_time)
            timer 66.158+toffset-app_time action Show("lane_3", dur=app_time)
            timer 66.694+toffset-app_time action Show("lane_31", dur=app_time)
            timer 67.230+toffset-app_time action Show("lane_2", dur=app_time)
            timer 67.587+toffset-app_time action Show("lane_1", dur=app_time)
            timer 68.301+toffset-app_time action Show("lane_2", dur=app_time)
            timer 68.658+toffset-app_time action Show("lane_1", dur=app_time)
            timer 71.158+toffset-app_time action Show("lane_1", dur=app_time)
            timer 71.515+toffset-app_time action Show("lane_2", dur=app_time)
            timer 71.872+toffset-app_time action Show("lane_3", dur=app_time)
            timer 72.408+toffset-app_time action Show("lane_31", dur=app_time)
            timer 72.944+toffset-app_time action Show("lane_2", dur=app_time)
            timer 73.301+toffset-app_time action Show("lane_21", dur=app_time)
            timer 74.015+toffset-app_time action Show("lane_1", dur=app_time)
            timer 74.372+toffset-app_time action Show("lane_11", dur=app_time)
            timer 76.872+toffset-app_time action Show("lane_3", dur=app_time)
            timer 77.230+toffset-app_time action Show("lane_2", dur=app_time)
            timer 78.301+toffset-app_time action Show("lane_2", dur=app_time)
            timer 78.658+toffset-app_time action Show("lane_1", dur=app_time)
            timer 79.730+toffset-app_time action Show("lane_3", dur=app_time)
            timer 80.087+toffset-app_time action Show("lane_2", dur=app_time)
            timer 81.158+toffset-app_time action Show("lane_1", dur=app_time)
            timer 81.515+toffset-app_time action Show("lane_2", dur=app_time)
            timer 82.587+toffset-app_time action Show("lane_1", dur=app_time)
            timer 82.944+toffset-app_time action Show("lane_11", dur=app_time)
            timer 84.372+toffset-app_time action Show("lane_1", dur=app_time)
            timer 84.730+toffset-app_time action Show("lane_2", dur=app_time)
            timer 85.444+toffset-app_time action Show("lane_3", dur=app_time)
            timer 85.801+toffset-app_time action Show("lane_2", dur=app_time)
            timer 89.551+toffset-app_time action Show("lane_1", dur=app_time)
            timer 89.908+toffset-app_time action Show("lane_2", dur=app_time)
            timer 90.444+toffset-app_time action Show("lane_3", dur=app_time)
            timer 91.158+toffset-app_time action Show("lane_31", dur=app_time)
            timer 91.515+toffset-app_time action Show("lane_2", dur=app_time)
            timer 92.229+toffset-app_time action Show("lane_1", dur=app_time)
            timer 92.944+toffset-app_time action Show("lane_3", dur=app_time)
            timer 93.301+toffset-app_time action Show("lane_31", dur=app_time)
            timer 93.658+toffset-app_time action Show("lane_32", dur=app_time)
            timer 94.015+toffset-app_time action Show("lane_2", dur=app_time)
            timer 94.372+toffset-app_time action Show("lane_1", dur=app_time)
            timer 95.087+toffset-app_time action Show("lane_3", dur=app_time)
            timer 95.444+toffset-app_time action Show("lane_2", dur=app_time)
            timer 95.801+toffset-app_time action Show("lane_1", dur=app_time)
            timer 96.872+toffset-app_time action Show("lane_1", dur=app_time)
            timer 97.229+toffset-app_time action Show("lane_2", dur=app_time)
            timer 97.587+toffset-app_time action Show("lane_3", dur=app_time)
            timer 97.944+toffset-app_time action Show("lane_31", dur=app_time)
            timer 98.301+toffset-app_time action Show("lane_1", dur=app_time)
            timer 98.658+toffset-app_time action Show("lane_2", dur=app_time)
            timer 99.015+toffset-app_time action Show("lane_11", dur=app_time)
            timer 101.872+toffset-app_time action Show("lane_3", dur=app_time)
            timer 102.587+toffset-app_time action Show("lane_2", dur=app_time)
            timer 102.944+toffset-app_time action Show("lane_1", dur=app_time)
            timer 103.658+toffset-app_time action Show("lane_11", dur=app_time)
            timer 104.372+toffset-app_time action Show("lane_3", dur=app_time)
            timer 104.729+toffset-app_time action Show("lane_31", dur=app_time)
            timer 105.444+toffset-app_time action Show("lane_2", dur=app_time)
            timer 105.801+toffset-app_time action Show("lane_1", dur=app_time)
            timer 106.515+toffset-app_time action Show("lane_3", dur=app_time)
            timer 106.872+toffset-app_time action Show("lane_2", dur=app_time)
            timer 107.229+toffset-app_time action Show("lane_1", dur=app_time)
            timer 108.301+toffset-app_time action Show("lane_1", dur=app_time)
            timer 108.658+toffset-app_time action Show("lane_2", dur=app_time)
            timer 109.015+toffset-app_time action Show("lane_3", dur=app_time)
            timer 109.372+toffset-app_time action Show("lane_21", dur=app_time)
            timer 109.729+toffset-app_time action Show("lane_31", dur=app_time)
            timer 110.087+toffset-app_time action Show("lane_32", dur=app_time)
            timer 110.444+toffset-app_time action Show("lane_2", dur=app_time)
            
            timer 116.158+toffset action SetVariable("win", True)
        
        elif level == 5:
            
            timer toffset action Play("music", "mystation.mp3", loop=False)
            
            timer 09.270+toffset-app_time action Show("lane_1", dur=app_time)
            timer 09.815+toffset-app_time action Show("lane_11", dur=app_time)
            timer 10.360+toffset-app_time action Show("lane_12", dur=app_time)
            timer 10.633+toffset-app_time action Show("lane_13", dur=app_time)
            timer 10.906+toffset-app_time action Show("lane_1", dur=app_time)
            timer 11.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 11.997+toffset-app_time action Show("lane_21", dur=app_time)
            timer 12.542+toffset-app_time action Show("lane_22", dur=app_time)
            timer 12.815+toffset-app_time action Show("lane_23", dur=app_time)
            timer 13.088+toffset-app_time action Show("lane_2", dur=app_time)
            timer 13.633+toffset-app_time action Show("lane_1", dur=app_time)
            timer 14.179+toffset-app_time action Show("lane_11", dur=app_time)
            timer 14.724+toffset-app_time action Show("lane_12", dur=app_time)
            timer 14.997+toffset-app_time action Show("lane_13", dur=app_time)
            timer 15.270+toffset-app_time action Show("lane_1", dur=app_time)
            timer 15.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 16.360+toffset-app_time action Show("lane_31", dur=app_time)
            timer 16.906+toffset-app_time action Show("lane_32", dur=app_time)
            timer 17.179+toffset-app_time action Show("lane_33", dur=app_time)
            timer 17.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 17.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 18.542+toffset-app_time action Show("lane_21", dur=app_time)
            timer 19.088+toffset-app_time action Show("lane_22", dur=app_time)
            timer 19.360+toffset-app_time action Show("lane_23", dur=app_time)
            timer 19.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 20.179+toffset-app_time action Show("lane_3", dur=app_time)
            timer 20.724+toffset-app_time action Show("lane_31", dur=app_time)
            timer 21.270+toffset-app_time action Show("lane_32", dur=app_time)
            timer 21.542+toffset-app_time action Show("lane_33", dur=app_time)
            timer 21.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 22.360+toffset-app_time action Show("lane_1", dur=app_time)
            timer 22.906+toffset-app_time action Show("lane_11", dur=app_time)
            timer 23.451+toffset-app_time action Show("lane_12", dur=app_time)
            timer 23.724+toffset-app_time action Show("lane_13", dur=app_time)
            timer 23.997+toffset-app_time action Show("lane_1", dur=app_time)
            timer 24.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 25.088+toffset-app_time action Show("lane_21", dur=app_time)
            timer 25.633+toffset-app_time action Show("lane_22", dur=app_time)
            timer 25.906+toffset-app_time action Show("lane_23", dur=app_time)
            timer 26.179+toffset-app_time action Show("lane_2", dur=app_time)
            timer 26.724+toffset-app_time action Show("lane_1", dur=app_time)
            timer 27.270+toffset-app_time action Show("lane_2", dur=app_time)
            timer 27.815+toffset-app_time action Show("lane_11", dur=app_time)
            timer 28.088+toffset-app_time action Show("lane_21", dur=app_time)
            timer 28.360+toffset-app_time action Show("lane_22", dur=app_time)
            timer 28.906+toffset-app_time action Show("lane_23", dur=app_time)
            timer 29.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 29.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 30.270+toffset-app_time action Show("lane_31", dur=app_time)
            timer 30.542+toffset-app_time action Show("lane_32", dur=app_time)
            timer 31.088+toffset-app_time action Show("lane_1", dur=app_time)
            timer 31.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 32.179+toffset-app_time action Show("lane_11", dur=app_time)
            timer 32.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 32.724+toffset-app_time action Show("lane_22", dur=app_time)
            timer 33.270+toffset-app_time action Show("lane_3", dur=app_time)
            timer 33.815+toffset-app_time action Show("lane_2", dur=app_time)
            timer 34.360+toffset-app_time action Show("lane_31", dur=app_time)
            timer 34.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 34.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 35.451+toffset-app_time action Show("lane_23", dur=app_time)
            timer 35.997+toffset-app_time action Show("lane_1", dur=app_time)
            timer 36.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 36.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 37.088+toffset-app_time action Show("lane_31", dur=app_time)
            timer 37.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 38.179+toffset-app_time action Show("lane_1", dur=app_time)
            timer 38.724+toffset-app_time action Show("lane_11", dur=app_time)
            timer 38.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 39.270+toffset-app_time action Show("lane_21", dur=app_time)
            timer 39.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.360+toffset-app_time action Show("lane_31", dur=app_time)
            timer 40.906+toffset-app_time action Show("lane_2", dur=app_time)
            timer 41.179+toffset-app_time action Show("lane_32", dur=app_time)
            timer 41.451+toffset-app_time action Show("lane_33", dur=app_time)
            timer 41.997+toffset-app_time action Show("lane_3", dur=app_time)
            timer 42.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 43.633+toffset-app_time action Show("lane_3", dur=app_time)
            timer 44.179+toffset-app_time action Show("lane_2", dur=app_time)
            timer 44.724+toffset-app_time action Show("lane_31", dur=app_time)
            timer 45.270+toffset-app_time action Show("lane_21", dur=app_time)
            timer 45.542+toffset-app_time action Show("lane_32", dur=app_time)
            timer 45.815+toffset-app_time action Show("lane_33", dur=app_time)
            timer 46.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 46.906+toffset-app_time action Show("lane_3", dur=app_time)
            timer 47.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 47.724+toffset-app_time action Show("lane_1", dur=app_time)
            timer 47.997+toffset-app_time action Show("lane_11", dur=app_time)
            timer 48.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 49.088+toffset-app_time action Show("lane_3", dur=app_time)
            timer 49.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 50.179+toffset-app_time action Show("lane_31", dur=app_time)
            timer 50.724+toffset-app_time action Show("lane_22", dur=app_time)
            timer 51.542+toffset-app_time action Show("lane_1", dur=app_time)
            timer 52.360+toffset-app_time action Show("lane_3", dur=app_time)
            timer 52.906+toffset-app_time action Show("lane_2", dur=app_time)
            timer 53.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 53.997+toffset-app_time action Show("lane_21", dur=app_time)
            timer 54.270+toffset-app_time action Show("lane_3", dur=app_time)
            timer 54.542+toffset-app_time action Show("lane_31", dur=app_time)
            timer 55.088+toffset-app_time action Show("lane_2", dur=app_time)
            timer 55.633+toffset-app_time action Show("lane_1", dur=app_time)
            timer 56.179+toffset-app_time action Show("lane_21", dur=app_time)
            timer 56.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 56.724+toffset-app_time action Show("lane_31", dur=app_time)
            timer 57.270+toffset-app_time action Show("lane_2", dur=app_time)
            timer 57.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 58.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 58.633+toffset-app_time action Show("lane_11", dur=app_time)
            timer 58.906+toffset-app_time action Show("lane_12", dur=app_time)
            timer 59.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 59.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 60.270+toffset-app_time action Show("lane_21", dur=app_time)
            timer 61.088+toffset-app_time action Show("lane_3", dur=app_time)
            timer 61.633+toffset-app_time action Show("lane_22", dur=app_time)
            timer 62.179+toffset-app_time action Show("lane_31", dur=app_time)
            timer 62.724+toffset-app_time action Show("lane_23", dur=app_time)
            timer 62.997+toffset-app_time action Show("lane_32", dur=app_time)
            timer 63.270+toffset-app_time action Show("lane_33", dur=app_time)
            timer 63.815+toffset-app_time action Show("lane_2", dur=app_time)
            timer 64.360+toffset-app_time action Show("lane_1", dur=app_time)
            timer 64.906+toffset-app_time action Show("lane_21", dur=app_time)
            timer 65.179+toffset-app_time action Show("lane_11", dur=app_time)
            timer 65.451+toffset-app_time action Show("lane_12", dur=app_time)
            timer 65.997+toffset-app_time action Show("lane_22", dur=app_time)
            timer 66.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 66.815+toffset-app_time action Show("lane_31", dur=app_time)
            timer 67.633+toffset-app_time action Show("lane_2", dur=app_time)
            # Short break
            timer 69.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 70.088+toffset-app_time action Show("lane_2", dur=app_time)
            timer 70.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 70.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 71.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 71.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 72.542+toffset-app_time action Show("lane_1", dur=app_time)
            timer 73.088+toffset-app_time action Show("lane_2", dur=app_time)
            timer 73.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 73.633+toffset-app_time action Show("lane_22", dur=app_time)
            timer 73.906+toffset-app_time action Show("lane_1", dur=app_time)
            timer 74.179+toffset-app_time action Show("lane_11", dur=app_time)
            timer 74.451+toffset-app_time action Show("lane_12", dur=app_time)
            timer 74.724+toffset-app_time action Show("lane_13", dur=app_time)
            timer 75.270+toffset-app_time action Show("lane_2", dur=app_time)
            timer 75.542+toffset-app_time action Show("lane_21", dur=app_time)
            timer 76.906+toffset-app_time action Show("lane_3", dur=app_time)
            timer 77.315+toffset-app_time action Show("lane_2", dur=app_time)
            timer 77.724+toffset-app_time action Show("lane_1", dur=app_time)
            timer 77.997+toffset-app_time action Show("lane_21", dur=app_time)
            timer 78.270+toffset-app_time action Show("lane_22", dur=app_time)
            timer 78.542+toffset-app_time action Show("lane_11", dur=app_time)
            timer 78.815+toffset-app_time action Show("lane_23", dur=app_time)
            timer 79.088+toffset-app_time action Show("lane_2", dur=app_time)
            timer 79.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 79.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 80.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 80.997+toffset-app_time action Show("lane_11", dur=app_time)
            timer 81.270+toffset-app_time action Show("lane_2", dur=app_time)
            timer 81.542+toffset-app_time action Show("lane_21", dur=app_time)
            timer 81.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 82.088+toffset-app_time action Show("lane_22", dur=app_time)
            timer 82.633+toffset-app_time action Show("lane_23", dur=app_time)
            timer 83.179+toffset-app_time action Show("lane_1", dur=app_time)
            timer 83.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 83.724+toffset-app_time action Show("lane_21", dur=app_time)
            timer 83.997+toffset-app_time action Show("lane_3", dur=app_time)
            timer 84.270+toffset-app_time action Show("lane_22", dur=app_time)
            timer 84.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 85.633+toffset-app_time action Show("lane_11", dur=app_time)
            timer 86.724+toffset-app_time action Show("lane_2", dur=app_time)
            timer 87.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 88.360+toffset-app_time action Show("lane_31", dur=app_time)
            timer 88.906+toffset-app_time action Show("lane_32", dur=app_time)
            timer 89.179+toffset-app_time action Show("lane_2", dur=app_time)
            timer 89.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 89.997+toffset-app_time action Show("lane_1", dur=app_time)
            timer 90.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 90.815+toffset-app_time action Show("lane_31", dur=app_time)
            timer 91.088+toffset-app_time action Show("lane_32", dur=app_time)
            timer 91.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 91.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 91.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 92.179+toffset-app_time action Show("lane_1", dur=app_time)
            timer 92.724+toffset-app_time action Show("lane_2", dur=app_time)
            timer 92.997+toffset-app_time action Show("lane_21", dur=app_time)
            timer 94.360+toffset-app_time action Show("lane_1", dur=app_time)
            timer 94.770+toffset-app_time action Show("lane_2", dur=app_time)
            timer 95.179+toffset-app_time action Show("lane_3", dur=app_time)
            timer 95.451+toffset-app_time action Show("lane_31", dur=app_time)
            timer 95.724+toffset-app_time action Show("lane_32", dur=app_time)
            timer 95.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 96.270+toffset-app_time action Show("lane_21", dur=app_time)
            timer 96.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 96.815+toffset-app_time action Show("lane_31", dur=app_time)
            timer 97.088+toffset-app_time action Show("lane_22", dur=app_time)
            timer 97.360+toffset-app_time action Show("lane_23", dur=app_time)
            timer 97.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 97.906+toffset-app_time action Show("lane_1", dur=app_time)
            timer 98.724+toffset-app_time action Show("lane_3", dur=app_time)
            timer 99.270+toffset-app_time action Show("lane_2", dur=app_time)
            timer 99.542+toffset-app_time action Show("lane_31", dur=app_time)
            timer 100.088+toffset-app_time action Show("lane_21", dur=app_time)
            timer 100.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 101.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 101.724+toffset-app_time action Show("lane_23", dur=app_time)
            timer 101.997+toffset-app_time action Show("lane_2", dur=app_time)
            timer 102.270+toffset-app_time action Show("lane_11", dur=app_time)
            timer 103.088+toffset-app_time action Show("lane_21", dur=app_time)
            timer 104.179+toffset-app_time action Show("lane_3", dur=app_time)
            timer 105.270+toffset-app_time action Show("lane_31", dur=app_time)
            
            timer 113.997+toffset action SetVariable("win", True)
            
        elif level == 4:  # Was 6
            
            timer toffset action Play("music", "wish_short.mp3", loop=False)
            
            timer 09.269+toffset-app_time action Show("lane_1", dur=app_time)
            timer 09.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 09.815+toffset-app_time action Show("lane_21", dur=app_time)
            timer 10.087+toffset-app_time action Show("lane_3", dur=app_time)
            timer 11.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 11.724+toffset-app_time action Show("lane_2", dur=app_time)
            timer 11.996+toffset-app_time action Show("lane_21", dur=app_time)
            timer 12.269+toffset-app_time action Show("lane_1", dur=app_time)
            timer 13.633+toffset-app_time action Show("lane_1", dur=app_time)
            timer 13.906+toffset-app_time action Show("lane_2", dur=app_time)
            timer 14.178+toffset-app_time action Show("lane_21", dur=app_time)
            timer 14.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 15.269+toffset-app_time action Show("lane_31", dur=app_time)
            timer 15.815+toffset-app_time action Show("lane_2", dur=app_time)
            timer 16.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 17.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 17.996+toffset-app_time action Show("lane_2", dur=app_time)
            timer 18.815+toffset-app_time action Show("lane_11", dur=app_time)
            timer 19.633+toffset-app_time action Show("lane_12", dur=app_time)
            timer 20.178+toffset-app_time action Show("lane_2", dur=app_time)
            timer 20.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 20.996+toffset-app_time action Show("lane_1", dur=app_time)
            timer 21.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 21.815+toffset-app_time action Show("lane_21", dur=app_time)
            timer 22.087+toffset-app_time action Show("lane_22", dur=app_time)
            timer 22.906+toffset-app_time action Show("lane_1", dur=app_time)
            timer 23.178+toffset-app_time action Show("lane_11", dur=app_time)
            timer 23.996+toffset-app_time action Show("lane_2", dur=app_time)
            timer 24.542+toffset-app_time action Show("lane_1", dur=app_time)
            timer 25.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 26.178+toffset-app_time action Show("lane_3", dur=app_time)
            timer 27.269+toffset-app_time action Show("lane_2", dur=app_time)
            timer 28.360+toffset-app_time action Show("lane_1", dur=app_time)
            timer 28.906+toffset-app_time action Show("lane_21", dur=app_time)
            timer 29.178+toffset-app_time action Show("lane_22", dur=app_time)
            timer 29.724+toffset-app_time action Show("lane_11", dur=app_time)
            timer 30.269+toffset-app_time action Show("lane_23", dur=app_time)
            timer 30.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 30.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 31.087+toffset-app_time action Show("lane_31", dur=app_time)
            timer 32.178+toffset-app_time action Show("lane_2", dur=app_time)
            timer 32.587+toffset-app_time action Show("lane_3", dur=app_time)
            timer 32.996+toffset-app_time action Show("lane_21", dur=app_time)
            timer 33.269+toffset-app_time action Show("lane_22", dur=app_time)
            # Small break
            timer 35.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 35.996+toffset-app_time action Show("lane_3", dur=app_time)
            timer 36.542+toffset-app_time action Show("lane_21", dur=app_time)
            timer 37.087+toffset-app_time action Show("lane_1", dur=app_time)
            timer 37.360+toffset-app_time action Show("lane_11", dur=app_time)
            timer 37.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 38.178+toffset-app_time action Show("lane_3", dur=app_time)
            timer 38.724+toffset-app_time action Show("lane_21", dur=app_time)
            timer 39.815+toffset-app_time action Show("lane_2", dur=app_time)
            timer 40.087+toffset-app_time action Show("lane_21", dur=app_time)
            timer 40.360+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 41.178+toffset-app_time action Show("lane_23", dur=app_time)
            timer 41.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 41.996+toffset-app_time action Show("lane_3", dur=app_time)
            timer 42.542+toffset-app_time action Show("lane_21", dur=app_time)
            timer 43.087+toffset-app_time action Show("lane_1", dur=app_time)
            timer 43.360+toffset-app_time action Show("lane_11", dur=app_time)
            timer 43.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 44.178+toffset-app_time action Show("lane_21", dur=app_time)
            timer 44.451+toffset-app_time action Show("lane_22", dur=app_time)
            timer 44.724+toffset-app_time action Show("lane_3", dur=app_time)
            timer 45.269+toffset-app_time action Show("lane_23", dur=app_time)
            timer 45.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 46.087+toffset-app_time action Show("lane_11", dur=app_time)
            timer 46.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 46.906+toffset-app_time action Show("lane_3", dur=app_time)
            timer 47.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 47.996+toffset-app_time action Show("lane_22", dur=app_time)
            timer 48.269+toffset-app_time action Show("lane_23", dur=app_time)
            timer 48.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 49.087+toffset-app_time action Show("lane_2", dur=app_time)
            timer 49.633+toffset-app_time action Show("lane_1", dur=app_time)
            timer 50.178+toffset-app_time action Show("lane_21", dur=app_time)
            timer 50.451+toffset-app_time action Show("lane_22", dur=app_time)
            timer 50.724+toffset-app_time action Show("lane_3", dur=app_time)
            timer 51.269+toffset-app_time action Show("lane_2", dur=app_time)
            timer 51.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 52.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 52.906+toffset-app_time action Show("lane_31", dur=app_time)
            timer 53.451+toffset-app_time action Show("lane_22", dur=app_time)
            timer 53.996+toffset-app_time action Show("lane_23", dur=app_time)
            timer 54.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 55.087+toffset-app_time action Show("lane_21", dur=app_time)
            # Small break
            timer 57.269+toffset-app_time action Show("lane_1", dur=app_time)
            timer 57.542+toffset-app_time action Show("lane_11", dur=app_time)
            timer 57.815+toffset-app_time action Show("lane_2", dur=app_time)
            timer 58.360+toffset-app_time action Show("lane_3", dur=app_time)
            timer 58.906+toffset-app_time action Show("lane_21", dur=app_time)
            timer 59.178+toffset-app_time action Show("lane_22", dur=app_time)
            timer 59.451+toffset-app_time action Show("lane_3", dur=app_time)
            timer 59.996+toffset-app_time action Show("lane_1", dur=app_time)
            timer 60.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 61.087+toffset-app_time action Show("lane_31", dur=app_time)
            timer 61.360+toffset-app_time action Show("lane_32", dur=app_time)
            timer 61.633+toffset-app_time action Show("lane_21", dur=app_time)
            timer 62.178+toffset-app_time action Show("lane_22", dur=app_time)
            timer 62.451+toffset-app_time action Show("lane_23", dur=app_time)
            timer 62.724+toffset-app_time action Show("lane_3", dur=app_time)
            timer 63.269+toffset-app_time action Show("lane_2", dur=app_time)
            timer 63.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 64.087+toffset-app_time action Show("lane_11", dur=app_time)
            timer 64.360+toffset-app_time action Show("lane_21", dur=app_time)
            timer 64.906+toffset-app_time action Show("lane_22", dur=app_time)
            timer 65.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 65.996+toffset-app_time action Show("lane_11", dur=app_time)
            timer 66.269+toffset-app_time action Show("lane_12", dur=app_time)
            timer 66.542+toffset-app_time action Show("lane_2", dur=app_time)
            timer 67.087+toffset-app_time action Show("lane_21", dur=app_time)
            timer 67.633+toffset-app_time action Show("lane_3", dur=app_time)
            timer 67.906+toffset-app_time action Show("lane_31", dur=app_time)
            timer 68.178+toffset-app_time action Show("lane_2", dur=app_time)
            timer 68.724+toffset-app_time action Show("lane_21", dur=app_time)
            timer 68.996+toffset-app_time action Show("lane_22", dur=app_time)
            timer 69.269+toffset-app_time action Show("lane_1", dur=app_time)
            timer 69.815+toffset-app_time action Show("lane_11", dur=app_time)
            timer 70.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 70.906+toffset-app_time action Show("lane_3", dur=app_time)
            timer 71.178+toffset-app_time action Show("lane_31", dur=app_time)
            timer 71.451+toffset-app_time action Show("lane_21", dur=app_time)
            timer 71.996+toffset-app_time action Show("lane_22", dur=app_time)
            timer 72.542+toffset-app_time action Show("lane_1", dur=app_time)
            timer 73.087+toffset-app_time action Show("lane_11", dur=app_time)
            timer 73.360+toffset-app_time action Show("lane_12", dur=app_time)
            timer 73.633+toffset-app_time action Show("lane_2", dur=app_time)
            timer 74.724+toffset-app_time action Show("lane_21", dur=app_time)
            timer 75.269+toffset-app_time action Show("lane_3", dur=app_time)
            timer 75.815+toffset-app_time action Show("lane_22", dur=app_time)
            timer 76.360+toffset-app_time action Show("lane_23", dur=app_time)
            timer 76.906+toffset-app_time action Show("lane_1", dur=app_time)
            timer 77.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 77.996+toffset-app_time action Show("lane_21", dur=app_time)
            timer 78.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 79.087+toffset-app_time action Show("lane_22", dur=app_time)
            timer 79.633+toffset-app_time action Show("lane_23", dur=app_time)
            timer 80.178+toffset-app_time action Show("lane_1", dur=app_time)
            timer 80.724+toffset-app_time action Show("lane_2", dur=app_time)
            timer 81.269+toffset-app_time action Show("lane_21", dur=app_time)
            timer 81.815+toffset-app_time action Show("lane_3", dur=app_time)
            timer 82.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 82.906+toffset-app_time action Show("lane_21", dur=app_time)
            timer 83.178+toffset-app_time action Show("lane_22", dur=app_time)
            timer 83.451+toffset-app_time action Show("lane_1", dur=app_time)
            timer 83.996+toffset-app_time action Show("lane_23", dur=app_time)
            timer 84.542+toffset-app_time action Show("lane_3", dur=app_time)
            timer 85.087+toffset-app_time action Show("lane_2", dur=app_time)
            timer 85.633+toffset-app_time action Show("lane_1", dur=app_time)
            timer 86.178+toffset-app_time action Show("lane_2", dur=app_time)
            timer 86.724+toffset-app_time action Show("lane_3", dur=app_time)
            timer 87.269+toffset-app_time action Show("lane_2", dur=app_time)
            timer 87.815+toffset-app_time action Show("lane_1", dur=app_time)
            timer 88.360+toffset-app_time action Show("lane_2", dur=app_time)
            timer 88.906+toffset-app_time action Show("lane_3", dur=app_time)
            timer 89.451+toffset-app_time action Show("lane_2", dur=app_time)
            timer 89.996+toffset-app_time action Show("lane_1", dur=app_time)
            
            timer 91.633+toffset action SetVariable("win", True)
            
        elif level == 6:  # Was 7
            
            timer toffset action Play("music", "reunion_short.mp3", loop=False)
            
            timer 00.540+toffset-app_time action Show("lane_2", dur=app_time)
            timer 01.637+toffset-app_time action Show("lane_3", dur=app_time)
            timer 01.820+toffset-app_time action Show("lane_2", dur=app_time)
            timer 02.735+toffset-app_time action Show("lane_1", dur=app_time)
            timer 03.100+toffset-app_time action Show("lane_2", dur=app_time)
            timer 03.466+toffset-app_time action Show("lane_3", dur=app_time)
            timer 04.381+toffset-app_time action Show("lane_21", dur=app_time)
            timer 04.564+toffset-app_time action Show("lane_31", dur=app_time)
            timer 04.747+toffset-app_time action Show("lane_22", dur=app_time)
            timer 05.661+toffset-app_time action Show("lane_1", dur=app_time)
            timer 06.027+toffset-app_time action Show("lane_2", dur=app_time)
            timer 06.393+toffset-app_time action Show("lane_3", dur=app_time)
            timer 07.491+toffset-app_time action Show("lane_21", dur=app_time)
            timer 07.674+toffset-app_time action Show("lane_22", dur=app_time)
            timer 08.588+toffset-app_time action Show("lane_23", dur=app_time)
            timer 08.954+toffset-app_time action Show("lane_1", dur=app_time)
            timer 09.320+toffset-app_time action Show("lane_2", dur=app_time)
            timer 10.052+toffset-app_time action Show("lane_3", dur=app_time)
            timer 10.783+toffset-app_time action Show("lane_31", dur=app_time)
            timer 11.515+toffset-app_time action Show("lane_1", dur=app_time)
            timer 12.247+toffset-app_time action Show("lane_3", dur=app_time)
            timer 12.796+toffset-app_time action Show("lane_31", dur=app_time)
            timer 13.344+toffset-app_time action Show("lane_32", dur=app_time)
            timer 13.710+toffset-app_time action Show("lane_2", dur=app_time)
            timer 14.259+toffset-app_time action Show("lane_21", dur=app_time)
            timer 14.808+toffset-app_time action Show("lane_22", dur=app_time)
            timer 15.174+toffset-app_time action Show("lane_3", dur=app_time)
            timer 15.722+toffset-app_time action Show("lane_31", dur=app_time)
            timer 16.271+toffset-app_time action Show("lane_32", dur=app_time)
            timer 16.637+toffset-app_time action Show("lane_2", dur=app_time)
            timer 17.186+toffset-app_time action Show("lane_21", dur=app_time)
            timer 17.735+toffset-app_time action Show("lane_22", dur=app_time)
            timer 18.100+toffset-app_time action Show("lane_1", dur=app_time)
            timer 18.649+toffset-app_time action Show("lane_11", dur=app_time)
            timer 19.198+toffset-app_time action Show("lane_12", dur=app_time)
            timer 19.564+toffset-app_time action Show("lane_2", dur=app_time)
            timer 20.113+toffset-app_time action Show("lane_21", dur=app_time)
            timer 20.661+toffset-app_time action Show("lane_22", dur=app_time)
            timer 21.027+toffset-app_time action Show("lane_1", dur=app_time)
            timer 21.576+toffset-app_time action Show("lane_11", dur=app_time)
            timer 22.125+toffset-app_time action Show("lane_12", dur=app_time)
            timer 22.491+toffset-app_time action Show("lane_2", dur=app_time)
            timer 23.039+toffset-app_time action Show("lane_21", dur=app_time)
            timer 23.588+toffset-app_time action Show("lane_22", dur=app_time)
            # Small break
            timer 25.509+toffset-app_time action Show("lane_2", dur=app_time)
            timer 25.692+toffset-app_time action Show("lane_21", dur=app_time)
            timer 26.065+toffset-app_time action Show("lane_1", dur=app_time)
            timer 26.431+toffset-app_time action Show("lane_11", dur=app_time)
            timer 26.797+toffset-app_time action Show("lane_2", dur=app_time)
            timer 27.163+toffset-app_time action Show("lane_21", dur=app_time)
            timer 27.529+toffset-app_time action Show("lane_3", dur=app_time)
            timer 27.895+toffset-app_time action Show("lane_31", dur=app_time)
            timer 28.260+toffset-app_time action Show("lane_2", dur=app_time)
            timer 28.626+toffset-app_time action Show("lane_1", dur=app_time)
            timer 28.992+toffset-app_time action Show("lane_11", dur=app_time)
            timer 29.358+toffset-app_time action Show("lane_21", dur=app_time)
            timer 29.724+toffset-app_time action Show("lane_22", dur=app_time)
            timer 30.090+toffset-app_time action Show("lane_3", dur=app_time)
            timer 30.456+toffset-app_time action Show("lane_31", dur=app_time)
            timer 30.821+toffset-app_time action Show("lane_2", dur=app_time)
            timer 31.187+toffset-app_time action Show("lane_1", dur=app_time)
            timer 31.553+toffset-app_time action Show("lane_11", dur=app_time)
            timer 31.919+toffset-app_time action Show("lane_21", dur=app_time)
            timer 32.285+toffset-app_time action Show("lane_22", dur=app_time)
            timer 32.651+toffset-app_time action Show("lane_3", dur=app_time)
            timer 33.017+toffset-app_time action Show("lane_31", dur=app_time)
            timer 33.382+toffset-app_time action Show("lane_2", dur=app_time)
            timer 33.748+toffset-app_time action Show("lane_1", dur=app_time)
            timer 34.114+toffset-app_time action Show("lane_11", dur=app_time)
            timer 34.480+toffset-app_time action Show("lane_21", dur=app_time)
            timer 34.846+toffset-app_time action Show("lane_22", dur=app_time)
            timer 35.212+toffset-app_time action Show("lane_3", dur=app_time)
            timer 35.578+toffset-app_time action Show("lane_31", dur=app_time)
            timer 35.760+toffset-app_time action Show("lane_32", dur=app_time)
            timer 36.126+toffset-app_time action Show("lane_2", dur=app_time)
            timer 36.492+toffset-app_time action Show("lane_21", dur=app_time)
            timer 36.858+toffset-app_time action Show("lane_22", dur=app_time)
            timer 37.224+toffset-app_time action Show("lane_23", dur=app_time)
            timer 37.407+toffset-app_time action Show("lane_2", dur=app_time)
            timer 37.773+toffset-app_time action Show("lane_3", dur=app_time)
            timer 38.139+toffset-app_time action Show("lane_31", dur=app_time)
            timer 38.504+toffset-app_time action Show("lane_21", dur=app_time)
            timer 38.870+toffset-app_time action Show("lane_22", dur=app_time)
            timer 39.236+toffset-app_time action Show("lane_1", dur=app_time)
            timer 39.602+toffset-app_time action Show("lane_11", dur=app_time)
            timer 39.968+toffset-app_time action Show("lane_2", dur=app_time)
            timer 40.334+toffset-app_time action Show("lane_3", dur=app_time)
            timer 40.699+toffset-app_time action Show("lane_31", dur=app_time)
            timer 41.065+toffset-app_time action Show("lane_21", dur=app_time)
            timer 41.431+toffset-app_time action Show("lane_22", dur=app_time)
            timer 41.797+toffset-app_time action Show("lane_1", dur=app_time)
            timer 42.163+toffset-app_time action Show("lane_11", dur=app_time)
            timer 42.529+toffset-app_time action Show("lane_2", dur=app_time)
            timer 42.895+toffset-app_time action Show("lane_3", dur=app_time)
            timer 43.260+toffset-app_time action Show("lane_31", dur=app_time)
            timer 43.626+toffset-app_time action Show("lane_21", dur=app_time)
            timer 43.992+toffset-app_time action Show("lane_22", dur=app_time)
            timer 44.358+toffset-app_time action Show("lane_1", dur=app_time)
            timer 44.724+toffset-app_time action Show("lane_11", dur=app_time)
            timer 45.090+toffset-app_time action Show("lane_2", dur=app_time)
            timer 45.456+toffset-app_time action Show("lane_3", dur=app_time)
            timer 45.821+toffset-app_time action Show("lane_31", dur=app_time)
            timer 46.187+toffset-app_time action Show("lane_21", dur=app_time)
            timer 46.553+toffset-app_time action Show("lane_22", dur=app_time)
            timer 46.919+toffset-app_time action Show("lane_1", dur=app_time)
            timer 47.285+toffset-app_time action Show("lane_11", dur=app_time)
            timer 47.651+toffset-app_time action Show("lane_2", dur=app_time)
            timer 48.017+toffset-app_time action Show("lane_3", dur=app_time)
            timer 48.382+toffset-app_time action Show("lane_31", dur=app_time)
            timer 48.748+toffset-app_time action Show("lane_21", dur=app_time)
            timer 49.114+toffset-app_time action Show("lane_22", dur=app_time)
            timer 49.480+toffset-app_time action Show("lane_1", dur=app_time)
            timer 49.846+toffset-app_time action Show("lane_11", dur=app_time)
            timer 50.212+toffset-app_time action Show("lane_2", dur=app_time)
            timer 50.578+toffset-app_time action Show("lane_3", dur=app_time)
            timer 51.309+toffset-app_time action Show("lane_31", dur=app_time)
            timer 51.675+toffset-app_time action Show("lane_21", dur=app_time)
            timer 52.041+toffset-app_time action Show("lane_1", dur=app_time)
            timer 52.590+toffset-app_time action Show("lane_3", dur=app_time)
            timer 53.139+toffset-app_time action Show("lane_31", dur=app_time)
            timer 53.504+toffset-app_time action Show("lane_2", dur=app_time)
            timer 54.053+toffset-app_time action Show("lane_21", dur=app_time)
            timer 54.602+toffset-app_time action Show("lane_22", dur=app_time)
            timer 54.968+toffset-app_time action Show("lane_3", dur=app_time)
            timer 55.517+toffset-app_time action Show("lane_31", dur=app_time)
            timer 56.065+toffset-app_time action Show("lane_32", dur=app_time)
            timer 56.431+toffset-app_time action Show("lane_2", dur=app_time)
            timer 56.980+toffset-app_time action Show("lane_21", dur=app_time)
            timer 57.529+toffset-app_time action Show("lane_22", dur=app_time)
            timer 57.895+toffset-app_time action Show("lane_1", dur=app_time)
            timer 58.443+toffset-app_time action Show("lane_11", dur=app_time)
            timer 58.992+toffset-app_time action Show("lane_12", dur=app_time)
            timer 59.358+toffset-app_time action Show("lane_2", dur=app_time)
            timer 59.907+toffset-app_time action Show("lane_21", dur=app_time)
            timer 60.456+toffset-app_time action Show("lane_22", dur=app_time)
            timer 60.821+toffset-app_time action Show("lane_3", dur=app_time)
            timer 61.370+toffset-app_time action Show("lane_31", dur=app_time)
            timer 61.919+toffset-app_time action Show("lane_32", dur=app_time)
            timer 62.285+toffset-app_time action Show("lane_2", dur=app_time)
            timer 62.834+toffset-app_time action Show("lane_21", dur=app_time)
            timer 63.382+toffset-app_time action Show("lane_22", dur=app_time)
            timer 63.748+toffset-app_time action Show("lane_1", dur=app_time)
            timer 64.297+toffset-app_time action Show("lane_11", dur=app_time)
            timer 64.846+toffset-app_time action Show("lane_12", dur=app_time)
            timer 65.212+toffset-app_time action Show("lane_2", dur=app_time)
            timer 65.760+toffset-app_time action Show("lane_21", dur=app_time)
            timer 66.309+toffset-app_time action Show("lane_22", dur=app_time)
            timer 66.675+toffset-app_time action Show("lane_1", dur=app_time)
            timer 67.224+toffset-app_time action Show("lane_11", dur=app_time)
            timer 67.773+toffset-app_time action Show("lane_12", dur=app_time)
            timer 68.139+toffset-app_time action Show("lane_2", dur=app_time)
            timer 68.687+toffset-app_time action Show("lane_21", dur=app_time)
            timer 69.236+toffset-app_time action Show("lane_22", dur=app_time)
            timer 69.602+toffset-app_time action Show("lane_3", dur=app_time)
            timer 70.151+toffset-app_time action Show("lane_31", dur=app_time)
            timer 70.699+toffset-app_time action Show("lane_32", dur=app_time)
            timer 71.065+toffset-app_time action Show("lane_2", dur=app_time)
            timer 71.614+toffset-app_time action Show("lane_21", dur=app_time)
            timer 72.163+toffset-app_time action Show("lane_22", dur=app_time)
            timer 72.529+toffset-app_time action Show("lane_3", dur=app_time)
            timer 73.078+toffset-app_time action Show("lane_31", dur=app_time)
            timer 73.626+toffset-app_time action Show("lane_32", dur=app_time)
            timer 73.992+toffset-app_time action Show("lane_2", dur=app_time)
            timer 74.541+toffset-app_time action Show("lane_21", dur=app_time)
            timer 75.090+toffset-app_time action Show("lane_22", dur=app_time)
            timer 75.456+toffset-app_time action Show("lane_23", dur=app_time)
            # Small break
            timer 78.382+toffset-app_time action Show("lane_2", dur=app_time)
            timer 78.931+toffset-app_time action Show("lane_3", dur=app_time)
            timer 79.480+toffset-app_time action Show("lane_31", dur=app_time)
            timer 79.846+toffset-app_time action Show("lane_21", dur=app_time)
            timer 80.395+toffset-app_time action Show("lane_1", dur=app_time)
            timer 80.943+toffset-app_time action Show("lane_11", dur=app_time)
            timer 81.309+toffset-app_time action Show("lane_2", dur=app_time)
            timer 81.858+toffset-app_time action Show("lane_21", dur=app_time)
            timer 82.407+toffset-app_time action Show("lane_3", dur=app_time)
            timer 82.773+toffset-app_time action Show("lane_31", dur=app_time)
            timer 83.321+toffset-app_time action Show("lane_2", dur=app_time)
            timer 83.870+toffset-app_time action Show("lane_21", dur=app_time)
            timer 84.236+toffset-app_time action Show("lane_1", dur=app_time)
            timer 84.785+toffset-app_time action Show("lane_11", dur=app_time)
            timer 85.334+toffset-app_time action Show("lane_12", dur=app_time)
            timer 85.699+toffset-app_time action Show("lane_2", dur=app_time)
            timer 86.248+toffset-app_time action Show("lane_21", dur=app_time)
            timer 86.797+toffset-app_time action Show("lane_22", dur=app_time)
            
            timer 88.260+toffset action SetVariable("win", True)
        
    else:
        
        timer 0.01 action [Stop("music", fadeout=2), 
            Hide("lane_1", transition=Dissolve(1)), Hide("lane_11", transition=Dissolve(1)), Hide("lane_12", transition=Dissolve(1)), Hide("lane_13", transition=Dissolve(1)), 
            Hide("lane_2", transition=Dissolve(1)), Hide("lane_21", transition=Dissolve(1)), Hide("lane_22", transition=Dissolve(1)), Hide("lane_23", transition=Dissolve(1)), 
            Hide("lane_3", transition=Dissolve(1)), Hide("lane_31", transition=Dissolve(1)), Hide("lane_32", transition=Dissolve(1)), Hide("lane_33", transition=Dissolve(1))]
        
        add "gui/overlay/confirm.png" at ds_in(1.0):
            alpha 0.75
         
        add "gui/minigame/lose.png" at ds_in(1.0):
            align(0.5, 0.5)
        
        text "You lose!" at ds_in(1.0):
            size 84
            yoffset 10
            color "#EF533D"
            align(0.5, 0.5)
            
        if level == 1:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level1")
        elif level == 2:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level2")
        elif level == 3:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level3")
        elif level == 4:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level4")
        elif level == 5:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level5")
        elif level == 6:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level6")
        elif level == 7:
            timer 4 action Hide("minigame", transition=Dissolve(1)), SetVariable("minigame_mode", False), Jump("after_level7")

    # Ensure player won't escape
    button:
        area(0,0,0,0)
        keysym "game_menu", "hide_windows"
        action NullAction()
    
    
################################################################################
## In-game screens
################################################################################

transform ctc_move:
    subpixel True
    xpos 1770 ypos 935 zoom 0.875 alpha 1.0
    block:
        easein 0.825 ypos 930 alpha 0.5
        easeout 0.825 ypos 935 alpha 1.0
        repeat
    

screen ctc():
    add "gui/ui/next.png" at ctc_move


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    if who is not None:

        text who id "who" at bt(4):
            color "#0005"
            size 78
            pos(77, 745)
        text who id "who":
            color "#ECABD3"
            size 78
            pos(72, 737)
    
    add "gui/ui/textbox.png":
        align(0.5, 0.975)
    
    vbox:
        area(115, 820, 1800, 200)
        
        viewport:
            
            text what id "what":
                xsize 1700
                size 40
                color "#43527E"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        yalign 0.3825
        spacing 32
        
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        
        imagebutton:
            idle "gui/ui/g_button.png"
            hover "gui/ui/g_button_pressed.png"
            insensitive "gui/ui/g_button_insensitive.png"
            sensitive (not minigame_mode)
            align(0.005, 0.0075)
            
            action ShowMenu("preferences")
        if minigame_mode:
            add "gui/ui/settings_insensitive.png":
                align(0.06625, 0.0525)
                zoom 0.5
        else:
            add "gui/ui/settings.png":
                align(0.06625, 0.0525)
                zoom 0.5
            
        imagebutton:
            idle "gui/ui/b_button.png"
            hover "gui/ui/b_button_pressed.png"
            insensitive "gui/ui/b_button_insensitive.png"
            sensitive (not minigame_mode)
            align(0.005, 0.1325)
            
            action ShowMenu('save')
        if minigame_mode:
            add "gui/ui/save_insensitive.png":
                align(0.06875, 0.17)
                zoom 0.4
        else:
            add "gui/ui/save.png":
                align(0.06875, 0.17)
                zoom 0.4
            

        #hbox:
        #    style_prefix "quick"

        #    xalign 0.5
        #    yalign 1.0

        #    textbutton _("Back") action Rollback()
        #    textbutton _("History") action ShowMenu('history')
        #    textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #    textbutton _("Auto") action Preference("auto-forward", "toggle")
        #    textbutton _("Save") action ShowMenu('save')
        #    textbutton _("Q.Save") action QuickSave()
        #    textbutton _("Q.Load") action QuickLoad()
        #    textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

# Blur text
transform bt(b=2):
    blur b

screen main_menu():

    tag menu

    #add gui.main_menu_background
    
    add "gui/ui/home_bg.jpg"

    #use navigation
    
    text "Intum OwO Project" at bt:
        align(0.51, 0.415)
        color "#0005"
        font "thebold.ttf"
        size 100
    text "Intum OwO Project":
        align(0.5, 0.4)
        color "#ECABD5"
        font "thebold.ttf"
        size 100
        outlines [ (absolute(8), "#fff", absolute(0), absolute(0)) ]
    
    imagebutton:
        idle "gui/ui/button.png"
        hover "gui/ui/button_pressed.png"
        align(0.5, 0.64)
        
        action Start()
    text "Start New Game!":
        color "#42527C"
        font "thebold.ttf"
        size 42
        align(0.5, 0.6325)
        
    imagebutton:
        idle "gui/ui/button.png"
        hover "gui/ui/button_pressed.png"
        align(0.5, 0.75)
        
        action ShowMenu("load")
    text "Load Game!":
        color "#42527C"
        font "thebold.ttf"
        size 42
        align(0.5, 0.7325)
        
    imagebutton:
        idle "gui/ui/button.png"
        hover "gui/ui/button_pressed.png"
        align(0.5, 0.86)
        
        action Quit(confirm=not main_menu)
    text "Quit!":
        color "#42527C"
        font "thebold.ttf"
        size 42
        align(0.5, 0.8325)
        
    imagebutton:
        idle "gui/ui/g_button.png"
        hover "gui/ui/g_button_pressed.png"
        align(0.99, 0.995)
        
        action ShowMenu("preferences")
    add "gui/ui/settings.png":
        align(0.9325, 0.949)
        zoom 0.5


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):
    
    tag menu
    
    add "gui/ui/bg.jpg"
    
    imagebutton:
        idle "gui/ui/b_button.png"
        hover "gui/ui/b_button_pressed.png"
        align(0.005, 0.0075)
        
        action Return()
    add "gui/ui/back.png":
        align(0.0575, 0.04) zoom 0.72
        
    if not main_menu:
        imagebutton:
            idle "gui/ui/r_button.png"
            hover "gui/ui/r_button_pressed.png"
            align(0.995, 0.0075)
            
            action MainMenu()
        add "gui/ui/home.png":
            align(0.9375, 0.051) zoom 0.525
    
    text "[title]":
        size 80
        color "#ECABD5"
        font "thebold.ttf"
        align(0.5, 0.075)
    
    add "gui/ui/save/bg.png":
        align(0.5, 0.75)
    
    vbox:
        area(463, 250, 1009, 677) # 50 pixels spacing
        
        viewport:
            #mousewheel True
            
            grid 3 3:
                
                xspacing 16
                yspacing 10
                
                for i in range(9):

                    $ slot = i + 1

                    button:
                        # BG size: 312 x 180 px
                        background "gui/ui/save/save.png"
                        hover_background "gui/ui/save/save_selected.png"
                        xsize 325
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot):
                            xalign 0.5
                            size(300, 168)
                            
                        null height 16

                        text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):  # (#file_time}%A, %B %d %Y, %H:%M
                            style "slot_time_text"
                            size 24
                            font "thebold.ttf"
                            color "#44527E"
                            hover_color "#6479B7"

                        key "save_delete" action FileDelete(slot)
            
            #text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pulvinar pulvinar ante, at efficitur odio dapibus vel. Phasellus lacinia tincidunt sodales. Proin eleifend libero ante, et accumsan lorem lobortis et. Vivamus et gravida diam, sit amet mollis est. Aenean eget nulla eu ipsum auctor facilisis. Nulla elementum enim turpis, a eleifend lorem elementum quis. Nam finibus orci non tortor lobortis aliquam. Donec sit amet tellus nibh. In massa turpis, condimentum quis interdum nec, auctor eu mauris. Fusce placerat massa auctor rhoncus dictum. Aenean pulvinar vel justo eu egestas. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque tristique efficitur nisl, id volutpat felis lacinia eu. Pellentesque lacinia orci id pharetra dictum. Sed neque enim, vestibulum non dignissim ut, suscipit sed nibh.Cras ipsum ipsum, posuere sed sollicitudin fermentum, euismod ac lacus. In fringilla vehicula enim. Duis sed euismod orci. Ut faucibus volutpat odio tincidunt suscipit. Cras varius fringilla enim in consequat. Quisque eu risus ut quam lacinia iaculis. Nullam sit amet ante ut libero suscipit malesuada. Mauris vestibulum faucibus turpis, eu finibus ipsum condimentum eget.":
            #    size 50
            #    font "thebold.ttf"
            #    color "#44527E"
    
    
screen backup_file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    
    add "gui/ui/bg.jpg"
    
    imagebutton:
        idle "gui/ui/b_button.png"
        hover "gui/ui/b_button_pressed.png"
        align(0.005, 0.0075)
        
        action Return()
    add "gui/ui/back.png":
        align(0.0575, 0.04) zoom 0.72
        
    if not main_menu:
        imagebutton:
            idle "gui/ui/r_button.png"
            hover "gui/ui/r_button_pressed.png"
            align(0.995, 0.0075)
            
            action MainMenu()
        add "gui/ui/home.png":
            align(0.9375, 0.051) zoom 0.525
    
    text "Settings":
        size 80
        color "#ECABD5"
        font "thebold.ttf"
        align(0.5, 0.075)
        
    add "gui/ui/settings/frame.png":
        align(0.5, 0.75)
        
    # Sound Setting
    add "gui/ui/settings/setting_bg.png":
        align(0.5, 0.3275)
        ysize 0.325
    
    text "Audio Setting":
        color "#43527D"
        size 46
        font "thebold.ttf"
        align(0.5, 0.2)
        
    text "Music Volume":
        color "#43527D"
        size 36
        font "roboto_reg.ttf"
        align(0.5, 0.275)
    frame:
        align(0.5, 0.325)
        background None
        bar value Preference("music volume"):
            ysize 69
            xsize 564
            left_bar "gui/ui/settings/volume_fill.png"
            right_bar "gui/ui/settings/volume_empty.png"
            left_gutter 10
            right_gutter 10
            thumb_offset 40
            thumb "gui/ui/settings/volume_knob.png"
            
    text "Sound Volume":
        color "#43527D"
        size 36
        font "roboto_reg.ttf"
        align(0.5, 0.4)
    frame:
        align(0.5, 0.45)
        background None
        bar value Preference("sound volume"):
            ysize 69
            xsize 564
            left_bar "gui/ui/settings/volume_fill.png"
            right_bar "gui/ui/settings/volume_empty.png"
            left_gutter 10
            right_gutter 10
            thumb_offset 40
            thumb "gui/ui/settings/volume_knob.png"
    
    # Text Settings
    add "gui/ui/settings/setting_bg.png":
        align(0.5, 0.8615)
        ysize 0.325
    
    text "Game Setting":
        color "#43527D"
        size 46
        font "thebold.ttf"
        align(0.5, 0.58)
        
    text "Text Speed":
        color "#43527D"
        size 36
        font "roboto_reg.ttf"
        align(0.5, 0.6525)
    frame:
        align(0.5, 0.715)
        background None
        bar value Preference("text speed"):
            ysize 69
            xsize 564
            left_bar "gui/ui/settings/volume_fill.png"
            right_bar "gui/ui/settings/volume_empty.png"
            left_gutter 10
            right_gutter 10
            thumb_offset 40
            thumb "gui/ui/settings/volume_knob.png"
            
    text "Windowed":
        color "#43527D"
        size 36
        font "roboto_reg.ttf"
        align(0.425, 0.78)
    imagebutton:
        align(0.425, 0.8375)
        idle "gui/ui/settings/switch_bg.png"
        selected_idle "gui/ui/settings/switch.png"
        selected_hover "gui/ui/settings/switch.png"
        
        action Preference("display", "toggle")
    if preferences.fullscreen:
        text "ON":
            size 36
            color "#44537D"
            font "thebold.ttf"
            align(0.409, 0.8375)
    else:
        text "ON":
            size 36
            color "#fff"
            font "thebold.ttf"
            align(0.409, 0.8375)
    if not preferences.fullscreen:
        text "OFF":
            size 36
            color "#44537D"
            font "thebold.ttf"
            align(0.4485, 0.8375)
    else:
        text "OFF":
            size 36
            color "#fff"
            font "thebold.ttf"
            align(0.4485, 0.8375)
    
    text "Skip Unseen":
        color "#43527D"
        size 36
        font "roboto_reg.ttf"
        align(0.575, 0.78)
    imagebutton:
        align(0.575, 0.8375)
        idle "gui/ui/settings/switch.png"
        selected_idle "gui/ui/settings/switch_bg.png"
        selected_hover "gui/ui/settings/switch_bg.png"
        
        action Preference("skip", "toggle")
    if not preferences.skip_unseen:
        text "ON":
            size 36
            color "#44537D"
            font "thebold.ttf"
            align(0.552, 0.8375)
    else:
        text "ON":
            size 36
            color "#fff"
            font "thebold.ttf"
            align(0.552, 0.8375)
    if preferences.skip_unseen:
        text "OFF":
            size 36
            color "#44537D"
            font "thebold.ttf"
            align(0.592, 0.8375)
    else:
        text "OFF":
            size 36
            color "#fff"
            font "thebold.ttf"
            align(0.592, 0.8375)
    

screen pref_backup():
    
    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    
    add "gui/ui/prompt.png":
        align(0.5, 0.5)

    vbox:
        area (660, 395, 700, 200)

        viewport:
            xalign 0.5
            yalign 0.5
            
            label _(message):
                text_color "#45527E"
                text_size 46
                text_text_align 0.5

    imagebutton:
        idle "gui/ui/b_button.png"
        hover "gui/ui/b_button_pressed.png"
        align(0.4, 0.62)
        
        action yes_action
    text _("Yes"):
        size 46
        color "#fff"
        align(0.41, 0.61125)
    
    imagebutton:
        idle "gui/ui/r_button.png"
        hover "gui/ui/r_button_pressed.png"
        align(0.6, 0.62)
        
        action no_action
    text _("No"):
        size 46
        color "#fff"
        align(0.59, 0.61125)

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping"):
                yalign 1.0

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle":
                ypos -4
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle":
                ypos -4
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle":
                ypos -4


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]":
            ypos 3

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
