init python:
    # style.default.font = "9569.ttf"
    style.default.outlines = [(1, "#494949", 0, 0)]
    # style.default.size = 24
    style.default.color = '#d9d5d1'
    # style.default.size = 20
    style.my_text = Style(style.default)
    style.warning = Style(style.default)
    style.green = Style(style.default)
    style.description = Style(style.default)
    style.bigRed = Style(style.default)
    style.normalRed = Style(style.default)
    style.myBox = Style(style.default)
    style.navigation_button = Style(style.button_text)
    # style.navigation_button.background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.hover_background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.selected_background = Frame("images/interface/music_library_button_selected.png", 25, 25)
    style.navigation_button_text.color = "#FFFFFF"
    style.navigation_button_text.size = 22
    style.navigation_button_text.outlines = [(2, "#494949", 0, 0)]
    style.navigation_button_text.hover_color = "#00FF80AA"
    # style.navigation_button_text.selected_color = "#00FF00"
    
    style.action_button_text.color = "#FF8B8B"
    style.action_button_text.size = 22
    style.action_button_text.outlines = [(1, "#494949", 0, 0)]
    style.action_button_text.hover_color = "#FF0010AA"
    
    
    style.small_button = Style(style.button_text)
    style.small_button_text.color = "#FFFFFF"
    style.small_button_text.outlines = [(1, "#494949", 0, 0)]
    style.small_button_text.hover_color = "#0000FF"
    # style.small_button_text.selected_color = "#00FF00"
    style.small_button_text.size = 14
    
    style.bluesmall_button = Style(style.button_text)
    style.bluesmall_button.color = "#60D5FC"
    style.bluesmall_button.outlines = [(1, "#494949", 0, 0)]
    style.bluesmall_button.hover_color = "#0000FF"
    # style.bluesmall_button.selected_color = "#00FF00"
    style.bluesmall_button.size = 14
    
    style.myFrame = Style(style.frame)
    style.myFrame.background = "#0000FF50"
    style.myFrame.xmargin  = 10
    style.myFrame.ymargin   = 10
    
    style.peopleTextList = Style(style.frame)
    style.peopleTextList.background = Frame("pic/frame.png", 0, 0)
    # style.peopleTextList.xmargin  = 100
    # style.peopleTextList.ymargin   = 100
    style.peopleTextList.xpadding  = 10
    style.peopleTextList.ypadding  = 10
    
    style.myBar = Style(style.vbar)
    style.myBar.background = "#FF0000"
    style.myBar.thumb = "#FF0000"
    
    style.energyBar = Style(style.bar)   
    style.energyBar.left_bar = Frame("green.png", 0, 0)
    style.energyBar.right_bar = Frame("black.png", 0, 0)
    style.energyBar.right_gutter  = 30
    style.energyBar.left_gutter  = 40
    style.energyBar.thumb = None
    
    style.healthBar = Style(style.bar)   
    style.healthBar.left_bar = Frame("red.png", 0, 0)
    style.healthBar.right_bar = Frame("black.png", 0, 0)
    style.healthBar.right_gutter  = 30
    style.healthBar.left_gutter  = 40
    style.healthBar.thumb = None
    
    style.manaBar = Style(style.bar)   
    style.manaBar.left_bar = Frame("blue.png", 0, 0)
    style.manaBar.right_bar = Frame("black.png", 0, 0)
    style.manaBar.right_gutter  = 30
    style.manaBar.left_gutter  = 40
    style.manaBar.thumb = None
    
    style.lustBar = Style(style.bar)   
    style.lustBar.left_bar = Frame("pink.png", 0, 0)
    style.lustBar.right_bar = Frame("black.png", 0, 0)
    style.lustBar.right_gutter  = 30
    style.lustBar.left_gutter  = 40
    style.lustBar.thumb = None
    
    # style.energyBar = Style(style.bar)   
    # style.energyBar.left_bar = Frame("green.png", 0, 0)
    # style.energyBar.right_bar = Frame("red.png", 0, 0)
    # style.energyBar.right_gutter  = 0
    # style.energyBar.left_gutter  = 15
    # style.energyBar.thumb = None
    
    # style.healthBar = Style(style.bar)   
    # style.healthBar.left_bar = Frame("red.png", 0, 0)
    # style.healthBar.right_bar = Frame("blue.png", 0, 0)
    # style.healthBar.right_gutter  = 0
    # style.healthBar.left_gutter  = 15
    # style.healthBar.thumb = None
    
    # style.manaBar = Style(style.bar)   
    # style.manaBar.left_bar = Frame("lightblue.png", 0, 0)
    # style.manaBar.right_bar = Frame("red.png", 0, 0)
    # style.manaBar.right_gutter  = 0
    # style.manaBar.left_gutter  = 15
    # style.manaBar.thumb = None
    
    # style.lustBar = Style(style.bar)   
    # style.lustBar.left_bar = Frame("pink.png", 0, 0)
    # style.lustBar.right_bar = Frame("blue.png", 0, 0)
    # style.lustBar.right_gutter  = 0
    # style.lustBar.left_gutter  = 15
    # style.lustBar.thumb = None
style button_text:
    size 20
    
style my_text is text:
    size 15
    outlines [(1, "#494949", 0, 0)]
    
style small_text is text:
    size 10
    outlines [(1, "#494949", 0, 0)]
    
style verticalText is text:
    vertical True
    size 18
    outlines [(2, "#494949", 0, 0)]

style param is text:
    size 15
    outlines [(2, "#494949", 0, 0)]
    bold True
    # drop_shadow [ (2, 1) ,(3, 2)] 

style smallText is text:
    size 15
    outlines [(1, "#494949", 0, 0)]
    # color "#FF1E1E"
    # bold True
