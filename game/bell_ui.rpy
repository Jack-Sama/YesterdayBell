init offset = 10

style bell_text:
    font "fonts/BellSans.ttf"
    color bell_ink

style bell_button:
    background Frame("ui/option_idle.svg", 20, 16)
    hover_background Frame("ui/option_hover.svg", 20, 16)
    insensitive_background Frame("ui/option_idle.svg", 20, 16)
    padding (22, 12)
    yminimum 49

style bell_button_text is bell_text:
    size 22
    hover_color "#762f23"
    insensitive_color "#687b6d"

style bell_title_button:
    background None
    hover_background Solid("#fff3d61a")
    padding (12, 6)
    xsize 365

style bell_title_button_text is bell_text:
    color "#fff1db"
    hover_color "#ffcda9"
    size 25

style bell_quick_button:
    background None
    hover_background Solid("#95574820")
    padding (7, 2)

style bell_quick_button_text is bell_text:
    size 15
    color "#425b50"
    hover_color "#813c2f"
    selected_color "#813c2f"
    insensitive_color "#596b62"

style say_dialogue:
    font bell_serif
    color bell_ink
    size 27
    xsize 1030
    line_spacing 5
    layout "greedy"

style say_label:
    font bell_serif
    size 22
    color "#fff3df"
    xanchor 0
    yanchor 0

screen say(who, what):
    zorder 10
    window:
        id "window"
        background None
        padding (0, 0)
        pos (51, 526)
        anchor (0, 0)
        xysize (1178, 181)

        fixed:
            add "ui/dialogue.svg"
            if memory_date:
                add "ui/dialogue_echo.svg"
            if who:
                text who id "who" pos (91, 6)
            else:
                text "旁白" style "say_label" pos (91, 6)
            text what id "what" pos (67, 43)
            text chapter_title style "bell_text" size 13 color "#596b60" pos (67, 143)

screen quick_menu():
    zorder 100
    if quick_menu and not main_menu and renpy.get_screen("say") and not renpy.get_screen("choice"):
        hbox:
            xpos 1143
            xanchor 1.0
            ypos 667
            spacing 3
            textbutton "回退" action Rollback() style "bell_quick_button"
            textbutton "历史" action ShowMenu("history") style "bell_quick_button"
            textbutton "自动" action Preference("auto-forward", "toggle") style "bell_quick_button"
            textbutton "快进" action Skip() style "bell_quick_button"
            textbutton "保存" action ShowMenu("save") style "bell_quick_button"
            textbutton "快存" action QuickSave() style "bell_quick_button"
            textbutton "快读" action QuickLoad() style "bell_quick_button"
            textbutton "设置" action ShowMenu("preferences") style "bell_quick_button"

screen scene_heading():
    zorder 2
    if memory_date:
        add "ui/echo_wash.svg"
        fixed:
            pos (55, 37)
            xysize (434, 58)
            add Solid("#282f31f2")
            add Solid("#bd8267") xysize (3, 58)
            add "ui/echo_meter.svg" pos (18, 16) at bell_pulse
            text "听见过去" font bell_serif size 19 color "#edbf9c" pos (72, 13)
            text memory_date style "bell_text" size 21 color "#fff2df" pos (185, 12)

screen main_menu():
    tag menu
    add "bg classroom"
    add "ui/title_wash.svg"
    add "ui/bell.svg" pos (80, 66)
    text "三月二日  /  15:40" style "bell_text" size 18 color "#e7bc97" pos (130, 71)
    text "昨天的" font bell_serif size 65 color "#fff3e0" pos (78, 115)
    text "放学铃" font bell_serif size 101 color "#fff3e0" pos (75, 181)
    text "旧教室里，还有人没走。" font bell_serif size 22 color "#ead1b5" pos (83, 316)
    add Solid("#d5916e99") pos (83, 364) xysize (280, 1)

    vbox:
        pos (72, 385)
        spacing 5
        textbutton "开始阅读" action Start() style "bell_title_button" id "start_reading"
        textbutton "读取存档" action ShowMenu("load") style "bell_title_button"
        textbutton "留影簿" action ShowMenu("bell_album") style "bell_title_button"
        textbutton "设置" action ShowMenu("preferences") style "bell_title_button"
        textbutton "退出" action Quit(confirm=False) style "bell_title_button"

    text "短篇视觉小说  /  放学留影版" style "bell_text" size 16 color "#d7d0b8" pos (83, 646)

screen choice(items):
    modal True
    zorder 25
    $ beside_print = renpy.get_screen("photo_view") is not None
    vbox:
        xpos (656 if beside_print else 66)
        yalign (.48 if beside_print else .45)
        spacing 11
        frame:
            background Solid("#29433bef")
            padding (13, 4)
            text "此刻，你想怎么做？" font bell_serif size 17 color "#fff2db"
        for i, item in enumerate(items, 1):
            button:
                action item.action
                style "bell_button"
                xsize (552 if beside_print else 627)
                hbox:
                    spacing 15
                    text "{:02d}".format(i) style "bell_text" size 16 color bell_copper yalign .5
                    text item.caption style "bell_button_text" yalign .5

