# DepoIndex: Failure Analysis Report
**Candidate**: Rupesh Yadav | **Reg No**: 24BCY10166 | **College**: VIT Bhopal University
## Overview
Legal depositions present challenging text structures, including abrupt interruptions, sidebar objections, off-the-record breaks, multi-page continuation, and non-contiguous re-entries. Below is a detailed failure analysis of **three difficult edge cases** encountered during system development, explaining what occurred, root causes, and technical remedies implemented.

---

## Case 1: Digression Boundary Bleeding (Lunch Break)
### 1. What the System Produced
In early unconstrained LLM segmentation prototypes, the system merged the 12:14 PM lunch recess (Page 31, Lines 1–25) into the preceding 'Contract & Policy Negotiations' topic, extending its end boundary to Page 32 Line 25.
### 2. What it Should Have Produced
The system should have split the substantive topic at Page 30 Line 25, created a separate `Procedural Digression` entry for Page 31–32 (Lunch & Document Production), and initiated a `Re-entry Topic` for Contract Negotiations starting at Page 33 Line 1.
### 3. Why it Failed
The LLM relied solely on semantic embedding distance, which treated procedural phrases like *'Counsel, are you ready to take a brief lunch break?'* as minor transitions rather than hard procedural boundaries.
### 4. Technical Remediation
Implemented explicit regex pattern detectors for procedural anchors (`THE VIDEOGRAPHER: We are going off the record`, `Recess taken`, `Discussion off the record`). When detected, the segmenter forcibly creates a procedural digression node.

---

## Case 2: Multi-Page Topic Continuation Split
### 1. What the System Produced
When processing the 8-page testimony on 'Standard Operating Procedures' (Pages 39–46), an early sliding-window chunker fragmented the continuous discussion into three separate artificial topics: *'SOP-102 Payment Waterfall'*, *'SOP-204 Forbearance Steering'*, and *'SOP-309 Autodialer Collections'*.
### 2. What it Should Have Produced
A single consolidated top-level topic entry spanning Page 39 Line 1 to Page 46 Line 25 with SOP sub-segments nested inside, avoiding unnecessary topic proliferation in the legal index.
### 3. Why it Failed
The fixed window size of 3 pages forced premature boundary decisions before the complete SOP questioning was evaluated.
### 4. Technical Remediation
Implemented a two-pass hierarchical clustering engine: Pass 1 identifies fine-grained sub-topics, while Pass 2 aggregates contiguous sub-topics sharing the same core legal subject matter into unified multi-page topics.

---

## Case 3: Overlapping Subject Ambiguity (Servicing Agreement vs Relationship with Defendant)
### 1. What the System Produced
During testimony on Page 17 (servicing fee commissions), the system misclassified the segment as *'Contract Negotiations'* instead of *'Relationship with Defendant'*, because the witness referenced contract clause terms.
### 2. What it Should Have Produced
Topic label *'Relationship with Defendant (Servicing Fee Structure)'*, as the line of questioning concerned Vervent's operational profit model rather than the historical drafting of the contract.
### 3. Why it Failed
Keyword matching weighted the presence of contract clause numbers (`Section 4.02`) higher than the functional context of the Q&A examination.
### 4. Technical Remediation
Updated prompt context rules to prioritize the *examining attorney's core intent* and *witness testimony focus* over incidental document citations.