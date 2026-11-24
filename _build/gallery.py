# Part of the 432348 build kit (2026-11-24): usage python3 gallery.py deck.html outdir. # All slides of a deck on one page, every reveal shown and every question answered, in ONE Chrome run; sliced into contact sheets.
import os, subprocess, sys, tempfile
from PIL import Image
SRC, OUT = sys.argv[1], sys.argv[2]
COLS = 4
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
src = open(SRC, encoding='utf8').read()
n = src.count('<section class="slide')
rows = (n + COLS - 1) // COLS
Z = 0.3
W, H = int(COLS * 1310 * Z) + 20, int(rows * 750 * Z) + 40
JS = '''<style>*{transition:none!important;animation:none!important}
body.gal{overflow:visible!important;height:auto!important;background:#333!important}
body.gal #stage{transform:none!important;position:absolute!important;left:0!important;top:0!important;width:auto!important;height:auto!important;display:grid!important;grid-template-columns:repeat(%d,1280px);gap:30px;zoom:%s;margin:0!important}
body.gal .slide{position:relative!important;inset:auto!important;visibility:visible!important;opacity:1!important;transform:none!important;width:1280px!important;height:720px!important;overflow:hidden!important}
body.gal .slide::before{content:attr(data-n);position:absolute;top:4px;left:8px;z-index:99;background:#e0454f;color:#fff;font:700 30px sans-serif;padding:2px 10px;border-radius:6px}
</style><script>setTimeout(function(){(document.fonts?document.fonts.ready:Promise.resolve()).then(function(){
 window.__autofit&&window.__autofit();
 document.querySelectorAll('.slide').forEach(function(s,i){s.setAttribute('data-n',(i+1)+' '+s.id);});
 document.querySelectorAll('.st').forEach(function(e){e.classList.add('show');});
 document.querySelectorAll('.mc').forEach(function(m){m.classList.add('done');var o=m.querySelectorAll('.o')[+m.dataset.a];o&&o.classList.add('ok');});
 document.body.classList.add('gal');});},1200);</script></body>''' % (COLS, Z)
d = tempfile.mkdtemp()
p = os.path.join(d, 'g.html')
open(p, 'w', encoding='utf8').write(src.replace('</body>', JS))
png = os.path.join(d, 'g.png')
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/prof', f'--window-size={W},{H}', '--virtual-time-budget=15000', '--hide-scrollbars', f'--screenshot={png}', 'file://' + p], capture_output=True, timeout=900)
im = Image.open(png).convert('RGB')
os.makedirs(OUT, exist_ok=True)
sh = int(750 * Z)
per = 3   # rows per contact sheet
k = 0
for r0 in range(0, rows, per):
    im.crop((0, r0 * sh, W, min(H, (r0 + per) * sh + 10))).save(os.path.join(OUT, f'g{k:02d}.png')); k += 1
print(n, 'slides', k, 'sheets', im.size)
