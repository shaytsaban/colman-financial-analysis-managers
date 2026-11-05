# Syllabus PDF. Run: python3 build_syllabus.py  ->  ../materials/syllabus.pdf
import html, os, shutil, subprocess, tempfile
H = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(H, '..', '..', 'iit-build', 'fonts')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SITE = 'https://shaytsaban.github.io/colman-financial-analysis-managers/'
NOTE = 'ייתכנו שינויים קלים בתוכן הקורס ובסדר הנושאים במהלך הסמסטר, בהתאם להתקדמות בשיעורים. עדכונים יפורסמו באתר הקורס.'
n = lambda s: f'<span class="n">{s}</span>'
en = lambda s: f'<div class="en">{s}</div>'
he = lambda s: f'<div>{s}</div>'
# topics and readings as in the official syllabus form (432348, 2027 semester A)
L = [('1', 'מבוא', 'מהותה ומטרותיה של החשבונאות הפיננסית, תפקיד המידע החשבונאי בקבלת החלטות, המשתמשים בדוחות הכספיים, ומקורות רגולטוריים המחייבים בדיווח.',
      en('Weygandt et al., Ch. 1; Wahlen et al., Ch. 1; Barth et al. (2008).')),
     ('2', 'הדוחות הכספיים', 'הדוח על המצב הכספי (מאזן): נכסים, התחייבויות והון עצמי, והקשר ביניהם (משוואת המאזן). דוח רווח והפסד: מבנה הדוח ומדידת תוצאות הפעילות. הדוח על השינויים בהון. הדוח על תזרימי המזומנים: פעילות שוטפת, השקעה ומימון. קריאה משולבת של הדוחות והקשרים ביניהם.',
      he('אריה ואח׳ ובניסטי, הפרקים המקבילים.') + en('Weygandt et al., Ch. 2 to 4 and 13; Wahlen et al., Ch. 2 to 3.') + he('דוחות מתוך מאי״ה.')),
     ('3', 'ניתוח דוחות כספיים באמצעות יחסים פיננסיים', 'יחסי נזילות, איתנות, יעילות ורווחיות: חישוב, פרשנות והשוואה בין חברות ובין תקופות. זיהוי מגמות ואיתותי אזהרה בדיווח.',
      he('עדן ושוב, פרקי היחסים הפיננסיים.') + en('Wahlen et al., Ch. 4 to 5; Palepu et al., Ch. 5; Nissim &amp; Penman (2001); Altman (1968).') + he('דוחות מתוך מאי״ה לתרגול השוואתי.')),
     ('4', 'יסודות המימון', 'ריבית וערך הזמן של הכסף, מושג הריבית, ערך עתידי ונוכחי של סכומים בודדים ושל סדרות, כבסיס למהות החישובים הפיננסיים.',
      he('טלמור ושרוני, פרקים 1 עד 3.') + en('Brealey et al., Ch. 2; Berk &amp; DeMarzo, Ch. 4; Benninga &amp; Mofkadi, Ch. 1 to 2.')),
     ('5', 'חישובי ערך: המשך, והחלטות השקעה', 'יישומי ערך נוכחי ועתידי במקרים מורכבים ובהקשר של קבלת החלטות. ריבית נומינלית, אפקטיבית וריאלית, כולל בעיות כלכליות של חילוץ ריבית. בחירה בין השקעות חלופיות באמצעות ערך נוכחי נקי (<span class="n">NPV</span>), שיעור תשואה פנימי (<span class="n">IRR</span>) ותקופת החזר.',
      he('טלמור ושרוני, פרקים 3 עד 5.') + en('Brealey et al., Ch. 2 and 5; Berk &amp; DeMarzo, Ch. 5 and 7; Ross et al., Ch. 4 to 5; Benninga &amp; Mofkadi, Ch. 3; Graham &amp; Harvey (2001).')),
     ('6', 'לוחות שפיצר ומימון בתנאי אינפלציה', 'לוח שפיצר וגרסאותיו: משכנתאות וקצבאות, וקצבת פנסיה. מימון בתנאי אינפלציה: הצמדה וריבית ריאלית. יישום ב-Excel.',
      he('טלמור ושרוני, פרקי לוחות הסילוקין והריבית הריאלית.') + en('Brealey et al., Ch. 3; Berk &amp; DeMarzo, Ch. 5; Benninga &amp; Mofkadi, Ch. 2.')),
     ('7', 'סיכום וחזרה לקראת הבחינה', 'חזרה על נושאי הקורס המרכזיים, פתרון שאלות לדוגמה, ומענה לשאלות.', 'ללא.')]
