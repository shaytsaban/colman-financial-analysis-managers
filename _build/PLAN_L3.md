# Meeting 3, rebuilt after Shay's review of 2026-11-19

Shay liked slides 1 to 9 (title, route, the recap of meeting 2). From slide 10 on the meeting is rebuilt.

## Decisions

1. **The checker checks results only.** `xl.js` treats every sheet as `values` mode unless a sheet says `values: False`:
   a typed number or any formula is accepted if its result is right. No "you typed a number", no "use a function", no anchoring checks.
2. **One transaction per slide, and the sheet takes the slide.** `QT(..., one=True)`: a single line with the transaction at the top
   (with a "more explanation" button beside it), the live sheet below it, using all the height that is left. No chips and no
   bands above the sheet; what each step teaches goes into the step notes and the popup.
3. **Part 2: a full question from start to end, Noa's second year (2027).** It starts from the closing balances of 2026 (the
   statements students already know), so it practises: a balance sheet carries over, revenues and expenses start again at
   zero, and the first transactions settle 2026 items (collecting from customers, paying the December electricity bill: neither
   is a revenue or an expense of 2027). Twelve transactions, each on its own slide, plus two one-question slides on the traps.
4. **Part 3: from the table to the statements, with the data always beside the template.**
   - sum the columns (live sheet);
   - a map slide: the summed table, columns lit group by group, with the report each group goes to;
   - a "fly" slide for the income statement: the data summary on one side, the empty statement on the other; each click flies
     the amounts into their line. Every line opens its composition as a sub-table (cost of sales = inventory used + baristas);
   - the live sheet that builds the statement, with the data in columns A:B beside it;
   - the same two slides for the balance sheet (retained earnings = opening 92,400 + profit 123,200);
   - what we learned.
5. **Part 4: Omer, a second full exercise with a full solution, one transaction per slide**, then the same statements stage.
6. **Part 5 replaces the rules, equity and cash flow parts: what do we do with the statements?** Non-exhaustive demos on Noa,
   2026 against 2027, each as example first, then the definition, then a live sheet:
   horizontal analysis (change in shekels and in percent), vertical analysis of the income statement (out of every 100 shekels
   of sales), the structure of the balance sheet (who finances the assets), and a few ratios (current ratio, ROA, ROE).
   It closes on a decision: Noa asks the bank for a loan for a second branch, but she holds 185,600 in cash.
7. **Part 6: self practice.** The eight exercises of the old part (identity, Liat's statements, traps) plus three on analysis
   (Omer's vertical analysis, Omer's ratios against Noa's, Liat's two years side by side).
8. **Booklet:** meeting 3 gets 3-4 (profitability, taught in part 5) and a new 3-6 (horizontal and vertical analysis).
   1-5, 2-3, 2-4, 2-5 wait for the meeting that teaches regulation, equity changes and cash flows.
9. **Parked, not deleted** (Shay may want them later): `parked/content_l3a.py` (rules and who checks), `parked/content_l3b.py`
   (changes in equity, cash flows, links), `parked/content_l3c.py` (their self practice), `parked/content_l3s.py` (the 2026
   statements stage, replaced by 2027).

## Numbers (asserted in the content files)

Noa 2027: opening 31.12.2026 as in meeting 1. Closing 31.12.2027: cash 185,600, customers 20,000, inventory 12,000, equipment
120,000 (assets 337,600); suppliers 14,000, accrued 3,000, loan 25,000; share capital 80,000, retained earnings 92,400 + 123,200.
Income statement 2027: sales 600,000, cost of sales 270,000, gross 330,000, selling 36,000, G&A 130,000, operating 164,000,
finance 4,000, before tax 160,000, tax 36,800 (23%), net 123,200.
