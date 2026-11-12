# Course hub. Run: python3 build_hub.py  ->  ../index.html
import os, re
H = os.path.dirname(os.path.abspath(__file__))
n = lambda s: f'<span class="n">{s}</span>'
# the recordings of each meeting: (YouTube id or '' until it is uploaded, label)
REC = {1: [('esIJkot7pak', 'חלק א׳: עד ההפסקה'), ('c-G8rGVlHvk', 'חלק ב׳: אחרי ההפסקה')]}


def rec(k, date='5.11.2026'):
    items = ''
    for v, lab in REC.get(k, []):
        inner = (f'<iframe src="https://www.youtube-nocookie.com/embed/{v}" title="הקלטת מפגש {k}, {lab}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
                 if v else '<div class="recwait"><span class="play">▶</span><b>הקלטת השיעור</b><span>תעלה כאן בקרוב</span></div>')
        items += f'<div class="recone"><div class="reclab">{lab}</div><div class="recbox">{inner}</div></div>'
    return f'<div class="rec1" id="rec-{k}"><h4>הקלטת המפגש, {n(date)}</h4><div class="recrow">{items}</div></div>'


def rec_wait(k, date):
    """A large placeholder until the recording of the meeting is uploaded (Shay, 2026-11-12)."""
    return (f'<div class="rec1" id="rec-{k}"><h4>הקלטת המפגש, {n(date)}</h4><div class="recbig"><div class="rb-in"><span class="rb-play">▶</span>'
            f'<b>הקלטת השיעור</b><span>תועלה כאן אחרי השיעור</span></div></div></div>')


UP = [(3, 'ניתוח דוחות באמצעות יחסים פיננסיים: נזילות, איתנות, יעילות ורווחיות'), (4, 'יסודות המימון: ריבית וערך הזמן של הכסף'), (5, 'ריבית נומינלית, אפקטיבית וריאלית, והחלטות השקעה'), (6, 'לוחות שפיצר ומימון בתנאי אינפלציה'), (7, 'סיכום וחזרה לקראת הבחינה')]
D = open(os.path.join(H, '..', 'lectures', 'lecture-1', 'presentation.html'), encoding='utf8').read()
D2 = open(os.path.join(H, '..', 'lectures', 'lecture-2', 'presentation.html'), encoding='utf8').read()
D3 = open(os.path.join(H, '..', 'lectures', 'lecture-3', 'presentation.html'), encoding='utf8').read()
NS3, NX3 = D3.count('<section class="slide'), D3.count('act xlq')
NS2, NX2 = D2.count('<section class="slide'), D2.count('act xlq')
NS, NX, NM = D.count('<section class="slide'), D.count('act xlq'), D.count('class="mc"')
NB = len(re.findall(r"^E\('", open(os.path.join(H, 'booklet.py'), encoding='utf8').read(), re.M))
_ns = {}
exec(open(os.path.join(H, 'booklet.py'), encoding='utf8').read(), _ns)
MEET, MEET_T = _ns['MEET'], _ns['MEET_T']

MAPNOTE = ' · '.join(f'אחרי מפגש {n(m)}: ' + ', '.join(n(i) for i in ids) for m, ids in MEET.items())


def bk(m):
    """The part of the exercise booklet that belongs to meeting m: only exercises on what that meeting taught."""
    ids = MEET[m]
    lst = ', '.join(n(i) for i in ids)
    return (f'<div class="grp bkm"><h5>{"4" if m < 3 else "2"}. חוברת התרגילים: רק מה שנלמד במפגש {m}</h5><p class="bkl">תרגילים {lst} מהחוברת. אלה כל התרגילים שאפשר לפתור עכשיו; כל השאר מחכים למפגשים הבאים.</p><div class="links">'
            f'<a class="lk s" href="materials/booklet-m{m}.pdf" target="_blank" rel="noopener"><span class="e">📘</span><span><b>התרגילים של מפגש {m} (PDF)</b><span class="d">{n(len(ids))} תרגילים, השאלה המלאה של כל אחד.</span></span></a>'
            f'<a class="lk x" href="materials/booklet-m{m}-practice.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול שלהם (Excel)</b><span class="d">גיליון לכל תרגיל, תאים צהובים ריקים לנוסחאות.</span></span></a>'
            f'<a class="lk r" href="materials/booklet-m{m}-solutions.pdf" target="_blank" rel="noopener"><span class="e">✅</span><span><b>הפתרונות שלהם (PDF)</b><span class="d">הנוסחה בכל תא, התוצאה והמסקנה.</span></span></a>'
            f'<a class="lk r" href="materials/booklet-m{m}-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות שלהם (Excel)</b><span class="d">אותם גיליונות, עם נוסחאות חיות.</span></span></a>'
            '</div></div>')
