# Meeting 3, part 1: an animated recap of meeting 2 (the accounting identity and the table), step by step, with pictures.
opener(1, 'רענון: מה למדנו במפגש 2', 'שאלת החלק: איך רושמים כל עסקה בטבלה אחת, בלי לשבור את המאזן?',
       ['לכל נכס יש מקור מימון', 'טבלת הזהות: עמודה לכל חשבון, ובקרה', 'הרווח נצבר בעודפים, בתוך ההון העצמי', 'שלוש שאלות לכל עסקה, וארבע מלכודות', 'שאלה אחת לחימום'], 10)

_tw3 = lambda head, blocks: '<div class="tower"><div class="tw-h">' + head + '</div><div class="tw-b">' + ''.join(blocks) + '</div></div>'
_bk3 = lambda n, lab, amt, cls, flex: ST(n, f'<b>{lab}</b><span class="n">{amt}</span>', cls=f'blk {cls}" style="flex:{flex} 1 0')
S('r2-src', 'רענון: מקור מימון', 'רענון 1: לכל נכס יש מקור מימון',
  '<div class="row eq2 top">'
  + '<div class="col"><div class="mt-h"><b>' + TX('הדירה שלי') + '</b></div><div class="towers big">'
  + _tw3('השימוש: מה קניתי', [ST(1, '<div class="blkart">' + _svg(TOONS['apt']) + '</div><b>דירה</b><span class="n">1,500,000</span>', cls='blk nca" style="flex:1 1 0')])
  + POP(2, '<div class="eqs">=</div>', 'eqw')
  + _tw3('המקורות: מי מימן', [_bk3(2, 'משכנתא: התחייבות', '400,000', 'ncl', 400), _bk3(2, 'הכסף שלי: הון עצמי', '1,100,000', 'eqb', 1100)]) + '</div></div>'
  + '<div class="col"><div class="mt-h"><b>' + TX('קפה נועה בע״מ, 31.12.2026') + '</b></div><div class="towers big">'
  + _tw3('נכסים', [_bk3(3, 'מזומן', '81,400', 'ca', 3), _bk3(3, 'לקוחות ומלאי', '20,000', 'ca', 2), _bk3(3, 'ציוד וריהוט', '120,000', 'nca', 4)])
  + POP(4, '<div class="eqs">=</div>', 'eqw')
  + _tw3('מקורות', [_bk3(4, 'התחייבויות', '49,000', 'cl', 2), _bk3(4, 'הון מניות', '80,000', 'eqb', 3), _bk3(4, 'עודפים', '92,400', 'eqb', 3.4)]) + '</div></div>'
  + '</div>'
  + BAND('dg', 'כל נכס הגיע ממקור: מישהו הלווה ([[liab|התחייבות]]), או שהבעלים השקיעו או השאירו רווח ([[equity|הון עצמי]]). לכן תמיד: נכסים = התחייבויות + הון עצמי, 221,400 = 221,400.', 5), kick='חלק 1 · רענון')

_G3 = {'a': 'נכסים', 'l': 'התחייבויות', 'e': 'הון עצמי', 'pl': 'עודפים: הכנסות והוצאות'}
_grow = '<tr><th class="gt"></th>' + ''.join(f'<th class="g{g}" colspan="{sum(1 for *_, x in A2 if x == g)}">{_G3[g]}</th>' for g in ('a', 'l', 'e', 'pl')) + '<th class="gc">מאוזן?</th></tr>'
_hrow = _h([('עסקה', 't')] + [(n, g) for _, n, g in A2] + [('בקרה', 'c')])
_cell = lambda v: '' if v is None else (f'<span class="n">({abs(v):,})</span>' if v < 0 else f'<span class="n">{v:,}</span>')
_trs = ''.join(ST(i + 1, f'<td>{NOA[k][0]}</td>' + ''.join(f'<td>{_cell(_amt(NOA[k][1][a])) if a in NOA[k][1] else ""}</td>' for a, _, _ in A2) + '<td class="ok">-</td>', 'tr')
               for i, k in enumerate([0, 2, 3, 6, 7, 11]))
S('r2-table', 'רענון: טבלת הזהות', 'רענון 2: טבלת הזהות, עמודה לכל חשבון',
  '<div class="card"><table class="xhead rtab"><colgroup><col style="width:250px">' + '<col>' * (len(A2) + 1) + '</colgroup>' + _grow + _hrow + _trs + '</table></div>'
  + '<div class="row eq3 top">'
  + ST(7, '<b class="ct">' + TX('שורה לכל עסקה') + '</b><p class="lg">' + TX('פלוס בעמודה של חשבון שגדל, ומינוס (בסוגריים) בעמודה של חשבון שקטן.') + '</p>', cls='card')
  + ST(8, '<b class="ct">' + TX('הכנסות והוצאות בתוך ההון') + '</b><p class="lg">' + TX('הכנסה מגדילה את ההון, והוצאה מקטינה אותו. לכן ההוצאות נרשמות במינוס.') + '</p>', cls='card')
  + ST(9, '<b class="ct">' + TX('הבקרה: תמיד 0') + '</b><p class="lg">' + TX('נכסים פחות התחייבויות פחות הון. מקף בעמודה האחרונה: השורה מאוזנת.') + '</p>', cls='card') + '</div>', kick='חלק 1 · רענון')

