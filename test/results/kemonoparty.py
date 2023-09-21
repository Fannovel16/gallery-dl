# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import kemonoparty


__tests__ = (
{
    "#url"     : "https://kemono.party/fanbox/user/6993449",
    "#category": ("", "kemonoparty", "fanbox"),
    "#class"   : kemonoparty.KemonopartyUserExtractor,
    "#range"   : "1-25",
    "#count"   : 25,
},

{
    "#url"     : "https://kemono.party/patreon/user/881792?o=150",
    "#comment" : "'max-posts' option, 'o' query parameter (#1674)",
    "#category": ("", "kemonoparty", "patreon"),
    "#class"   : kemonoparty.KemonopartyUserExtractor,
    "#options" : {"max-posts": 25},
    "#count"   : "< 100",
},

{
    "#url"     : "https://kemono.su/subscribestar/user/alcorart",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyUserExtractor,
},

{
    "#url"     : "https://kemono.party/subscribestar/user/alcorart",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyUserExtractor,
},

{
    "#url"     : "https://kemono.party/fanbox/user/6993449/post/506575",
    "#category": ("", "kemonoparty", "fanbox"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#pattern"     : r"https://kemono.party/data/21/0f/210f35388e28bbcf756db18dd516e2d82ce75[0-9a-f]+\.jpg",
    "#sha1_content": "900949cefc97ab8dc1979cc3664785aac5ba70dd",

    "added"      : "Wed, 06 May 2020 20:28:02 GMT",
    "content"    : str,
    "count"      : 1,
    "date"       : "dt:2019-08-11 02:09:04",
    "edited"     : None,
    "embed"      : dict,
    "extension"  : "jpeg",
    "filename"   : "P058kDFYus7DbqAkGlfWTlOr",
    "hash"       : "210f35388e28bbcf756db18dd516e2d82ce758e0d32881eeee76d43e1716d382",
    "id"         : "506575",
    "num"        : 1,
    "published"  : "Sun, 11 Aug 2019 02:09:04 GMT",
    "service"    : "fanbox",
    "shared_file": False,
    "subcategory": "fanbox",
    "title"      : "c96取り置き",
    "type"       : "file",
    "user"       : "6993449",
},

{
    "#url"     : "https://kemono.party/fanbox/user/7356311/post/802343",
    "#comment" : "inline image (#1286)",
    "#category": ("", "kemonoparty", "fanbox"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#pattern" : r"https://kemono\.party/data/47/b5/47b5c014ecdcfabdf2c85eec53f1133a76336997ae8596f332e97d956a460ad2\.jpg",

    "hash": "47b5c014ecdcfabdf2c85eec53f1133a76336997ae8596f332e97d956a460ad2",
},

{
    "#url"     : "https://kemono.party/gumroad/user/trylsc/post/IURjT",
    "#comment" : "kemono.party -> data.kemono.party",
    "#category": ("", "kemonoparty", "gumroad"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#pattern" : r"https://kemono\.party/data/(a4/7b/a47bfe938d8c1682eef06e885927484cd8df1b.+\.jpg|c6/04/c6048f5067fd9dbfa7a8be565ac194efdfb6e4.+\.zip)",
},

{
    "#url"     : "https://kemono.party/gumroad/user/3252870377455/post/aJnAH",
    "#comment" : "username (#1548, #1652)",
    "#category": ("", "kemonoparty", "gumroad"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#options" : {"metadata": True},

    "username": "Kudalyn's Creations",
},

{
    "#url"     : "https://kemono.party/patreon/user/4158582/post/32099982",
    "#comment" : "allow duplicates (#2440)",
    "#category": ("", "kemonoparty", "patreon"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#count"   : 2,
},

{
    "#url"     : "https://kemono.party/patreon/user/4158582/post/32099982",
    "#comment" : "allow duplicates (#2440)",
    "#category": ("", "kemonoparty", "patreon"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#options" : {"duplicates": True},
    "#count"   : 3,
},

{
    "#url"     : "https://kemono.party/patreon/user/34134344/post/38129255",
    "#comment" : "DMs (#2008)",
    "#category": ("", "kemonoparty", "patreon"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#options" : {"dms": True},

    "dms": [{
    "body"     : r"re:Hi! Thank you very much for supporting the work I did in May. Here's your reward pack! I hope you find something you enjoy in it. :\)\n\nhttps://www.mediafire.com/file/\w+/Set13_tier_2.zip/file",
    "date"     : "2021-07-31 02:47:51.327865",
}],
},

{
    "#url"     : "https://kemono.party/patreon/user/19623797/post/29035449",
    "#comment" : "invalid file (#3510)",
    "#category": ("", "kemonoparty", "patreon"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
    "#pattern"     : r"907ba78b4545338d3539683e63ecb51cf51c10adc9dabd86e92bd52339f298b9\.txt",
    "#sha1_content": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
},

{
    "#url"     : "https://kemono.su/subscribestar/user/alcorart/post/184330",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
},

{
    "#url"     : "https://kemono.party/subscribestar/user/alcorart/post/184330",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
},

{
    "#url"     : "https://www.kemono.party/subscribestar/user/alcorart/post/184330",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
},

{
    "#url"     : "https://beta.kemono.party/subscribestar/user/alcorart/post/184330",
    "#category": ("", "kemonoparty", "subscribestar"),
    "#class"   : kemonoparty.KemonopartyPostExtractor,
},

{
    "#url"     : "https://kemono.party/discord/server/488668827274444803#finish-work",
    "#category": ("", "kemonoparty", "discord"),
    "#class"   : kemonoparty.KemonopartyDiscordExtractor,
    "#count"   : 4,

    "channel_name": "finish-work",
},

{
    "#url"     : "https://kemono.su/discord/server/256559665620451329/channel/462437519519383555#",
    "#category": ("", "kemonoparty", "discord"),
    "#class"   : kemonoparty.KemonopartyDiscordExtractor,
    "#pattern" : r"https://kemono\.su/data/(e3/77/e377e3525164559484ace2e64425b0cec1db08.*\.png|51/45/51453640a5e0a4d23fbf57fb85390f9c5ec154.*\.gif)",
    "#count"   : ">= 2",

    "hash": r"re:e377e3525164559484ace2e64425b0cec1db08|51453640a5e0a4d23fbf57fb85390f9c5ec154",
},

{
    "#url"     : "https://kemono.party/discord/server/315262215055736843/channel/315262215055736843#general",
    "#comment" : "'inline' files",
    "#category": ("", "kemonoparty", "discord"),
    "#class"   : kemonoparty.KemonopartyDiscordExtractor,
    "#options" : {"image-filter": "type == 'inline'"},
    "#pattern" : r"https://cdn\.discordapp\.com/attachments/\d+/\d+/.+$",
    "#range"   : "1-5",

    "hash": "",
},

{
    "#url"     : "https://kemono.party/discord/server/488668827274444803",
    "#category": ("", "kemonoparty", "discord-server"),
    "#class"   : kemonoparty.KemonopartyDiscordServerExtractor,
    "#pattern" : kemonoparty.KemonopartyDiscordExtractor.pattern,
    "#count"   : 13,
},

{
    "#url"     : "https://kemono.su/discord/server/488668827274444803",
    "#category": ("", "kemonoparty", "discord-server"),
    "#class"   : kemonoparty.KemonopartyDiscordServerExtractor,
    "#pattern" : kemonoparty.KemonopartyDiscordExtractor.pattern,
    "#count"   : 13,
},

{
    "#url"     : "https://kemono.party/favorites",
    "#category": ("", "kemonoparty", "favorite"),
    "#class"   : kemonoparty.KemonopartyFavoriteExtractor,
    "#pattern" : kemonoparty.KemonopartyUserExtractor.pattern,
    "#count"   : 3,
    "#sha1_url": "f4b5b796979bcba824af84206578c79101c7f0e1",
},

{
    "#url"     : "https://kemono.party/favorites?type=post",
    "#category": ("", "kemonoparty", "favorite"),
    "#class"   : kemonoparty.KemonopartyFavoriteExtractor,
    "#pattern" : kemonoparty.KemonopartyPostExtractor.pattern,
    "#count"   : 3,
    "#sha1_url": "ecfccf5f0d50b8d14caa7bbdcf071de5c1e5b90f",
},

{
    "#url"     : "https://kemono.su/favorites?type=post",
    "#category": ("", "kemonoparty", "favorite"),
    "#class"   : kemonoparty.KemonopartyFavoriteExtractor,
    "#pattern" : kemonoparty.KemonopartyPostExtractor.pattern,
    "#count"   : 3,
    "#sha1_url": "4be8e84cb384a907a8e7997baaf6287b451783b5",
},

)
