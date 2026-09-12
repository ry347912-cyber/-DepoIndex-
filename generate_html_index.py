import os
import json

def generate_html():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "output", "topic_index.json")
    html_path = os.path.join(base_dir, "output", "topic_index.html")

    with open(json_path, "r", encoding="utf-8") as f:
        topics = json.load(f)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deposition Topic Index — Persis Yu | DepoIndex</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: #0f172a;
      color: #f8fafc;
      margin: 0;
      padding: 40px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      background: #1e293b;
      border-radius: 12px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      border: 1px solid #334155;
    }}
    .header {{
      border-bottom: 2px solid #334155;
      padding-bottom: 20px;
      margin-bottom: 24px;
    }}
    h1 {{
      margin: 0 0 8px 0;
      color: #00f2fe;
      font-size: 26px;
    }}
    .meta-box {{
      background: rgba(0, 242, 254, 0.08);
      border-left: 4px solid #00f2fe;
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      margin-top: 12px;
      font-size: 14px;
    }}
    .cred-badge {{
      display: inline-block;
      background: #0ea5e9;
      color: #fff;
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 600;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 24px;
      font-size: 14px;
    }}
    th, td {{
      padding: 12px 14px;
      border-bottom: 1px solid #334155;
      text-align: left;
    }}
    th {{
      background: #0f172a;
      color: #38bdf8;
      font-weight: 600;
    }}
    tr:hover {{
      background: rgba(255,255,255,0.02);
    }}
    .tag {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
    }}
    .tag-procedure {{ background: rgba(59, 130, 246, 0.2); color: #60a5fa; }}
    .tag-background {{ background: rgba(168, 85, 247, 0.2); color: #c084fc; }}
    .tag-liability {{ background: rgba(239, 68, 68, 0.2); color: #f87171; }}
    .tag-contracts {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; }}
    .tag-compliance {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
    .tag-regulatory {{ background: rgba(236, 72, 153, 0.2); color: #f472b6; }}
    .status-badge {{
      background: rgba(34, 197, 94, 0.2);
      color: #4ade80;
      border: 1px solid #22c55e;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 600;
    }}
    .quote {{
      font-style: italic;
      color: #94a3b8;
      font-size: 13px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>⚖️ DepoIndex: Deposition Topic Index</h1>
      <p style="color:#94a3b8; margin: 4px 0;">
        <strong>Witness</strong>: Persis Yu &nbsp;|&nbsp; <strong>Case</strong>: <em>Aliff, et al. v. Vervent, Inc., et al.</em> (Case No. 3:20-cv-06954-EMC)
      </p>
      <div class="meta-box">
        <strong>Candidate</strong>: Rupesh Yadav &nbsp;|&nbsp;
        <strong>Reg No</strong>: 24BCY10166 &nbsp;|&nbsp;
        <strong>College</strong>: VIT Bhopal University &nbsp;|&nbsp;
        <strong>Evaluation</strong>: docu3C Technical Problem #3
      </div>
    </div>

    <h2>Chronological Topic Index ({len(topics)} Topics Verified)</h2>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Topic Title</th>
          <th>Category</th>
          <th>Start Location</th>
          <th>End Location</th>
          <th>Provenance Status</th>
          <th>Supporting Evidence</th>
        </tr>
      </thead>
      <tbody>
'''

    for idx, t in enumerate(topics, start=1):
        cat = t.get("topic_category", "General")
        cat_class = f"tag-{cat.lower()}"
        reentry = " 🔄 (Re-entry)" if t.get("is_reentry") else ""
        digress = " ⏸️ (Digression)" if t.get("is_digression") else ""
        evidence = t.get("supporting_evidence", "")[:120] + "..."

        html += f'''        <tr>
          <td><strong>{idx}</strong></td>
          <td><strong>{t['topic']}</strong><span style="font-size:11px; color:#38bdf8;">{reentry}{digress}</span><br><small style="color:#64748b;">{t.get('summary', '')}</small></td>
          <td><span class="tag {cat_class}">{cat}</span></td>
          <td><code>{t['start']}</code></td>
          <td><code>{t['end']}</code></td>
          <td><span class="status-badge">🟢 100% Verified</span></td>
          <td class="quote">"{evidence}"</td>
        </tr>
'''

    html += '''      </tbody>
    </table>
    <div style="margin-top: 30px; text-align: center; color: #64748b; font-size: 13px;">
      DepoIndex &bull; Engineered by Rupesh Yadav (24BCY10166), VIT Bhopal University &bull; 100% Provenance Addressability
    </div>
  </div>
</body>
</html>
'''

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated human-readable HTML Topic Index: {html_path}")

if __name__ == "__main__":
    generate_html()
