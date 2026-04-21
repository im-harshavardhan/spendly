# Video 7 Notes — Spec Driven Development (SDD)
**Claude Code Learning Journey**

---

## 🎯 What This Video Is About
One of the **core pillars of agentic coding** — how to give AI the right instructions before it writes a single line of code.

---

## 🎲 Vibe Coding — What It Is & The Problem

**Vibe Coding** is a modern style of programming where instead of carefully planning everything upfront, you build software by interacting with an AI in a fast, conversational, and experimental way.

Popular tools associated with vibe coding: **Cursor, Loveable, Replit**

> It has become a big thing after LLMs became mainstream.

### Why it's appealing:
- Fast to start
- No upfront planning needed
- Great for beginners learning to code

### The core problem — **loss of control**

When you give an AI a vague prompt, the AI makes all the decisions for you.

**Example prompt:** *"Build me a user authentication system"*

The AI now has to decide:
- Which framework to use?
- JWT or sessions for login?
- What are the password rules?
- What happens after 3 failed login attempts?

The LLM picks all of these on its own — based on its training, not your actual requirements. You get code fast, but it may not be the right code for your situation.

**Result:** You end up in a loop of corrections and patches — fixing things that were never right in the first place.

> **Analogy:** Vibe coding is like calling a builder and saying *"build me a house"* without giving them blueprints. They'll build something — but the number of rooms, the layout, the materials — all their choice. You'll spend months asking them to change things that should have been decided before they poured the foundations.

---

## 📋 Spec Driven Development (SDD) — The Solution

**Spec Driven Development** is a software development approach where a **detailed specification document is written before any code is written.**

The spec acts as the **single source of truth** for what the system should do — and all development flows from it.

> **Analogy:** The spec document is the architect's blueprint. No builder breaks ground without one. The blueprint decides everything upfront so there are no surprises mid-build.

### What goes inside a Spec Document:

| Section | What it answers |
|---|---|
| **Problem Statement** | What problem are we solving and why? |
| **Functional Requirements** | What should the system actually do? |
| **API Contracts** | What are the inputs, outputs, and data shapes? |
| **Constraints** | What are the limits? (time, budget, tech stack) |
| **Edge Cases & Error Handling** | What happens when things go wrong? |
| **Acceptance Criteria** | How do we know when it's done correctly? |

💡 **Job Tip:** In real companies, spec documents (also called PRDs — Product Requirements Documents) are written by Product Managers before any developer writes a line of code. Knowing how to read and write them is a genuine professional skill.

---

## 🗺️ The SDD Roadmap

```
Spec → Review → Design → Review → Tasks → Build → Validate
```

### Each stage explained:

**1. Spec**
Write the specification document. Non-technical language is fine here — focus on *what* the system should do, not *how*.

**2. Review**
Check the spec. Is anything missing? Are the requirements clear? Fix gaps before moving forward.

**3. Design**
Convert the non-technical spec into a **technical design document** — this is the *how*. Which database? Which API structure? Which framework?

> The spec and design documents are kept **separate on purpose** — if you ever switch tech stacks, you only rewrite the design document, not the spec. The requirements stay the same even if the implementation changes.

**4. Review**
Check the technical design. Does it match the spec? Is the approach sensible? Any technical risks?

**5. Tasks**
Extract individual tasks from the technical design plan. Break it into small, actionable pieces of work.

**6. Build**
Code each task. Now Claude Code builds — but with full context from the spec, design, and tasks.

**7. Validate**
Test whether it's working correctly. Did it achieve everything the spec required? Does it meet the acceptance criteria?

---

## ⚔️ Vibe Coding vs Spec Driven Development

| | Vibe Coding | Spec Driven Development |
|---|---|---|
| **Planning** | Little to none | Detailed upfront |
| **Speed to first code** | Very fast | Slower start |
| **Who makes decisions** | The AI | You |
| **Control** | Low | High |
| **Best for** | Quick experiments, learning, prototypes | Real projects, team work, production code |
| **Risk** | High — ends up in correction loops | Low — problems caught before coding |
| **Code quality** | Inconsistent | Consistent and intentional |
| **Scalability** | Hard to maintain | Easier to maintain and extend |

💡 **Job Tip:** In professional environments, vibe coding without specs leads to what developers call **technical debt** — messy code that works but is expensive to maintain or change later. SDD prevents this by making decisions consciously, upfront.

---

## 🧠 Key Concepts Explained Simply

### What is an API Contract?
An **API contract** defines exactly what data goes in and what data comes out of a system.

> **Analogy:** Think of it like a restaurant order form. The form says exactly what information the customer fills in (dish name, quantity, allergies) and what the kitchen sends back (the dish, the bill). Both sides know exactly what to expect — no surprises.

### What are Edge Cases?
**Edge cases** are unusual situations that don't happen in normal use but could break the system.

> **Example:** What if a user leaves the password field blank? What if they paste in 10,000 characters? What if two users register with the same email at the same second?

These need to be thought about in the spec — not discovered in production.

### What are Acceptance Criteria?
These are the specific conditions that must be true for a feature to be considered **done**.

> **Example for a login feature:**
> - User can log in with correct email and password ✅
> - User sees an error message with wrong password ✅
> - Account locks after 3 failed attempts ✅
> - Locked account sends a reset email ✅

---

## 🧠 Key Takeaways

1. **Vibe coding = fast but low control** — AI makes all decisions, you patch later
2. **SDD = slower start but much more control** — you decide, AI executes
3. **Spec = what the system does** (non-technical, focused on requirements)
4. **Design = how the system does it** (technical, focused on implementation)
5. **Keep spec and design separate** — so switching tech stacks doesn't throw away your requirements
6. **Tasks come from the design** — break it down before building
7. **Validate at the end** — check against the original spec, not just "does it run"

---
*Notes from Video 7 | Claude Code Learning Journey*
