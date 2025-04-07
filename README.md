# 🎯 Bowling Game with Test Driven Development (TDD)

Hey! This is a personal project where I practiced **Test Driven Development (TDD)** by implementing a bowling score calculator in Python. It was a great hands-on way to get deeper into TDD while solving a problem that’s simple at first—but actually gets pretty tricky when you dig into the edge cases.

---

## 🔧 What is TDD and Why I Used It

I built this using the **TDD** approach: write a failing test first, then write the minimum code to pass it, and finally refactor. It's a development style that helps me:

- Stay focused on the *expected behavior* from the start
- Write clean, modular code
- Catch bugs early
- Feel confident while refactoring

### 🔁 My TDD Cycle

Here’s the cycle I followed for every new feature:

| Step         | What I Did                                           |
|--------------|------------------------------------------------------|
| 🔴 **Red**     | Wrote a test that fails (e.g. "Gutter game should score 0") |
| 🟢 **Green**   | Implemented just enough logic to make that test pass       |
| 🟡 **Refactor**| Cleaned up the code (naming, structure) with tests still passing |

Following this over and over made the implementation super solid. Plus, by the end, I had a full test suite I could rely on.

---

## 🎳 Bowling Game: Rules I Had to Implement

The game itself has pretty specific rules, which made this kata a great challenge:

1. A game has **10 frames**, and each frame has **2 rolls** (unless you get a strike).
2. A **strike** is knocking down all 10 pins in the first roll → score = 10 + next two rolls.
3. A **spare** is knocking down 10 pins in two rolls → score = 10 + next one roll.
4. In the **10th frame**, if you get a strike or spare, you get **bonus rolls**.
5. The maximum possible score is **300** (a perfect game of 12 strikes).

---

## 📁 My Project Structure

```bash
.
├── bowlinggame.py      # All the game logic
└── testbowling.py      # My test suite (drives the implementation)
