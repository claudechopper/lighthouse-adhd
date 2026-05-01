"""Convert lighthouse-audit-design.md to a clean designed PDF."""
import re
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, ListFlowable, ListItem, KeepTogether,
)

ROOT = Path("/Users/Claude/ADHD/ADHD Workflow")
SRC = ROOT / "lighthouse-audit-design.md"
OUT = ROOT / "lighthouse-audit-design.pdf"

# ---------- Styles ----------
styles = getSampleStyleSheet()

NAVY = HexColor("#0b3d91")
TEXT = HexColor("#1a1a1a")
MUTED = HexColor("#555555")
ACCENT = HexColor("#b87a18")
TABLE_HEADER_BG = HexColor("#0b3d91")
TABLE_HEADER_FG = HexColor("#ffffff")
TABLE_ROW_ALT = HexColor("#f6f4ee")

title_style = ParagraphStyle("TitleBig", parent=styles["Title"],
    fontSize=24, leading=28, spaceAfter=4, textColor=TEXT)
subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"],
    fontSize=11, leading=14, spaceAfter=20, textColor=MUTED)
h1 = ParagraphStyle("H1", parent=styles["Heading1"],
    fontSize=18, leading=22, spaceBefore=22, spaceAfter=10,
    textColor=NAVY, keepWithNext=True)
h2 = ParagraphStyle("H2", parent=styles["Heading2"],
    fontSize=14, leading=18, spaceBefore=14, spaceAfter=6,
    textColor=TEXT, keepWithNext=True)
h3 = ParagraphStyle("H3", parent=styles["Heading3"],
    fontSize=12, leading=16, spaceBefore=10, spaceAfter=4,
    textColor=TEXT, keepWithNext=True)
body = ParagraphStyle("Body", parent=styles["Normal"],
    fontSize=10.5, leading=15, spaceAfter=8, alignment=TA_LEFT)
small = ParagraphStyle("Small", parent=styles["Normal"],
    fontSize=9.5, leading=13, spaceAfter=6, textColor=MUTED)
mono = ParagraphStyle("Mono", parent=styles["Code"],
    fontSize=8.5, leading=11.5, spaceAfter=10,
    fontName="Courier",
    backColor=HexColor("#f4f4f4"), borderPadding=8,
    leftIndent=6, rightIndent=6)
quote = ParagraphStyle("Quote", parent=styles["Normal"],
    fontSize=10.5, leading=15, spaceAfter=10,
    leftIndent=14, rightIndent=14,
    textColor=MUTED, fontName="Helvetica-Oblique")

# ---------- Helpers ----------
def md_inline(s: str) -> str:
    """Convert markdown inline to reportlab markup."""
    # bold
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    # italic
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
    # inline code
    s = re.sub(r"`([^`]+)`", r"<font face='Courier'>\1</font>", s)
    # arrows / em-dashes already display fine
    # & must be escaped for reportlab XML
    # but bold/italic tags use <>... so we need to be careful
    # ReportLab uses XML-like markup, so escape stray & and unsafe < / >
    return s

def make_table(rows, col_widths=None):
    """Render a markdown-style table as a styled Table flowable."""
    # rows[0] is header
    data = []
    for i, row in enumerate(rows):
        data.append([Paragraph(md_inline(c), small if i > 0 else body) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("TEXTCOLOR", (0, 0), (-1, 0), TABLE_HEADER_FG),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, NAVY),
        ("LINEBELOW", (0, 1), (-1, -2), 0.25, HexColor("#dddddd")),
    ]
    # Alternating row backgrounds
    for r in range(1, len(data)):
        if r % 2 == 0:
            style.append(("BACKGROUND", (0, r), (-1, r), TABLE_ROW_ALT))
    t.setStyle(TableStyle(style))
    return t

# ---------- Parse markdown into flowables ----------
def parse_markdown(text):
    flowables = []
    lines = text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip blank lines
        if not line.strip():
            i += 1
            continue

        # Code fence
        if line.startswith("```"):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(code_lines)
            code_html = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            code_html = code_html.replace("\n", "<br/>").replace(" ", "&nbsp;")
            flowables.append(Paragraph(code_html, mono))
            continue

        # Horizontal rule
        if re.match(r"^---+$", line.strip()):
            flowables.append(Spacer(1, 12))
            i += 1
            continue

        # Headings
        if line.startswith("# "):
            flowables.append(Paragraph(md_inline(line[2:]), title_style))
            i += 1
            continue
        if line.startswith("## "):
            flowables.append(Paragraph(md_inline(line[3:]), h1))
            i += 1
            continue
        if line.startswith("### "):
            flowables.append(Paragraph(md_inline(line[4:]), h2))
            i += 1
            continue
        if line.startswith("#### "):
            flowables.append(Paragraph(md_inline(line[5:]), h3))
            i += 1
            continue

        # Table
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[i+1]):
            table_lines = [line]
            i += 2  # skip separator
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = []
            for tl in table_lines:
                cells = [c.strip() for c in tl.strip().strip("|").split("|")]
                rows.append(cells)
            # Header column widths: equal split for now
            n = len(rows[0])
            page_w = letter[0] - 1.5 * inch
            cw = [page_w / n] * n
            flowables.append(make_table(rows, cw))
            flowables.append(Spacer(1, 8))
            continue

        # Bullet list
        if re.match(r"^[\-\*] ", line):
            items = []
            while i < len(lines) and re.match(r"^[\-\*] ", lines[i]):
                content = lines[i][2:]
                items.append(ListItem(Paragraph(md_inline(content), body),
                                      leftIndent=12))
                i += 1
            flowables.append(ListFlowable(items, bulletType="bullet",
                                          start="•", leftIndent=14,
                                          bulletFontSize=9))
            continue

        # Numbered list
        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                content = re.sub(r"^\d+\. ", "", lines[i])
                items.append(ListItem(Paragraph(md_inline(content), body),
                                      leftIndent=12))
                i += 1
            flowables.append(ListFlowable(items, bulletType="1",
                                          leftIndent=18))
            continue

        # Blockquote
        if line.startswith("> "):
            quote_lines = []
            while i < len(lines) and (lines[i].startswith("> ") or lines[i] == ">"):
                quote_lines.append(lines[i].lstrip(">").lstrip())
                i += 1
            text_block = " ".join(l for l in quote_lines if l)
            flowables.append(Paragraph(md_inline(text_block), quote))
            continue

        # Regular paragraph
        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", "- ", "* ", "> ", "|", "```")) and not re.match(r"^\d+\. ", lines[i]):
            para_lines.append(lines[i])
            i += 1
        text_block = " ".join(para_lines)
        flowables.append(Paragraph(md_inline(text_block), body))

    return flowables

# ---------- Build ----------
text = SRC.read_text()
flowables = parse_markdown(text)

doc = SimpleDocTemplate(
    str(OUT), pagesize=letter,
    leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    topMargin=0.75 * inch, bottomMargin=0.75 * inch,
    title="The Lighthouse Audit — design doc v0.1",
    author="Claudechopper",
)
doc.build(flowables)
print(f"Wrote: {OUT}  ({OUT.stat().st_size} bytes)")
