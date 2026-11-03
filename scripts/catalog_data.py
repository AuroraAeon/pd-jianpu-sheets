# -*- coding: utf-8 -*-
"""100 public-domain melodies for jianpu rendering."""

SONGS = []

def add(**kwargs):
    SONGS.append(kwargs)

add(
    slug='molihua',
    titles=['茉莉花', '江苏民歌'],
    key='C', meter='2/4', tempo='优美地',
    source='江苏民歌（传统曲调，公有领域）',
    body="Q: 3 3 | 5. 6/ | 5 3 | 1 2 |\nQ: 3 5 | 6 1' | 6 5 | 3 - |\nQ: 5 5 | 6. 5/ | 3 5 | 2 3 |\nQ: 5 3 | 2 1 | 6, 1 | 2 - |\nQ: 3 3 | 5. 6/ | 5 3 | 1 2 |\nQ: 3 5 | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 3 | 2 1 | 6, 5, |\nQ: 1 2 | 3 5 | 2 1 | 1 - ||",
)
add(
    slug='xiaobaicai',
    titles=['小白菜', '河北民歌'],
    key='C', meter='4/4', tempo='稍慢 伤感地',
    source='河北民歌（传统曲调，公有领域）',
    body="Q: 5 6 1' 6 | 5 - - - | 3 5 6 5 | 3 - - - |\nQ: 2 3 5 3 | 2 - 1 - | 6, 1 2 3 | 1 - - - |\nQ: 5 6 1' 6 | 5 - - - | 3 5 6 5 | 3 - - - |\nQ: 2 3 5 2 | 1 - 6, - | 5, 6, 1 2 | 1 - - - ||",
)
add(
    slug='yimengshan',
    titles=['沂蒙山小调', '山东民歌'],
    key='C', meter='2/4', tempo='中速 抒情地',
    source='山东民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 6 5 | 3 5 |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 5 5 | 6 1' | 6 5 | 3 5 |\nQ: 2 3 | 5 2 | 1 6, | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 3 |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 5 5 | 6 1' | 6 5 | 3 2 |\nQ: 1 6, | 5, 6, | 1 - | 1 - ||",
)
add(
    slug='xiuhebao',
    titles=['绣荷包', '山西民歌'],
    key='D', meter='2/4', tempo='中速',
    source='山西民歌（传统曲调，公有领域）',
    body='Q: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 3 2 | 1 6, | 5, 6, | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 3 | 2 1 | 6, - ||',
)
add(
    slug='kangding',
    titles=['康定情歌', '四川民歌'],
    key='G', meter='2/4', tempo='中速 亲切地',
    source='四川民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 6 5 | 3 - |\nQ: 5 6 | 5 3 | 2 3 | 2 - |\nQ: 5 5 | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 2 | 1 - | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 6, - |\nQ: 5 5 | 6 1' | 6 5 | 3 2 |\nQ: 1 - | 1 - ||",
)
add(
    slug='mengjiangnv',
    titles=['孟姜女', '江苏民歌'],
    key='C', meter='4/4', tempo='稍慢',
    source='江苏民歌（传统曲调，公有领域）',
    body='Q: 6, 1 2 3 | 5 - 3 2 | 1 6, 5, 6, | 1 - - - |\nQ: 2 3 5 6 | 5 - 3 2 | 1 2 3 5 | 2 - - - |\nQ: 6, 1 2 3 | 5 - 3 2 | 1 6, 5, 6, | 1 - - - |\nQ: 2 3 5 3 | 2 1 6, 5, | 6, 1 2 3 | 1 - - - ||',
)
add(
    slug='fengyang',
    titles=['凤阳花鼓', '安徽民歌'],
    key='C', meter='2/4', tempo='活泼地',
    source='安徽民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 5 3 | 2 - |\nQ: 3 5 | 2 3 | 1 6, | 5, - |\nQ: 5 5 | 6 1' | 5 3 | 2 - |\nQ: 3 2 | 1 6, | 5, 6, | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 1 - ||",
)
add(
    slug='zizhudiao',
    titles=['紫竹调', '江南丝竹曲调'],
    key='G', meter='2/4', tempo='中速 优美',
    source='江南传统曲调（公有领域）',
    body="Q: 3 5 | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 3 5 | 6 1' | 6 5 | 3 5 |\nQ: 6 5 | 3 2 | 1 - | 1 - ||",
)
add(
    slug='wuxijing',
    titles=['无锡景', '江苏民歌'],
    key='C', meter='2/4', tempo='中速',
    source='江苏民歌（传统曲调，公有领域）',
    body="Q: 5. 6/ | 5 3 | 2 3 | 5 - |\nQ: 6 1' | 6 5 | 3 5 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 2 | 1 6, | 5, - |\nQ: 5. 6/ | 5 3 | 2 3 | 5 - |\nQ: 6 5 | 3 2 | 1 - | 1 - ||",
)
add(
    slug='xiaofangniu',
    titles=['小放牛', '河北民歌'],
    key='C', meter='2/4', tempo='活泼 对话风',
    source='河北民歌（传统曲调，公有领域）',
    body="Q: 5 6 | 5 3 | 2 3 | 5 - |\nQ: 6 1' | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 6, - |\nQ: 5 6 | 5 3 | 2 3 | 5 - |\nQ: 3 2 | 1 6, | 1 - | 1 - ||",
)
add(
    slug='zoukou',
    titles=['走西口', '山西民歌'],
    key='C', meter='2/4', tempo='稍慢',
    source='山西/内蒙古民歌（传统曲调，公有领域）',
    body='Q: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 5, 6, | 1 2 | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 6, - |\nQ: 6, 1 | 2 3 | 5 3 | 2 1 |\nQ: 6, 5, | 6, 1 | 2 - | 1 - ||',
)
add(
    slug='lanhuahua',
    titles=['兰花花', '陕北民歌'],
    key='C', meter='2/4', tempo='稍自由',
    source='陕北民歌（传统曲调，公有领域）',
    body="Q: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 5 - |\nQ: 6 5 | 3 2 | 1 - | 1 - ||",
)
add(
    slug='xintianyou',
    titles=['信天游', '陕北民歌'],
    key='C', meter='2/4', tempo='高亢 自由地',
    source='陕北民歌（传统曲调，公有领域）',
    body="Q: 5 - | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 - | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 1 6, | 5, - | 6, 1 | 2 - |\nQ: 5 6 | 1' - | 6 5 | 3 2 |\nQ: 1 - | 1 - ||",
)
add(
    slug='ganshengling',
    titles=['赶牲灵', '陕北民歌'],
    key='C', meter='2/4', tempo='中速',
    source='陕北民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 6 5 | 3 5 |\nQ: 2 - | 3 5 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 2 | 1 6, | 5, 6, | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 - | 1 - | 1 - ||",
)
add(
    slug='sanshilipu',
    titles=['三十里铺', '陕北民歌'],
    key='C', meter='2/4', tempo='叙事地',
    source='陕北民歌（传统曲调，公有领域）',
    body="Q: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 1' 6 | 5 - |\nQ: 3 5 | 2 3 | 2 1 | 6, - |\nQ: 5, 6, | 1 2 | 3 5 | 2 1 |\nQ: 6, - | 1 - ||",
)
add(
    slug='duihua',
    titles=['对花', '华北民歌'],
    key='C', meter='2/4', tempo='活泼',
    source='华北传统对花调（公有领域）',
    body="Q: 5 6 | 5 3 | 2 3 | 5 - |\nQ: 6 1' | 6 5 | 3 5 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 6, |\nQ: 5, 6, | 1 2 | 3 2 | 1 - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 1 - ||",
)
add(
    slug='fangfengzheng',
    titles=['放风筝', '河北民歌'],
    key='C', meter='2/4', tempo='轻快',
    source='河北民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 5 6 | 5 3 |\nQ: 2 3 | 5 - | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 2 | 1 - | 1 - ||",
)
add(
    slug='caichapudie',
    titles=['采茶扑蝶', '福建民歌'],
    key='C', meter='2/4', tempo='轻快 舞蹈风',
    source='福建民歌（传统曲调，公有领域）',
    body="Q: 3 5 | 6 5 | 3 5 | 2 - |\nQ: 1 2 | 3 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 3 2 | 1 6, | 5, 6, | 1 - |\nQ: 3 5 | 6 1' | 6 5 | 3 5 |\nQ: 2 3 | 5 2 | 1 - | 1 - ||",
)
add(
    slug='bagengluchaihua',
    titles=['拔根芦柴花', '江苏民歌'],
    key='C', meter='2/4', tempo='中速 明朗',
    source='江苏民歌（传统曲调，公有领域）',
    body="Q: 5 6 | 5 3 | 2 3 | 5 - |\nQ: 6 1' | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 1' 6 | 5 - |\nQ: 3 5 | 2 3 | 1 6, | 5, - |\nQ: 5 6 | 5 3 | 2 1 | 6, 5, |\nQ: 1 2 | 3 5 | 2 1 | 1 - ||",
)
add(
    slug='yangliuqing',
    titles=['杨柳青', '江苏民歌'],
    key='C', meter='2/4', tempo='欢快',
    source='江苏民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 3 5 | 6 5 | 3 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 3 |\nQ: 5 2 | 1 - | 1 - ||",
)
add(
    slug='midushange',
    titles=['弥渡山歌', '云南民歌'],
    key='C', meter='2/4', tempo='抒情',
    source='云南民歌（传统曲调，公有领域）',
    body="Q: 6, 1 | 3 5 | 6 5 | 3 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 6 5 | 3 2 |\nQ: 1 6, | 5, 6, | 1 - | 1 - |\nQ: 3 5 | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 2 | 1 - | 1 - ||",
)
add(
    slug='caidiao',
    titles=['猜调', '云南民歌'],
    key='C', meter='2/4', tempo='活泼 诙谐',
    source='云南彝族民歌（传统曲调，公有领域）',
    body="Q: 5 6 | 5 3 | 2 3 | 1 6, |\nQ: 5, 6, | 1 2 | 3 5 | 2 - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 5 | 2 1 | 6, 5, | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 - | 1 - ||",
)
add(
    slug='shidajie',
    titles=['十大姐', '云南民歌'],
    key='C', meter='2/4', tempo='中速',
    source='云南民歌（传统曲调，公有领域）',
    body="Q: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 1 |\nQ: 6, 5, | 6, 1 | 2 - | 1 - |\nQ: 3 5 | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 2 | 1 - | 1 - ||",
)
add(
    slug='alamuhan',
    titles=['阿拉木汗', '新疆维吾尔族民歌'],
    key='C', meter='2/4', tempo='活泼',
    source='新疆维吾尔族民歌（传统曲调，公有领域）',
    body="Q: 5 5 | 6 1' | 6 5 | 3 5 |\nQ: 2 3 | 5 - | 3 2 | 1 - |\nQ: 2 3 | 5 6 | 5 3 | 2 1 |\nQ: 6, 1 | 2 3 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 2 | 1 6, | 1 - | 1 - ||",
)
add(
    slug='taiyangchulai',
    titles=['太阳出来喜洋洋', '四川民歌'],
    key='A', meter='2/4', tempo='高亢 自由地',
    source='四川民歌（传统曲调，公有领域；简谱为常见教学版）',
    body='Q: 2/ 3/ 2/ 1/ | 2 - | 2/ 3/ 2/ 1/ | 6, - |\nQ: 5, 6,/ | 2/ 2/ 6,/ 5,/ | 6, 0/ 2/ | 6,. 2/ |\nQ: 6,. 0/ | 5, 0/ 6,/ | 2/ 2/ 6,/ 5,/ | 6, - |\nQ: 2/ 3/ 2/ 1/ | 2 3/ 0/ | 1/ 2/ 3/ 2/ | 1/ 6,/ 5,/ 0/ |\nQ: 5,/ 6,/ 1/ 6,/ | 2/ 2/ 6, | 5, 6,/ 0/ | 1/ 6,/ 2 1/ |\nQ: 6,/ 2 | 2 - ||',
)
add(
    slug='paipaizuo',
    titles=['排排坐', '传统儿歌'],
    key='D', meter='4/4', tempo='中速',
    source='传统幼儿歌曲（佚名词曲，公有领域）',
    body='Q: 1 1 2 - | 3 3 2 - | 5 5 3 1 | 2 3 2 - |\nQ: 3 3 2 - | 6, 1 2 - | 5 5 3 1 | 2 3 1 - ||',
)
add(
    slug='liuyanghe',
    titles=['浏阳河', '湖南民歌风'],
    key='C', meter='2/4', tempo='中速 优美',
    source='湖南民间歌曲风格曲调（常见简谱教学版；曲调流传作民歌曲调使用）',
    body="Q: 5 6 | 5 3 | 2 3 | 5 - |\nQ: 6 1' | 6 5 | 3 5 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 2 3 | 5 2 | 1 6, | 5, - |\nQ: 5 6 | 1' 6 | 5 3 | 2 3 |\nQ: 5 6 | 5 3 | 2 1 | 1 - ||",
)
add(
    slug='hongcai-meimei',
    titles=['红彩妹妹', '内蒙古民歌'],
    key='C', meter='2/4', tempo='中速',
    source='内蒙古民歌（传统曲调，公有领域）',
    body="Q: 5 6 | 1' 6 | 5 3 | 2 - |\nQ: 3 5 | 6 5 | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 3 | 2 - |\nQ: 1 2 | 3 5 | 2 1 | 6, - |\nQ: 5 6 | 1' 6 | 5 3 | 5 - |\nQ: 3 2 | 1 - | 1 - ||",
)
add(
    slug='senjidemae',
    titles=['森吉德玛', '内蒙古民歌'],
    key='C', meter='2/4', tempo='稍慢 辽阔',
    source='内蒙古民歌（传统曲调，公有领域）',
    body="Q: 5 - | 6 1' | 6 5 | 3 - |\nQ: 2 3 | 5 - | 3 2 | 1 - |\nQ: 6, 1 | 2 3 | 5 6 | 5 - |\nQ: 3 5 | 2 3 | 2 1 | 6, - |\nQ: 5 6 | 1' - | 6 5 | 3 2 |\nQ: 1 - | 1 - ||",
)
add(
    slug='twinkle-twinkle',
    titles=['Twinkle Twinkle Little Star', '小星星'],
    key='C', meter='4/4', tempo='Moderato',
    source='French folk melody Ah! vous dirai-je, maman (18th c.) — public domain',
    body='Q: 1 1 5 5 | 6 6 5 - | 4 4 3 3 | 2 2 1 - |\nQ: 5 5 4 4 | 3 3 2 - | 5 5 4 4 | 3 3 2 - |\nQ: 1 1 5 5 | 6 6 5 - | 4 4 3 3 | 2 2 1 - ||',
)
add(
    slug='mary-lamb',
    titles=['Mary Had a Little Lamb', '玛丽有只小羊羔'],
    key='C', meter='4/4', tempo='Moderato',
    source='American nursery song (19th c. melody) — public domain',
    body='Q: 3 2 1 2 | 3 3 3 - | 2 2 2 - | 3 5 5 - |\nQ: 3 2 1 2 | 3 3 3 3 | 2 2 3 2 | 1 - - - ||',
)
add(
    slug='london-bridge',
    titles=['London Bridge', '伦敦桥'],
    key='C', meter='4/4', tempo='Moderato',
    source='English nursery rhyme melody — traditional, public domain',
    body='Q: 5 6 5 4 | 3 4 5 - | 2 3 4 - | 3 4 5 - |\nQ: 5 6 5 4 | 3 4 5 - | 2 5 3 1 | 1 - - - ||',
)
add(
    slug='row-your-boat',
    titles=['Row Row Row Your Boat', '划船歌'],
    key='C', meter='6/8', tempo='Lively',
    source='American nursery round — traditional, public domain',
    body="Q: 1 - 1 - 1 | 2 3 - - - | 3 2 3 4 | 5 - - - - |\nQ: 1' 1' 1' 5 5 5 | 3 3 3 1 1 1 | 5 4 3 2 | 1 - - - - ||",
)
add(
    slug='frere-jacques',
    titles=['Frère Jacques', '两只老虎'],
    key='C', meter='4/4', tempo='Moderato',
    source='French traditional round — public domain',
    body='Q: 1 2 3 1 | 1 2 3 1 | 3 4 5 - | 3 4 5 - |\nQ: 5/ 6/ 5/ 4/ 3 1 | 5/ 6/ 5/ 4/ 3 1 | 1 5, 1 - | 1 5, 1 - ||',
)
add(
    slug='old-macdonald',
    titles=['Old MacDonald Had a Farm', '老麦克唐纳'],
    key='C', meter='4/4', tempo='Lively',
    source='American folk / nursery — traditional, public domain',
    body='Q: 5 5 5 2 | 3 3 2 - | 6 6 5 4 | 4 3 2 - |\nQ: 5 5 5 2 | 3 3 2 - | 6 6 5 4 | 4 3 2 - |\nQ: 2 2 5 5 | 5 5 5 - | 5 5 5 5 | 5 5 5 - |\nQ: 5 5 5 2 | 3 3 2 - | 6 6 5 4 | 3 2 1 - ||',
)
add(
    slug='this-old-man',
    titles=['This Old Man', '这位老人'],
    key='C', meter='4/4', tempo='Lively',
    source='English nursery song — traditional, public domain',
    body='Q: 5 3 5 - | 5 3 5 - | 6 5 4 3 | 2 3 4 - |\nQ: 5 5 5 5 | 5 3 2 1 | 2 5, 1 - ||',
)
add(
    slug='three-blind-mice',
    titles=['Three Blind Mice', '三只盲鼠'],
    key='C', meter='6/8', tempo='Moderato',
    source='English nursery round — traditional, public domain',
    body="Q: 3 - 2 | 1 - - | 3 - 2 | 1 - - |\nQ: 5 - 4 | 3 - - | 5 - 4 | 3 - - |\nQ: 1' 7 6 5 4 | 3 4 5 - - | 1' 7 6 5 4 | 3 2 1 - - ||",
)
add(
    slug='skip-to-lou',
    titles=['Skip to My Lou', '跳向我的露'],
    key='C', meter='4/4', tempo='Lively',
    source='American play-party song — traditional, public domain',
    body='Q: 5 5 3 5 | 6 5 3 - | 5 5 3 5 | 6 5 3 - |\nQ: 4 4 2 4 | 5 4 2 - | 5 5 6 5 | 4 3 1 - ||',
)
add(
    slug='clementine',
    titles=['Oh My Darling Clementine', '克莱门汀'],
    key='C', meter='3/4', tempo='Moderato',
    source='American folk song (19th c.) — public domain',
    body='Q: 5, 1 1 | 1 6, 1 | 2 3 3 | 3 - - |\nQ: 3 2 1 | 1 7, 1 | 2 5, 5, | 5, - - |\nQ: 5, 1 1 | 1 6, 1 | 2 3 3 | 3 - - |\nQ: 3 2 1 | 2 1 7, | 1 - - | 1 - - ||',
)
add(
    slug='oh-susanna',
    titles=['Oh Susanna', '哦苏珊娜'],
    key='C', meter='2/4', tempo='Lively',
    source='Stephen Foster (1848) — composer d.1864; public domain',
    body='Q: 1/ 2/ | 3 5 | 6 5 | 3 1 |\nQ: 2 3 | 2 5, | 1 - | 1/ 2/ |\nQ: 3 5 | 6 5 | 3 1 | 2 3 |\nQ: 2 1 | 1 - | 5 5 |\nQ: 6 5 | 3 1 | 2 3 | 2 5, |\nQ: 1 - | 1 - ||',
)
add(
    slug='camptown',
    titles=['Camptown Races', '坎普镇赛马'],
    key='C', meter='2/4', tempo='Lively',
    source='Stephen Foster (1850) — public domain',
    body='Q: 5 5 | 5 3 | 5 6 | 5 3 |\nQ: 2 3 | 2 1 | 2 - | 5 5 |\nQ: 5 3 | 5 6 | 5 3 | 2 1 |\nQ: 2 3 | 1 - | 5 6 |\nQ: 5 3 | 2 3 | 2 1 | 2 - |\nQ: 5 5 | 6 5 | 3 2 | 1 - ||',
)
add(
    slug='yankee-doodle',
    titles=['Yankee Doodle', '扬基歌'],
    key='C', meter='2/4', tempo='March-like',
    source='Anglo-American traditional (18th c.) — public domain',
    body='Q: 1 1 | 1 2 | 3 1 | 3 2 |\nQ: 1 1 | 1 2 | 3 - | 5, - |\nQ: 1 1 | 1 2 | 3 1 | 3 2 |\nQ: 1 3 | 2 5, | 1 - | 1 - ||',
)
add(
    slug='when-the-saints',
    titles=['When the Saints Go Marching In', '圣者进行曲'],
    key='C', meter='4/4', tempo='Swing / march',
    source='American gospel/spiritual — traditional, public domain',
    body='Q: 1 3 | 4 5 - - | 1 3 | 4 5 - - |\nQ: 1 3 | 4 5 3 1 | 3 2 - - | 3 2 |\nQ: 1 3 | 4 5 - - | 5 5 | 4 3 1 2 | 1 - - - ||',
)
add(
    slug='swing-low',
    titles=['Swing Low Sweet Chariot', '荡得低，甜蜜马车'],
    key='C', meter='4/4', tempo='Andante',
    source='African-American spiritual — traditional, public domain',
    body='Q: 5, 1 3 1 | 2 - - - | 5, 1 2 1 | 6, - - - |\nQ: 5, 1 3 5 | 6 5 3 1 | 2 3 2 1 | 1 - - - ||',
)
add(
    slug='shenandoah',
    titles=['Shenandoah', '谢南多厄'],
    key='C', meter='4/4', tempo='Andante',
    source='American sea shanty / folk — traditional, public domain',
    body='Q: 5, 1 1 2 | 3 - 5 - | 6 5 3 1 | 2 - - - |\nQ: 3 5 6 5 | 3 1 2 3 | 2 1 6, 5, | 1 - - - ||',
)
add(
    slug='home-on-range',
    titles=['Home on the Range', '牧场上的家'],
    key='C', meter='3/4', tempo='Andante',
    source='American folk (1870s melody) — public domain',
    body='Q: 5, 1 2 | 3 - 5 | 6 - 5 | 3 - - |\nQ: 2 3 2 | 1 - 6, | 5, - - | 5, - - |\nQ: 5, 1 2 | 3 - 5 | 6 - 5 | 3 - - |\nQ: 2 1 2 | 1 - - | 1 - - ||',
)
add(
    slug='red-river-valley',
    titles=['Red River Valley', '红河谷'],
    key='C', meter='4/4', tempo='Andante',
    source='North American folk — traditional, public domain',
    body='Q: 5, 1 2 3 | 3 - 2 1 | 6, 1 2 3 | 2 - - - |\nQ: 5, 1 2 3 | 5 - 3 1 | 2 3 2 1 | 1 - - - ||',
)
add(
    slug='aura-lee',
    titles=['Aura Lee', '奥拉丽'],
    key='C', meter='4/4', tempo='Andante',
    source='George R. Poulton (1861) — public domain; later used for Love Me Tender melody',
    body='Q: 1 2 3 1 | 3 1 3 - | 2 1 7, 5, | 1 - - - |\nQ: 1 2 3 1 | 3 1 3 - | 2 3 4 2 | 3 - - - |\nQ: 5 5 4 3 | 4 3 2 - | 3 2 1 7, | 1 - - - ||',
)
add(
    slug='my-bonnie',
    titles=['My Bonnie Lies Over the Ocean', '我的邦尼'],
    key='C', meter='3/4', tempo='Moderato',
    source='Scottish traditional — public domain',
    body='Q: 5, 1 2 | 3 - 5 | 4 - 3 | 2 - - |\nQ: 5, 2 3 | 4 - 6 | 5 - 4 | 3 - - |\nQ: 5, 1 2 | 3 - 5 | 6 - 5 | 4 - 3 |\nQ: 2 3 2 | 1 - - | 1 - - ||',
)
add(
    slug='auld-lang-syne',
    titles=['Auld Lang Syne', '友谊地久天长'],
    key='C', meter='4/4', tempo='Moderato',
    source='Scottish traditional melody (Burns text 1788) — public domain',
    body='Q: 5, 1 1 1 | 3 2 1 2 | 3 1 1 3 | 5 - - - |\nQ: 6 5 3 1 | 3 2 1 2 | 3 1 2 5, | 1 - - - |\nQ: 6 5 3 1 | 3 2 1 2 | 3 1 1 3 | 5 - - - |\nQ: 6 5 3 1 | 3 2 1 2 | 3 1 2 5, | 1 - - - ||',
)
add(
    slug='greensleeves',
    titles=['Greensleeves', '绿袖子'],
    key='Am', meter='6/8', tempo='Andante',
    source='English traditional (16th c.) — public domain',
    body='Q: 6, - 1 | 2 - 3 | 4 3 2 | 7, - 5, |\nQ: 6, - 1 | 2 - 3 | 2 1 7, | 6, - - |\nQ: 6, - 1 | 2 - 3 | 4 3 2 | 7, - 5, |\nQ: 6, - 1 | 2 - 1 | 7, 6, 7, | 6, - - ||',
)
add(
    slug='scarborough',
    titles=['Scarborough Fair', '斯卡布罗集市'],
    key='Em', meter='3/4', tempo='Andante',
    source='English ballad melody — traditional, public domain',
    body='Q: 6, 1 2 | 3 - 5 | 3 - 2 | 1 - - |\nQ: 6, 1 2 | 3 - 2 | 1 7, 6, | 6, - - |\nQ: 3 5 6 | 5 - 3 | 2 - 1 | 2 - - |\nQ: 6, 1 2 | 3 - 2 | 1 7, 6, | 6, - - ||',
)
add(
    slug='amazing-grace',
    titles=['Amazing Grace', '奇异恩典'],
    key='G', meter='3/4', tempo='Andante',
    source='Melody New Britain / traditional American; Newton text 1779 — public domain',
    body='Q: 5, | 1 - 3 /1/ | 3 - 2 | 1 - 6, | 5, - 5, |\nQ: 1 - 3 /1/ | 3 - 2 | 5 - - | 5 - 3 |\nQ: 5 - 3 /5/ | 1 - 5, | 6, - 1 /6,/ | 5, - 5, |\nQ: 1 - 3 /1/ | 3 - 2 | 1 - - ||',
)
add(
    slug='simple-gifts',
    titles=['Simple Gifts', '朴实的礼物'],
    key='C', meter='4/4', tempo='Moderato',
    source='Shaker song (Joseph Brackett, 1848) — public domain',
    body='Q: 5, 1 1 2 | 3 5 3 1 | 2 3 2 5, | 1 - - - |\nQ: 5, 1 1 2 | 3 5 3 1 | 2 3 2 1 | 1 - - - |\nQ: 5 5 3 1 | 2 3 2 5, | 5 5 3 1 | 2 - - - |\nQ: 5, 1 1 2 | 3 5 3 1 | 2 3 2 1 | 1 - - - ||',
)
add(
    slug='water-is-wide',
    titles=['The Water Is Wide', '河水宽又宽'],
    key='C', meter='4/4', tempo='Andante',
    source='British folk (O Waly Waly family) — traditional, public domain',
    body='Q: 1 3 5 5 | 6 - 5 - | 4 3 2 1 | 2 - - - |\nQ: 1 3 5 5 | 6 - 5 - | 4 3 2 3 | 1 - - - ||',
)
add(
    slug='ash-grove',
    titles=['The Ash Grove', '梣树林'],
    key='C', meter='3/4', tempo='Andante',
    source='Welsh traditional Llwyn Onn — public domain',
    body='Q: 1 2 3 | 5 - 3 | 2 1 2 | 3 - - |\nQ: 1 2 3 | 5 - 6 | 5 3 2 | 1 - - |\nQ: 5 6 5 | 3 - 1 | 2 3 2 | 5, - - |\nQ: 1 2 3 | 5 - 3 | 2 1 7, | 1 - - ||',
)
add(
    slug='early-one-morning',
    titles=['Early One Morning', '一天清早'],
    key='C', meter='3/4', tempo='Andante',
    source='English folk song — traditional, public domain',
    body='Q: 5, 1 2 | 3 - 5 | 4 3 2 | 1 - - |\nQ: 5, 2 3 | 4 - 6 | 5 4 3 | 2 - - |\nQ: 5, 1 2 | 3 - 5 | 6 5 4 | 3 2 1 |\nQ: 2 3 2 | 1 - - ||',
)
add(
    slug='barbara-allen',
    titles=['Barbara Allen', '芭芭拉·艾伦'],
    key='C', meter='3/4', tempo='Andante',
    source='English/Scottish ballad — traditional, public domain',
    body='Q: 5, 1 2 | 3 - 5 | 3 2 1 | 6, - - |\nQ: 5, 1 2 | 3 - 2 | 1 7, 6, | 5, - - |\nQ: 3 5 6 | 5 - 3 | 2 1 2 | 3 - - |\nQ: 5, 1 2 | 3 - 2 | 1 - - ||',
)
add(
    slug='long-long-ago',
    titles=['Long Long Ago', '很久很久以前'],
    key='C', meter='4/4', tempo='Andante',
    source='Thomas Haynes Bayly (1833) — public domain',
    body='Q: 1 2 3 1 | 5 3 1 - | 6 5 4 3 | 2 - - - |\nQ: 1 2 3 1 | 5 3 1 - | 2 3 4 2 | 1 - - - ||',
)
add(
    slug='shell-be-coming',
    titles=["She'll Be Coming Round the Mountain", '她将绕山而来'],
    key='C', meter='4/4', tempo='Lively',
    source='American folk (spiritual-derived) — traditional, public domain',
    body='Q: 5 5 5 5 | 5 3 1 3 | 5 - - - | 6 6 6 6 |\nQ: 6 5 4 3 | 2 - - - | 5 5 5 5 | 5 3 1 3 |\nQ: 5 5 6 5 | 4 3 2 1 | 1 - - - ||',
)
add(
    slug='la-cucaracha',
    titles=['La Cucaracha', '蟑螂歌'],
    key='C', meter='2/4', tempo='Lively',
    source='Mexican traditional — public domain',
    body='Q: 5 5 | 5 3 | 6 6 | 6 4 |\nQ: 5 5 | 5 3 | 2 3 | 1 - |\nQ: 5 5 | 5 3 | 6 6 | 6 4 |\nQ: 5 6 | 5 4 | 3 2 | 1 - ||',
)
add(
    slug='cielito-lindo',
    titles=['Cielito Lindo', '美丽的天堂'],
    key='C', meter='3/4', tempo='Moderato',
    source='Mexican song (Quirino Mendoza y Cortés, 1882) — public domain',
    body="Q: 5 5 5 | 3 - 5 | 6 - 5 | 3 - - |\nQ: 2 3 4 | 5 - 3 | 2 - - | 5, - - |\nQ: 5 5 5 | 3 - 5 | 6 - 1' | 5 - - |\nQ: 4 3 2 | 1 - - | 1 - - ||",
)
add(
    slug='santa-lucia',
    titles=['Santa Lucia', '圣露琪亚'],
    key='C', meter='3/4', tempo='Andante',
    source='Neapolitan song (Teodoro Cottrau, 1849) — public domain',
    body='Q: 1 3 5 | 5 - 3 | 4 6 5 | 3 - - |\nQ: 1 3 5 | 5 - 3 | 2 4 3 | 1 - - |\nQ: 5 5 5 | 6 - 5 | 4 4 4 | 5 - 4 |\nQ: 3 5 3 | 2 - 5, | 1 - - | 1 - - ||',
)
add(
    slug='sakura',
    titles=['Sakura Sakura', '樱花'],
    key='C', meter='4/4', tempo='Andante',
    source='Japanese traditional (Edo period) — public domain',
    body="Q: 6 6 7 1' | 7 6 7 - | 6 6 7 1' | 7 6 7 - |\nQ: 6 7 1' 2' | 1' 7 6 7 | 6 5 6 - | 6 - - - ||",
)
add(
    slug='arirang',
    titles=['Arirang', '阿里郎'],
    key='C', meter='3/4', tempo='Andante',
    source='Korean traditional folk song — public domain',
    body="Q: 5 6 5 | 3 - 5 | 6 1' 6 | 5 - - |\nQ: 5 6 5 | 3 - 2 | 1 2 3 | 2 - - |\nQ: 5 6 1' | 6 5 3 | 5 3 2 | 1 - - ||",
)
add(
    slug='sur-le-pont',
    titles=["Sur le Pont d'Avignon", '在亚维农桥上'],
    key='C', meter='2/4', tempo='Lively',
    source='French traditional — public domain',
    body='Q: 1 2 | 3 1 | 2 5, | 1 - |\nQ: 1 2 | 3 1 | 2 5, | 1 - |\nQ: 3 4 | 5 - | 5 4 | 3 2 |\nQ: 1 2 | 3 1 | 2 5, | 1 - ||',
)
add(
    slug='alouette',
    titles=['Alouette', '云雀'],
    key='C', meter='4/4', tempo='Lively',
    source='French-Canadian folk — traditional, public domain',
    body='Q: 5 5 6 5 | 4 3 2 - | 5 5 6 5 | 4 3 2 - |\nQ: 1 1 2 3 | 4 3 2 - | 5 5 4 3 | 2 1 1 - ||',
)
add(
    slug='silent-night',
    titles=['Silent Night', '平安夜'],
    key='C', meter='3/4', tempo='Andante',
    source='Franz Xaver Gruber (1818) — public domain',
    body="Q: 5. 6/ 5 | 3 - - | 5. 6/ 5 | 3 - - |\nQ: 2' - 2' | 7 - - | 1' - 1' | 5 - - |\nQ: 6 - 6 | 1'. 7/ 6 | 5. 6/ 5 | 3 - - |\nQ: 6 - 6 | 1'. 7/ 6 | 5. 6/ 5 | 3 - - |\nQ: 2' - 2' | 4'. 2'/ 7 | 1' - - | 3' - - |\nQ: 1'. 5/ 3 | 5. 4/ 2 | 1 - - ||",
)
add(
    slug='jingle-bells',
    titles=['Jingle Bells', '铃儿响叮当'],
    key='C', meter='4/4', tempo='Allegro',
    source='James Lord Pierpont (1857) — public domain',
    body='Q: 5 3 2 1 | 5 - - 5/ 5/ | 5 3 2 1 | 6 - - - |\nQ: 6 4 3 2 | 7 - - - | 5 5 4 2 | 3 - - - |\nQ: 5 3 2 1 | 5 - - 5/ 5/ | 5 3 2 1 | 6 - - - |\nQ: 6 4 3 2 | 5 5 5 5 | 6 5 4 2 | 1 - - - ||',
)
add(
    slug='deck-the-halls',
    titles=['Deck the Halls', '装饰大厅'],
    key='C', meter='4/4', tempo='Allegro',
    source='Welsh traditional Nos Galan — public domain',
    body='Q: 5 4 3 2 | 1 2 3 1 | 2 3/4/ 3 2 | 1 2 5, 1 |\nQ: 5 4 3 2 | 1 2 3 1 | 2 3/4/ 3 2 | 1 - - - |\nQ: 2 3 2 5, | 2 3 2 5, | 2 3/4/ 5 6 | 5 - - - |\nQ: 5 4 3 2 | 1 2 3 1 | 2 3/4/ 3 2 | 1 - - - ||',
)
add(
    slug='joy-to-world',
    titles=['Joy to the World', '普世欢腾'],
    key='C', meter='4/4', tempo='Allegro',
    source='Melody after Handel / Lowell Mason (19th c.) — public domain',
    body="Q: 1' 7 6 5 | 4 3 2 1 | 5 6 6 7 | 7 1' - - |\nQ: 3 3 3 3 4/5/ | 6 - 4 4 4 4 5/6/ | 7 - |\nQ: 5 1' 7 6 5 | 5 4 3 | 2 1 - - ||",
)
add(
    slug='ode-to-joy',
    titles=['Ode to Joy', '欢乐颂'],
    key='C', meter='4/4', tempo='Allegro',
    source='Ludwig van Beethoven, Symphony No.9 theme (1824) — public domain',
    body='Q: 3 3 4 5 | 5 4 3 2 | 1 1 2 3 | 3. 2/ 2 - |\nQ: 3 3 4 5 | 5 4 3 2 | 1 1 2 3 | 2. 1/ 1 - |\nQ: 2 2 3 1 | 2 3/4/ 3 1 | 2 3/4/ 3 2 | 1 2 5, - |\nQ: 3 3 4 5 | 5 4 3 2 | 1 1 2 3 | 2. 1/ 1 - ||',
)
add(
    slug='minuet-in-g',
    titles=['Minuet in G', 'G大调小步舞曲'],
    key='G', meter='3/4', tempo='Moderato',
    source='Christian Petzold (attr. Bach Anh.114) — public domain',
    body='Q: 5 4# 5 | 6 5 4 | 3 2 3 | 4 3 2 |\nQ: 1 2 3 | 4 5 6 | 5 - - | 5 - - |\nQ: 5 4# 5 | 6 5 4 | 3 2 3 | 4 3 2 |\nQ: 1 7, 1 | 2 5, 7, | 1 - - | 1 - - ||',
)
add(
    slug='fur-elise',
    titles=['Für Elise (theme)', '致爱丽丝'],
    key='Am', meter='3/8', tempo='Poco moto',
    source='Ludwig van Beethoven (c.1810) — public domain',
    body='Q: 5 4# | 5 4# 5 | 2 4 3 | 1 - - |\nQ: 0 1, 3, | 6, 1 3 | 2 - - | 0 5,, 7,, |\nQ: 5, 7, 2 | 1 - - | 0 1, 3, | 6, 1 3 |\nQ: 2 - - | 0 5,, 7,, | 5, 7, 2 | 1 - - ||',
)
add(
    slug='canon-in-d',
    titles=['Canon in D (theme)', 'D大调卡农'],
    key='D', meter='4/4', tempo='Andante',
    source='Johann Pachelbel (c.1680) — public domain',
    body="Q: 1 - 5, - | 6, - 3, - | 4, - 1, - | 4, - 5, - |\nQ: 1 3 5 1' | 5, 1 3 5 | 6, 1 3 6 | 3, 5, 1 3 |\nQ: 4, 6, 1 4 | 1, 4, 6, 1 | 4, 6, 1 4 | 5, 7, 2 5 ||",
)
add(
    slug='brahms-lullaby',
    titles=['Brahms Lullaby', '勃拉姆斯摇篮曲'],
    key='C', meter='3/4', tempo='Andante',
    source='Johannes Brahms, Wiegenlied Op.49 No.4 (1868) — public domain',
    body='Q: 5, 5, | 6, - 5, | 5, - 3 | 1 - - |\nQ: 5, 5, | 6, - 5, | 5, - 3 | 1 - - |\nQ: 5 3 | 1 - 5, | 4 2 | 7, - - |\nQ: 3 1 | 6, - 5, | 1 - - ||',
)
add(
    slug='eine-kleine',
    titles=['Eine kleine Nachtmusik (theme)', '小夜曲主题'],
    key='G', meter='4/4', tempo='Allegro',
    source='W.A. Mozart, K.525 (1787) — public domain',
    body="Q: 5 0 0 2 | 5 0 0 2 | 5 2 5 7 | 1' - - - |\nQ: 6 0 0 1' | 6 0 0 1' | 6 4# 6 1' | 7 - - - ||",
)
add(
    slug='turkish-march',
    titles=['Turkish March (Mozart)', '土耳其进行曲'],
    key='Am', meter='2/4', tempo='Allegretto',
    source='W.A. Mozart, Rondo Alla Turca K.331 — public domain',
    body="Q: 1/ 2/ | 3/ 2/ 1/ 7,/ | 6,/ 7,/ 1/ 6,/ | 5,/ 6,/ 7,/ 5,/ |\nQ: 1/ 2/ 3/ 1/ | 2/ 3/ 4/ 2/ | 3/ 4/ 5/ 3/ | 1' - |\nQ: 5/ 4/ 3/ 2/ | 1 - ||",
)
add(
    slug='blue-danube',
    titles=['Blue Danube (theme)', '蓝色多瑙河'],
    key='C', meter='3/4', tempo='Tempo di valse',
    source='Johann Strauss II (1866) — public domain',
    body="Q: 0 0 5,/ | 5, - 1 | 1 - 3 | 3 - 5 |\nQ: 5 - 1' | 1' - 7 | 6 - - | 0 0 5,/ |\nQ: 5, - 1 | 1 - 3 | 3 - 5 | 5 - 6 |\nQ: 5 - - | 0 0 5,/ | 5, - 2 | 2 - 4# |\nQ: 4# - 6 | 6 - 2' | 2' - 1' | 7 - - ||",
)
add(
    slug='william-tell',
    titles=['William Tell Overture (theme)', '威廉·退尔序曲'],
    key='C', meter='2/4', tempo='Allegro vivace',
    source='Gioachino Rossini (1829) — public domain',
    body='Q: 1 1 | 1 5,/ 5,/ | 1 1 | 1 5,/ 5,/ |\nQ: 1 3 | 5 3 | 1 1 | 1 - |\nQ: 5 5 | 5 5 | 6 5 4 3 | 2 - |\nQ: 4 4 | 4 4 | 5 4 3 2 | 1 - ||',
)
add(
    slug='spring-vivaldi',
    titles=['Spring (Vivaldi theme)', '春（维瓦尔第）'],
    key='C', meter='4/4', tempo='Allegro',
    source='Antonio Vivaldi, Four Seasons Op.8 No.1 (1725) — public domain',
    body="Q: 1 3 5 1' | 7 5 7 1' | 5 0 0 0 | 3 5 1' 3' |\nQ: 2' 1' 7 5 | 1' - - - ||",
)
add(
    slug='morning-mood',
    titles=['Morning Mood', '晨景'],
    key='C', meter='6/8', tempo='Andante',
    source='Edvard Grieg, Peer Gynt (1875) — Grieg d.1907; public domain',
    body='Q: 5, - 6, | 1 - 2 | 3 - 2 | 1 - 6, |\nQ: 5, - 6, | 1 - 2 | 3 - - | 3 - - |\nQ: 5 - 4 | 3 - 2 | 1 - 6, | 5, - - ||',
)
add(
    slug='hall-mountain-king',
    titles=['In the Hall of the Mountain King', '山魔王的宫殿'],
    key='Am', meter='4/4', tempo='Alla marcia e molto marcato',
    source='Edvard Grieg, Peer Gynt — public domain',
    body='Q: 6, 7, 1 7, | 6, 7, 1 7, | 6, 7, 1 2 | 3 - - - |\nQ: 3 4# 5 4# | 3 4# 5 4# | 3 4# 5 6 | 7 - - - ||',
)
add(
    slug='swan-lake',
    titles=['Swan Lake (theme)', '天鹅湖主题'],
    key='Bm', meter='4/4', tempo='Moderato',
    source='Pyotr Tchaikovsky (1876) — public domain',
    body="Q: 5 1' 7 6 | 5 - 4# - | 5 6 5 4# | 3 - - - |\nQ: 5 1' 7 6 | 5 - 3 - | 4# 5 4# 3 | 2 - - - ||",
)
add(
    slug='nutcracker-march',
    titles=['Nutcracker March', '胡桃夹子进行曲'],
    key='C', meter='4/4', tempo='Tempo di marcia vivace',
    source='Pyotr Tchaikovsky (1892) — public domain',
    body='Q: 5 0 5 0 | 5 0 5 5/6/ | 5 4 3 2 | 1 0 0 0 |\nQ: 5 0 5 0 | 5 0 5 5/6/ | 5 4 3 2 | 1 0 0 0 ||',
)
add(
    slug='sugar-plum',
    titles=['Dance of the Sugar Plum Fairy', '糖梅仙子之舞'],
    key='Em', meter='2/4', tempo='Andante con moto',
    source='Pyotr Tchaikovsky, Nutcracker — public domain',
    body="Q: 0 3/ | 5/ 0/ 0/ 6/ | 5/ 0/ 0/ 3/ | 5/ 0/ 0/ 6/ | 5/ 0/ 0/ 2'/ |\nQ: 1'/ 0/ 0/ 7/ | 6/ 0/ 0/ 5/ | 4#/ 0/ 0/ 5/ | 3 - ||",
)
add(
    slug='carmen-habanera',
    titles=['Carmen Habanera (theme)', '卡门·哈巴涅拉'],
    key='Dm', meter='2/4', tempo='Allegretto quasi Andantino',
    source='Georges Bizet (1875) — public domain',
    body='Q: 1 7,/ | 1 2 3 4 | 5 - 4 3 | 4 3 2 1 |\nQ: 7, - 1 7, | 1 - - - ||',
)
add(
    slug='toreador',
    titles=['Toreador Song (theme)', '斗牛士之歌'],
    key='C', meter='4/4', tempo='Allegro',
    source='Georges Bizet, Carmen — public domain',
    body='Q: 5 5 5 5 | 5 6 5 4 | 3 4 5 6 | 5 - - - |\nQ: 4 4 4 4 | 4 5 4 3 | 2 3 4 5 | 3 - - - ||',
)
add(
    slug='la-donna',
    titles=['La donna è mobile', '女人善变'],
    key='C', meter='3/8', tempo='Allegretto',
    source='Giuseppe Verdi, Rigoletto (1851) — public domain',
    body="Q: 5 5 5 | 5 6 5 | 4 4 4 | 4 5 4 |\nQ: 3 3 3 | 3 4 3 | 2 - - | 5 - - |\nQ: 1' 1' 1' | 1' 7 6 | 5 5 5 | 5 4 3 |\nQ: 2 2 2 | 2 3 2 | 1 - - ||",
)
add(
    slug='bridal-chorus',
    titles=['Bridal Chorus', '婚礼合唱'],
    key='C', meter='4/4', tempo='Moderato',
    source='Richard Wagner, Lohengrin (1850) — public domain',
    body='Q: 1 - 1 - | 1 2 3 - | 2 1 2 3 | 1 - - - |\nQ: 5 - 5 - | 5 4 3 - | 4 3 4 5 | 3 - - - ||',
)
add(
    slug='wedding-march',
    titles=['Wedding March', '婚礼进行曲'],
    key='C', meter='4/4', tempo='Allegro vivace',
    source="Felix Mendelssohn, Midsummer Night's Dream (1842) — public domain",
    body="Q: 1 0 1 0 | 1 3 5 1' | 7 0 6 0 | 5 - - - |\nQ: 5 0 5 0 | 5 4 3 2 | 1 0 2 0 | 3 - - - ||",
)
add(
    slug='ave-maria-schubert',
    titles=['Ave Maria (Schubert theme)', '圣母颂'],
    key='C', meter='4/4', tempo='Andante',
    source='Franz Schubert, D.839 (1825) — public domain',
    body="Q: 5 - 5 - | 6 - 5 - | 5 - 4 - | 3 - - - |\nQ: 2 - 2 - | 3 - 2 - | 2 - 1 - | 5, - - - |\nQ: 5 - 5 - | 1' - 7 - | 6 - 5 - | 4 - 3 - |\nQ: 2 - 3 - | 1 - - - ||",
)
add(
    slug='moonlight-sonata',
    titles=['Moonlight Sonata (theme)', '月光奏鸣曲'],
    key='Cm', meter='4/4', tempo='Adagio sostenuto',
    source='Ludwig van Beethoven, Op.27 No.2 (1801) — public domain',
    body="Q: 1/ 3/ 5/ 1'/ 3'/ 5'/ 1'/ 3'/ | 1/ 3/ 5/ 1'/ 3'/ 5'/ 1'/ 3'/ |\nQ: 6,/ 1/ 3/ 6/ 1'/ 3'/ 6/ 1'/ | 5,/ 1/ 3/ 5/ 1'/ 3'/ 5/ 1'/ ||",
)
add(
    slug='haydn-surprise',
    titles=['Surprise Symphony (theme)', '惊愕交响曲主题'],
    key='C', meter='2/4', tempo='Andante',
    source='Joseph Haydn, Symphony No.94 (1791) — public domain',
    body='Q: 1 1 | 1 3 | 5 5 | 5 - |\nQ: 4 4 | 4 2 | 7, 7, | 7, - |\nQ: 1 1 | 1 3 | 5 5 | 5 - |\nQ: 6 5 | 4 3 | 2 1 | 1 - ||',
)
add(
    slug='chopin-prelude7',
    titles=['Chopin Prelude Op.28 No.7', '肖邦前奏曲'],
    key='C', meter='3/4', tempo='Andantino',
    source='Frédéric Chopin (1839) — public domain',
    body="Q: 5 - 3 | 6 - 5 | 4 - 2 | 5 - 4 |\nQ: 3 - 1 | 4 - 3 | 2 - - | 5, - - |\nQ: 5 - 3 | 6 - 5 | 1' - 6 | 5 - 3 |\nQ: 4 3 2 | 1 - - ||",
)
add(
    slug='radetzky',
    titles=['Radetzky March (theme)', '拉德茨基进行曲'],
    key='C', meter='2/4', tempo='Tempo di marcia',
    source='Johann Strauss I (1848) — public domain',
    body='Q: 5 5 | 5 3/4/ | 5 5 | 5 3/4/ |\nQ: 5 6 | 5 4 | 3 2 | 1 - |\nQ: 2 2 | 2 1/2/ | 3 3 | 3 2/3/ |\nQ: 4 5 | 4 3 | 2 7, | 1 - ||',
)
add(
    slug='funiculi',
    titles=['Funiculì Funiculà', '缆车歌曲'],
    key='C', meter='6/8', tempo='Allegro',
    source='Luigi Denza (1880) — public domain',
    body="Q: 5 5 5 | 5 6 5 | 4 4 4 | 4 5 4 |\nQ: 3 3 3 | 3 4 3 | 2 - - | 5 - - |\nQ: 1' 1' 1' | 1' 2' 1' | 7 7 7 | 7 1' 7 |\nQ: 6 6 6 | 5 4 3 | 2 - - | 1 - - ||",
)
add(
    slug='o-sole-mio',
    titles=['O Sole Mio', '我的太阳'],
    key='C', meter='2/4', tempo='Andante',
    source='Eduardo di Capua (1898) — public domain in US/China practice',
    body="Q: 5 5 | 1' 7 | 6 5 | 4 3 |\nQ: 2 3 | 4 5 | 3 - | 5 5 |\nQ: 1' 7 | 6 5 | 4 3 | 2 1 |\nQ: 7, 1 | 2 3 | 1 - ||",
)
add(
    slug='happy-birthday',
    titles=['Happy Birthday', '祝你生日快乐'],
    key='C', meter='3/4', tempo='Moderato',
    source='Mildred/Patty Hill melody (1893); PD in US since 2016',
    body='Q: 5, 5, | 6, - 5, | 1 - 7, | 5, - 5, |\nQ: 6, - 5, | 2 - 1 | 5, - 5, | 5 - 3 |\nQ: 1 - 7, | 6, - 4 | 3 - 1 | 2 - 1 ||',
)
add(
    slug='danny-boy',
    titles=['Danny Boy (Londonderry Air)', '丹尼男孩'],
    key='C', meter='4/4', tempo='Andante',
    source='Irish traditional Londonderry Air — public domain',
    body='Q: 5, 1 2 3 | 5 - 3 - | 2 1 2 3 | 1 6, 5, - |\nQ: 5, 1 2 3 | 5 - 6 - | 5 3 2 3 | 1 - - - |\nQ: 5 5 6 5 | 3 - 1 - | 2 3 5 6 | 5 - - - |\nQ: 5, 1 2 3 | 5 - 3 1 | 2 3 2 1 | 1 - - - ||',
)

assert len(SONGS) == 100, len(SONGS)
assert len({s["slug"] for s in SONGS}) == 100
