# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome again in {PROJECT_NAME}
✣️ {PROJECT_NAME} can Play Songs in Group Voice Chat In Easy way.
✣️ Assistant Music » @{ASSISTANT_NAME}\n\nClick Next for instructions**
""",

f"""
**Settings**
1. Make bot as admin
2. Start voice chat / VCG
3. Type `/userbotjoin` and try /play <song name>
× If Assistant Bot joins enjoy music,
× If Assistant Bot doesn't join Please Add @{ASSISTANT_NAME} to your group and try again
**» Commands for members in the group can also :**
 × /req <song title> : To Play the song you requested via youtube
 × /ytreq <link yt> : To Play the song you requested via the youtube link
 × /dplay : To Play the song you requested via deezer
 × /splay : To Play the song you requested via jio saavn
 × /playlist : To Display the current Song playlist
 × /current : Shows the current song currently playing
 × /song <song title> : To Download songs on YouTube
 × /video <song title> : To Download Videos on YouTube with details
 × /vsong <song title> : To Download Videos on YouTube with details
 × /deezer <song title> : To Download songs from deezer
 × /saavn <song title> : To Download songs from the saavn website
 × /search <song title> : To Search Videos on YouTube with details
**» Commands Only For Admin and Sudo:**
× /skip : To Skip playback of the song to the next Song
× /pause : To Pause Song playback
× /resume : To resume playback of the paused song
× /end : To Stop Song playback pemutaran
× /userbotjoin - To Invite assistant to your chat
× /admincache - To Refresh admin list
"""
      ]
