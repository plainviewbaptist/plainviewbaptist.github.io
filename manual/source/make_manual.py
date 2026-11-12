# Generates PBC-App-Manual.html (16:9 slides)
import html
S='brief-screenshots/'
H=lambda t: t  # text already HTML-safe
CHK='<td class="y">&#10003;</td>'; NO='<td class="n">&mdash;</td>'

B='brief-screenshots/'; C='crops/'
tabs=[
 ("Home","Your welcome page: our church, our pastor, and service times.",[
  (C+"home-top.png","Home",["The first screen you see. It welcomes you by name and shows the sanctuary and our pastor, Rev. Jody Mitchell.",
    "Tap <b>Add to Home Screen</b> at the top to put the app on your phone.",
    "The bell shows your notifications. Your initials at the top open your profile."]),
  (C+"home-times.png","Service times",["Scroll down on Home to see the service times.",
    "Sunday School, Sunday Morning Worship, Sunday Evening Service, and Wednesday Evening Service are all listed."])]),
 ("Events","What's coming up, birthdays and anniversaries, and event photos.",[
  (B+"events-list.png","Events list",["<b>Add</b> is the first button under the title. Tap it to suggest an event. The switch at the top opens <b>Birthdays &amp; Anniversaries</b>.",
    "Open photo-upload cards sit at the top, then announcements, then upcoming events.",
    "An event stays in the upcoming list until it ends."]),
  (B+"events-header-owner.png","Events header: leader buttons",["<span class='tag'>Owners</span> Owners see more buttons under the title, with <b>Add</b> still first.",
    "The row wraps onto a second line, so <b>Sunday slides</b> and <b>Preview events screen</b> are always visible."]),
  (B+"events-birthdays.png","Birthdays &amp; Anniversaries",["A month calendar of members' birthdays and wedding anniversaries, with cake and ring markers.",
    "No years or ages are shown, only the month and day.",
    "Use the arrows to move between months. That month's names are listed below the calendar."]),
  (B+"events-month-vbs.png","Month view",["Switch to <b>Month</b> to see events on a calendar. <b>Back</b> and <b>Next</b> change the month.",
    "A multi-day event shows as one colored bar across every day it covers, and the bar continues onto the next week's row.",
    "Here Vacation Bible School runs Monday, July 6 through Friday, July 10."]),
  (B+"events-detail.png","Event detail",["Tap an event to see its flyer, time, place, and description.",
    "If the event takes photos, its upload card is here too. Uploads close 3 days after the event ends, and then the pictures are shown in <b>Watch &rsaquo; Media &rsaquo; Photos</b>."]),
  (B+"event-detail-multiday.png","Multi-day event",["An event that lasts several days shows its dates as a range, like <b>Mon, July 6 - Fri, July 10, 2026, 6:00 PM</b>.",
    "It counts as upcoming until it ends, and photo uploads close 3 days after the end.",
    "<span class='tag'>Owners</span> Owners also see the <b>End-of-event video</b> box and <b>Edit</b> and <b>Delete</b>."]),
  (B+"events-new.png","New event",["Members can suggest an event. <b>Date and time</b> is when it starts.",
    "<b>Ends</b> is optional, for an event that runs several days. Leave it blank for a single-date event.",
    "The event stays off the calendar and the Sunday screen until an admin approves it, and you'll get a notice when it's approved or turned down."]),
  (B+"events-announcement.png","Announcement",["A posted announcement, like the Fellowship supper, also appears on the Events screen.",
    "Tap it to read the whole announcement. Tap <b>Back</b> to return."]),
  (B+"events-upload-checkbox.png","Members can upload photos",["<span class='tag'>Leaders</span> When setting up an event, check <b>Members can upload photos</b>.",
    "That creates a photo drop for the event, so members can add their pictures.",
    "The same form has optional sign-up fields: a sign-up link, a sign-up deadline, and <b>Collect sign-ups in the app</b>.",
    "Tap <b>Save event</b> when you're done."]),
  (B+"events-upload.png","Photo upload",["Share your photos from an event. <b>Photos only.</b>",
    "Tap <b>Choose photos</b> to pick pictures from your phone.",
    "Uploads close 3 days after the event ends. Then the pictures are shown to members in <b>Watch &rsaquo; Media &rsaquo; Photos</b>."]),
  (C+"montage-top.png","Owner montage: end-of-event video",["<span class='tag'>Owners</span> On a past event's page, the <b>End-of-event video</b> box holds one video for that event.",
    "Only a church owner can add or replace it, with <b>Replace video</b> or <b>Remove video</b>."]),
  (B+"watch-media-videos.png","Owner montage in Media",["The montage then shows in <b>Watch &rsaquo; Media &rsaquo; Videos</b> for everyone to watch.",
    "Montages and saved videos use the same full date, with the year, like <b>Sunday, June 14, 2026</b>. Here it's Vacation Bible School night."]),
 ]),
 ("Prayer","Share requests and pray for one another.",[
  (B+"prayer-list.png","Prayer list",["Active prayer requests that members can read.",
    "Tap <b>Praying</b> to show you're praying. The number shows how many are praying.",
    "Switch between <b>Active</b> and <b>Past prayers</b>, open <b>Daily prayer</b>, or tap <b>New request</b>."]),
  (B+"prayer-detail.png","Prayer request",["Open a request from the list to read all of it.",
    "Tap <b>Praying</b>, or write a note and tap <b>Send encouragement</b>."]),
  (B+"prayer-new.png","New prayer request",["Give your request a title, details, and a date.",
    "Check <b>Private</b> so only you and the admins see it.",
    "Or check <b>Hide my name</b>, and members see &ldquo;A church member.&rdquo;"]),
  (B+"prayer-daily.png","Daily prayer",["Today's prayer posted for the church, with earlier ones listed.",
    "The prayer is shown without the name of the person who wrote it.",
    "Daily prayers stay off the prayer request list and the Sunday screen."]),
  (B+"prayer-daily-detail.png","Daily prayer detail",["Open a daily prayer to read it in full.",
    "The prayer is shown without the name of the person who wrote it.",
    "Say <b>Amen</b> or tap a quick reaction."]),
 ]),
 ("Watch","The live service, then Media (photos and videos from past events), then Sermons.",[
  (C+"watch-live-top.png","Live",["When a service is live, a red <b>Watching live now</b> banner runs across the top, and Watch shows <b>Live now</b> with the service name.",
    "Services stream on Facebook Live. Tap <b>Open on Facebook</b> to watch there.",
    "Right below is <b>Media</b>, with photos and videos from past events."]),
  (B+"watch-media-videos.png","Media: Videos",["<b>Media</b> holds the photos and videos from past church events.",
    "<b>Videos</b> is shown first, including the owner's end-of-event video montages.",
    "Newest first, with the date under each, like Sunday, June 14, 2026."]),
  (B+"watch-media-photos.png","Media: Photos",["Tap <b>Photos</b> to see pictures saved from past events, including members' uploads once a photo drop closes.",
    "Newest first, with the date under each.",
    "<b>Add a photo</b> is for approved members, admins, and owners. People waiting for approval and visitors can't use it."]),
  (B+"photo-viewer.png","Photo viewer",["Tap an album in Media &rsaquo; Photos to see its pictures full screen.",
    "<b>Previous</b> and <b>Next</b> move between pictures, the counter shows where you are, and <b>Close</b> takes you back."]),
  (B+"watch-sermons.png","Sermons",["<b>Sermons</b> sit below Media.",
    "Search sermons, or tap a series name to narrow the list."]),
  (B+"watch-sermon.png","Sermon",["Open a sermon to see who preached, the date, Scripture, and series.",
    "Watch it on Facebook and read the sermon's main points."]),
  (B+"watch-add-photo.png","Add a photo",["The form for adding a photo to Media: title, date, category, and description.",
    "Tap <b>Upload photo</b>. <b>Photos only</b>; there's no video option.",
    "The photo then shows in Watch, under Media, then Photos. Only approved members, admins, and owners can use this form."]),
  (B+"watch-video.png","Saved event videos",["Saved event videos are listed in <b>Media &rsaquo; Videos</b>.",
    "For example, the Vacation Bible School highlight reel, dated Sunday, June 14, 2026.",
    "Tap a video to open it."]),
 ]),
 ("More","Directory, family, Bible, music, giving, contact, install, feedback, and leader tools.",[
  (B+"more.png","More",["Everything that isn't on the bottom bar.",
    "<b>Photo Drop</b> (add photos), Feedback, Directory, Daily prayer, Bible, music, giving, your profile, contact, and install help are all here."]),
  (B+"more-directory.png","Directory",["Church families and members.",
    "Search by name. A phone number shows only when that member has shared it."]),
  (B+"more-directory-person.png","Directory member",["Tap a name to see their card.",
    "<b>Call</b> or <b>Text</b> them, and see their email and birthday.",
    "On your own card, tap <b>Edit your listing</b>."]),
  (B+"more-family.png","Family page",["A family page shows the people in that household and how they're related."]),
  (B+"more-profile.png","Profile",["Your own profile. Tap <b>Change photo</b>, then update your name, phone, and email.",
    "Check that your number is a mobile so it can get texts.",
    "The <b>Show in directory</b> switch decides whether you're listed."]),
  (B+"more-profile-family.png","Profile: join a family",["New members can ask to join a family.",
    "Families are listed by name with their members' first names. Choose one, enter your relationship, and tap <b>Ask to join</b>.",
    "The family gets a notice to approve."]),
  (B+"more-bible.png","Bible",["Opens the New King James Version on Bible Gateway.",
    "Type a verse, like John 3:16, and tap <b>Open</b>, or pick a book."]),
  (B+"more-music.png","Music Ministry",["Ask the music team for a song by title and artist.",
    "If someone already asked for it, tap <b>+1</b> instead of adding it again.",
    "<b>Export CSV</b> saves the request list as a file."]),
  (B+"more-music-request.png","Request a song",["Enter the song title and artist or band, plus an optional note or dedication.",
    "Pick a preferred service, then tap <b>Add request</b>."]),
  (B+"more-give.png","Give",["Giving is still under construction.",
    "Online giving (Venmo, Cash App, Apple Pay) is coming soon. Until then, you can give in the offering plate on Sunday."]),
  (B+"more-contact.png","Contact",["Call, Text, or Email the church.",
    "You'll also find the address, our Facebook page, and service times."]),
  (B+"more-install.png","Install the app",["Step-by-step help for adding the app to your phone's home screen.",
    "On Android: open the page in Chrome, tap <b>Install app</b> or <b>Add to Home screen</b>, then allow notifications.",
    "A QR code is there to share the app with others."]),
  (B+"more-feedback.png","Feedback",["Have a suggestion or improvement for the app?",
    "Type it and tap <b>Submit</b>."]),
  (C+"v45-admin-approvals.png","Admin tools (admin)",["<span class='tag'>Admins</span> <b>Waiting for approval</b> is at the top of Admin tools, because approvals happen most often. Tap <b>Approve</b> or <b>Decline</b> for each new member.",
    "Below that are <b>Photo drops</b> and <b>Pending events</b>. After a photo drop closes (3 days after the event ends), the photos show in Watch &rsaquo; Media &rsaquo; Photos.",
    "Each section has a gold <b>Show</b>/<b>Hide</b> button. Approvals starts open when someone is waiting; the other sections start closed.",
    "Admins see only a new member's name and photo, never private details, the Members section, or families."]),
  (C+"v45-owner-overview.png","Owner tools: overview",["<span class='tag'>Owners</span> Every section in Admin tools has its own gold <b>Show</b>/<b>Hide</b> button. Most headers show a count, like <b>Members (11)</b>.",
    "<b>Members</b> sits directly under <b>Waiting for approval</b>.",
    "<b>Waiting for approval</b> starts open when someone is waiting. Every other section, including Members, starts closed until you tap <b>Show</b>."]),
  (C+"v45-owner-approvals.png","Owner tools: approvals",["<span class='tag'>Owners</span> Owners see <b>Waiting for approval</b> once, at the top, because approvals happen most often.",
    "Each new member has <b>Approve</b> and <b>Decline</b>.",
    "<b>Members</b> comes next."]),
  (C+"v45-owner-members.png","Owner tools: members list",["<span class='tag'>Owners</span> Only owners see the <b>Members</b> section. It starts closed; tap <b>Show</b> to open it.",
    "The <b>Members</b> list shows approved people.",
    "Use the <b>Family</b> list to put someone in a family, or pick <b>+ New family&hellip;</b> to start one.",
    "<b>Make admin</b> or <b>Make owner</b>. The app allows up to 2 owners."]),
  (C+"owner-2-pending.png","Owner tools: pending events",["Events that members suggest wait here.",
    "<b>Approve</b>, <b>Open</b>, <b>Edit</b>, or <b>Decline</b> with an optional note. You can check <b>Members can upload photos</b> before approving."]),
  (C+"owner-3-settings.png","Owner tools: church settings",["Owners set up the home screen: pastor name, welcome message, denomination, and banner photo.",
    "Also event reminders, the daily prayer check-in hour, and when prayers move to Past prayers."]),
  (C+"owner-4-servicetimes.png","Owner tools: service times",["Owners edit the service times shown on Home and Contact.",
    "Each service has a time and an optional note. Tap <b>Add a service time</b> for another."]),
  (B+"admin-tools-display.png","Owner tools: display links",["<span class='tag'>Owners</span> <b>Display links</b> feed ProPresenter, which uses two web slides: the events screen (one full slide per event) and a separate prayer screen.",
    "Tap <b>Preview events screen</b> or <b>Preview prayer screen</b> to check them.",
    "<b>Create a display link</b>, then <b>Copy</b> the Lobby screens addresses."]),
 ]),
]

