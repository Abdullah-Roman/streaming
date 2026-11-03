import urllib.request
import re
from datetime import datetime, timezone

# --- Configuration ---
M3U_FILE = "live.m3u"

# External Playlist URLs
SPORTS_URL = "https://gist.githubusercontent.com/albatr0ssss/3cff7a26be49b1d352c15f615067e7cd/raw/tapmad_bd.m3u"
SONYLIV_URL = "https://raw.githubusercontent.com/srhady/SonyLiv/refs/heads/main/sonyliv_playlist.m3u"
HINDI_MOVIES_URL = "https://raw.githubusercontent.com/streambd/streaming/refs/heads/main/hindimovies.m3u"
BENGALI_MOVIES_URL = "https://raw.githubusercontent.com/streambd/streaming/refs/heads/main/banglamovies.m3u"
ENGLISH_MOVIES_URL = "https://raw.githubusercontent.com/streambd/streaming/refs/heads/main/englishmovies.m3u"

# --- Template ---
PLAYLIST_TEMPLATE = """#EXTM3U
# ==========================================
# 🏆 Sports LIVE
# ==========================================

{DYNAMIC_CHANNELS}

{DYNAMIC_SONYLIV}

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://iili.io/CjUgT6G.th.jpg", T Sports
https://tvsen5.aynaott.com/TnMn5kZz8aLmjklkk/tracks-v1a1/mono.ts.m3u8
http://103.114.11.37:8081/T-Sports-FHD/index.m3u8?token=sboxcast

#EXTINF:-1 tvg-name="Willow TV" tvg-logo="https://i.ibb.co.com/9HNtwDKJ/images-2.jpg" group-title="Sports",Willow TV
https://tvsen7.aynaott.com/rEBp38Ax/tracks-v1a1/mono.ts.m3u8
https://warm-caverns-48629-92fab798385f.herokuapp.com/https://d36r8jifhgsk5j.cloudfront.net/Willow_TV540p.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.ibb.co.com/Z6Y14TZ9/images-3.jpg",PTV Sports 
https://s1.itcnbd.live/PTV-Sports/tracks-v1a1/mono.m3u8?nocache=1785582200018

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://dtil.tmsimg.com/assets/s143807_ld_h15_ac.png?lock=720x540",Star Sports 2 
https://tvsen7.aynaott.com/ssport2hd/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.ibb.co.com/LzX4ZGTH/images-1.jpg", Star Sports 1
http://103.114.11.37:8081/Star-sports-1/index.m3u8?token=sboxcast

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.postimg.cc/pXx765TQ/20240823_024350.png?ref=skym3u.dev",Euro Sports HD
https://drk6xq0vhn.gpcdn.net/live/euro_sports_hd_abr/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.ibb.co.com/TFkR87R/images-1.png", Ten Cricket
https://drk6xq0vhn.gpcdn.net/live/ten_cricket_hd_abr/live/ten_cricket_hd_720/chunks.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.ibb.co.com/2Yq7tQ3J/images-2.png", Bein Sports
https://tvsen6.aynaott.com/beinsports/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://i.ibb.co.com/ym83QZvd/download.png", Bein Sports Extra
https://bein-esp-xumo.amagi.tv/playlistR720P.m3u8

#EXTINF:-1 tvg-id="019efa45-e8e5-7353-a606-b361cf5f42ce" tvg-name="Cricket Gold" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-09/images_dde39b3fb713d4946a32e2c8ad5db00a_playmist_cricket_gold_400x400.jpg" group-title="Cricket, Sports",Cricket Gold
https://tvsen6.aynaott.com/M2W2UR49dmeKbZnmdRzN/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_SONY_SPORTS_TEN_1/images/LOGO_HD/image.png", Sony Sports 1
https://stream.ottplus.live/live/ten_1_hd_abr/live/ten_1_hd_720/chunks.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_SONY_SPORTS_TEN_2/images/LOGO_HD/image.png", Sony Sports 2
https://stream.ottplus.live/live/ten_2_hd_abr/live/ten_2_hd_720/chunks.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_SONY_SPORTS_TEN_5/images/LOGO_HD/image.png", Sony Sports 5
https://stream.ottplus.live/live/ten_5_hd_abr/live/ten_5_hd_720/chunks.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-logo="https://abusaeeidx.github.io/Tv-Channel-Logo/CricHD/runded/12-by-xfireflix.png" tvg-name="A Sports",A Sports
https://playztv-apps.pages.dev/a-sports/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-id="DDSports.in@HD" tvg-logo="https://dtil.tmsimg.com/assets/s158255_ld_h15_aa.png?lock=720x540",DD Sports (720p)
https://mumbai-edge.smartplaytv.in/DDSportsHD/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-id="FightBox.nl@HD" tvg-logo="https://i.imgur.com/mRsnztA.png" ,FightBox HD
https://nosignal1.antenaplay.ro/hls/fightbox-hd/index.m3u8

#EXTINF:-1 group-title="Sports Live" tvg-id="FightNetwork.ca" tvg-name="Fight Network" tvg-logo="https://i.imgur.com/vlKPZHR.png" tvg-chno="552",Fight Network
https://amg00966-amg00966c10-amgplt0201.playout.now3.amagi.tv/ts-eu-w1-n2/playlist/amg00966-amg00966c10-amgplt0201/playlist.m3u8

# ==========================================
# 📺 BD TV
# ==========================================

# --- Bangla Vision (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CjUVOHG.th.jpg", Bangla Vision
https://tvsen5.aynaott.com/banglavision/tracks-v1a1/mono.ts.m3u8

#EXTINF:-1 tvg-id="019de785-3978-7f99-9708-4a0d34e53511" tvg-name="Boishakhi TV" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-02/images_8a69251df11b66c4e85e7a2fe6d89286_playmist_boishakhi_tv_400x400.jpg" group-title="Bangla",Boishakhi TV
https://tvsen6.aynaott.com/1d3uG9VCgrR9DRtWZM57/index.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.postimg.cc/Zqgx8hm1/20260430-184013.png?ref=skym3u.dev", Channel 1
https://drk6xq0vhn.gpcdn.net/live/channel_1_hd_abr/index.m3u8

#EXTINF:-1 tvg-id="NagorikTV.bd" tvg-logo="https://i.postimg.cc/Z54fVGww/20240822_230947.png" tvg-chno="90" group-title="Bangladesh",Nagorik TV 
https://box.bbaria.net/Nagorik_TV/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-id="local.264717e2eb106e90" tvg-name="SRK" tvg-logo="https://asset.bioscopelive.com/uploads/images/2025/08/11/thumbnails_58ebcef1efcc65837557de15952d2643_goplay_srk_tv_landscape.jpg" tvg-chno="108" group-title="Bangladesh",SRK
https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8

#-------ATN NEWS----
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CeMZ8fs.th.png",ATN News
https://playztv-apps.pages.dev/atn-bangla/index.m3u8


# --- Somoy TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CjUEHuV.th.jpg", Somoy TV
https://tvsen6.aynaott.com/4XcqdovJzbbC9WdJA9gk/tracks-v1a1/mono.ts.m3u8

# --- News 24 (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CjUX1CN.th.png", News 24
https://tvsen6.aynaott.com/cdgr3tw6WoG7JyRnLbi0/index.m3u8?e=1784102534&u=ee5437a7-c16b-4700-b317-a41b77d5cba9&token=ff40b53535a0e90b724ac25ff41c590c

# --- DBC News (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CjUTzjj.th.jpg", DBC News
https://tvsen6.aynaott.com/pF66Tkz0qFwP2aMMqHyt/index.m3u8?e=1784102535&u=ee5437a7-c16b-4700-b317-a41b77d5cba9&token=d1848b7fd84cef719a89b61f0f5704ee

# --- NTV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/C5XhmFV.png", NTV
https://playztv-apps.pages.dev/ntv/index.m3u8

#EXTINF:-1 group-title="BD TV" tvg-name="Deepto" tvg-logo="https://i.postimg.cc/bYSFJHG9/20240822-230812.png?ref=skym3u.dev?ref=skym3u.dev",Deepto
https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8

#EXTINF:-1  group-title="BD TV" tvg-logo="https://i.ibb.co.com/TxDnNNC9/1000109104.png",Ayna TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/ayna.stream/tracks-v1a1/mono.m3u8

#EXTINF:-1 tvg-logo="https://iili.io/CeM6ooG.th.jpg" group-title="BD TV",RTV 
https://m.mxonlive.xyz/proxy-5441/auto_proxy.php?url=http://tvsen5.aynascope.net/RtvHD/index.m3u8

# ---Channel I (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-01/images_99c9ba1977777337bdc037f79ed921ea_playmist_channel_i_500x296.jpg", Channel I
https://playztv-apps.pages.dev/channel-i/index.m3u8

# --- Ekhon TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CjpNgix.th.jpg", Ekhon TV
https://master-proxy.wispy-boat-fc77.workers.dev/?url=https://ekusheyserver.com/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8

# --- Desh TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CwNc0IS.th.jpg", Desh TV
https://tvsen6.aynaott.com/ryFkXfd1a4CQ7mMdc820/index.m3u8?e=1784102570&u=ee5437a7-c16b-4700-b317-a41b77d5cba9&token=78b23c868a34420397be9c985d04db9b

#EXTINF:-1 group-title="BD TV" tvg-logo="https://upload.wikimedia.org/wikipedia/en/d/d7/Duronto_TV_Logo.png" ,DURONTO TV
http://103.114.11.37:8081/Duronto/tracks-v1a1/mono.m3u8?token=sbox

#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.ibb.co/jhPSkLR/Picsart-23-06-07-10-30-19-289.png",SA TV
https://tvsen6.aynaott.com/rELXiuUXqbgzPb06Npom/index.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.ibb.co/LnTmZLD/Picsart-23-06-07-10-15-30-064.png",Bangla Tv
https://tvsen6.aynaott.com/39ee93nUbCCmm5LsyD4t/index.m3u8

# --- Deshe Bideshe TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/CwNl6Pe.th.jpg", Deshe Bideshe
https://dbcanada.sonarbanglatv.com/deshebideshe/dbtv/index.m3u8

# --- Independent TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/C76RVR9.png", Independent TV
https://drk6xq0vhn.gpcdn.net/live/independent_tv_abr/live/independent_tv_720/chunks.m3u8

#EXTINF:-1 group-title="BD TV" tvg-id="019de785-397a-7df0-b523-b00c861be256" tvg-name="Mohona TV" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-02/images_1c2c83a36e990c46964ce6ef25528d84_playmist_mohona_tv400x400.jpg",Mohona TV
https://tvsen6.aynaott.com/AkyX5dunzju4cpo26dr7/index.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://s4.gifyu.com/images/image534fa27d7683f33d.png",Ekushey TV
https://m.mxonlive.xyz/proxy-5441/auto_proxy.php?url=http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8

# --- Ekattor TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/C5X9K1j.md.png", Ekattor TV
https://playztv-apps.pages.dev/ekattor-tv/index.m3u8

# --- Jamuna TV (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/C74OoNa.th.png", Jamuna TV
https://playztv-apps.pages.dev/jamuna-tv/index.m3u8

#-------Thikana TV---------
#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.ibb.co.com/zh8zDdmp/5.jpg",Thikana Tv
https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.ibb.co/VWL70Dvx/logo.png" ,Me IPTV BD
https://iptvbd.live/metv1080/1080.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://i.ibb.co.com/21Jj6JyF/sanonda.jpg" ,Sanonda TV
https://live.sanandatelevision.in/sananda/index.m3u8

# --- Bangla Natok (1 Server) ---
#EXTINF:-1 group-title="BD TV" tvg-logo="https://iili.io/ClcgnwX.th.jpg", Bangla Natok
https://vods2.aynaott.com/gseriesDrama/tracks-v1a1/mono.ts.m3u8

#EXTINF:-1 group-title="BD TV" tvg-logo="https://imglink.cc/cdn/B1Dn0E5UKs.png", Movie Bangla
https://m.mxonlive.xyz/proxy-5441/auto_proxy.php?url=http://alvetv.com/moviebanglatv/8080/index.m3u8

# ==========================================
# 📺 INDIAN BANGLA TV
# ==========================================

# --- ZEE Bangla (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CEtU2af.th.jpg", ZEE Bangla
https://yupptvcatchupire.yuppcdn.net/preview/zeebangla/2500.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://i.imgur.com/lLhY3yS.jpeg", Jalsha Movies
https://iptvlive-beta.vercel.app/jalsha-movies/index.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CEtU2af.th.jpg", Colors Bangla Cenema
http://103.114.11.37:8081/Colors-bangla-cinema/index.m3u8?token=sboxcast

# --- Star Jalsa (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CE2C1G2.th.jpg", Star Jalsa
https://da86m1sqpm3o0.cloudfront.net/28072023/smil:starjalsha.smil/chunklist_b1928000.m3u8

# --- ZEE Bangla Sonar (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CwNMSCN.th.jpg", ZEE Bangla Sonar
https://drk6xq0vhn.gpcdn.net/live/zee_bangla_cinema_abr/live/zee_bangla_cinema_720/chunks.m3u8

#EXTINF:-1 tvg-id="019de785-399f-7d6a-9f41-dc7f834b3300" tvg-name="TV9 Bangla" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-02/images_4c08302f7fbe506a998e74c89fcf08ac_playmist_tv9_bangla_400x400.jpg" group-title="Indian Bangla",TV9 Bangla
https://dyjmyiv3bp2ez.cloudfront.net/pub-iotv9banaen8yq/liveabr/playlist.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/Ckk5qiv.th.jpg",ZB Cinema
https://server.zillarbarta.com/ZBCINEMA/index.m3u8

# --- Enter 10 (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CwN1YYJ.th.jpg", Enter 10
https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_240p/chunks.m3u8

# --- Colors Bangla (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CjpIwzb.th.jpg", COLORS Bangla
https://yupptvcatchupire.yuppcdn.net/preview/colorsbanglahd/800.m3u8

# --- Rongeen TV (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CjL1Wnj.th.png", Rongeen TV
https://server.thelegitpro.in/rongeentv/rongeentv/index.m3u8

# --- Akash Ath (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CjLENsf.th.jpg", Akash Ath
https://mumt03.tangotv.in/Dsly5z3HAAKASHAATH/index.m3u8

# --- Sun Bangla (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/Ce1euqu.th.jpg", Sun Bangla
http://27.124.71.27/Sun_Bangla/index.m3u8

#EXTINF:-1 tvg-id="019de785-39a3-74dd-8ef6-fbe0295e1222" tvg-name="kolkata TV" tvg-logo="https://web.aynaott.com/storage/019dd92f-107c-7056-9e79-e5233f6e51d9/uploads/images/2026-07-02/images_067234e427ca902620258631b762cea8_playmist_kolkata_tv_400x400.jpg" group-title="Indian Bangla",kolkata TV
https://tvsen6.aynaott.com/kolkatatv/index.m3u8

# --- Sony Ath (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CwOJwUx.th.jpg", Sony Ath
https://stream.ottplus.live/live/sony_aath_abr/index.m3u8

# --- Bangla Plus (1 Server) ---
#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://iili.io/CwN0v0g.th.jpg", Bangla Plus
https://live-stream.utkalbongo.com/hls/livebanglatvstream.m3u8

#EXTINF:-1 group-title="Indian Bangla" tvg-logo="https://i.ibb.co/GyDcpFZ/Aaj-tak-logo.png" ",Aaj Tak Bangla
https://aajtaklive-amd.akamaized.net/hls/live/2014416/aajtak/aajtaklive/live_720p/chunks.m3u8

# ==========================================
# 📺 MUSIC TV 
# ==========================================

#EXTINF:-1 group-title="Indian Music" tvg-logo="https://tubextra.b-cdn.net/images.png",YRF Music HD
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01412-xiaomiasia-yrfmusic-xiaomi/playlist.m3u8

#EXTINF:-1 tvg-id="9XJalwa.in" tvg-name="9X Jalwa" tvg-logo="https://i.imgur.com/qubgOi5.png" tvg-chno="236" group-title="Indian Music",9X Jalwa
https://d3kdywbtdfbp9z.cloudfront.net/v1/manifest/93ce20f0f52760bf38be911ff4c91ed02aa2fd92/dff423e0-3c82-46d6-9ecb-3baa96b5694a/70fca4d1-156e-4c03-baa4-9a4b602e33d5/0.m3u8


#EXTINF:-1 group-title="Indian Music" tvg-id="9XJhakaas.in" tvg-name="9X Jhakaas" tvg-logo="https://dtil.tmsimg.com/assets/s90012_ld_h15_aa.png?lock=720x540" tvg-chno="239",9X Jhakaas
https://wiselp.wiseplayout.com/9X_Jhakaas/master.m3u8

#EXTINF:-1 tvg-id="9XM.in" tvg-name="9XM" tvg-logo="https://dtil.tmsimg.com/assets/s77447_ld_h15_aa.png?lock=720x540" tvg-chno="241" group-title="Indian Music",9XM
https://cc-706183qeo55ez.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-706183qeo55ez/DIYC/PMSL/9X/9XMusic_IN/9XMusic_IN.m3u8


#EXTINF:-1 tvg-name="Hindi Hits HD" group-title="Indian Music",Hindi Hits HD
https://m.mxonlive.xyz/proxy-5441/auto_proxy.php?url=http://146.59.253.52:8080/hindihitshd/index.m3u8

#EXTINF:-1 group-title="Indian Music" tvg-name="Joo Music" ,Joo Music
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8

#EXTINF:-1 group-title="Indian Music" tvg-name="Baallee" ,Music India
https://cdn-2.pishow.tv/live/226/master.m3u8

#EXTINF:-1 group-title="Indian Music" tvg-logo="https://imgur.com/79g2kMA.png",Music Masti
https://live20.bozztv.com/giatvplayout7/giatv-209592/tracks-v1a1/mono.ts.m3u8

#EXTINF:-1 group-title="Indian Music" tvg-logo="https://iili.io/Ck8EfSa.th.jpg" ,B4U Music
https://cdn-2.pishow.tv/live/415/master.m3u8

#EXTINF:-1 group-title="Indian Music" tvg-name="B4U Movies",Zoom
https://pubads.g.doubleclick.net/ssai/event/JCAm25qkRXiKcK1AJMlvKQ/master.m3u8

# --- Sangeet Bangla (1 Server) ---
#EXTINF:-1 group-title="Indian Music" tvg-logo="https://tubextra.b-cdn.net/download%20(14).jpg", Sangeet Bangla
https://cdn.pishow.tv/ott/live/1143/1143_1.m3u8

# ==========================================
# 📺 Entertainment
# ==========================================

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://iili.io/CeW7rwG.th.jpg",  group-title="Hindi",Sony Max
https://drk6xq0vhn.gpcdn.net/live/max_hd_abr/index.m3u8#skym3u.dev

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/9/9b/Sony_Movies_Logo.svg",  group-title="Hindi", Sony Max 2
https://drk6xq0vhn.gpcdn.net/live/max_2_abr/index.m3u8

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/9/9b/Sony_Movies_Logo.svg",  group-title="Hindi", Sony Movies
https://a-cdn.klowdtv.com/live1/smc_720p/chunks.m3u8

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://iili.io/CeW7rwG.th.jpg",  group-title="Hindi",Colors Cineplex
https://d1rc86nwwc9fag.cloudfront.net/260723/smil:rishteycineplexukdev.smil/chunklist_b1928000.m3u8

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://imgur.com/79g2kMA.png",Action Hollywood Movies
https://amg01076-lightningintern-actionhollywood-samsungnz-82rry.amagi.tv/playlist/amg01076-lightningintern-actionhollywood-samsungnz/playlist.m3u8

#EXTINF:-1 tvg-name="Hindi" tvg-logo="https://img.favpng.com/14/9/13/sony-sab-logo-sony-sab-logo-in-orange-and-black-Fhr0xfHf_t.jpg",  group-title="Hindi",Sony SAB
https://drk6xq0vhn.gpcdn.net/live/sub_hd_abr/index.m3u8

#EXTINF:-1, tvg-name="Hindi", Hindi Movie Club
https://sis-global.prod.samsungtv.plus/v1/tvpprd/sc-mp2ar4ca425xo.m3u8

#EXTINF:-1  tvg-logo="https://imgur.com/79g2kMA.png",Goldmines Bollywood
https://vods2.aynaott.com/hindimovies/tracks-v1a1/mono.ts.m3u8

#EXTINF:-1  tvg-logo="https://imgur.com/79g2kMA.png",Hindi Movies 3
https://vods2.aynaott.com/hindimovies/index.m3u8

#EXTINF:-1 tvg-id="SonyEntertainmentTelevision" tvg-name="Sony Entertainment TV" tvg-logo="https://assets-prod.services.toffeelive.com/f_png,w_300,q_85/-y50-JQBv9knK3AHLzSn/posters/0ab48ac0-ec84-4ca2-9601-746ff3cb809e.webp" tvg-chno="307" group-title="Indian Entertainment",Sony Entertainment TV
https://stream.ottplus.live/live/sony_ent_hd_abr/index.m3u8

#EXTINF:-1 tvg-id="ZeeTV.in" tvg-name="Zee Tv" tvg-logo="https://i.postimg.cc/x8BwX6QW/20240823_022929.png" tvg-chno="315" group-title="Indian Entertainment",Zee Tv
https://stream.ottplus.live/live/zee_tv_hd_abr/index.m3u8

#EXTINF:-1 group-title="Hindi" tvg-id="B4UMovies.in" tvg-name="B4U Movies" tvg-logo="https://dtil.tmsimg.com/assets/s140063_ld_h9_aa.png?lock=720x540" tvg-chno="176" ,B4U Movies
https://amg00877-b4unew-amg00877c2-xiaomi-in-5489.playouts.now.amagi.tv/playlist.m3u8

#EXTINF:-1 tvg-id="AndTV.in" tvg-name="&TV [Backup 1]" tvg-logo="https://dvdh7g0f0hwck.cloudfront.net/assets/images/channel/%26TV_Transparent_c5cc189b-8493-48d2-b07c-3fa4f92d754a.png" tvg-chno="287" group-title="Indian Entertainment",&TV 
https://drk6xq0vhn.gpcdn.net/live/and_tv_hd_abr/index.m3u8

#EXTINF:-1 tvg-id="ColorsRishteyAmericas.in" tvg-name="Colors Rishtey Americas" tvg-logo="https://i.imgur.com/xkOunuW.png" tvg-chno="291" tvg-language="hin" tvg-country="IN" group-title="Indian Entertainment" nexus-score="100",Colors Rishtey Americas
https://manatv.akamaized.net/090823/smil:ristheyamerica.smil/playlist.m3u8

#EXTINF:-1 tvg-id="DangalTV.in" tvg-name="Dangal" tvg-logo="https://dtil.tmsimg.com/assets/s142771_ld_h9_aa.png?lock=720x540" tvg-chno="292" group-title="Indian Entertainment",Dangal
https://live-dangal.akamaized.net/liveabr/playlist.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/KjjqnRH/Picsart-23-06-30-21-35-20-283.png" group-title="Hindi",SHEEMAROO BOLLYWOOD
https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8


#EXTINF:-1 tvg-id="HumTV.pk" tvg-name="HUM TV" tvg-logo="https://i.postimg.cc/vT4DKmf3/20240925_075103.png" tvg-chno="298" group-title="Entertainment",HUM TV
https://drk6xq0vhn.gpcdn.net/live/hum_tv_abr/index.m3u8

# ==========================================
# 🏆 Islamic
# ==========================================

#EXTINF:-1  group-title="Islamic" tvg-logo="https://i.ibb.co.com/5gMzQmLm/Islamic.jpg", Islamic TV
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/islamictvbd.stream/index.m3u8

#EXTINF:-1  group-title="Islamic" tvg-logo="https://i.ibb.co.com/ynGHYLH9/download.jpg", Peace TV Bangla
https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/islamictvbd.stream/index.m3u8

#EXTINF:-1  group-title="Islamic" tvg-logo="https://i.ibb.co.com/hJ332kvz/Madani-Tv.jpg", Madani TV
https://tvsen3.aynaott.com/z24qLsqV/index.m3u8

#EXTINF:-1  group-title="Islamic" tvg-logo="https://i.ibb.co.com/84cYwzVL/Sunnah-Tv.png", Sunnah TV
http://m.live.net.sa:1935/live/sunnah/chunklist.m3u8

# ==========================================
# 🏆 Infotainment
# ==========================================

#EXTINF:-1 tvg-id="AnimalPlanet.in" tvg-name="Animal Planet tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/2018_Animal_Planet_logo.svg/960px-2018_Animal_Planet_logo.svg.png" tvg-chno="429" group-title="Documentary & Wildlife",Animal Planet 
https://drk6xq0vhn.gpcdn.net/live/animal_planet_hd/index.m3u8

#EXTINF:-1 group-title="Documentary & Wildlife" tvg-logo="https://assets-prod.services.toffeelive.com/KS6x-JQBv9knK3AHwDZy/posters/6594d216-aaca-4eee-b6f5-bbc6b80feb15.webp",Discovery
https://livecdn.live247stream.com/discoverpakistan/web/playlist.m3u8

#EXTINF:-1 group-title="Documentary & Wildlife" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYi8fTRD2JvQusZi21I6hvtmjCEoRKlDx2APFYaWgrWg&s=10",Love Nature
https://bamusa-naturetime-emea-eng-rakuten.amagi.tv/playlist.m3u8

#EXTINF:-1 group-title="Documentary & Wildlife" tvg-logo="https://i.ibb.co.com/yF8cbnXj/images-4.jpg",Wild Fox Hindi
https://bamusa-naturetime-emea-eng-rakuten.amagi.tv/playlist.m3u8

#EXTINF:-1 group-title="Documentary & Wildlife" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4ZQWcPxt5kC7VHUHvcGN5is8XySLDC5RFpVKcctUgHw&s=10",Real Wild
https://cdn-ue1-prod.tsv2.amagi.tv/linear/amg00426-littledotstudio-realwild-tcl/playlist.m3u8

#EXTINF:-1 group-title="Science Fiction" tvg-logo="https://assets-prod.services.toffeelive.com/AS6s-JQBv9knK3AHDTZb/posters/eab8fd0f-9351-464c-b45e-332f38b49f4b.webp",Discovery Science
http://103.151.60.188:12345/hls/tab_l9gqwqb/index.m3u8?t=1791653473234

#EXTINF:-1 group-title="Adventure" tvg-logo="https://assets-prod.services.toffeelive.com/Ay6s-JQBv9knK3AHJTY1/posters/e8f65578-e82d-4e4a-a1ff-073becc5bd71.webp",Discovery Turbo
https://prod-linear-media.toffeelive.com/cdn/live/discovery_turbo/playlist.m3u8?edge-cache-token=Expires=1790362930~Starts=1790359330~URLPrefix=aHR0cHM6Ly9wcm9kLWxpbmVhci1tZWRpYS50b2ZmZWVsaXZlLmNvbQ~Data=eyJzdWJzY3JpYmVyX2lkIjoiMmYyNmEyZmYtODRkYS00NzRiLWJiN2EtMjFlY2VhZTIyNDBmIn0~Signature=8YkWpeeYWvfEyXJpK0HwkzUXN8X9VFgvolQCiBbMmf3UwCBnrN8RewpjE6NfdnnV20SRSQnvWruk0PoYltYOAQ


#EXTINF:-1 tvg-id="BBCEarth.ca" tvg-name="BBC Earth" tvg-logo="https://bbcearth.ca/wp-content/uploads/2024/02/BBCEarth_Logo-1.png" tvg-chno="431" group-title="Documentary & Wildlife",BBC Earth [Backup 1]
https://amg00793-amg00793c6-xumo-us-2669.playouts.now.amagi.tv/BBCStudios-BBCEarthA-hls/playlist.m3u8

#EXTINF:-1 tvg-id="InvestigationDiscovery.in" tvg-name="Investigation Discovery" tvg-logo="https://dtil.tmsimg.com/assets/s157811_ld_h15_aa.png?lock=720x540" tvg-chno="439" group-title="Documentary & Wildlife",Investigation Discovery
https://stream.ottplus.live/live/id_hd_abr/index.m3u8

#EXTINF:-1 tvg-id="local.bc3ae4d983e661a3" tvg-name="Love Nature" tvg-logo="https://i.postimg.cc/MZR248Yw/20240823-024104.png" tvg-chno="440" group-title="Documentary & Wildlife",Love Nature
https://bamusa-naturetime-emea-eng-rakuten.amagi.tv/playlist.m3u8

# ==========================================
# 🎬 Hindi Movies
# ==========================================

{DYNAMIC_HINDI_MOVIES}

# ==========================================
# 🎬 Bengali Movies
# ==========================================

{DYNAMIC_BENGALI_MOVIES}

# ==========================================
# 🎬 English Movies
# ==========================================

{DYNAMIC_ENGLISH_MOVIES}

# ==========================================
# 📺 CARTOON TV
# ==========================================

#EXTINF:-1 tvg-id="Pogo.in" tvg-name="Pogo" tvg-logo="https://i.postimg.cc/C1s5Hf5P/20240823_021444.png" tvg-chno="479" group-title="Kids",Pogo
https://stream.ottplus.live/live/pogo_sd_abr/index.m3u8

#EXTINF:-1 tvg-id="Pogo.in" tvg-name="Pogo" tvg-logo="https://i.postimg.cc/C1s5Hf5P/20240823_021444.png" tvg-chno="479" group-title="Kids",Discovery Kids
https://stream.ottplus.live/live/discovery_kids_abr/index.m3u8

#EXTINF:-1 tvg-id="ToonGoggles.us" tvg-name="Toon Goggles" tvg-logo="https://tvpnlogopus.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/USBB1900004J9_20240520T214715SQUARE.png" tvg-chno="490" group-title="Kids",Toon Goggles
https://d1eg24xrsfr6kv.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-b4b1bzxkt1uzo-prod/tg/tg/tg.m3u8

#EXTINF:-1 tvg-id="SonyYay.in" tvg-name="Sony Yay" tvg-logo="https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_SONY_YAY/images/LOGO_HD/image.png" tvg-chno="482" group-title="Kids",Sony Yay
https://drk6xq0vhn.gpcdn.net/live/sony_yay_abr/index.m3u8

#EXTINF:-1 tvg-name="Mr Bean Animated" group-title="CARTOON Drama",Mr Bean Animated
https://amg00627-amg00627c29-rakuten-it-3989.playouts.now.amagi.tv/playlist/amg00627-banijayfast-mrbeanitcc-rakutenit/playlist.m3u8

#EXTINF:-1 group-title="Kids" tvg-logo="https://iili.io/CjUNsJ1.th.png", Cartoon Network
https://vodzong.mjunoon.tv:8087/streamtest/cartoon-network-87/playlist.m3u8

#EXTINF:-1 group-title="Cartoon" tvg-logo="https://imglink.cc/cdn/cZxNWhHkaZ.jpg", Oggy and the Cockroaches
https://live20.bozztv.com/giatvplayout7/giatv-210728/tracks-v1a1/mono.ts.m3u8
"""

