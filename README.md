# מימון וניתוח פיננסי למנהלים (432348)

אתר הקורס: https://shaytsaban.github.io/colman-financial-analysis-managers/

המסלול האקדמי של המכללה למנהל, בית הספר לתקשורת וניהול, סמסטר א׳ תשפ״ז. ד״ר שי צבאן.

- `index.html`: דף הבית.
- `lectures/lecture-1/`: מצגת השיעור (`presentation.html`) וסיכום PDF (`summary.pdf`).
- `materials/`: סילבוס; חוברת תרגילים לשבעת נושאי הקורס (`booklet.pdf`), הפתרונות שלה (`booklet-solutions.pdf`), קובץ התרגול וקובץ הפתרונות שלה (`booklet-practice.xlsx`, `booklet-solutions.xlsx`); וקובץ התרגול וקובץ הפתרונות של מפגש 1 (`practice-1.xlsx`, `practice-1-solutions.xlsx`). הקורס: 13 מפגשים, שבעה נושאים.
- `_build/`: מקורות הבנייה. התוכן כתוב פעם אחת (`content_*.py`) ומזין גם את המצגת וגם את הסיכום.
  - `python3 build_deck.py 1`: המצגת. גיליונות ה-Excel החיים רצים על `xl.js`.
  - `python3 test_deck.py`: בדיקה בדפדפן ללא ממשק: שקפים שחורגים, כיוון מספרים, וכל גיליון: דוחה תשובה שגויה ומקבל נוסחה נכונה.
  - `python3 build_summary.py 1`, `python3 build_syllabus.py`, `python3 build_hub.py`.
  - `python3 build_xlsx.py 1` ו-`python3 build_booklet.py`: קובצי התרגול והפתרונות. התרגילים של החוברת ומסקנותיהם ב-`booklet.py`. כל תשובה נבדקת מול חישוב מחדש ב-LibreOffice.
  - פונטי David נטענים מ-`../iit-build/fonts` ואינם נשמרים כאן.