G='brief-screenshots/v43/'
guests=("Guests","No account yet, or still waiting for approval? You can look around as a guest.",[
  ("FINDUS","How guests find us",[]),
  (G+"guest-welcome.png","Welcome screen",["The welcome screen has a <b>Continue as guest</b> button, next to <b>Sign in with Google</b> and signing in with email.",
    "Anyone who isn't signed in, or whose account is still waiting for approval, is a guest."]),
  (G+"guest-events.png","Guest: Events",["Guests get only three bottom tabs: <b>Events</b>, <b>Watch</b>, and <b>Contact</b>. A <b>Sign in / Join</b> button sits in the header.",
    "Events has <b>List</b> and <b>Month</b> views, event details, past events, and montage videos.",
    "Birthdays &amp; Anniversaries aren't shown to guests."]),
  (G+"guest-watch.png","Guest: Watch",["Guests can watch the live stream and sermons.",
    "They can also browse <b>Media</b>, with both <b>Videos</b> and <b>Photos</b>."]),
  (G+"guest-contact.png","Guest: Contact",["Guests can <b>Call</b>, <b>Text</b>, or <b>Email</b> the church, open our Facebook page, and see the service times.",
    "The message form is hidden for guests."]),
  (None,"What guests can't do",[]),
])

def foot(n): return f'<div class="sfoot"><span><b>plainviewbaptist.github.io</b></span><span>Plainview Baptist Church &middot; App Guide</span><span class="pn">{n}</span></div>'

