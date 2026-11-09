# 放学留影版。保留段落编号，便于定位原稿与试玩节点。


label start:
    $ umbrella_joke = False
    $ replay_april = False
    $ replay_june = False
    $ ending_seen = ""
    $ umbrella_recalled = False
    $ memory_date = ""
    stop music fadeout 0.8
    play ambience "audio/wind.wav" fadein 1.0
    $ chapter_title = "01 / 最后一次值日"
    scene bg classroom with dissolve
    show screen scene_heading
    $ last_block = 5
    "三月二日。下午三点四十分。"
    $ last_block = 6
    "那扇窗户关不严。风一来，登记表就掀起一角。我拿笔压住纸，把旧教材放进箱子。"
    $ last_block = 7
    "刚放下，才想起又忘了登记。"
    $ last_block = 8
    u "……第四次了。"
    $ last_block = 9
    "我把书拿出来。封底夹着张旧通知。明天毕业典礼一过，这间教室就要改成活动室了。"
    show xc neutral at character_right with dissolve
    $ last_block = 10
    x "打扰了——"
    $ last_block = 11
    "门口出现了夏澄。她背着相机包，手里提着便利店袋子。"
    $ last_block = 15
    x "我在门口数了三遍。你把同一本书装了三次。"
    $ last_block = 16
    u "你是来监督工作的吗？"
    $ last_block = 17
    x "第四遍才进来。够体贴吧？"
    $ last_block = 18
    "她把一瓶麦茶放到讲台上。"
    menu:
        "那请监督员搭把手。":
            show xc tease at character_right
            u "那请监督员搭把手。"
            $ last_block = 22
            x "监督员主要负责监督。"
            $ last_block = 23
            u "那先搬一箱？算巡视。"
            $ last_block = 24
            "夏澄往箱子里看了一眼：「你对巡视的理解是不是有点偏？」"
        "那饮料算监督费？":
            show xc tease at character_right
            u "那饮料算监督费？"
            $ last_block = 26
            x "慰问品，不报销。"
            $ last_block = 27
            u "原来我是被监督的那个。"
            $ last_block = 28
            x "不然呢？你还想拿瓶麦茶就把我雇了？"
    show xc smile at character_right
    $ last_block = 30
    "她把便利店袋子挂到椅背上，笑着拍了拍相机包。"
    $ last_block = 31
    x "我先拍几张，马上来帮你。"
    $ last_block = 32
    "她自己拿的是柠檬茶。我记得她以前嫌它酸。"
    $ last_block = 33
    u "现在喜欢喝这个了？"
    $ last_block = 34
    x "嗯。去年开始吧。"
    $ last_block = 38
    x "看你这表情。下次换口味之前，我向你提交申请。"
    $ last_block = 40
    "夏澄笑着走向窗边。"
    $ last_block = 41
    "她绕过堆在一旁的课桌。桌脚移开以后，地板上还留着它们原来的印子。"
    play sound "audio/camera.wav"
    with shutter_flash
    $ last_block = 42
    "咔嚓。"
    $ last_block = 43
    x "往左一点。"
    $ last_block = 44
    "我指了指自己。她点头。"
    play sound "audio/camera.wav"
    with shutter_flash
    $ last_block = 46
    "我往旁边挪了半步。"
    $ keep_print("window")
    show screen photo_view("window", compact=True)
    $ last_block = 47
    x "……还是拍进去了。"
    $ last_block = 48
    "我凑过去，屏幕上除了窗户，还有半截校服袖子。"
    $ last_block = 49
    u "那得赔偿肖像权。"
    $ last_block = 50
    x "只有袖子。"
    $ last_block = 51
    u "袖子也是我的。一百日元，熟人价。"
    $ last_block = 52
    "夏澄端详照片：「那我裁掉吧。」"
    hide screen photo_view
    show xc smile at character_right
    $ last_block = 53
    "我无言以对。她终于忍不住笑了。"
    $ last_block = 54
    "她来帮我清点。能留的放左边，待处理的放右边。她念年份，我填登记表。"
    $ last_block = 55
    "「你还是这样。」她忽然说。"
    $ last_block = 56
    u "哪样？"
    $ last_block = 57
    x "以前值日时也爱分左右。扫帚都要按长短摆。"
    $ last_block = 58
    u "方便拿。"
    $ last_block = 61
    "她学我以前的样子，压低声音：「到底是谁又把扫帚——」"
    $ last_block = 62
    u "不像。"
    $ last_block = 65
    "夏澄把下一本册子递过来。我们各自工作了一会儿。"
    $ last_block = 66
    "「你宿舍申请办好了吗？」她问。"
    $ last_block = 67
    u "还没。差几天截止吧。"
    $ last_block = 68
    x "『吧』？"
    $ last_block = 69
    u "通知看了一半。"
    $ last_block = 70
    x "那最好把另一半看完。"
    $ last_block = 71
    "我说要是没地方住，干脆睡在改造后的活动室。她打量了房间一圈，建议我至少先把它打扫干净。"
    $ last_block = 72
    "我问她去外地的准备怎样。她去年年底就申请了宿舍，正收拾相机、电脑和一堆自己也数不清的配件。"
    $ last_block = 73
    u "能放下吗？"
    $ last_block = 74
    x "应该吧。"
    $ last_block = 75
    u "你也会说『应该』啊。"
    $ last_block = 76
    x "……你今天是专程抓我话柄的吗？"
    show xc quiet at character_right
    $ last_block = 77
    "她笑了一下，低头把相机包拉链重新拉紧。明明刚才已经拉过。"
    $ last_block = 78
    "「你去了大学，有什么想做的？」她又问。"
    $ last_block = 79
    u "还没想好。"
    $ last_block = 80
    x "真没有？"
    $ last_block = 81
    "我抬头望向窗外。学校后方的老街正在施工，那家文具店旁边的屋顶已经拆掉了。"
    $ last_block = 82
    u "那边的房子，拆得真快。"
    $ last_block = 83
    "夏澄顺着我的目光看去：「那不是以前我们绕路去车站的地方吗？」"
    $ last_block = 84
    u "文具店还在，拆的是旁边那栋。"
    $ last_block = 85
    x "你记得真清楚。"
    $ last_block = 86
    u "经常路过嘛。"
    $ last_block = 87
    "她点了点头，没有再追问大学的话题。我们低头整理纸页，走廊里传来一阵推车轮子碾过接缝的声音。"
    play sound "audio/bell.wav" volume 0.42
    $ last_block = 88
    "四点二十分，走廊响了一次预备铃。夏澄拿起相机，说要去拍操场。"
    $ last_block = 89
    x "你别趁我不在把东西全塞左边。"
    $ last_block = 90
    u "那我全塞右边。"
    $ last_block = 91
    x "更不行。"
    hide xc with dissolve
    $ last_block = 92
    "她带着笑走了。我弯腰抽出柜子底下那几本还没登记的册子。"
    $ last_block = 93
    "最上面一本封皮卷了边，写着：值日记录。"
    play sound "audio/paper.wav"
    $ last_block = 94
    "我翻开。纸上并排写着「朝仓悠」「夏澄」。我的那个「悠」写歪了。"
    play sound "audio/chair.wav"
    $ last_block = 95
    "咚。"
    $ last_block = 96
    "后排有椅子被推开。我抬起头。所有椅子都好好地挨着桌子。"
    $ memory_date = "日期不明"
    $ last_block = 97
    echo "窗户关了吗？"
    $ last_block = 98
    "声音近得像从后排传来。"
    $ last_block = 99
    "我去门口看了一眼。走廊是空的。回到桌边时，我的手指碰到了下一页。"
    play sound "audio/broom.wav"
    $ last_block = 100
    "沙沙，扫帚在地板上摩擦。"
    $ last_block = 101
    echo "喂，你又把灰扫到我这边了。"
    $ last_block = 102
    echo "哪有，明明是风吹的。"
    $ last_block = 103
    echo "窗户都关着呢。"
    $ last_block = 104
    echo "那就是扫帚的问题。"
    $ last_block = 105
    "有人笑了。"
    $ last_block = 106
    "我不动了。"
    $ last_block = 107
    "那是夏澄的声音。另一个……是我自己的。"
    $ chapter_title = "02 / 四月十二日"
    scene bg classroom with dissolve
    show screen scene_heading
    play sound "audio/paper.wav"
    $ last_block = 109
    "我合上册子。声音停了。翻开，刚才的扫帚声从头响起。"
    $ last_block = 110
    "我试了三次。窗边有人拖椅子，讲台旁有人敲粉笔盒。我伸手摸过去，只摸到凉凉的桌面。"
    $ memory_date = "高一 / 四月十二日"
    $ last_block = 111
    "我翻看记录上的日期。四月十二日，高一。"
    $ last_block = 112
    "那时的夏澄还会为了一点灰尘和我争半天。她说话比现在快，也更不肯让步。可细听下去，过去的我也不是什么好相处的人。"
    $ last_block = 113
    px "你擦黑板了吗？"
    $ last_block = 114
    pu "擦了。"
    $ last_block = 115
    px "上面还有一个字。"
    $ last_block = 116
    pu "那个是前天留下的吧。"
    $ last_block = 117
    px "……字还分今天前天啊？"
    $ last_block = 118
    "我笑出了声。"
    $ last_block = 119
    "收书包的时候，我说笔不见了。找了半天，她说：「你耳朵上那支呢？」"
    play sound "audio/bell.wav"
    $ last_block = 120
    "他们走到门口时，放学铃响了。那段旋律一直没换，只是现在听起来，响得格外近。"
    $ last_block = 121
    "我摸了摸自己的耳朵，那里当然什么也没有。"
    $ last_block = 122
    "换到另一个日期，听见两名同学说「灯关了吗」「关了」，然后是门关上的声音。再翻一页，只有拖地声，甚至一句话也没有。"
    $ last_block = 123
    "大部分过去都这样平淡。册子不会给我解释，更不会挑出我想听的部分。"
    $ memory_date = "高一 / 六月二十一日"
    play memory "audio/rain.wav" fadein 0.4
    $ last_block = 124
    "六月二十一日有雨。纸页展开时，雨点敲在窗上，远处有雷。"
    $ last_block = 125
    px "你带伞了吗？"
    $ last_block = 126
    pu "带了。"
    $ last_block = 127
    px "那走吧。"
    $ last_block = 128
    pu "你没带？"
    $ last_block = 129
    px "所以才叫你一起走啊。"
    $ last_block = 130
    pu "你还真理直气壮。"
    $ last_block = 131
    px "你带的伞有多大？"
    $ last_block = 132
    pu "普通折叠伞。"
    $ last_block = 133
    px "……听起来很危险。"
    stop memory fadeout 0.5
    $ memory_date = ""
    $ last_block = 134
    "随后是开门、脚步声。记录到此结束。"
    $ last_block = 135
    "我倒记得伞下的事。到了车站，我们各湿了一边肩膀，还蹲在自动贩卖机前捡了半天零钱，差点错过车。"
    $ last_block = 136
    "我记得那天，却完全不记得我们从哪一天开始不再一起回家。"
    show xc neutral at character_right with dissolve
    $ last_block = 137
    "夏澄拍完走廊回来，看我对着册子发呆。"
    $ last_block = 138
    x "发现什么宝贝了？"
    $ last_block = 139
    u "旧值日簿。"
    $ last_block = 140
    x "哦，你的扫帚犯罪记录。"
    $ last_block = 141
    u "我那时候名声这么差吗？"
    $ last_block = 142
    x "主要在我这里比较差。"
    $ last_block = 143
    "我提起那场雨。她想了想：「你那把伞小得要命。」"
    $ last_block = 144
    u "我记得你一直抱怨。"
    $ last_block = 145
    x "因为你把伞都往我这边偏。你书包湿得最厉害。"
    $ last_block = 146
    "我愣了一下。这个我没记得。"
    menu:
        "原来你还记得。":
            u "原来你还记得。"
            $ last_block = 150
            x "当然。你一路都在看车站的钟。"
            $ last_block = 151
            u "差点赶不上。"
            $ last_block = 152
            x "最后还不是赶上了。"
            show xc smile at character_right
            $ last_block = 153
            "她笑了一下，我也跟着笑了。"
        "看来得换把大伞了。":
            $ umbrella_joke = True
            u "看来得换把大伞了。"
            $ last_block = 155
            x "先学会好好撑伞吧。"
            $ last_block = 156
            u "怎么又成我的问题了。"
            $ last_block = 157
            x "总不能怪下雨。"
            show xc smile at character_right
            $ last_block = 158
            "她说得一本正经，自己却先笑了。"
    $ last_block = 160
    "「你怎么突然想起这事？」她问。"
    $ last_block = 161
    u "翻到那天的日期。"
    $ last_block = 162
    x "哦。真亏你还记得。"
    $ last_block = 163
    "她转身去整理桌椅。我本想问她还记不记得更多，又把话收了回去。她就在这里，我却一直想听两年前的她说话。"
    play sound "audio/paper.wav"
    $ last_block = 164
    "我合上册子，去帮她扶住那张缺了一颗螺丝的桌子。"
    $ chapter_title = "03 / 没有发生的争吵"
    scene bg classroom with dissolve
    show screen scene_heading
    hide xc with dissolve
    play sound "audio/paper.wav"
    $ memory_date = "十月 / 值日记录"
    $ last_block = 166
    "夏澄去储物间取新的归档箱。我留在教室，翻到十月。"
    $ last_block = 167
    "这一页有夏澄的名字。她说周末要去上摄影课，过去的我说模拟考试快到了。"
    $ last_block = 168
    px "那这周不一起去书店了？"
    $ last_block = 169
    pu "等考完吧。"
    $ last_block = 170
    px "好啊。你别又忘。"
    $ last_block = 171
    pu "不会。"
    $ last_block = 172
    "他们都没生气。连语气都轻快。"
    $ last_block = 173
    "下一页两人分开得更早。再下一页换了别的值日生。夏澄去参加校外课程，我开始放学后留在图书室。没有哪一页写着告别。"
    $ last_block = 174
    "我开始不耐烦。总该有一次争吵，一次爽约，或者某句说错的话。"
    $ memory_date = ""
    $ last_block = 175
    "我把几页有我们名字的记录折出很小的角。四月，六月，还有一页是冬天。"