S('r2-re', 'רענון: הרווח בעודפים', 'רענון 3: הרווח לא נעלם, הוא נצבר בעודפים',
  '<div class="plre">'
  + POP(1, '<div class="pr-h">' + TX('עמודות ההכנסות וההוצאות, 2026') + '</div><table class="tbl2 stmt mini"><tr><td>הכנסות</td><td class="amt"><span class="n">504,000</span></td></tr><tr><td>הוצאות</td><td class="amt">' + PAREN('411,600') + '</td></tr><tr class="tot hl"><td><b>רווח נקי</b></td><td class="amt"><b class="n">92,400</b></td></tr></table>', 'card prc')
  + ST(2, '<div class="pr-ar"><span>' + TX('הרווח שייך לבעלים, ונשאר בחברה') + '</span></div>', cls='wipe prw')
  + POP(3, '<div class="pr-h">' + TX('ההון העצמי, 31.12.2026') + '</div><table class="tbl2 stmt mini"><tr><td>הון מניות</td><td class="amt"><span class="n">80,000</span></td></tr><tr class="hl"><td><b>' + TX('[[re|עודפים]]') + '</b></td><td class="amt"><b class="n">92,400</b></td></tr><tr class="tot"><td><b>סך הון עצמי</b></td><td class="amt"><b class="n">172,400</b></td></tr></table>', 'card prc')
  + '</div>'
  + '<div class="row eq2 top">'
  + ST(4, '<b class="ct">' + TX('הכנסה מגדילה את ההון העצמי') + '</b><p class="lg">' + TX('בטבלה: פלוס בעמודת הכנסות. בצד הנכסים: מזומן, או לקוחות שעוד ישלמו.') + '</p>', cls='card inc')
  + ST(5, '<b class="ct">' + TX('הוצאה מקטינה את ההון העצמי') + '</b><p class="lg">' + TX('בטבלה: מינוס בעמודת הוצאות. בצד השני: מזומן שיצא, מלאי שנצרך, או הוצאות לשלם.') + '</p>', cls='card exp') + '</div>'
  + BAND('dg', 'היום נעשה את הצעד הבא: נסכם כל עמודה, ונבנה מהטבלה את דוח רווח והפסד ואת המאזן.', 6)
  + TOON('cup', 'הרווח של השנה לא הולך לשום מקום: הוא מחכה בהון העצמי.', 7), kick='חלק 1 · רענון')

S('r2-ask', 'רענון: שלוש שאלות', 'רענון 4: שלוש שאלות לכל עסקה, וארבע מלכודות',
  '<div class="row g55 top"><div class="col">'
  + ''.join(ST(i + 1, f'<b class="ct">{i + 1}. {TX(q)}</b><p class="lg">{TX(t)}</p>', cls='card') for i, (q, t) in enumerate([
      ('איזה נכס השתנה?', 'מזומן, לקוחות, מלאי, ציוד: מה גדל ומה קטן.'),
      ('איזו התחייבות השתנתה?', 'ספקים, הוצאות לשלם, הלוואה: האם נוסף חוב, או שהוא קטן.'),
      ('האם הבעלים התעשרו, או נעשו עניים יותר?', 'אם כן: הכנסה או הוצאה. אם לא: ההון לא זז.')]))
  + '</div><div class="col"><div class="learn">'
  + ''.join(POP(i + 4, f'<div class="ln-i">{ic}</div><b>{TX(h)}</b><p>{TX(t)}</p>', 'lcard') for i, (ic, h, t) in enumerate([
      ('📦', 'קנייה אינה הוצאה', 'מלאי הוא נכס, עד שהוא נצרך.'),
      ('🏦', 'פירעון הלוואה אינו הוצאה', 'רק הריבית היא הוצאה.'),
      ('💳', 'גבייה אינה הכנסה', 'ההכנסה נרשמה כשהשירות ניתן.'),
      ('💡', 'הוצאה שלא שולמה', 'נרשמת עכשיו, עם הוצאות לשלם.')]))
  + '</div></div></div>', kick='חלק 1 · רענון')

MC1('m-r2', 'שאלה אחת: תשלום לספק', 'מה רושמים בטבלת הזהות?',
    ['מזומן (5,000), ספקים (5,000)', 'מזומן (5,000), הוצאות (5,000)', 'ספקים 5,000, הוצאות (5,000)', 'מזומן (5,000) בלבד'], 0,
    'תשלום חוב מקטין נכס והתחייבות באותו סכום. ההון לא השתנה, ולכן אין הוצאה. הבקרה: מינוס 5,000 פחות מינוס 5,000, כלומר 0.',
    art='box', story='קפה נועה שילמה לספקים 5,000 ש״ח מתוך החוב שלה.')