screen notebook_pages():
    modal True
    zorder 28
    add Solid("#10251fc9")
    add "ui/notebook.svg" pos (53, 58)
    text "值日簿" font bell_serif size 54 color bell_ink pos (125, 126)
    text "朝仓悠  /  夏澄" font bell_serif size 25 color bell_copper pos (131, 212)
    text "合上就会安静。\n再翻开，教室就回到了那一天。" font bell_serif size 24 line_spacing 9 color "#485e51" pos (131, 300)
    text "选一页，听听那天的教室。" style "bell_text" size 19 color "#405d51" pos (570, 118)
    vbox:
        pos (563, 164)
        spacing 16
        for number, date, value, subtitle, heard in (
            ("04.12", "四月十二日", "april", "扫帚与找不到的笔", replay_april),
            ("06.21", "六月二十一日", "june", "窗上的雨声", replay_june),
            ("01.17", "一月十七日", "january", "还没拍成的合照", False),
        ):
            button:
                id ("page_" + value)
                action [Play("sound", "audio/paper.wav"), Return(value)]
                style "bell_button"
                xysize (559, 105)
                fixed:
                    text number style "bell_text" size 17 color bell_copper pos (0, 7)
                    text date font bell_serif size 26 color bell_ink pos (84, -2)
                    text subtitle style "bell_text" size 17 color "#4c6659" pos (84, 45)
                    text ("已听 / 重听" if heard else ("继续故事" if value == "january" else "听这一页")) style "bell_text" size 16 color bell_copper xpos 510 xanchor 1.0 ypos 39

    text "前两页可以重听。一月的记录会继续故事。" style "bell_text" size 16 color "#556c60" pos (571, 528)
    textbutton "保存" action ShowMenu("save") style "bell_button" pos (995, 642)
    textbutton "设置" action ShowMenu("preferences") style "bell_button" pos (1093, 642)

screen bell_print(name, width=516, height=286):
    $ caption, date, note = bell_prints[name]
    frame:
        background Solid("#fff1dc")
        padding (10, 10, 10, 8)
        vbox:
            spacing 6
            add ("print " + name) xysize (width, height)
            fixed:
                xysize (width, 26)
                text caption font bell_serif size 17 color bell_ink pos (3, 0)
                text date style "bell_text" size 15 color bell_copper xpos (width - 3) xanchor 1.0 ypos 1

screen photo_view(name, compact=False):
    zorder 4
    fixed:
        pos ((567, 335) if compact else (65, 109))
        xysize ((270, 192) if compact else (536, 336))
        at bell_print_enter
        use bell_print(name, 250 if compact else 516, 140 if compact else 286)

screen bell_album():
    tag menu
    use game_menu("留影簿"):
        vbox:
            spacing 13
            text "在故事里看到的照片，会留在这里。" font bell_serif size 21 color "#f3dac0"
            grid 3 2:
                spacing 14
                for name, (caption, date, note) in bell_prints.items():
                    button:
                        xysize (263, 195)
                        padding (0, 0)
                        background Solid("#2c4740")
                        hover_background Solid("#b6654e")
                        action (Show("album_print", name=name) if name in persistent.bell_album else None)
                        if name in persistent.bell_album:
                            use bell_print(name, 243, 147)
                        else:
                            text "待冲洗" font bell_serif size 24 color "#d7c4ac" align (.5, .5)
                fixed:
                    xysize (263, 195)
                    vbox:
                        pos (19, 25)
                        spacing 16
                        text "读到的结局" font bell_serif size 23 color "#f4d5b3"
                        text ("再听一次" if persistent.ending_a else "尚未读到") style "bell_text" size 18 color "#f8eddb"
                        text ("明天之后" if persistent.ending_b else "尚未读到") style "bell_text" size 18 color "#f8eddb"

screen album_print(name):
    modal True
    zorder 200
    add Solid("#152721ec")
    key "game_menu" action Hide("album_print")
    vbox:
        align (.5, .5)
        spacing 12
        use bell_print(name, 760, 427)
        text bell_prints[name][2] font bell_serif size 20 color "#f7e8d4" xalign .5
        textbutton "合上相片" action Hide("album_print") style "bell_button" xalign .5

screen ending_card(title, code):
    modal True
    zorder 30
    add "bg corridor"
    add "ui/title_wash.svg"
    add "ui/bell.svg" pos (80, 137)
    text "昨天的放学铃" font bell_serif size 24 color "#f0c6a3" pos (132, 140)
    text title font bell_serif size 82 color "#fff3df" pos (74, 216)
    add Solid("#d5916e99") pos (81, 342) xysize (355, 1)
    text ("那句话还留在草稿里。" if code == "A" else "周六，还是从这条街出发。") font bell_serif size 25 color "#f3ddc6" pos (80, 368)
    textbutton "回到标题" action Return() style "bell_button" pos (81, 473)
