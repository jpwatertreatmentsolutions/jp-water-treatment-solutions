import os,re,sys,threading,http.server,socketserver,urllib.request,json
from html.parser import HTMLParser
os.chdir('out')
class P(HTMLParser):
    def __init__(s):super().__init__();s.h1=0;s.links=[];s.imgs=[];s.ids=set();s.t="";s.meta={};s.canon=None;s.in_t=False;s.hs=[]
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag=="h1":s.h1+=1
        if tag in("h1","h2","h3"):s.hs.append(tag)
        if tag=="title":s.in_t=True
        if tag=="meta" and a.get("name") in("description","robots"):s.meta[a["name"]]=a.get("content")
        if tag=="link" and a.get("rel")=="canonical":s.canon=a["href"]
        if tag=="a" and a.get("href"):s.links.append(a["href"])
        if tag=="img":s.imgs.append(a)
        if "id" in a:s.ids.add(a["id"])
    def handle_data(s,d):
        if s.in_t:s.t+=d
    def handle_endtag(s,tag):
        if tag=="title":s.in_t=False
pages={"/":"index.html","/services/":"services/index.html","/about-us/":"about-us/index.html","/contact-us/":"contact-us/index.html","/privacy-policy/":"privacy-policy/index.html"}
socketserver.TCPServer.allow_reuse_address=True;srv=socketserver.TCPServer(("127.0.0.1",8791),http.server.SimpleHTTPRequestHandler);threading.Thread(target=srv.serve_forever,daemon=True).start()
def code(u):
    try:return urllib.request.urlopen("http://127.0.0.1:8791"+u).status
    except urllib.error.HTTPError as e:return e.code
parsed={};bad=0
for u,f in pages.items():
    p=P();p.feed(open(f).read());parsed[u]=p
    print(u,"status",code(u),"| h1:",p.h1,"| canonical:",p.canon,"| noindex:", "noindex" in (p.meta.get("robots") or ""),"| title",len(p.t),"| desc",len(p.meta["description"]))
    for im in p.imgs:
        if not im.get("alt") or not im.get("width"):print("  IMG issue",im);bad+=1
for u,p in parsed.items():
    for l in p.links:
        if l.startswith(("tel:","http","mailto:")):continue
        path,_,frag=l.partition("#");path=path or u
        if code(path)!=200:print("BROKEN",u,l);bad+=1
        elif frag and frag not in parsed.get(path,P()).ids:print("BAD ANCHOR",u,l);bad+=1
print("dup titles:",len({p.t for p in parsed.values()})!=4,"dup desc:",len({p.meta['description'] for p in parsed.values()})!=4)
for f in ["sitemap.xml","robots.txt","assets/style.css","assets/site.js"]:print(f,code("/"+f))
for f in os.listdir("public/images"):
    if code("/public/images/"+f)!=200:print("missing img",f);bad+=1
for h in open("index.html").read().count('application/ld+json'),:pass
import re
for u,f in pages.items():
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',open(f).read()):json.loads(m)
print("JSON-LD parses OK; problems:",bad)
import re
allh="".join(open(f).read() for f in pages.values())
print("branch/office mentions:",re.findall(r"(?i)(?:branch|office)[^<.]{0,60}(?:kerala|bengaluru)",allh))
hm=open("index.html").read()
print("home H1 ok:","Water Treatment Solutions Across Tamil Nadu</h1>" in hm, "| support text ok:","Complete water treatment solutions, from plant manufacturing and installation to operation, staff training, and ongoing maintenance." in hm)
print("cards on home:",hm.count('class="card pc'),"| service sections:",open("services/index.html").read().count('class="svc"'))
print("phone intact:", all("+91 99948 85701" in open(f).read() or "+919994885701" in open(f).read() for f in pages.values()))