slides=[]
slides.append('''<section class="slide cover">
 <div class="cl">
  <img class="clogo" src="../pbc-logo-cutout.png">
  <div class="kicker">Plainview Baptist Church &middot; Hornbeck, Louisiana</div>
  <h1>Our Church App</h1>
  <div class="csub">A guide to every screen &middot; Version 45</div>
  <div class="inst">
   <div class="os">Same app on iPhone and Android</div>
   <p><b>iPhone:</b> Open the link in Safari, tap <b>Share</b>, then <b>Add to Home Screen</b>.</p>
   <p><b>Android:</b> Open the link and tap <b>Install</b> or <b>Add to Home screen</b>.</p>
   <p class="small">Services stream on Facebook Live.</p>
  </div>
 </div>
 <div class="cr">
  <div class="q"><img src="../pbc-app-qr.png"></div>
  <div class="url">https://plainviewbaptist.github.io/</div>
  <div class="sc">SCAN TO INSTALL</div>
 </div>
</section>''')
n=2
order=tabs[:4]+[guests]+tabs[4:]
ti=-1
for (tab,tag,secs) in order:
    isg = tab=="Guests"
    if not isg: ti+=1
    lis=''.join(f'<li><span class="num">{i+1}</span>{t}</li>' for i,(f,t,_) in enumerate(secs))
    cls='two' if len(secs)>8 else ''
    slides.append(f'''<section class="slide intro"><div class="il">
 <div class="tabno">{"Guest access" if isg else f"Tab {ti+1} of 5"}</div><h1>{tab}</h1><p class="tag2">{tag}</p>
 <div class="tabbar">{''.join(f'<span class="on">{t}</span>' for t in ["Events","Watch","Contact"]) if isg else ''.join(f'<span class="{"on" if t[0]==tab else ""}">{t[0]}</span>' for t in tabs)}</div>{'<p class="tag2" style="font-size:12pt;margin-top:.12in">The three tabs guests see</p>' if isg else ''}</div>
 <div class="ir"><div class="kicker" style="color:var(--gold2)">In this section</div><ol class="seclist {cls}">{lis}</ol></div>{foot(n)}</section>''')
    n+=1
    for i,(f,title,pts) in enumerate(secs):
        if f=="FINDUS":
            slides.append(f'''<section class="slide findus"><div class="fl">
 <div class="crumb">{tab} <span>&rsaquo;</span> {i+1} of {len(secs)}</div>
 <h2>{title}</h2>
 <div class="fitem"><div class="fic"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="2"/></svg></div><p>Starting <b>Nov 11, 2026</b>, people who aren't members can open the app from the church's Facebook page and the church website.</p></div>
 <div class="fitem"><div class="fic"><svg viewBox="0 0 24 24"><rect x="6" y="2" width="12" height="20" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 18.5h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M9 9l2 2 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div><p>Visitors tap <b>Continue as guest</b> to look around, or <b>Sign in / Join</b> to become a member.</p></div></div>
 <div class="fr">
  <div class="fcard"><div class="fic big"><svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-4 4v-4H4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="9" cy="10.5" r="1.2" fill="currentColor"/><circle cx="12" cy="10.5" r="1.2" fill="currentColor"/><circle cx="15" cy="10.5" r="1.2" fill="currentColor"/></svg></div><h3>Facebook</h3><p>The app link <b>plainviewbaptist.github.io</b> goes in the Page's website field and in a pinned post.</p></div>
  <div class="fcard"><div class="fic big"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></div><h3>Church website</h3><p>The old church website will send visitors straight to the app.</p></div>
 </div>{foot(n)}</section>''')
            n+=1; continue
        if f is None:
            slides.append(f'''<section class="slide gcant"><div class="gl">
 <div class="crumb">{tab} <span>&rsaquo;</span> {i+1} of {len(secs)}</div>
 <h2>{title}</h2><p>Guests see only a cleaned-up copy of event and media information, with no member names, phones, or emails.</p>
 <p>To do more, tap <b>Sign in / Join</b> and wait for approval.</p></div>
 <div class="gr"><div class="gcard"><h3>Guests can't see</h3><ul><li>The Directory</li><li>Prayer requests</li><li>Profile and family</li><li>Announcements</li><li>Feedback</li><li>Admin tools</li></ul></div>
 <div class="gcard"><h3>Guests can't</h3><ul><li>Add events</li><li>RSVP or sign up</li><li>Upload photos</li><li>Post anything</li></ul></div></div>{foot(n)}</section>''')
            n+=1; continue
        ps=''.join(f'<li>{p}</li>' for p in pts)
        slides.append(f'''<section class="slide sec"><div class="sl">
 <div class="crumb">{tab} <span>&rsaquo;</span> {i+1} of {len(secs)}</div>
 <h2>{title}</h2><ul class="pts">{ps}</ul></div>
 <div class="sr"><div class="phone"><img src="{f}"></div></div>{foot(n)}</section>''')
        n+=1