label notebook_hub:
    $ memory_date = ""
    stop memory fadeout 0.3
    window hide
    call screen notebook_pages
    window auto
    if _return == "april":
        $ replay_april = True
        $ memory_date = "高一 / 四月十二日"
        play sound "audio/broom.wav"
        $ last_block = 182
        "扫帚声又响起来。"
        $ last_block = 183
        px "那走吧？"
        $ last_block = 184
        pu "等一下，笔不见了。"
        $ last_block = 185
        "书包被翻得窸窣作响。随后，她指出那支笔就夹在我耳朵上。"
        $ last_block = 186
        "我没有再去摸耳朵，只低头看着纸上并排写着的两个名字。"
        jump notebook_hub
    elif _return == "june":
        $ replay_june = True
        $ memory_date = "高一 / 六月二十一日"
        play memory "audio/rain.wav" fadein 0.3
        $ last_block = 189
        "窗上重新落下雨点。"
        $ last_block = 190
        px "你带伞了吗？"
        $ last_block = 191
        pu "带了。"
        $ last_block = 192
        px "那走吧。"
        $ last_block = 193
        pu "你没带？"
        $ last_block = 194
        px "所以才叫你一起走啊。"
        $ last_block = 195
        "我等着她抱怨伞太小。脚步声却已经离开教室。"
        jump notebook_hub
    else:
        $ memory_date = "一月十七日"
        $ last_block = 198
        "一月十七日，窗外呼呼刮风。夏澄正在收相机。"
        $ last_block = 199
        px "今天要不要拍一张？"
        $ last_block = 200
        pu "拍什么？"
        $ last_block = 201
        px "我们啊。教室也一起拍进去。"
        $ last_block = 202
        pu "现在？我还得赶车。"
        $ last_block = 203
        px "那就下次。"
        $ last_block = 204
        pu "嗯，下次。"
        $ last_block = 205
        "她问天气预报说的雪还下不下。我说不知道，顺手替她把窗关上了。谁都没再提那张照片。"
        $ last_block = 206
        "后来我们还在教室里见过。谈作业，借订书机，什么都说过一点。"
        $ last_block = 207
        "那张照片始终没有拍。"
    $ memory_date = ""
    stop memory fadeout 0.3
    $ last_block = 209
    "我继续往后翻。许多纸页只有椅子、风、粉笔的声音；有些说话的人，我已经叫不出名字。"
    $ last_block = 210
    "翻到学期末，也没听见谁说过一句重话。"
    show xc neutral at character_right with dissolve
    $ last_block = 211
    "夏澄搬着空箱子回来，看到我把册子摊了一桌。"
    $ last_block = 212
    x "你这是查案啊？"
    $ last_block = 213
    u "……可能是失物招领。"
    $ last_block = 214
    x "丢了什么？"
    $ last_block = 215
    u "不知道。"
    $ last_block = 216
    "她看了我一眼，没继续问，只把箱子挪到旁边，给我腾地方。"
    $ last_block = 217
    x "那你先找。我把这边收了。"
    $ last_block = 218
    "我看着她俯身搬书的背影。她肩上的相机带换过了，不再是以前那条。我连她什么时候换的都不知道。"
    $ last_block = 219
    "她抱起下一摞书。我把册子合起来，伸手接过上面快要滑下去的几本。"
    $ chapter_title = "04 / 现在的夏澄"
    scene bg classroom with dissolve
    show xc neutral at character_right with dissolve
    show screen scene_heading
    $ last_block = 221
    "旧教室渐渐收拾出了原来的地面。夏澄将相机放在讲台上，翻出拍摄改建老街的照片。"
    $ last_block = 222
    "「这张本来想删掉。」她说。"
    $ keep_print("street")
    show screen photo_view("street")
    $ last_block = 223
    "画面里一半是旧文具店，一半是施工围挡。围挡挡住招牌，路面的箭头也没有拍全。"
    $ last_block = 224
    "「为什么？」我问。"
    $ last_block = 225
    x "乱。想把右边裁了，又觉得少了点什么。"
    $ last_block = 226
    "我指向围挡后露出来的路口：「这边下个月可能要改成单行道。现在这样，以后拍不到了。」"
    $ last_block = 227
    x "你连这个都知道？"
    $ last_block = 228
    u "有张施工公示贴在站牌上。"
    $ last_block = 229
    "夏澄放大照片，看了一阵：「好像也是。」"
    $ last_block = 230
    u "不过我不懂构图。"
    $ last_block = 231
    x "没事，我也还没弄明白。"
    hide screen photo_view
    $ last_block = 232
    "她没删照片，把相机收起来。"
    $ last_block = 233
    "我们开始装最后一箱资料。谈到下个月，夏澄说新学校的课表可能很满。"
    $ last_block = 234
    "「至少你已经知道自己想做什么。」我说。"
    $ last_block = 235
    x "也不一定做得好啊。"
    $ last_block = 236
    u "可你看起来挺轻松的。"
    show xc quiet at character_right
    $ last_block = 237
    "夏澄停下手。她没有立刻发火，只是问：「我哪里轻松了？」"
    $ last_block = 238
    "我知道自己说得不公平，却不知怎么把话收回来。"
    $ last_block = 239
    "「我只是没跟你说过而已。」她说。"
    $ last_block = 240
    "我搬桌子，她贴标签。她找不到胶带头，我替她挑起来。她接过去，小声说了句谢谢。"
    $ keep_print("light")
    show screen photo_view("light")
    $ last_block = 241
    "后来夏澄拿出另一张照片。逆光拍的，焦点有点偏，天空发白。"
    $ last_block = 242
    x "这个我拍了好多次。准备作品集的时候，一直不敢用。"
    $ last_block = 243
    u "后来用了？"
    $ last_block = 244
    x "没有。交了另一张。"
    menu:
        "你喜欢的是哪一部分？":
            u "你喜欢的是哪一部分？"
            $ last_block = 248
            "夏澄把照片放大，指着墙角一道很小的光。"
            $ last_block = 249
            x "这里。拍的时候刚好照进来，后来再去，就不是这个样子了。"
            $ last_block = 250
            u "我刚才都没注意。"
            $ last_block = 251
            x "我也差点把它裁掉。太靠边了。"
        "能看看你最后选的那张吗？":
            u "能看看你最后选的那张吗？"
            $ last_block = 253
            x "可以啊。"
            $ keep_print("portfolio")
            show screen photo_view("portfolio")
            $ last_block = 254
            "她往后翻了几张。交进作品集的照片，天空有颜色，墙面的线也端端正正。"
            $ last_block = 255
            "「至少这张对上焦了。」她说。"
            $ last_block = 256
            u "你更喜欢哪张？"
            show screen photo_view("light")
            $ last_block = 257
            "夏澄来回切了两次，最后停在刚才那张上。"
            $ last_block = 258
            x "……还是这张吧。"
    hide screen photo_view
    $ last_block = 260
    "她没有立刻收起相机，拇指沿着屏幕边缘蹭了一下。"
    $ last_block = 261
    x "交作品集那晚，我把提交页面开着，一直开到我妈起来喝水。她以为我在等录取结果。"
    x "我连提交都还没按。"
    $ last_block = 262
    "我道了歉：「刚才说你轻松，是我自己乱猜的。」"
    $ last_block = 263
    x "嗯，你确实乱猜。"
    $ last_block = 264
    "过了一会儿，她补充：「不过我也没跟你说。」"
    $ last_block = 265
    "我打开手机给她看。施工公示下面，还存着我从市役所网站找来的旧地图。"
    u "我也不知道存这些干嘛。有时候回家会特地绕过去，看看又拆到哪里了。"
    $ last_block = 266
    "「你为什么不去了解一下？」她问。"
    $ last_block = 267
    u "这也不一定能当职业。"
    $ last_block = 268
    x "那就先去看看啊。你不是已经看了很久吗？"
    $ last_block = 269
    "我一时答不上来。"
    $ last_block = 270
    "她把那张照片缩回原来的大小。墙角那条光一下就看不见了。"
    show screen photo_view("street")
    $ last_block = 271
    "她用指尖把照片放大，又缩回去。我说那条巷子其实以前有一条很窄的排水沟，她问在哪里。我讲得比自己预想的久，她也没打断。"
    hide screen photo_view
    $ last_block = 272
    "窗外光线斜了些。夏澄架好相机，回头问：「要不要拍张照？」"
    $ last_block = 273
    u "现在？东西还没搬完。"
    $ last_block = 274
    x "拍完再搬。"
    $ last_block = 275
    u "背景有点乱。"
    $ last_block = 276
    x "本来就乱啊。"
    $ last_block = 277
    u "那就下——"
    $ last_block = 278
    "我停了一下。夏澄的手还扶在相机上，等着我。"
    $ last_block = 279
    u "……拍吧。"
    show xc shy at character_right
    $ last_block = 280
    "我把手里的胶带放下，走过去。"
    play sound "audio/phone.wav"
    pause 0.4
    play sound "audio/camera.wav"
    with shutter_flash
    $ last_block = 281
    "倒计时响起。她让我靠近一点，我去整理衣领。快门正好在这时响了。"
    $ keep_print("together")
    show screen photo_view("together")
    $ last_block = 282
    "照片里我低着头，她眨着一只眼睛。我们看着那张照片，都笑了。"
    $ last_block = 283
    "「重拍？」她问。"
    $ last_block = 284
    u "算了，留着吧。"
    $ last_block = 285
    x "你确定？"
    $ last_block = 286
    u "嗯。至少袖子拍全了。"
    hide screen photo_view
    show xc smile at character_right
    $ last_block = 287
    "夏澄笑着按下保存。"
    $ last_block = 288
    "离开前，她说回去整理今天的照片，晚点发给我。她得先把相机包送回家，再准备毕业典礼的东西。"
    $ last_block = 289
    "「到了那边……」我开了个头。"
    $ last_block = 290
    x "嗯？"
    $ last_block = 291
    "到了那边，也发给我看看吧。"
    $ last_block = 292
    "话到了嘴边，变成了「路上小心」。我替她把门拉开一半，又想起自己真正要说的那句。"
    $ last_block = 293
    u "还有，今天的照片别忘了。"
    $ last_block = 294
    x "忘不了。你那一百日元还没结呢。"
    $ last_block = 295
    "我松开门把，给她腾出位置。"
    $ last_block = 296
    x "明天见。"
    $ last_block = 297
    u "嗯，明天见。"
    hide xc with dissolve
    $ last_block = 298
    "她提了提肩上的相机包，往楼梯口走去。"
    $ last_block = 299
    "明天毕业典礼结束，我们还得回来还钥匙。我知道在哪儿能见到她。"
    $ chapter_title = "05 / 明天"
    scene bg classroom_evening with dissolve
    show screen scene_heading
    $ last_block = 301
    "我把最后一箱资料封好。走廊的灯已经亮了，窗里只照得出空桌和我。"
    $ last_block = 302
    "旧值日簿还放在桌上。老师说这批资料要归档，不必今天丢弃。我把它放进箱子，又忍不住抽出来。"
    play sound "audio/phone.wav"
    $ last_block = 303
    "手机震动。夏澄发来刚才那张合照，后面跟着一条消息："
    $ last_block = 304
    mx "还有几张没发过的。要看吗？"
    $ last_block = 305
    "通知里的合照缩成小小一张，能看见我们靠在一起的肩膀。"
    $ last_block = 306
    "我在输入框里写下「你到了那边」，停了一会儿，又删掉。"
    $ last_block = 307
    "值日簿摊在旁边。四月那一页翘起一点，刚好露出我们两个的名字。"

