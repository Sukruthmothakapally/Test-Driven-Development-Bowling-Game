# 🎯 Bowling Game with Test Driven Development (TDD)

Hey! This is a personal project where I practiced **Test Driven Development (TDD)** by implementing a bowling score calculator in Python — twice. First using a traditional approach with a **rolls array**, and then a more **optimized version without using an array** (pure state tracking). This kata is an excellent way to sharpen edge-case thinking, test coverage discipline, and clean design.

---

## 🔧 What is TDD and Why I Used It

I built both implementations using the **TDD** approach: write a failing test first, write the minimum code to make it pass, and then refactor. This method helped me:

- Stay focused on the *expected behavior* from the beginning
- Write clean, modular, and maintainable code
- Catch subtle bugs and edge cases early
- Refactor confidently, knowing tests had my back

### 🔁 My TDD Cycle

| Step         | What I Did                                                   |
|--------------|--------------------------------------------------------------|
| 🔴 **Red**     | Wrote a test that fails (e.g. "Gutter game should score 0") |
| 🟢 **Green**   | Wrote just enough logic to pass that test                   |
| 🟡 **Refactor**| Cleaned up the code (naming, structure, logic)              |

Repeating this cycle consistently helped me build up solid logic and complete test coverage — including tricky edge cases like consecutive strikes, 10th frame bonuses, and spares.

---

## 🎳 Bowling Game: Rules I Had to Implement

1. A game has **10 frames**, and each frame can have **2 rolls** (except strikes).
2. A **strike** (10 pins on first roll) gives a bonus of the next **2 rolls**.
3. A **spare** (10 pins across two rolls) gives a bonus of the next **1 roll**.
4. In the **10th frame**, players may get **extra rolls** for a strike or spare.
5. The **maximum score** is **300** (a perfect game of 12 strikes).

---

## 🧠 What Makes This Interesting

There are two versions in this repo:

### 1. ✅ Traditional Approach with `rolls[]` Array

- File: `bowlinggame.py`
- Tracks all rolls in a list and calculates scores by iterating.
- Very common and easier to reason about for beginners.

### 2. 🚀 Optimized Version without Rolls Array (Stateful Logic)

- Files:  
  - `bowling_game_optimized.py`  
  - `test_bowling_game_optimized.py`
- Tracks everything using state variables: frame, bonuses, extra rolls.
- No use of a `rolls` list at all — closer to how you'd think about bowling in real life.
- More challenging logic — useful for learning stateful design and debugging.

---

## 📁 Project Structure

```bash
.
├── bowlinggame.py                    # Original version with rolls array
├── testbowling.py                   # Tests for original version
├── bowling_game_optimized.py        # Optimized state-based version (no array)
├── test_bowling_game_optimized.py   # Tests for optimized version