rows = ''.join(f'<tr{" class=hi" if i == 0 else ""}><td class="c">{n(k)}</td><td><b>{t}</b><div class="w">{w}</div></td><td class="rd">{r}</td></tr>' for i, (k, t, w, r) in enumerate(L))
OUT = ['קריאת דוחות כספיים, הסבר הקשרים בין הדוחות, והגדרת רכיבי היסוד בדיווח הכספי: נכסים, התחייבויות, הון עצמי, הכנסות והוצאות.',
       'חישוב יחסים פיננסיים (נזילות, איתנות, יעילות ורווחיות) ופרשנותם, לצורך הערכת מצבה הפיננסי של חברה.',
       'זיהוי מגמות ואיתותי אזהרה בדיווחים הכספיים, והשוואה בין חברות ובין תקופות דיווח.',
       'חישוב ריבית נומינלית, אפקטיבית וריאלית, והשוואה בין חלופות מימון על בסיס עלותן האפקטיבית.',
       'בניית תזרימי מזומנים לתוכניות השקעה ולמודלים עסקיים, ויישום תחשיבי כדאיות המתבססים על מהות ערכן הנוכחי.',
       'בחירה מבין השקעות חלופיות של ההשקעה העדיפה כלכלית, באמצעות קריטריונים כמותיים.',
       'בניית לוחות סילוקין (שפיצר) להלוואות, וחישוב תשלומי הלוואה, משכנתאות וקצבאות.',
       'שימוש ב-Excel לביצוע חישובים פיננסיים.']
