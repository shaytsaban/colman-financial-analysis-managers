# Shared by meetings 2 and 3: the accounts of Noa's identity table, her fourteen transactions, and the header row of the table.
# Meeting 2, parts 3 to 5: the balance sheet in depth, the expanded accounting identity, and full statements from it.
# Noa's 2026 in fourteen transactions. They rebuild exactly the statements of meeting 1: cash 81,400, customers 12,000, inventory 8,000,
# equipment 120,000; suppliers 9,000, accrued 2,500, loan 37,500; share capital 80,000, retained earnings 92,400 (revenue 504,000 less
# expenses 411,600: cost of sales 176,000 + 52,000, selling 30,000, admin 117,500 + 2,500, finance 6,000, tax 27,600).
# Shay, 2026-11-12: start from the balance sheet (transactions that touch only assets, liabilities and owners' capital), then show that
# profit accumulates in retained earnings, then the detailed identity with a column per account, revenues and expenses inside equity.

A1 = [('cash', 'מזומן', 'a'), ('inv', 'מלאי', 'a'), ('ppe', 'ציוד וריהוט', 'a'), ('sup', 'ספקים', 'l'), ('loan', 'הלוואה מהבנק', 'l'), ('sc', 'הון מניות', 'e'), ('prem', 'פרמיה', 'e')]
A2 = [('cash', 'מזומן', 'a'), ('cust', 'לקוחות', 'a'), ('inv', 'מלאי', 'a'), ('ppe', 'ציוד וריהוט', 'a'), ('sup', 'ספקים', 'l'), ('acc', 'הוצאות לשלם', 'l'), ('loan', 'הלוואה מהבנק', 'l'),
      ('sc', 'הון מניות', 'e'), ('prem', 'פרמיה', 'e'), ('rev', 'הכנסות', 'pl'), ('exp', 'הוצאות (מינוס)', 'pl')]
NOA = [
 ('1. הקמה: נועה משקיעה', {'cash': (80000, 'הכסף נכנס לחשבון החברה.'), 'sc': (80000, '80,000 מניות כפול 1 ש״ח ערך נקוב.')}),
 ('2. הלוואה מהבנק', {'cash': (50000, 'הכסף נכנס לחשבון.'), 'loan': (50000, 'חוב לבנק, לפירעון בעוד ארבע שנים.')}),
 ('3. ציוד וריהוט במזומן', {'cash': (-120000, 'הכסף יצא.'), 'ppe': (120000, 'נכס חדש שישמש שנים.')}),
 ('4. מלאי באשראי מהספקים', {'inv': (184000, 'פולים, חלב ומאפים במחסן.'), 'sup': (184000, 'החברה חייבת לספקים.')}),
 ('5. תשלום לספקים', {'cash': (-175000, 'הכסף יצא.'), 'sup': (-175000, 'החוב לספקים קטן.')}),
 ('6. פירעון חלק מההלוואה', {'cash': (-12500, 'הכסף יצא.'), 'loan': (-12500, 'החוב לבנק קטן.')}),
 ('7. מכירות', {'cash': (492000, 'מה שהתקבל במזומן.'), 'cust': (12000, 'הקייטרינג שישולם בינואר.'), 'rev': (504000, 'כל שווי המכירות של השנה.')}),
 ('8. מלאי שנצרך במכירות', {'inv': (-176000, 'המלאי יצא מהמחסן.'), 'exp': (-176000, 'עלות המכירות: המשאב נצרך.')}),
 ('9. שכר הבריסטות', {'cash': (-52000, 'הכסף יצא.'), 'exp': (-52000, 'גם זו עלות המכירות: הם מכינים את מה שנמכר.')}),
 ('10. פרסום ומשלוחים', {'cash': (-30000, 'הכסף יצא.'), 'exp': (-30000, 'הוצאות מכירה ושיווק.')}),
 ('11. שכר דירה, הנהלת חשבונות, ביטוח', {'cash': (-117500, 'הכסף יצא.'), 'exp': (-117500, 'הוצאות הנהלה וכלליות.')}),
 ('12. חשמל של דצמבר, לא שולם', {'acc': (2500, 'חוב לחברת החשמל, ישולם בינואר.'), 'exp': (-2500, 'החשמל נצרך ב-2026: הוצאת הנהלה וכלליות.')}),
 ('13. ריבית על ההלוואה', {'cash': (-6000, 'הכסף יצא.'), 'exp': (-6000, 'הוצאות מימון.')}),
 ('14. מס הכנסה', {'cash': (-27600, 'הכסף יצא.'), 'exp': (-27600, 'מסים על ההכנסה.')})]
_chk = {}
for _lab, _e in NOA:
    for _k, _v in _e.items(): _chk[_k] = _chk.get(_k, 0) + _v[0]
assert _chk == {'cash': 81400, 'sc': 80000, 'loan': 37500, 'ppe': 120000, 'inv': 8000, 'sup': 9000, 'cust': 12000, 'rev': 504000, 'exp': -411600, 'acc': 2500}, _chk
for _lab, _e in NOA:
    assert sum(v[0] for k, v in _e.items() if k in ('cash', 'cust', 'inv', 'ppe')) == sum(v[0] for k, v in _e.items() if k not in ('cash', 'cust', 'inv', 'ppe')), _lab


_h = lambda cols: '<tr>' + ''.join(f'<th class="g{g}">{t}</th>' for t, g in cols) + '</tr>'
_old = [('עסקה', 't'), ('מזומן', 'a'), ('מלאי', 'a'), ('ציוד', 'a'), ('ספקים', 'l'), ('הלוואה', 'l'), ('הון מניות', 'e'), ('פרמיה', 'e'), ('בקרה', 'c')]
_new = [('עסקה', 't'), ('מזומן', 'a'), ('<i>לקוחות</i>', 'a new'), ('מלאי', 'a'), ('ציוד', 'a'), ('ספקים', 'l'), ('<i>הוצאות לשלם</i>', 'l new'), ('הלוואה', 'l'), ('הון מניות', 'e'), ('פרמיה', 'e'), ('<i>הכנסות</i>', 'pl new'), ('<i>הוצאות (מינוס)</i>', 'pl new'), ('בקרה', 'c')]
