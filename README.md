# מימון וניתוח פיננסי למנהלים (432348)

אתר הקורס: https://shaytsaban.github.io/colman-financial-analysis-managers/

המסלול האקדמי של המכללה למנהל, בית הספר לתקשורת וניהול, סמסטר א׳ תשפ״ז. ד״ר שי צבאן.

- `index.html`: דף הבית.
- `lectures/lecture-1/`: מצגת השיעור (`presentation.html`) וסיכום PDF (`summary.pdf`).
- `materials/`: סילבוס, חוברת תרגילים לשבעת השיעורים (`booklet.pdf`) וקובץ התרגול שלה (`booklet-practice.xlsx`), וקובץ התרגול של שיעור 1 (`practice-1.xlsx`). הפתרונות אינם מתפרסמים.
- `_build/`: מקורות הבנייה. התוכן כתוב פעם אחת (`content_*.py`) ומזין גם את המצגת וגם את הסיכום.
  - `python3 build_deck.py 1`: המצגת. גיליונות ה-Excel החיים רצים על `xl.js`.
  - `python3 test_deck.py`: בדיקה בדפדפן ללא ממשק: שקפים שחורגים, כיוון מספרים, וכל גיליון: דוחה תשובה שגויה ומקבל נוסחה נכונה.
  - `python3 build_summary.py 1`, `python3 build_syllabus.py`, `python3 build_hub.py`.
  - `python3 build_xlsx.py 1` ו-`python3 build_booklet.py`: קובצי התרגול. התרגילים של החוברת (`booklet.py`) וקובצי הפתרונות נשמרים מחוץ למאגר, ב-`../colman-financial-analysis-managers-private`, ונבדקים מול חישוב מחדש ב-LibreOffice.
  - פונטי David נטענים מ-`../iit-build/fonts` ואינם נשמרים כאן.
