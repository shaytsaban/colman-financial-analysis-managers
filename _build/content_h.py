# Helpers shared by every lesson: statements revealed line by line, and the statement-format sheets.
def PAREN(x):
    return f'<span class="n">({x})</span>'


def STEPROWS(rows, start=1, why=True):
    """A statement revealed line by line: (label, amount, why, total?)."""
    out, n = '', start
    for lab, amt, w, tot in rows:
        out += ST(n, f'<td>{TX(lab)}</td><td class="amt">{amt if amt.startswith("<") else TX(amt)}</td>' + (f'<td class="why">{TX(w)}</td>' if why else ''), 'tr', 'tot' if tot else '')
        n += 1
    return out, n



def ISQ(sid, tag, title, stem, v, note=None, done='', xtitle='', build=None):
    """An income statement in its own format: the lines in the order of the statement, amounts typed in, every profit a formula."""
    d = {'A1': 'סעיף', 'B1': 'ש״ח', 'A2': 'הכנסות ממכירות', 'A3': 'עלות המכירות', 'A4': 'רווח גולמי', 'A5': 'הוצאות מכירה ושיווק', 'A6': 'הוצאות הנהלה וכלליות', 'A7': 'רווח תפעולי',
         'A8': 'הוצאות מימון', 'A9': 'רווח לפני מסים על ההכנסה', 'A10': 'מסים על ההכנסה', 'A11': 'רווח נקי', 'A13': 'שיעור מס',
         'B2': v['rev'], 'B3': v['cogs'], 'B5': v['sm'], 'B6': v['ga'], 'B8': v['fin'], 'B13': v['tax']}
    sol = {'B4': '=B2-B3', 'B7': '=B4-B5-B6', 'B9': '=B7-B8', 'B10': '=B9*B13', 'B11': '=B9-B10'}
    QX(sid, tag, title, stem, 'הקלידו כל סכום בשורה שלו בדוח, ואת שיעור המס ב-B13. השורות הלבנות של הרווחים הן נוסחאות: השורה שמעל, פחות הקטגוריה הבאה.',
       d, sol, [230, 110], [1], fmt={**{f'B{i}': 'num0' for i in range(2, 12)}, 'B13': 'pct0'},
       hints=['רווח גולמי: =B2-B3. רווח תפעולי: =B4-B5-B6.', 'המס מחושב על הרווח לפני מס: =B9*B13. רווח נקי: =B9-B10.'], remind='=B4-B5-B6', partial=['B4'],
       traps={'B10': [('=B7*B13', 'המס מחושב על הרווח <b>לפני מס</b>, אחרי הוצאות המימון: =B9*B13.')], 'B7': [('=B4-B5', 'שכחתם את הוצאות ההנהלה והכלליות.')]},
       steps=[dict(cells={'B4': '=B2-B3'}, note='רווח גולמי: =B2-B3.'), dict(cells={'B7': '=B4-B5-B6'}, note='רווח תפעולי: =B4-B5-B6.'),
              dict(cells={'B9': '=B7-B8'}, note='רווח לפני מס: =B7-B8.'), dict(cells={'B10': '=B9*B13', 'B11': '=B9-B10'}, note='מס: =B9*B13. רווח נקי: =B9-B10.')],
       note=note or [], done=done, xtitle=xtitle, build=build)


def BSQ(sid, tag, title, stem, ca, nca, cl, ncl, sc, re_, note=None, done='', xtitle=''):
    """A balance sheet in its own format: assets on one side, liabilities and equity on the other, each group with its total.
    ca: three (label, amount); nca, ncl: one (label, amount); cl: two (label, amount)."""
    d = {'A1': 'נכסים', 'B1': 'ש״ח', 'C1': 'התחייבויות והון עצמי', 'D1': 'ש״ח',
         'A2': 'נכסים שוטפים', 'A6': 'סך נכסים שוטפים', 'A7': 'נכסים לא שוטפים', 'A11': 'סך הנכסים',
         'C2': 'התחייבויות שוטפות', 'C5': 'סך התחייבויות שוטפות', 'C6': 'התחייבויות לא שוטפות', 'C8': 'הון מניות', 'C9': 'עודפים', 'C10': 'סך הון עצמי', 'C11': 'סך התחייבויות והון'}
    for i, (lab, x) in enumerate(ca): d[f'A{3 + i}'] = lab; d[f'B{3 + i}'] = x
    d['A8'] = nca[0]; d['B8'] = nca[1]
    for i, (lab, x) in enumerate(cl): d[f'C{3 + i}'] = lab; d[f'D{3 + i}'] = x
    d['C7'] = ncl[0]; d['D7'] = ncl[1]; d['D8'] = sc; d['D9'] = re_
    sol = {'B6': '=SUM(B3:B5)', 'B11': '=B6+B8', 'D5': '=D3+D4', 'D10': '=D8+D9', 'D11': '=D5+D7+D10'}
    QX(sid, tag, title, stem, 'הקלידו כל סכום ליד הפריט שלו. שורות הסיכום הן נוסחאות.',
       d, sol, [165, 90, 180, 90], [1], fmt={f'{c}{r}': 'num0' for c in 'BD' for r in range(2, 12)},
       hints=['נכסים שוטפים: =SUM(B3:B5). סך הנכסים: ועוד הנכס הלא שוטף, =B6+B8.', 'בצד השני: שוטפות =D3+D4, הון =D8+D9, והכול יחד =D5+D7+D10.'], remind='=D5+D7+D10', partial=['B6'],
       traps={'D11': [('=D5+D10', 'שכחתם את ההתחייבות הלא שוטפת בשורה 7.')], 'B11': [('=B6', 'שכחתם את הנכס הלא שוטף בשורה 8.')]},
       steps=[dict(cells={'B6': '=SUM(B3:B5)', 'B11': '=B6+B8'}, note='צד הנכסים: סך נכסים שוטפים, ואז סך הנכסים.'),
              dict(cells={'D5': '=D3+D4', 'D10': '=D8+D9', 'D11': '=D5+D7+D10'}, note='הצד השני: שוטפות, הון עצמי, ובסוף הכול יחד. שני הסכומים בשורה 11 שווים.', sel='D5', sel2='D11')],
       note=note or [], done=done, xtitle=xtitle)