# chart
rows=[("guest","Everyone, including guests",[
 "Events (List and Month), Watch, and Contact"]),
 ("member","Signed-in members",[
 "Use Home, Prayer, More, and Birthdays &amp; Anniversaries",
 "Suggest events and share prayer requests",
 "Add photos to events that allow uploads",
 "Ask to join a family",
 "Send app feedback (under More)"]),
 ("admin","Admins and owners",[
 "Approve or decline new members (name and photo only)",
 "Approve events",
 "Create photo drops and check &ldquo;Members can upload photos&rdquo; on events",
 "Help with prayer requests and feedback"]),
 ("owner","Owners only (up to 2)",[
 "The members list and families (including + New family&hellip;)",
 "Make admin and Make owner",
 "Announcements",
 "Settings and service times",
 "Display links",
 "The end-of-event video montage"])]
tr=''
for k,g,items in rows:
    tr+=f'<tr class="grp"><td colspan="5">{g}</td></tr>'
    for it in items:
        g_,m,a,o={'guest':(1,1,1,1),'member':(0,1,1,1),'admin':(0,0,1,1),'owner':(0,0,0,1)}[k]
        tr+=f'<tr><td>{it}</td>{CHK if g_ else NO}{CHK if m else NO}{CHK if a else NO}{CHK if o else NO}</tr>'