body = f"""
<div class="hd"><div class="k">המסלול האקדמי של המכללה למנהל · בית הספר לתקשורת וניהול · סמסטר א׳ תשפ״ז</div><h1 class="t">מימון וניתוח פיננסי למנהלים</h1><div class="s">סילבוס הקורס · <span class="en2">Financial Statements Analysis</span></div></div>
<table class="meta"><tr><td>קוד הקורס</td><td>{n('432348')}</td></tr><tr><td>היקף</td><td>{n('2')} נקודות זכות, {n('3')} שעות שבועיות, {n('13')} מפגשים</td></tr>
<tr><td>שנה וסמסטר</td><td>{n('2027')}, סמסטר א׳ (תשפ״ז)</td></tr>
<tr><td>מרצה</td><td>ד״ר שי צבאן, {n('shay.tsaban@gmail.com')}</td></tr>
<tr><td>אתר הקורס</td><td><span class="url">{SITE}</span></td></tr></table>
<h3>תיאור הקורס ומטרותיו</h3>
<p>הקורס נועד להקנות למשתתפים בסיס של ידע וכלים אנליטיים הדרושים לעוסקים בתחום הפיננסי, תוך הצגת ההיבטים המרכזיים של ניתוח דוחות כספיים ומימון.</p>
<p><b>חלק א׳: קריאה וניתוח של דוחות כספיים.</b> תחילה נעסוק במבנה הדוחות הכספיים: נכיר את ארבעת הדוחות הכספיים שחברות בכל ענפי המשק מחויבות לפרסם באופן תקופתי, בהתאם לכללי חשבונאות מקובלים (<span class="n">GAAP</span>) ולתקני הדיווח הכספי הבינלאומיים (<span class="n">IFRS</span>): הדוח על המצב הכספי (מאזן), דוח רווח או הפסד, הדוח על השינויים בהון העצמי, והדוח על תזרימי המזומנים, בחלוקה לפעילות שוטפת, פעילות השקעה ופעילות מימון. לאחר מכן נציג עקרונות ועיקרים בניתוח דוחות כספיים: יחסי נזילות; יחסי פעילות ויעילות, הבוחנים את התנהלות החברה מול ספקים ולקוחות ואת ניצול המלאי; יחסי איתנות פיננסית, הבוחנים את מבנה ההון וחוסנו של החברה לטווח הארוך; ויחסי רווחיות, הבוחנים את יכולת החברה להפיק רווחים מהכנסותיה, מנכסיה ומהונה.</p>
<p><b>חלק ב׳: מימון.</b> בחלק זה יוגדרו מושגי היסוד במימון: ריבית, שווי, ערך הזמן של הכסף, ועיתוי תזרימי המזומנים. מושגים אלה ישמשו בסיס להכרת שיטות כמותיות לחישוב שווי של נכסים ולקבלת החלטות השקעה בתנאי ודאות. כן ייבחנו היבטים מרכזיים של חישובים פיננסיים: חישובי הלוואות, סוגי ריביות (נומינלית, אפקטיבית, ריאלית), חישוב תזרימי מזומנים, וערכים רלוונטיים לקבלת החלטות.</p>
<h3>שיטת ההוראה</h3>
<p>הרצאות פרונטליות, שבהן שזורים דיונים ותרגילים. לכל מפגש באתר הקורס: מצגת אינטראקטיבית עם גיליונות Excel חיים, סיכום כתוב וקובץ תרגול. חוברת תרגילים לכל שבעת נושאי הקורס, עם פתרונות מלאים, מתפרסמת באתר.</p>
<h3>תוצרי למידה: בסוף הקורס הסטודנטים ידעו</h3>
<ol>{''.join(f'<li>{x}</li>' for x in OUT)}</ol>
<h3>תוכנית הקורס וקריאה</h3>
<p>הקורס נמשך {n(13)} מפגשים. הטבלה מציגה את שבעת הנושאים של הקורס, לפי הסדר. נושא יכול להימשך יותר ממפגש אחד.</p>
<table class="plan"><thead><tr><th>נושא</th><th>תוכן</th><th>חומר קריאה</th></tr></thead><tbody>{rows}</tbody></table>
<div class="note">{NOTE}</div>
<h3>מרכיבי הציון</h3>
<table class="meta"><tr><td>מבחן</td><td>{n('100%')} מהציון הסופי. מבחן מסכם על כלל נושאי הקורס.</td></tr></table>
<h3>מדיניות השימוש בבינה מלאכותית</h3>
<p><b>היתר מלא:</b> בקורס זה אנו מעודדים שימוש בבינה מלאכותית בכל המטלות. על הסטודנט לבדוק את אמינות התוצרים, לאזכרם בעבודה, ולמלא טופס הצהרה באתר הקורס. הפרת מדיניות זו היא עבירת משמעת.</p>
<h3>מדיניות המרצה</h3>
<ul><li>אין חובת נוכחות בקורס זה.</li><li>אין איחורים: הכניסה מותרת עד {n(15)} דקות אחרי תחילת השיעור. לאחר מכן לא תתאפשר כניסה לשיעור.</li>
<li>השימוש בטלפונים סלולריים במהלך השיעור אסור. סטודנט שישתמש בטלפון במהלך השיעור יידרש לעזוב את הכיתה.</li><li>לא תתקבל הגשה מאוחרת של מטלות ועבודות.</li></ul>
<h3>רשימה ביבליוגרפית</h3>
<p><b>פריטי קריאה בעברית:</b></p><ul>
<li>טלמור, א׳ ושרוני, א׳ ({n(2006)}). <i>יסודות המימון: תיאוריה, תרגילים ופתרונות</i>, מהדורה שלישית מורחבת. דיונון.</li>
<li>עדן, י׳ ושוב, ש׳ ({n(2019)}). <i>ניתוח דוחות כספיים והערכות שווי</i>, מהדורה שנייה מעודכנת. הוצאת IFRS.</li>
<li>אריה, ג׳, ימפולר, א׳ וקונצקי, י׳ ({n(2010)}). <i>חשבונאות בעסקים מעודכן IFRS</i>, מהדורה {n(12)}. דיונון.</li>
<li>בניסטי, ג׳ ({n(2010)}). <i>חשבונאות פיננסית: תיאוריה ויישומים, עידן התקינה הבינלאומית (IFRS)</i>. פלס.</li>
<li>דוחות כספיים של חברות ציבוריות, כפי שייבחרו במהלך הקורס, מתוך מערכת מאי״ה של הבורסה לניירות ערך: <span class="url">https://maya.tase.co.il</span></li></ul>
<p><b>פריטי קריאה באנגלית</b> (כפי שמופיעים בתוכנית הקורס):</p>
<ul class="enl"><li>Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. Journal of Finance, 23(4), 589-609.</li>
<li>Barth, M. E., Landsman, W. R., &amp; Lang, M. H. (2008). International accounting standards and accounting quality. Journal of Accounting Research, 46(3), 467-498.</li>
<li>Benninga, S., &amp; Mofkadi, T. Principles of Finance with Excel.</li>
<li>Berk, J., &amp; DeMarzo, P. Corporate Finance.</li>
<li>Brealey, R. A., Myers, S. C., &amp; Allen, F. Principles of Corporate Finance.</li>
<li>Graham, J. R., &amp; Harvey, C. R. (2001). The theory and practice of corporate finance: Evidence from the field. Journal of Financial Economics, 60(2-3), 187-243.</li>
<li>Nissim, D., &amp; Penman, S. H. (2001). Ratio analysis and equity valuation: From research to practice. Review of Accounting Studies, 6(1), 109-154.</li>
<li>Palepu, K. G., Healy, P. M., &amp; Peek, E. Business Analysis and Valuation: IFRS Edition.</li>
<li>Ross, S. A., Westerfield, R. W., &amp; Jaffe, J. Corporate Finance.</li>
<li>Wahlen, J. M., Baginski, S. P., &amp; Bradshaw, M. T. Financial Reporting, Financial Statement Analysis, and Valuation.</li>
<li>Weygandt, J. J., Kimmel, P. D., &amp; Kieso, D. E. Financial Accounting with International Financial Reporting Standards.</li></ul>
<h3>יצירת קשר</h3>
<p>פניות לד״ר שי צבאן במייל: {n('shay.tsaban@gmail.com')}. חובה לרשום בכל פנייה את שם המוסד ואת שם הקורס.</p>"""
CSS = '''
@font-face{font-family:"David";src:url("david.ttf");font-weight:400}
@font-face{font-family:"David";src:url("davidbd.ttf");font-weight:700}
@page{size:A4;margin:16mm;@bottom-center{content:counter(page);font-family:"David";font-size:10pt;color:#5d6a86}}
:root{--ink:#16213a;--navy:#1b2d55;--coral:#ff6a4d;--mut:#5d6a86;--line:#d9d2c3}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html{direction:rtl}body{font-family:"David";font-size:11.8pt;line-height:1.34;color:var(--ink);margin:0}
.n{direction:ltr;unicode-bidi:isolate}
.hd{background:linear-gradient(160deg,#0f1b33 0%,#1b2d55 60%,#27447f 100%);color:#fff;border-radius:3mm;padding:6mm 8mm;margin-bottom:4mm}
.hd .k{color:#7fe3d6;font-weight:700;font-size:12pt}.hd h1.t{color:#fff;margin:1.5mm 0 1mm;font-size:24pt}.hd .s{color:#d6e0f7;font-size:13.5pt}
h3{font-size:13.4pt;color:var(--navy);margin:4mm 0 1.2mm;break-after:avoid;border-bottom:.5mm solid var(--coral);padding-bottom:.6mm}
p{margin:0 0 1.6mm}ul{margin:0 0 1.6mm;padding-right:6mm}li{margin-bottom:.5mm}
table{width:100%;border-collapse:collapse;font-size:10.8pt;margin:1.2mm 0 2mm}th{background:var(--navy);color:#fff;text-align:right;padding:1mm 2mm}td{padding:1mm 2mm;border-bottom:.25mm solid var(--line);vertical-align:top}tr{break-inside:avoid}
table.meta td:first-child{font-weight:700;width:30mm;color:var(--navy)}td.c{text-align:center;font-weight:700}td.r{white-space:nowrap}
tr.hi td{background:#fff0d2}.note{background:#eef2ff;border-right:1.2mm solid var(--navy);border-radius:1mm;padding:1.2mm 2.6mm;font-size:10.8pt}
.url{direction:ltr;unicode-bidi:isolate;font-family:Arial,sans-serif;font-size:10pt;color:var(--navy)}
.tbd{background:#fff0d2;border:.3mm dashed #a86703;border-radius:1mm;padding:0 2mm;font-weight:700;color:#7a4a00}
.lit{list-style:none;padding:0}.lit .n{display:block;text-align:left}
.w{font-size:10.4pt;color:#2a3858;margin-top:.4mm}td.rd{font-size:10pt;width:62mm}li.en,div.en{direction:ltr;text-align:left;unicode-bidi:isolate}.en2{direction:ltr;unicode-bidi:isolate}ul.enl{direction:ltr;text-align:left;padding-left:6mm;padding-right:0;font-size:10.4pt}ol{margin:0 0 1.6mm;padding-right:6mm}
'''
page = f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>מימון וניתוח פיננסי למנהלים | סילבוס</title><style>{CSS}</style></head><body>{body}</body></html>'
assert '—' not in page and '־' not in page
d = tempfile.mkdtemp(dir=os.environ.get('TMPDIR'))
for f in ('david.ttf', 'davidbd.ttf'): shutil.copy(os.path.join(FONTS, f), d)
open(os.path.join(d, 's.html'), 'w', encoding='utf8').write(page)
out = os.path.abspath(os.path.join(H, '..', 'materials', 'syllabus.pdf'))
subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', f'--user-data-dir={d}/p', '--no-pdf-header-footer', '--virtual-time-budget=6000', f'--print-to-pdf={out}', 'file://' + d + '/s.html'], capture_output=True, timeout=120)
shutil.rmtree(d, True)
import fitz
D = fitz.open(out); print('pages', len(D), 'bytes', os.path.getsize(out), sorted({f[3].split('+')[-1] for p in D for f in p.get_fonts()}))