label final_choice:
    menu:
        "翻开四月十二日那一页":
            jump listen_again
        "点开夏澄发来的合照":
            jump ending_b

label listen_again:
    play sound "audio/paper.wav"
    $ memory_date = "高一 / 四月十二日"
    $ last_block = 313
    "我把手机放到一边，翻开四月十二日的记录。"
    play sound "audio/broom.wav"
    $ last_block = 314
    "扫帚摩擦地面。黑板上还剩一个没擦掉的字。"
    $ last_block = 315
    px "你擦黑板了吗？"
    $ last_block = 316
    pu "擦了。"
    $ last_block = 317
    px "上面还有一个字。"
    $ last_block = 318
    pu "那个是前天留下的吧。"
    $ last_block = 319
    px "……字还分今天前天啊？"
    $ last_block = 320
    "我跟着笑了一下。后面的话已经知道了，还是听到他们收好书包。"
    $ last_block = 321
    px "那走吧？"
    $ last_block = 322
    "过去的我又在找那支夹在耳朵上的笔。她等在门边，说了什么，我没听清。"
    play sound "audio/phone.wav"
    $ last_block = 324
    "手机又震了一下。"
    $ memory_date = ""
    $ last_block = 325
    mx "等等，合照好像发的原图，有点大。"
    play sound "audio/paper.wav"
    $ last_block = 326
    "我合上册子。她又发来一句：「收到了吗？」"
    menu:
        "点开合照，回复她。":
            jump ending_b
        "等明天见面再说。":
            jump ending_a

