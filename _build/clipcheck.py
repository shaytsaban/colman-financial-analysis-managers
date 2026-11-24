# Part of the 432348 build kit (2026-11-24): table cells whose content is wider than the cell (a cut number), every reveal shown.
# Usage: python3 clipcheck.py deck.html
import json, os, re, subprocess, sys, tempfile, html as hh
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
JS = r'''(document.fonts?document.fonts.ready:Promise.resolve()).then(function(){setTimeout(function(){
 window.__autofit&&window.__autofit();const out=[];
 document.querySelectorAll('.slide').forEach(function(s,i){s.querySelectorAll('.st').forEach(function(e){e.classList.add('show');});
  s.querySelectorAll('.mc').forEach(function(m){m.classList.add('done');});
  s.querySelectorAll('td,th').forEach(function(c){if(c.closest('.xl-g'))return;if(c.offsetParent&&c.scrollWidth>c.clientWidth)out.push({i:i+1,id:s.id,t:c.textContent.trim().slice(0,30),sw:c.scrollWidth,cw:c.clientWidth});});});
 document.documentElement.setAttribute('data-clip',JSON.stringify(out));},800);});'''
src = open(sys.argv[1], encoding='utf8').read()
d = tempfile.mkdtemp(); p = os.path.join(d, 't.html')
open(p, 'w', encoding='utf8').write(src.replace('</body>', '<script>' + JS + '</script></body>'))
r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/prof', '--window-size=1280,764', '--virtual-time-budget=30000', '--dump-dom', 'file://' + p], capture_output=True, text=True, timeout=900)
m = re.search(r'data-clip="([^"]*)"', r.stdout)
rows = json.loads(hh.unescape(m.group(1))) if m else None
print('clipped cells:', 'no result' if rows is None else len(rows))
for x in (rows or [])[:40]: print(x)