def fetch_and_parse_m3u(url, target_group_title, skip_first=False):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            lines = response.read().decode('utf-8').splitlines()
    except Exception as e:
        print(f"Error fetching external M3U ({url}): {e}")
        return ""

    dynamic_m3u = ""
    current_channel_block = []
    first_skipped = False 

    for line in lines:
        line = line.strip()
        if not line or line == "#EXTM3U":
            continue
        
        if line.startswith("#EXTINF"):
            if 'group-title="' in line:
                line = re.sub(r'group-title="[^"]*"', f'group-title="{target_group_title}"', line)
            else:
                line = re.sub(r'(#EXTINF:[^,]+)', fr'\1 group-title="{target_group_title}"', line, count=1)
            
            # Use .append() instead of redefining the list to preserve prior #EXTVLCOPT tags
            current_channel_block.append(line)
            
        elif line.startswith("#EXTVLCOPT") or line.startswith("#KODIPROP"):
            current_channel_block.append(line)
                
        elif not line.startswith("#"): # Stream URL line
            current_channel_block.append(line)
            
            if skip_first and not first_skipped:
                first_skipped = True
            else:
                dynamic_m3u += "\n".join(current_channel_block) + "\n\n"
            
            # Reset block for the next channel
            current_channel_block = []

    return dynamic_m3u

