# Meeting 3. DRAFT. Shay, 2026-11-12: meeting 2 stopped at slide 47, so meeting 3 opens with a recap of meeting 2 and everything
# it did not reach (from the table to the statements, and Omer's full exercise from the identity to the statements),
# then the old meeting 3 draft: the rules and who checks them, changes in equity, cash flows, the links, and self practice.
SL.append(dict(id='s-title', title='פתיחה', kind='title', part=None, h='מהזהות לדוחות, ומהדוחות להחלטות', body='', cls='', kick=None))

ROUTE = [(1, 'רענון: מה למדנו במפגש 2', 'מקור מימון, טבלת הזהות, רווח בתוך ההון', 'כ-10 דקות'),
         (2, 'שאלה מלאה: קפה נועה, 2027', 'השנה השנייה, עסקה בכל שקף', 'כ-35 דקות'),
         (3, 'מהטבלה לדוחות', 'מה הולך לאן, רווח והפסד ומאזן', 'כ-30 דקות'),
         (4, 'תרגיל מלא עם פתרון: עומר', 'מעבדת התיקונים, עסקה בכל שקף', 'כ-30 דקות'),
         (5, 'מה עושים עם הדוחות?', 'ניתוח אופקי, אנכי, ויחסים', 'כ-35 דקות'),
         (6, 'תרגול עצמי', 'אחד עשר תרגולים, עם פתרון מלא', 'לתרגול עצמי')]
S('s-route', 'מסלול המפגש', 'מסלול המפגש',
  '<p class="lead">' + TX('במפגש 2 רשמנו את 2026 של קפה נועה בטבלת הזהות. היום: השנה השנייה שלה, מההתחלה ועד הדוחות; תרגיל מלא נוסף; ואז מה עושים עם הדוחות: ניתוחים בסיסיים, והחלטה בבנק.' + (' לחצו על חלק כדי לעבור אליו.' if MODE == 'deck' else '')) + '</p><div class="route r6">'
  + ''.join(rcard(n, t, d, m, f'p-{n}') for n, t, d, m in ROUTE) + '</div>'
  + BAND('note', 'טיוטה. הדקות הן הערכה. קפה נועה בע״מ והחברות האחרות במצגת הן דוגמאות שהומצאו להמחשה, וכל המספרים להמחשה בלבד.'), kick='לפני שמתחילים')
