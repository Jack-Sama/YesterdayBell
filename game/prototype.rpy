init offset = 5

default umbrella_joke = False
default umbrella_recalled = False
default replay_april = False
default replay_june = False
default chapter_title = ""
default memory_date = ""
default last_block = 0
default ending_seen = ""
default persistent.ending_a = False
default persistent.ending_b = False
default persistent.bell_album = set()

define u = Character("悠")
define x = Character("夏澄")
define pu = Character("悠 / 过去")
define px = Character("夏澄 / 过去")
define mu = Character("悠 / 消息")
define mx = Character("夏澄 / 消息")
define echo = Character("旧教室")

define bell_serif = "fonts/BellSerif.ttf"
define bell_ink = "#263c35"
define bell_paper = "#fff2dd"
define bell_copper = "#9c5544"
define bell_prints = {
    "window": ("窗边", "03.02", "窗框边还留着一点校服袖子。"),
    "street": ("旧街改道前", "03.02", "围挡过些日子就会撤掉。"),
    "light": ("墙角的光", "冬末", "夏澄留下来的那一张。"),
    "portfolio": ("交进作品集", "冬末", "她最后选的同一个街角。"),
    "together": ("最后一次值日", "03.02", "我的领子还没理好，夏澄正眨眼。"),
}

init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True)
    renpy.music.register_channel("memory", mixer="sfx", loop=True)

    def keep_print(name):
        if name not in persistent.bell_album:
            persistent.bell_album = persistent.bell_album | {name}

image bg classroom = Transform("images/classroom.png", xysize=(1280, 720))
image bg classroom_evening = Transform("images/classroom_evening.png", xysize=(1280, 720))
image bg corridor = Transform("images/corridor.png", xysize=(1280, 720))
image xc neutral = Transform("images/xiacheng_neutral.png", xysize=(494, 707))
image xc smile = Transform("images/xiacheng_smile.png", xysize=(514, 703))
image xc quiet = Transform("images/xiacheng_quiet.png", xysize=(514, 703))
image xc tease = Transform("images/xiacheng_tease.png", xysize=(514, 703))
image xc shy = Transform("images/xiacheng_shy.png", xysize=(514, 703))

image print street = Transform("images/prints.png", crop=(0, 0, 835, 470))
image print light = Transform("images/prints.png", crop=(837, 0, 835, 470))
image print portfolio = Transform("images/prints.png", crop=(0, 471, 835, 470))
image print window = Transform("images/prints.png", crop=(837, 471, 835, 470))
image print together = "images/photo_together.png"

transform character_right:
    xpos 744
    ypos 46

transform bell_print_enter:
    on show:
        alpha 0.0 yoffset 14
        easeout .28 alpha 1.0 yoffset 0

transform bell_pulse:
    alpha .62
    ease 1.1 alpha 1.0
    ease 1.2 alpha .62
    repeat

define shutter_flash = Fade(.035, 0.0, .18, color="#fff4e1")