ups = ''.join(f'<li><span class="un">{n(i if isinstance(i, int) else i.replace(" ו-", "-").replace(" עד ", "-"))}</span><span>{t}</span><em>בקרוב</em></li>' for i, t in UP)
src = open(os.path.join(H, '..', '..', 'finance-for-managers', 'index.html'), encoding='utf8').read()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
css += '''
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
.cnote{font-size:15px;color:var(--mut);margin-top:8px}
.bkm .bkl{font-size:15.5px;color:var(--ink2);margin:-2px 0 8px}
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
.draft{display:inline-block;background:#fff0d2;border:1.5px dashed #a86703;color:#7a4a00;border-radius:8px;padding:0 8px;font-size:15px;vertical-align:middle;margin-right:6px}.rec1{margin-top:18px}.recbig{position:relative;aspect-ratio:16/9;width:100%;border-radius:18px;overflow:hidden;background:radial-gradient(circle at 30% 20%,#3b5fa8,#16213a 70%);box-shadow:0 10px 26px rgba(15,27,51,.22);display:grid;place-items:center}.rb-in{display:flex;flex-direction:column;align-items:center;gap:8px;color:#d6e0f7;text-align:center}.rb-play{width:86px;height:86px;border-radius:50%;background:rgba(255,255,255,.16);border:2px solid rgba(255,255,255,.4);display:grid;place-items:center;font-size:34px;color:#fff;direction:ltr}.rb-in b{color:#fff;font-size:24px}.rb-in span:last-child{font-size:18px;color:#ffd37a;font-weight:700}.rec1 h4{margin-bottom:8px}.recrow{display:flex;gap:12px;flex-wrap:wrap}.recone{flex:1 1 220px;min-width:0;margin-bottom:12px}.reclab{font-size:15px;font-weight:700;color:var(--navy2);margin-bottom:5px}
.recbox{position:relative;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:linear-gradient(150deg,#0f1b33,#27447f);box-shadow:0 6px 18px rgba(15,27,51,.18)}
.recbox iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.recwait{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;color:#d6e0f7;text-align:center;font-size:15px}
.recwait .play{width:54px;height:54px;border-radius:50%;background:rgba(255,255,255,.14);display:grid;place-items:center;font-size:22px;color:#fff;margin-bottom:6px;direction:ltr}
.recwait b{color:#fff;font-size:17px}
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
<p class="lead">הקורס עוסק בקריאה ובניתוח של דוחות כספיים, וביסודות המימון: ריבית, ערך הזמן של הכסף, הלוואות והחלטות השקעה. לכל מפגש באתר: מצגת אינטראקטיבית עם גיליונות Excel חיים שבודקים את הנוסחה שלכם, סיכום כתוב וקובץ תרגול. חוברת תרגילים לכל שבעת נושאי הקורס, עם פתרונות, נמצאת בקובצי הקורס.</p>
<p class="meta">ד״ר שי צבאן · קוד הקורס {n('432348')}</p>
</div></header>
<main class="wrap">
<section class="contact" id="contact" style="margin-top:-26px;position:relative;z-index:2">
<div class="ic">✉️</div>
<div><h2>פניות לד״ר שי צבאן במייל: <a href="mailto:shay.tsaban@gmail.com">shay.tsaban@gmail.com</a></h2>
<p><b>חובה לרשום בכל פנייה את שם המוסד ואת שם הקורס.</b></p></div>
</section>
<section class="block" id="course-files">
<h2 class="sec">קובצי הקורס</h2>
<div class="cgrid">
<a class="lk s" href="materials/syllabus.pdf" target="_blank" rel="noopener"><span class="e">📋</span><span><b>סילבוס הקורס (PDF)</b><span class="d">שבעת נושאי הקורס, שנלמדים ב-13 מפגשים, קריאה, מדיניות הקורס, והציון: מבחן מסכם, {n('100%')}.</span></span></a>
<a class="lk s" href="materials/booklet.pdf" target="_blank" rel="noopener"><span class="e">📘</span><span><b>חוברת תרגילים (PDF)</b><span class="d">{n(NB)} תרגילים לכל הקורס, מסודרים לפי שבעת הנושאים. ליד כל מפגש למטה: רק התרגילים שלו, בקובץ נפרד.</span></span></a>
<a class="lk x" href="materials/booklet-practice.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של החוברת (Excel)</b><span class="d">גיליון לכל תרגיל: הנתונים בתאים כחולים, ותאים צהובים ריקים לנוסחאות שלכם.</span></span></a>
<a class="lk r" href="materials/booklet-solutions.pdf" target="_blank" rel="noopener"><span class="e">✅</span><span><b>פתרונות החוברת (PDF)</b><span class="d">לכל תרגיל: הנוסחה בכל תא, התוצאה והמסקנה. פותחים רק אחרי שפותרים.</span></span></a>
<a class="lk r" href="materials/booklet-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות של החוברת (Excel)</b><span class="d">אותם גיליונות, עם נוסחאות חיות.</span></span></a>
</div>
<p class="cnote">מדיניות בינה מלאכותית: היתר מלא. חובה לבדוק את אמינות התוצרים, לציין את השימוש, ולמלא טופס הצהרה באתר הקורס. פתרונות החוברת מתפרסמים לצד התרגילים. כדאי לפתור קודם לבד.</p>
<p class="cnote"><b>מה מתרגלים אחרי כל מפגש?</b> {MAPNOTE}. התרגילים האחרים בחוברת מחכים למפגשים הבאים.</p>
</section>
<section class="block">
<h2 class="sec">המפגשים</h2>
<article class="lec" id="lesson-1">
<div class="lec-head"><div class="lec-n">1</div><div><h3>מבוא: חשבונאות פיננסית ומידע לקבלת החלטות</h3><div class="sub">מפגש {n(1)} · {n("5.11.2026")}</div></div></div>
<div class="lec-body">
<div><h4>מה לומדים בשיעור</h4><ul class="learn">
<li>מה צריך לדעת על חברה: הכנסות, הוצאות ורווח</li>
<li>דוח רווח והפסד, שורה אחר שורה, וסיווג הוצאות לקטגוריות</li>
<li>בסיס מצטבר: מתי נרשמת הכנסה</li>
<li>הדוח על המצב הכספי: נכסים והתחייבויות שוטפים ולא שוטפים, והון עצמי כמקור מימון</li>
<li>תרגול עצמי: עשרה תרגולים, כל אחד עם גיליון, רמזים, פתרון צעד אחר צעד וכפתור ״הסבר נוסף״</li>
</ul>{rec(1)}</div>
<div><h4>חומרי השיעור</h4>
<div class="grp"><h5>1. בשיעור</h5><div class="links">
<a class="lk p" href="lectures/lecture-1/presentation.html"><span class="e">🖥️</span><span><b>מצגת השיעור</b><span class="d">{n(NS)} שקפים, וגיליון Excel חי ליד כל שאלה ({n(NX)} גיליונות), עם בדיקה, רמזים ופתרון צעד אחר צעד.</span></span></a>
</div></div>
<div class="grp"><h5>2. אחרי השיעור, לחזרה</h5><div class="links">
<a class="lk s" href="lectures/lecture-1/summary.pdf"><span class="e">📄</span><span><b>סיכום השיעור (PDF)</b><span class="d">כל תוכן המצגת במסמך אחד: הגדרות, השאלות והפתרון שלהן בגיליון, ומילון מושגים.</span></span></a>
</div></div>
<div class="grp"><h5>3. תרגול</h5><div class="links">
<a class="lk x" href="materials/practice-1.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של מפגש 1 (Excel)</b><span class="d">כל {n(NX)} השאלות של המצגת, באותן כתובות תאים. התאים הצהובים ריקים: כותבים בהם את הנוסחאות.</span></span></a>
<a class="lk r" href="materials/practice-1-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות של מפגש 1 (Excel)</b><span class="d">אותם גיליונות עם נוסחאות חיות. פותחים רק אחרי שפותרים.</span></span></a>
</div></div>
{bk(1)}
</div>
</div>
<div class="todo"><h4>📝 מה עושים בשיעור {n(1)}</h4><ol>
<li><b>בשיעור:</b> עובדים במצגת, בגיליונות שבתוך השקפים.</li>
<li><b>אחרי השיעור:</b> קוראים את הסיכום, ופותרים בקובץ התרגול את כל השאלות של המצגת. אחר כך בודקים בקובץ הפתרונות.</li>
<li><b>מהחוברת:</b> התרגילים של מפגש 1 ({', '.join(n(i) for i in MEET[1])}), בקובץ הנפרד שלמעלה, ובדיקה מול הפתרונות שלהם.</li>
</ol></div>
</article>
<article class="lec" id="lesson-2">
<div class="lec-head"><div class="lec-n">2</div><div><h3>הזהות החשבונאית: כל עסקה בטבלה אחת</h3><div class="sub">מפגש {n(2)} · {n("12.11.2026")}</div></div></div>
<div class="lec-body">
<div><h4>מה לומדים בשיעור</h4><ul class="learn">
<li>רענון של מפגש 1: פעילות, רווח והפסד, ומאזן</li>
<li>בשביל מי הדוחות, מה הופך מידע לשימושי, ומי מחייב לערוך אותם</li>
<li>לכל נכס יש מקור מימון: הזהות החשבונאית</li>
<li>טבלת הזהות: עמודה לכל חשבון, והכנסות והוצאות בתוך ההון העצמי</li>
<li>עסקאות שנוגעות רק במאזן, ועסקאות של הכנסות והוצאות</li>
<li>תרגול עצמי: גלידריית תמר, שנה שלמה בטבלת הזהות, בשלושה שלבים עם פתרון מלא</li>
</ul>{rec_wait(2, "12.11.2026")}</div>
<div><h4>חומרי השיעור</h4>
<div class="grp"><h5>1. בשיעור</h5><div class="links">
<a class="lk p" href="lectures/lecture-2/presentation.html"><span class="e">🖥️</span><span><b>מצגת השיעור</b><span class="d">{n(NS2)} שקפים, וגיליון Excel חי ליד כל שאלה ({n(NX2)} גיליונות), עם בדיקה, רמזים ופתרון צעד אחר צעד.</span></span></a>
</div></div>
<div class="grp"><h5>2. אחרי השיעור, לחזרה</h5><div class="links">
<a class="lk s" href="lectures/lecture-2/summary.pdf"><span class="e">📄</span><span><b>סיכום השיעור (PDF)</b><span class="d">כל תוכן המצגת במסמך אחד: הגדרות, טבלאות הזהות והפתרון שלהן בגיליון, ומילון מושגים.</span></span></a>
</div></div>
<div class="grp"><h5>3. תרגול</h5><div class="links">
<a class="lk x" href="materials/practice-2.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של מפגש 2 (Excel)</b><span class="d">כל {n(NX2)} השאלות של המצגת, באותן כתובות תאים. התאים הצהובים ריקים.</span></span></a>
<a class="lk r" href="materials/practice-2-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות של מפגש 2 (Excel)</b><span class="d">אותם גיליונות עם נוסחאות חיות. פותחים רק אחרי שפותרים.</span></span></a>
</div></div>
{bk(2)}
</div>
</div>
<div class="todo"><h4>📝 מה עושים בשיעור {n(2)}</h4><ol>
<li><b>בשיעור:</b> רושמים כל עסקה בטבלת הזהות שבתוך השקף. הגענו עד סוף חלק 4, שקף 47.</li>
<li><b>אחרי השיעור:</b> קוראים את הסיכום, ופותרים לבד את התרגיל של גלידריית תמר (חלק 5 במצגת, ובקובץ התרגול). אחר כך בודקים בקובץ הפתרונות.</li>
<li><b>מהחוברת:</b> התרגילים של מפגש 2 ({', '.join(n(i) for i in MEET[2])}), בקובץ הנפרד שלמעלה. מהטבלה לדוחות ממשיכים במפגש 3.</li>
</ol></div>
</article>
<article class="lec" id="lesson-3">
<div class="lec-head"><div class="lec-n">3</div><div><h3>מהזהות לדוחות, וארבעת הדוחות <span class="draft">טיוטה</span></h3><div class="sub">מפגש {n(3)}</div></div></div>
<div class="lec-body">
<div><h4>מה לומדים בשיעור</h4><ul class="learn">
<li>רענון של מפגש 2, ומהטבלה לדוחות: סיכום העמודות, דוח רווח והפסד ומאזן</li>
<li>תרגיל מלא, מהזהות ועד הדוחות: מעבדת התיקונים של עומר</li>
<li>מי כותב את הכללים ומי בודק: תקני דיווח, חוקים, מאי״ה וביקורת</li>
<li>הדוח על השינויים בהון, ודיבידנד</li>
<li>הדוח על תזרימי המזומנים: שוטפת, השקעה ומימון, ולמה מזומן אינו רווח</li>
<li>שלושה גשרים בין הדוחות, ודוחות אמיתיים במאי״ה</li>
</ul></div>
<div><h4>חומרי השיעור</h4>
<div class="grp"><h5>טיוטה</h5><div class="links">
<a class="lk p" href="lectures/lecture-3/presentation.html"><span class="e">🖥️</span><span><b>מצגת השיעור (טיוטה)</b><span class="d">{n(NS3)} שקפים, {n(NX3)} גיליונות Excel חיים.</span></span></a>
<a class="lk s" href="lectures/lecture-3/summary.pdf"><span class="e">📄</span><span><b>סיכום השיעור (טיוטה, PDF)</b><span class="d">כל תוכן המצגת במסמך אחד.</span></span></a>
<a class="lk x" href="materials/practice-3.xlsx" download><span class="e">📊</span><span><b>קובץ התרגול של מפגש 3 (Excel, טיוטה)</b><span class="d">השאלות של המצגת, באותן כתובות תאים.</span></span></a>
<a class="lk r" href="materials/practice-3-solutions.xlsx" download><span class="e">✅</span><span><b>קובץ הפתרונות של מפגש 3 (Excel, טיוטה)</b><span class="d">אותם גיליונות עם נוסחאות חיות.</span></span></a>
</div></div>
{bk(3)}
</div>
</div>
</article>
<h2 class="sec" style="margin-top:36px">הנושאים הבאים</h2>
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
