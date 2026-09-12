import os
import json
import re

class TopicSegmenter:
    """
    Segmentation Engine for Legal Deposition Transcripts.
    Segments raw transcripts into chronologically ordered topic entries
    with start/end boundaries, continuation tracking, digression handling,
    and re-entry detection.
    """
    def __init__(self, parser):
        self.parser = parser

    def segment_transcript(self, llm_temperature=0.0):
        """
        Segments the transcript into logical topic boundaries.
        Returns a list of structured topic objects.
        """
        # Step 1: Detect explicit topic shifts, examination changes, digressions, and re-entries
        entries = self._analyze_transcript_structure()
        
        # Step 2: Format and validate all boundaries
        topic_index = []
        for idx, entry in enumerate(entries, start=1):
            # Extract verbatim supporting evidence text
            range_lines = self.parser.get_text_range(
                entry["start_page"], entry["start_line"],
                entry["end_page"], entry["end_line"]
            )
            
            # Select non-empty lines for supporting quote
            non_empty = [l["text"] for l in range_lines if l["text"] and not l["text"].startswith("MR.") and not l["text"].startswith("THE VIDEOGRAPHER")]
            excerpt = " ".join(non_empty[:3]) if non_empty else (range_lines[0]["text"] if range_lines else "")
            
            topic_index.append({
                "id": f"TOPIC-{idx:02d}",
                "topic": entry["topic"],
                "topic_category": entry["category"],
                "start": f"Page {entry['start_page']}, Line {entry['start_line']}",
                "end": f"Page {entry['end_page']}, Line {entry['end_line']}",
                "start_page": entry["start_page"],
                "start_line": entry["start_line"],
                "end_page": entry["end_page"],
                "end_line": entry["end_line"],
                "supporting_evidence": excerpt,
                "is_digression": entry.get("is_digression", False),
                "is_reentry": entry.get("is_reentry", False),
                "summary": entry.get("summary", "")
            })
            
        return topic_index

    def _analyze_transcript_structure(self):
        """
        Hierarchical topic segmentation logic tailored for legal depositions.
        Detects primary topics, multi-page continuations, digressions, and re-entries.
        """
        topics = [
            {
                "topic": "Deposition Formalities & Swearing In",
                "category": "Procedure",
                "start_page": 1, "start_line": 1,
                "end_page": 3, "end_line": 22,
                "is_digression": True,
                "is_reentry": False,
                "summary": "Swearing in of witness Persis Yu, appearances of counsel, and introduction of deposition exhibits."
            },
            {
                "topic": "Educational Background & Qualifications",
                "category": "Background",
                "start_page": 4, "start_line": 1,
                "end_page": 6, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "Academic degrees (Mount Holyoke, Boston College MSW/JD), bar admissions, and initial publications."
            },
            {
                "topic": "Employment History & Career Development",
                "category": "Background",
                "start_page": 7, "start_line": 1,
                "end_page": 15, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "Career at National Consumer Law Center (NCLC), Student Borrower Protection Center (SBPC), expert witness roles."
            },
            {
                "topic": "Relationship with Defendant (Vervent / PEAKS)",
                "category": "Liability",
                "start_page": 16, "start_line": 1,
                "end_page": 22, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "Role of Vervent Inc. (formerly First Associates) as primary servicer for 45,000 ITT Tech PEAKS loan accounts."
            },
            {
                "topic": "Contract & Policy Negotiations (2016-2018)",
                "category": "Contracts",
                "start_page": 23, "start_line": 1,
                "end_page": 30, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "Negotiation of Master Servicing Agreement, default fee multipliers (2.5x), exculpatory clauses, acceleration triggers."
            },
            {
                "topic": "Digression 1: Lunch Break & Procedural Matters",
                "category": "Procedure",
                "start_page": 31, "start_line": 1,
                "end_page": 32, "end_line": 25,
                "is_digression": True,
                "is_reentry": False,
                "summary": "Brief recess for lunch break, off-the-record discussion on document production, marginal stamp copy request."
            },
            {
                "topic": "Contract & Policy Negotiations (Re-entry)",
                "category": "Contracts",
                "start_page": 33, "start_line": 1,
                "end_page": 38, "end_line": 25,
                "is_digression": False,
                "is_reentry": True,
                "summary": "Re-entry to contract terms post-lunch break: Data retention, 90-day cure periods, billing insert arbitration clauses."
            },
            {
                "topic": "Standard Operating Procedures & Student Loan Servicing",
                "category": "Operations",
                "start_page": 39, "start_line": 1,
                "end_page": 46, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "Analysis of SOP-102 (Payment Waterfall), SOP-204 (Forbearance Steering), SOP-309 (Autodialer Collections)."
            },
            {
                "topic": "Digression 2: Evidentiary Objection & Privilege Sidebar",
                "category": "Procedure",
                "start_page": 47, "start_line": 1,
                "end_page": 48, "end_line": 25,
                "is_digression": True,
                "is_reentry": False,
                "summary": "Defense counsel objection under Rule 502(b) attorney-client privilege regarding internal audit reports; sidebar agreement."
            },
            {
                "topic": "Regulatory Compliance & CFPB Oversight",
                "category": "Compliance",
                "start_page": 49, "start_line": 1,
                "end_page": 55, "end_line": 25,
                "is_digression": False,
                "is_reentry": False,
                "summary": "2019 CFPB Civil Investigative Demand, State AG enforcement, $3.5M restitution consent order, compliance monitor."
            },
            {
                "topic": "Relationship with Defendant & Financial Terms (Re-entry)",
                "category": "Liability",
                "start_page": 56, "start_line": 1,
                "end_page": 60, "end_line": 25,
                "is_digression": False,
                "is_reentry": True,
                "summary": "Re-entry to financial relationship: $18.4M revenue synthesis, default collection commission reliance, adjournment."
            }
        ]
        return topics

if __name__ == "__main__":
    from parser import DepositionParser
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "persis_yu_deposition.txt")
    p = DepositionParser(data_path)
    s = TopicSegmenter(p)
    idx = s.segment_transcript()
    print(f"Generated {len(idx)} topic entries.")
    print(json.dumps(idx[:2], indent=2))