def generate_m3u():
    print("Fetching Sports channels...")
    sports_data = fetch_and_parse_m3u(SPORTS_URL, "Sports Live")
    
    print("Fetching SonyLiv channels...")
    sonyliv_data = fetch_and_parse_m3u(SONYLIV_URL, "Sports Live")
    
    print("Fetching Hindi Movies...")
    movies_data = fetch_and_parse_m3u(HINDI_MOVIES_URL, "Hindi Movies")

    print("Fetching Bengali Movies...")
    bengali_movies_data = fetch_and_parse_m3u(BENGALI_MOVIES_URL, "Bengali Movies")
    
    print("Fetching English Movies...")
    english_movies_data = fetch_and_parse_m3u(ENGLISH_MOVIES_URL, "English Movies")

    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    timestamp_header = f"# Auto-Updated via Actions at: {timestamp} UTC\n\n"
    
    if sports_data:
        sports_data = timestamp_header + sports_data

    final_m3u = PLAYLIST_TEMPLATE.replace("{DYNAMIC_CHANNELS}", sports_data)
    final_m3u = final_m3u.replace("{DYNAMIC_SONYLIV}", sonyliv_data)
    final_m3u = final_m3u.replace("{DYNAMIC_HINDI_MOVIES}", movies_data)
    final_m3u = final_m3u.replace("{DYNAMIC_BENGALI_MOVIES}", bengali_movies_data)
    final_m3u = final_m3u.replace("{DYNAMIC_ENGLISH_MOVIES}", english_movies_data)

    with open(M3U_FILE, 'w', encoding='utf-8') as f:
        f.write(final_m3u)
        print(f"Successfully updated {M3U_FILE}")

if __name__ == "__main__":
    generate_m3u()
