import unittest
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from parser import DepositionParser
from segmenter import TopicSegmenter
from verifier import ProvenanceVerifier
from stability_analyzer import StabilityAnalyzer

class TestDepoIndexPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.data_path = os.path.join(cls.base_dir, "data", "persis_yu_deposition.txt")
        cls.parser = DepositionParser(cls.data_path)
        cls.segmenter = TopicSegmenter(cls.parser)
        cls.verifier = ProvenanceVerifier(cls.parser)

    def test_parser_page_and_line_counts(self):
        """Verify parser correctly ingests all 60 pages and 1,500 lines."""
        self.assertEqual(len(self.parser.pages), 60)
        self.assertEqual(len(self.parser.lines_by_coord), 1500)

    def test_coordinate_addressability(self):
        """Verify random-access line coordinate lookup."""
        line_text = self.parser.get_line_text(1, 1)
        self.assertIn("IN THE UNITED STATES DISTRICT COURT", line_text)
        
        witness_line = self.parser.get_line_text(1, 12)
        self.assertIn("PERSIS YU", witness_line)
        
        exhibit_line = self.parser.get_line_text(4, 23)
        self.assertTrue(len(exhibit_line) > 0)

    def test_segmentation_topic_structure(self):
        """Verify segmenter generates topic records with required fields."""
        topics = self.segmenter.segment_transcript()
        self.assertGreaterEqual(len(topics), 10)
        
        for t in topics:
            self.assertIn("topic", t)
            self.assertIn("start_page", t)
            self.assertIn("start_line", t)
            self.assertIn("end_page", t)
            self.assertIn("end_line", t)
            self.assertIn("supporting_evidence", t)
            self.assertLessEqual(t["start_page"], t["end_page"])

    def test_provenance_verification_100pct(self):
        """Verify deterministic provenance verifier achieves 100% verification rate."""
        topics = self.segmenter.segment_transcript()
        verified_topics, report = self.verifier.verify_index(topics)
        self.assertEqual(report["verification_rate_pct"], 100.0)
        self.assertEqual(report["verified_entries"], len(topics))

    def test_three_run_stability(self):
        """Verify 3-run stability test yields zero count variance and zero line drift."""
        analyzer = StabilityAnalyzer(self.parser, self.segmenter, self.verifier)
        runs, comp = analyzer.run_stability_test()
        self.assertEqual(comp["count_variance"], 0)
        self.assertEqual(comp["average_boundary_line_drift"], 0.0)
        self.assertEqual(comp["provenance_accuracy_all_runs_pct"], 100.0)

    def test_presentation_deck_exists(self):
        """Verify that the 5-slide PowerPoint deck exists and has valid size."""
        pptx_path = os.path.join(self.base_dir, "slides", "DepoIndex_Presentation.pptx")
        self.assertTrue(os.path.exists(pptx_path))
        self.assertGreater(os.path.getsize(pptx_path), 10000)

if __name__ == "__main__":
    unittest.main()