label ending_a:
    $ last_block = 333
    "我回了句「收到了」。"
    play sound "audio/phone.wav"
    $ last_block = 334
    "夏澄很快发来一个点头的表情。对话框安静下来。"
    $ last_block = 335
    "我重新输入：「你到了那边，也拍点照片给我吧。」"
    $ last_block = 336
    "字已经写全了，发送键就在旁边。"
    $ last_block = 337
    "走廊里有人推着车经过。我抬起头，看见玻璃上映着空荡荡的后排。"
    $ last_block = 338
    "明天见面的时候再问吧。还能指着照片说，哪条街和这里有点像。"
    $ last_block = 339
    "我退出输入框。那句话留在草稿里。"
    $ last_block = 340
    "四月那页还翘着，像有人拿笔在那儿占了个位置。"
    $ last_block = 341
    "我把它抚平，连同册子一起放回归档箱。"
    $ last_block = 342
    "我把手机收进口袋。"
    $ last_block = 343
    u "……明天再说吧。"
    $ last_block = 344
    "教室里最后一点光退到窗框外。远处有人关上走廊的门。"
    $ last_block = 345
    "我站在空教室里，等了几秒。"
    scene bg corridor with dissolve
    $ last_block = 346
    "教室后面的钟走了一格。我关上灯，跟着自己的脚步声往楼梯口走。"
    $ last_block = 347
    "到了楼下，我记起钥匙还在我这里。明天还钥匙时，她会在我旁边。我把那句话在心里又说了一遍。"
    $ ending_seen = "A"
    $ persistent.ending_a = True
    call finish_story("再听一次", "A")
    return

