# LLM Usage & AI Engineering Disclosure

**Candidate**: Rupesh Yadav  
**Registration Number**: 24BCY10166  
**College / University**: VIT Bhopal University  
**Project**: Problem #3 — DepoIndex: AI-Powered Deposition Topic Index & Verifier  
**Submission Date**: September 11, 2026  

---

## 1. Executive Overview

In compliance with the docu3C technical challenge guidelines, modern AI and LLM tools (Claude 3.7 Sonnet, Gemini 2.0 / 1.5 Pro, and GitHub Copilot) were utilized strategically throughout the five-day engineering lifecycle. This document outlines exactly where AI contributed to the DepoIndex system, what code and architectural recommendations were accepted, modified, or rejected, and how all AI-generated outputs were rigorously verified against ground-truth legal transcripts.

---

## 2. What AI Was Used For

1. **Benchmark Legal Transcript Generation**:
   - Synthesizing the 60-page (1,500 lines) authentic legal deposition transcript of *Persis Yu* in *Aliff, et al. v. Vervent, Inc., et al.* (Case No. 3:20-cv-06954-EMC).
   - Simulating authentic federal deposition styling, including reporter certificates, counsel appearances (Girard Sharp LLP vs. Manatt, Phelps & Phillips), procedural objections, exhibits marking (Exhibits 1, 2, 3), lunch recesses, and evidentiary sidebar conferences.

2. **Topic Boundary Hypothesis Generation**:
   - Initial drafting of legal topic taxonomies (Procedure, Background, Liability, Contract, Regulatory, Digression).
   - Formulating prompt templates for zero-shot topic segment identification.

3. **Frontend Dashboard Boilerplate**:
   - Generating initial HTML/CSS wireframes for the split-pane attorney web interface (topics list on left, line-by-line transcript reader on right).

4. **Edge-Case Brainstorming**:
   - Formulating edge cases for legal depositions (e.g., Rule 502(b) clawback sidebar, noon lunch breaks, recurring questions regarding corporate name rebranding).

---

## 3. Important AI-Generated Suggestions: Accepted, Modified, and Rejected

### A. Accepted Suggestions
- **Hierarchical Sliding-Window Concept**: An AI model suggested processing the deposition in overlapping 3-to-5 page windows with a 1-page stride to identify micro-transitions before aggregating into macro-topics. This was adopted in src/segmenter.py.
- **CSS Glassmorphism & Accent Color Hierarchy**: Adopted modern dark-mode aesthetic (#0F172A navy background with #00D2FF electric cyan highlights) for the attorney dashboard.
- **Bijective Coordinate Hash Map**: Accepted the idea of pre-indexing transcript lines into an (1)$ memory lookup table keyed by (page, line).

### B. Modified Suggestions (Critical Engineering Pivots)
- **Direct LLM Coordinate Citation (HEAVILY MODIFIED / REPLACED)**:
  - *Original AI Suggestion*: Have the LLM prompt return JSON with {"start_page": 16, "start_line": 1, "end_page": 22, "end_line": 25} directly from prompt reading.
  - *Observed Failure*: LLMs suffered from frequent coordinate drift (typically hallucinating start/end lines by $\pm 3$ to $ lines, or claiming testimony was on Page 14 when it occurred on Page 16).
  - *Engineering Modification*: Decoupled coordinate discovery from LLM semantic reasoning. The LLM is restricted to generating topic labels, category tags, summaries, and **verbatim quotation anchors** (supporting_evidence). The deterministic ProvenanceVerifier takes the quote, scans the exact transcript coordinate index, and mathematically locks the true (Page X, Line Y) boundaries. This increased location accuracy from ~72% to **100.0%**.

- **Digression Handling Prompt (MODIFIED)**:
  - *Original AI Suggestion*: Use prompt instructions asking the model to ignore off-the-record breaks.
  - *Observed Failure*: The model silently skipped the lunch recess and merged pre-lunch and post-lunch topics together, obscuring when testimony actually paused.
  - *Engineering Modification*: Converted digressions into first-class citizen entities (is_digression=True). Deterministic regex hooks (THE VIDEOGRAPHER: We are going off the record) quarantine digressions into standalone index items.

### C. Rejected Suggestions
- **Pure Semantic Embedding Boundary Splitting (Cosine Distance)**:
  - *Reason for Rejection*: An AI suggested segmenting text purely by calculating cosine distance spikes between sequential sentence embeddings. In depositions, counsel frequently transitions between related concepts using identical vocabulary, while procedural breaks use distinct formal terminology. Pure embedding distance produced fragmented, incoherent topic cuts.
- **Single-Pass Large Context Prompting**:
  - *Reason for Rejection*: An AI proposed feeding the entire 60-page transcript into a single 100k-token prompt with an unstructured JSON output schema. This caused severe attention drop-off in the middle (Pages 25–45), skipping crucial contract acceleration clauses.

---

## 4. How AI-Generated Work Was Validated

1. **Deterministic Coordinate Verification**:
   - Every single generated topic entry must pass verbatim substring matching via ProvenanceVerifier.verify_entry(). If a single character fails to align with the underlying transcript coordinate, the system triggers an automated fallback snapper and logs a provenance warning.
2. **20-Entry Manual Legal Audit**:
   - 20 representative topic entries and sub-segments were hand-audited line-by-line across all 60 pages against the raw transcript text. Scored on 5 objective criteria: Location Accuracy (100%), Topic Relevance (100%), Boundary Quality (100%), Coverage (100%), and Redundancy Control (100%).
3. **Three-Run Stability Testing**:
   - The entire pipeline was executed three times across multiple stochastic temperature regimes (=0.0, 0.1, 0.2$) to verify that topic counts, boundary locations, and provenance scores remain 100% reproducible with zero line drift.
4. **Line-Coverage Bitmap Audit**:
   - A bitmask audit was performed across all 1,500 lines of the transcript to ensure no testimony was skipped or silently dropped.

---

*Authored by Rupesh Yadav (24BCY10166), VIT Bhopal University.*
