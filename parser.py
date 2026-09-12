import re
import os

class DepositionParser:
    """
    Parses legal deposition transcripts formatted with 'PAGE X' headers
    and line numbers (1..25) per page.
    Maintains a strict coordinate index: (page, line) -> text.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines_by_coord = {} # (page, line) -> text
        self.coords_by_line_idx = [] # list of (page, line, text)
        self.pages = {} # page -> dict of line -> text
        self.raw_text = ""
        self._parse()

    def _parse(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Deposition transcript file not found at {self.filepath}")

        with open(self.filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        self.raw_text = "".join(lines)
        current_page = None
        
        for raw_line in lines:
            line_str = raw_line.rstrip('\r\n')
            
            # Match Page header: "PAGE X" or "Page X"
            page_match = re.match(r"^\s*PAGE\s+(\d+)", line_str, re.IGNORECASE)
            if page_match:
                current_page = int(page_match.group(1))
                if current_page not in self.pages:
                    self.pages[current_page] = {}
                continue

            if current_page is None:
                continue

            # Match Line number prefix: e.g. " 1  TEXT", "25  TEXT", " 4"
            line_match = re.match(r"^\s*(\d{1,2})(?:\s+(.*))?$", line_str)
            if line_match:
                line_num = int(line_match.group(1))
                text = (line_match.group(2) or "").strip()
                
                # Store all lines 1 to 25
                if 1 <= line_num <= 25:
                    self.lines_by_coord[(current_page, line_num)] = text
                    self.pages[current_page][line_num] = text
                    self.coords_by_line_idx.append((current_page, line_num, text))

    def get_line_text(self, page, line):
        return self.lines_by_coord.get((page, line), "")

    def get_text_range(self, start_page, start_line, end_page, end_line):
        """
        Returns all lines between (start_page, start_line) and (end_page, end_line) inclusive.
        """
        results = []
        in_range = False
        
        for page, line, text in self.coords_by_line_idx:
            if page == start_page and line == start_line:
                in_range = True
            
            if in_range:
                results.append({
                    "page": page,
                    "line": line,
                    "text": text
                })

            if page == end_page and line == end_line:
                break
                
        return results

    def find_excerpt_location(self, snippet):
        """
        Searches for a verbatim or fuzzy snippet in the transcript and returns
        the exact matching (start_page, start_line, end_page, end_line).
        """
        snippet_clean = re.sub(r'\s+', ' ', snippet.strip().lower())
        if not snippet_clean:
            return None

        full_coords = [item for item in self.coords_by_line_idx if item[2]] # Non-empty lines
        for i in range(len(full_coords)):
            window_text = ""
            for j in range(i, min(i + 15, len(full_coords))):
                window_text += " " + full_coords[j][2]
                window_clean = re.sub(r'\s+', ' ', window_text.strip().lower())
                
                if snippet_clean in window_clean:
                    start_p, start_l, _ = full_coords[i]
                    end_p, end_l, _ = full_coords[j]
                    return {
                        "start_page": start_p,
                        "start_line": start_l,
                        "end_page": end_p,
                        "end_line": end_l,
                        "match_score": 1.0
                    }

        # Fallback substring match
        words = snippet_clean.split()
        if len(words) >= 3:
            sub_snippet = " ".join(words[:3])
            for i in range(len(full_coords)):
                if sub_snippet in full_coords[i][2].lower():
                    start_p, start_l, _ = full_coords[i]
                    end_idx = min(i + max(1, len(words) // 4), len(full_coords) - 1)
                    end_p, end_l, _ = full_coords[end_idx]
                    return {
                        "start_page": start_p,
                        "start_line": start_l,
                        "end_page": end_p,
                        "end_line": end_l,
                        "match_score": 0.85
                    }

        return None

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "persis_yu_deposition.txt")
    parser = DepositionParser(data_path)
    print(f"Parsed {len(parser.pages)} pages, total line entries: {len(parser.lines_by_coord)}")
    sample_text = parser.get_text_range(4, 1, 4, 5)
    print("Sample lines (P4 L1-5):", sample_text)