slides.append(f'''<section class="slide chart"><div class="chl">
 <div class="crumb">Leaders</div><h2>Who Can Do What</h2>
 <p>Everything members can do, admins and owners can do too.</p>
 <p><b>Admins</b> approve new members, but they see only a name and photo, never private details, the members list, or families.</p>
 <p><b>Owners</b> (up to 2) can do everything.</p>
 <p><b>Guests</b> (not signed in, or still waiting for approval) see only Events, Watch, and Contact.</p></div>
 <div class="chr"><table><tr><th style="width:52%">Task</th><th>Guests</th><th>Members</th><th>Admins</th><th>Owners</th></tr>{tr}</table></div>{foot(n)}</section>''')
n+=1
wl=lambda lab,pre='': f'<div class="wl"><span>{lab}</span><i class="{"pre" if pre else ""}">{pre}</i></div>'
slides.append(f'''<section class="slide decide-s"><div class="decide">
 <h2>For the church to decide</h2>
 <div class="dcols">
  <div class="qblock"><p class="q"><span>1</span>Who should be the app owners?</p>
   <div class="rec"><div class="rk">Our recommendation</div><p>The app allows up to two owners. Two owners share full control (the members list and families, announcements, settings and admins), so the church is never locked out. Ronald Sellers is one owner, and the church chooses the second.</p></div>
   <div class="writein">{wl("Owner 1","Ronald Sellers")}{wl("Owner 2")}</div></div>
  <div class="qblock"><p class="q"><span>2</span>Who should serve as app admins?</p>
   <div class="rec"><div class="rk">Our recommendation</div><p>Four admins share the work of approving new members and events, setting up photo drops, and helping with prayer requests and app feedback.</p></div>
   <div class="writein">{wl("Admin 1")}{wl("Admin 2")}{wl("Admin 3")}{wl("Admin 4")}</div></div>
 </div></div>{foot(n)}</section>''')

css=open('manual.css').read()
open('PBC-App-Manual.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Plainview Baptist Church App Guide</title><style>{css}</style></head><body>{"".join(slides)}</body></html>')
print(len(slides),'slides')