label ending_b:
    show screen photo_view("together")
    $ last_block = 350
    "我点开那张合照。"
    $ last_block = 351
    "原图慢慢清楚起来。我的衣领还没整理好，夏澄眨着一只眼睛。"
    $ last_block = 352
    "我先发了句「收到了，没问题」，又回到她问要不要看照片的那条消息。"
    $ last_block = 353
    mu "好啊。发我看看。"
    play sound "audio/phone.wav"
    show screen photo_view("window")
    $ last_block = 354
    "几张照片传过来。旧街的围挡、一个雨后的公交站、空教室里的窗户。最后那张窗户照片，边缘还留着一点校服袖子。"
    $ last_block = 355
    mu "你没裁掉啊。"
    $ last_block = 356
    mx "裁了就少一块窗框，算了。"
    $ last_block = 357
    mu "我觉得留着挺好。"
    $ last_block = 358
    mx "你看，肖像权已经处理好了。"
    show screen photo_view("street")
    $ last_block = 359
    "我笑了。又翻回那张改道前的旧街。"
    $ last_block = 360
    mu "你到了新城市，也拍点街道给我看看吧。"
    $ last_block = 361
    mx "你想看？"
    $ last_block = 362
    mu "嗯。我最近查了些城市规划的东西，发现自己还挺感兴趣。"
    $ last_block = 363
    mx "下午你说不清的，就是这个？"
    $ last_block = 364
    mu "大概吧。还没想好能做什么，先了解一下。"
    $ last_block = 365
    "夏澄过了一会儿才回复。"
    $ last_block = 366
    mx "那我到那边拍给你。你也拍点这边的变化。"
    $ last_block = 367
    mu "我拍得不好可别笑。"
    $ last_block = 368
    mx "这要求有点难。"
    $ last_block = 369
    mu "……"
    $ last_block = 370
    mx "开玩笑啦。下次见面教你。"
    $ last_block = 371
    "我盯着「下次」两个字看了一会儿。"
    $ last_block = 372
    mu "周末方便吗？就算还没过去，也可以先拍点这边的。"
    $ last_block = 373
    mx "可以啊。"
    $ last_block = 374
    mu "那先约周六下午？你到时候忙的话再改。"
    play sound "audio/phone.wav"
    $ last_block = 375
    "夏澄回得很快：「嗯！在文具店门口等。」"
    if umbrella_joke:
        $ umbrella_recalled = True
        $ last_block = 377
        mx "先看天气预报。你的伞我可不敢再信了。"
        $ last_block = 378
        mu "这次带大的。"
    $ last_block = 380
    "随后又补了一句：「不过你得先把宿舍申请办了。」"
    $ last_block = 381
    mu "现在就回去看通知。"
    $ last_block = 382
    mx "这次真的？"
    $ last_block = 383
    mu "真的。"
    hide screen photo_view
    scene bg corridor with dissolve
    $ last_block = 384
    "我把值日簿放回归档箱，关上教室的灯。手机还握在手里，屏幕上是那张拍得不怎么好看的合照。"
    $ last_block = 385
    "我走进亮着灯的走廊。外面有风，冷得很普通。"
    play sound "audio/phone.wav"
    $ last_block = 386
    "手机又震了一下。"
    $ last_block = 387
    mx "对了，刚才那张合照，别删哦。"
    $ last_block = 388
    "我边走边回：「不会。」"
    $ ending_seen = "B"
    $ persistent.ending_b = True
    call finish_story("明天之后", "B")
    return

label finish_story(title, code):
    stop memory fadeout 1.0
    stop ambience fadeout 1.0
    hide screen scene_heading
    hide screen photo_view
    window hide
    play music "audio/after_bell.wav" fadein 1.0 noloop
    call screen ending_card(title, code)
    return
