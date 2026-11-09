testsuite global:
    teardown:
        exit

testcase full_routes:
    parameter (route, umbrella, photo) = [("direct", False, False), ("listen", True, True), ("wait", True, False)]
    $ _test.transition_timeout = 0.02
    $ preferences.text_cps = 0
    $ _test.screenshot_directory = renpy.config.savedir
    assert screen "main_menu"
    if eval (route == "direct"):
        screenshot "title.png"
    click id "start_reading"
    advance until screen "choice"
    if eval (route == "direct"):
        screenshot "first-choice.png"
    if eval photo:
        click "那饮料算监督费？"
    else:
        click "那请监督员搭把手。"
    if eval (route == "direct"):
        advance until eval (last_block == 47)
        assert screen "photo_view"
        assert eval ("window" in persistent.bell_album)
        pause 0.35
        screenshot "shutter.png"
        advance until eval (last_block == 54)
        pause 0.25
        screenshot "reading.png"
        advance until eval (last_block == 97)
        pause 0.25
        screenshot "echo.png"
    advance until screen "choice"
    if eval umbrella:
        click "看来得换把大伞了。"
    else:
        click "原来你还记得。"
    advance until screen "notebook_pages"
    assert eval (umbrella_joke == umbrella)
    if eval (route == "listen"):
        click id "page_april"
        advance until screen "notebook_pages"
        assert eval replay_april
        click id "page_june"
        advance until screen "notebook_pages"
        assert eval replay_june
        screenshot "notebook.png"
        run QuickSave()
        $ umbrella_joke = False
        $ replay_april = False
        $ replay_june = False
        run QuickLoad(confirm=False)
        assert screen "notebook_pages"
        assert eval (umbrella_joke and replay_april and replay_june)
    click id "page_january"
    advance until screen "choice"
    assert screen "photo_view"
    assert eval (renpy.get_screen("choice").zorder > renpy.get_screen("photo_view").zorder)
    if eval (route == "direct"):
        pause 0.35
        screenshot "photo-choice.png"
    if eval photo:
        click "能看看你最后选的那张吗？"
    else:
        click "你喜欢的是哪一部分？"
    if eval (route == "direct"):
        advance until eval (last_block == 249)
        pause 0.35
        screenshot "photo.png"
        advance until eval (last_block == 282)
        assert screen "photo_view"
        assert eval ("together" in persistent.bell_album)
        pause 0.35
        screenshot "together.png"
        advance until eval (last_block == 304)
        pause 0.25
        screenshot "evening.png"
    advance until screen "choice"
    if eval (route == "direct"):
        click "点开夏澄发来的合照"
    else:
        click "翻开四月十二日那一页"
        advance until screen "choice"
        if eval (route == "listen"):
            click "点开合照，回复她。"
        else:
            click "等明天见面再说。"
    advance until screen "ending_card"
    if eval (route == "wait"):
        assert eval (ending_seen == "A")
        assert eval (not umbrella_recalled)
        screenshot "ending-a.png"
    else:
        assert eval (ending_seen == "B")
        assert eval (umbrella_recalled == umbrella)
        if eval (route == "listen"):
            screenshot "ending-b.png"
    click "回到标题"
    assert screen "main_menu"
    if eval (route == "listen"):
        click "留影簿"
        assert screen "bell_album"
        assert eval ({"window", "street", "light", "portfolio", "together"} <= persistent.bell_album)
        pause 0.55
        screenshot "album.png"
        click "交进作品集"
        assert screen "album_print"
        click "合上相片"
        click "返回"
        assert screen "main_menu"

testcase menu_screens:
    $ _test.transition_timeout = 0.02
    $ preferences.text_cps = 0
    $ _test.screenshot_directory = renpy.config.savedir
    click id "start_reading"
    advance until eval (last_block == 8)
    click "保存"
    assert screen "save"
    pause 0.25
    screenshot "save-menu.png"
    click "返回"
    click "设置"
    assert screen "preferences"
    pause 0.25
    screenshot "preferences.png"
    click "返回"
    click "历史"
    assert screen "history"
    screenshot "history.png"
    click "返回"
    run Jump("ending_b")
    advance until eval (last_block == 354)
    screenshot "photo-window.png"
    run MainMenu(confirm=False)
    assert screen "main_menu"
