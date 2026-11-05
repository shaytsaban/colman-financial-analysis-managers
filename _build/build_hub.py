# Course hub. Run: python3 build_hub.py  ->  ../index.html
import os, re
H = os.path.dirname(os.path.abspath(__file__))
n = lambda s: f'<span class="n">{s}</span>'
UP = [(2, 'ארבעת הדוחות הכספיים והקשרים ביניהם'), (3, 'ניתוח דוחות באמצעות יחסים פיננסיים: נזילות, איתנות, יעילות ורווחיות'), (4, 'יסודות המימון: ריבית וערך הזמן של הכסף'), (5, 'ריבית נומינלית, אפקטיבית וריאלית, והחלטות השקעה'), (6, 'לוחות שפיצר ומימון בתנאי אינפלציה'), (7, 'סיכום וחזרה לקראת הבחינה')]
D = open(os.path.join(H, '..', 'lectures', 'lecture-1', 'presentation.html'), encoding='utf8').read()
NS, NX, NM = D.count('<section class="slide'), D.count('act xlq'), D.count('class="mc"')
NB = len(re.findall(r"^E\('", open(os.path.join(H, '..', '..', 'colman-financial-analysis-managers-private', 'booklet.py'), encoding='utf8').read(), re.M))
ups = ''.join(f'<li><span class="un">{n(i if isinstance(i, int) else i.replace(" ו-", "-").replace(" עד ", "-"))}</span><span>{t}</span><em>בקרוב</em></li>' for i, t in UP)
src = open(os.path.join(H, '..', '..', 'finance-for-managers', 'index.html'), encoding='utf8').read()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
css += '''
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.cnote{font-size:15px;color:var(--mut);margin-top:8px}
.grp{margin-bottom:14px}.grp h5{font-size:15.5px;font-weight:800;color:var(--navy2);margin:0 0 8px}
@media (max-width:760px){.cgrid{grid-template-columns:1fr}}
.contact{margin-top:14px;background:#fff7e0;border:2px solid #f0b429;border-radius:18px;padding:16px 24px;display:flex;gap:16px;align-items:center}
.contact .ic{font-size:34px;flex:none}
.contact h2{font-size:20px;font-weight:800;line-height:1.3;color:var(--navy2)}
.contact h2 a{direction:ltr;unicode-bidi:isolate;display:inline-block;text-decoration:underline;overflow-wrap:anywhere}
.contact p{font-size:16.5px;line-height:1.45;margin-top:3px;color:#4a4130}
@media (max-width:760px){.contact{padding:14px 16px}.contact .ic{display:none}.contact h2{font-size:18px}}
.live{margin-top:-26px;position:relative;z-index:2;background:linear-gradient(120deg,#ff6a4d,#ff8f5a);color:#fff;border-radius:20px;padding:22px 28px;display:flex;gap:20px;align-items:center;box-shadow:0 14px 34px rgba(255,106,77,.35)}
.live .ic{font-size:44px;flex:none}
.live h2{font-size:26px;font-weight:800;line-height:1.2}
.live p{font-size:16.5px;margin-top:4px;line-height:1.4}
.live p a{text-decoration:underline;font-weight:700}
.live .go{flex:none;margin-right:auto;background:#fff;color:#c4421f;font-weight:800;font-size:19px;padding:14px 26px;border-radius:14px;text-align:center;transition:transform .15s}
.live .go:hover{transform:translateY(-2px)}
.live .go small{display:block;font-weight:600;font-size:13px;color:#5d6a86}
@media (max-width:760px){.live{flex-direction:column;align-items:stretch;padding:20px 18px;margin-top:-18px}.live .ic{display:none}.live .go{margin-right:0}}
.solutions{margin-top:18px;background:#fff;border-radius:20px;padding:24px 28px;display:flex;gap:22px;align-items:flex-start;box-shadow:0 2px 0 var(--line),0 10px 30px rgba(22,33,58,.07);border-right:8px solid #6d4df2}
.solutions .ic{font-size:44px;flex:none}
.solutions h3{font-size:22px;font-weight:800;line-height:1.25}
.solutions .tag{display:inline-block;background:#ece8ff;color:#4f33c9;border-radius:99px;padding:2px 14px;font-weight:700;font-size:14px;margin-bottom:6px}
.solutions p{font-size:16px;color:var(--ink2);margin-top:6px}
.solutions .warn{margin-top:12px;background:#fff7e0;border-right:5px solid #f0b429;border-radius:10px;padding:10px 14px;font-size:15px;color:#4a4130}
.solutions .btn2{flex:none;margin-right:auto;align-self:center;background:#6d4df2;color:#fff;font-weight:800;font-size:17px;padding:12px 22px;border-radius:14px;text-align:center;transition:transform .15s}
.solutions .btn2:hover{transform:translateY(-2px)}
.solutions .btn2 small{display:block;font-weight:500;font-size:13px;opacity:.9}
.lk.x .e{background:#e3f6ea}.lk.r .e{background:#fff0d2}
.todo{margin:0 30px 26px;background:#fff7e0;border:2px solid #f0b429;border-radius:18px;padding:18px 22px}
.todo h4{font-size:18px;color:var(--navy2);margin-bottom:8px}
.todo ol{padding-inline-start:22px;font-size:16px;line-height:1.6}
.ups{list-style:none;margin-top:18px;background:var(--card);border-radius:18px;box-shadow:0 2px 0 var(--line);overflow:hidden}
.ups li{display:flex;gap:14px;align-items:center;padding:11px 22px;border-bottom:1px solid var(--line);font-size:16.5px;font-weight:600}
.ups li:last-child{border:0}
.ups .un{flex:none;min-width:34px;padding:0 6px;white-space:nowrap;height:34px;border-radius:10px;background:#eef0f6;color:var(--navy2);display:grid;place-items:center;font-weight:800}
.ups em{margin-right:auto;font-style:normal;color:var(--mut);font-size:14px;font-weight:500}
@media (max-width:760px){.solutions{flex-direction:column;padding:20px 18px}.solutions .btn2{margin-right:0;width:100%}.todo{margin:0 18px 22px;padding:14px 16px}.ups li{padding:10px 14px}}
'''
page = f'''<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>מימון וניתוח פיננסי למנהלים | אתר הקורס</title>
<meta name="description" content="אתר הקורס מימון וניתוח פיננסי למנהלים, המסלול האקדמי של המכללה למנהל: מצגות אינטראקטיביות עם גיליונות Excel חיים, סיכומים, חוברת תרגילים וקובצי תרגול.">
<link rel="stylesheet" href="assets/fonts.css">
<style>{css}</style>
</head>
<body>
<header class="hero"><div class="wrap">
<div class="kick"><span>המסלול האקדמי של המכללה למנהל · בית הספר לתקשורת וניהול · סמסטר א׳ תשפ״ז</span></div>
<h1>מימון וניתוח פיננסי למנהלים</h1>
<p class="lead">הקורס עוסק בקריאה ובניתוח של דוחות כספיים, וביסודות המימון: ריבית, ערך הזמן של הכסף, הלוואות והחלטות השקעה. לכל שיעור באתר: מצגת אינטראקטיבית עם גיליונות Excel חיים שבודקים את הנוסחה שלכם, סיכום כתוב וקובץ תרגול. חוברת תרגילים לכל שבעת השיעורים נמצאת בקובצי הקורס.</p>
<p class="meta">ד״ר שי צבאן · קוד הקורס {n('432348')}</p>
</div></header>
<main class="wrap">
<section class="contact" id="contact" style="margin-top:-26px;position:relative;z-index:2">
<div class="ic">✉️</div>
<div><h2>פניות לד״ר שי צבאן במייל: <a href="mailto:shay.tsaban@gmail.com">shay.tsaban@gmail.com</a></h2>
<p><b>חובה לרשום בכל פנייה את שם המוסד ואת שם הקורס.</b> שעת קבלה: יום א׳, {n('20:00')} עד {n('21:00')}, ב-Zoom, בתיאום מראש.</p></div>
</section>
<section class="block" id="course-files">
<h2 class="sec">קובצי הקורס</h2>
<div class="cgrid">
<a class="lk s" href="materials/syllabus.pdf" target="_blank" rel="noopener"><span class="e">📋</span><span><b>סילבוס הקורס (PDF)</b><span class="d">נושאי שבעת המפגשים, קריאה, מדיניות הקורס, והציון: מבחן מסכם, {n('100%')}.</span></span></a>
<a class="lk s" href="materials/booklet.pdf" target="_blank" rel="noopener"><span class="e">📘</span><span><b>חוברת תרגילים (PDF)</b><span class="d">{n(NB)} תרגילים, לפי שיעור, לכל שבעת המפגשים. החוברת היא הערכה לפי הסילבוס, ותתעדכן לפי ההתקדמות.</span></span></a>
<a class="lk x" href="materials/booklet-practice.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של החוברת (Excel)</b><span class="d">גיליון לכל תרגיל: הנתונים בתאים כחולים, ותאים צהובים ריקים לנוסחאות שלכם.</span></span></a>
</div>
<p class="cnote">מדיניות בינה מלאכותית: היתר מלא. חובה לבדוק את אמינות התוצרים, לציין את השימוש, ולמלא טופס הצהרה באתר הקורס. הפתרונות של החוברת אינם מתפרסמים: שאלות על תרגיל בשעת הקבלה או במייל.</p>
</section>
<section class="block">
<h2 class="sec">השיעורים</h2>
<article class="lec" id="lesson-1">
<div class="lec-head"><div class="lec-n">1</div><div><h3>מבוא: חשבונאות פיננסית ומידע לקבלת החלטות</h3><div class="sub">מפגש {n(1)}</div></div></div>
<div class="lec-body">
<div><h4>מה לומדים בשיעור</h4><ul class="learn">
<li>מה צריך לדעת על חברה: הכנסות, הוצאות ורווח</li>
<li>דוח רווח והפסד, שורה אחר שורה, וסיווג הוצאות לקטגוריות</li>
<li>הדוח על המצב הכספי: נכסים והתחייבויות שוטפים ולא שוטפים, והון עצמי כמקור מימון</li>
<li>מי משתמש בדוחות: משקיעים ונושים, ומעגל שני</li>
<li>מי מחייב לדווח: חברה פרטית וציבורית, חוק, תקינה וביקורת</li>
<li>משוואת המאזן, עסקה אחר עסקה, ותרגול בניית דוחות מרשימת פריטים</li>
</ul></div>
<div><h4>חומרי השיעור</h4>
<div class="grp"><h5>1. בשיעור</h5><div class="links">
<a class="lk p" href="lectures/lecture-1/presentation.html"><span class="e">🖥️</span><span><b>מצגת השיעור</b><span class="d">{n(NS)} שקפים, וגיליון Excel חי ליד כל שאלה ({n(NX)} גיליונות), עם בדיקה, רמזים ופתרון צעד אחר צעד.</span></span></a>
</div></div>
<div class="grp"><h5>2. אחרי השיעור, לחזרה</h5><div class="links">
<a class="lk s" href="lectures/lecture-1/summary.pdf"><span class="e">📄</span><span><b>סיכום השיעור (PDF)</b><span class="d">כל תוכן המצגת במסמך אחד: הגדרות, השאלות והפתרון שלהן בגיליון, ומילון מושגים.</span></span></a>
</div></div>
<div class="grp"><h5>3. תרגול</h5><div class="links">
<a class="lk x" href="materials/practice-1.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של שיעור 1 (Excel)</b><span class="d">כל {n(NX)} השאלות של המצגת, באותן כתובות תאים. התאים הצהובים ריקים: כותבים בהם את הנוסחאות.</span></span></a>
<a class="lk s" href="materials/booklet.pdf" target="_blank" rel="noopener"><span class="e">📘</span><span><b>חוברת התרגילים: שיעור 1</b><span class="d">תרגילים 1-1 עד 1-7 בחוברת, וגיליונות באותם מספרים בקובץ התרגול של החוברת.</span></span></a>
</div></div>
</div>
</div>
<div class="todo"><h4>📝 מה עושים בשיעור {n(1)}</h4><ol>
<li><b>בשיעור:</b> עובדים במצגת, בגיליונות שבתוך השקפים.</li>
<li><b>אחרי השיעור:</b> קוראים את הסיכום, ופותרים בקובץ התרגול את כל השאלות של המצגת.</li>
<li><b>לקראת מפגש 2:</b> תרגילי שיעור 1 בחוברת, וקריאה: Weygandt et al., Ch. 1; Wahlen et al., Ch. 1; Barth et al. (2008).</li>
</ol></div>
</article>
<h2 class="sec" style="margin-top:36px">השיעורים הבאים</h2>
<ul class="ups">{ups}</ul>
</section>
<footer>ד״ר שי צבאן · פניות במייל: <a href="mailto:shay.tsaban@gmail.com">shay.tsaban@gmail.com</a>, עם שם המוסד ושם הקורס</footer>
</main>
</body>
</html>
'''
assert '—' not in page and '־' not in page
open(os.path.join(H, '..', 'index.html'), 'w', encoding='utf8').write(page)
print('hub', len(page))
