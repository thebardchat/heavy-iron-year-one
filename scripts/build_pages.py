#!/usr/bin/env python3
"""Build the standalone GitHub Pages index.html from heavy-iron-updated.html.

heavy-iron-updated.html mirrors the live Claude artifact and carries a
frame-runtime wrapper meant for the claude.ai iframe sandbox (a <base href>
that would break relative URLs if served standalone, plus dead-weight JS).
This strips that wrapper, moves <title>/fonts/<style> into a proper <head>,
adds SEO/social meta tags and a favicon, and patches the existing switchTab()
function with URL hash routing so individual tabs are shareable/bookmarkable
deep links (e.g. index.html#launchtiming) with working back/forward.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "heavy-iron-updated.html"
OUTPUT = REPO_ROOT / "index.html"

FRAME_RUNTIME_END = "</style></head><body>"
BODY_START_MARKER = "<!-- MASTHEAD -->"
CLOSING = "</body></html>"

HASH_ROUTING_SCRIPT = """
<!-- HASH-BASED TAB NAVIGATION — deep links to any proposal tab -->
<script>
function activateFromHash() {
  var id = (location.hash || '').slice(1);
  if (!id) return;
  var btn = document.querySelector('.tab-btn[onclick*="\\'' + id + '\\'"]');
  var panel = document.getElementById('tab-' + id);
  if (btn && panel) switchTab(id, btn);
}
document.addEventListener('DOMContentLoaded', activateFromHash);
window.addEventListener('popstate', activateFromHash);
</script>
"""

HEAD_EXTRAS = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="SDVOSB heavy equipment business playbook: GSAxcess flywheel model, three business proposals, government bidding, veteran advantages, and a full Year One execution plan.">
<meta property="og:title" content="Heavy Iron / Year One">
<meta property="og:description" content="Federal surplus heavy equipment at 5-20% of replacement cost, built into a veteran-owned business flywheel. Three business proposals, launch timing, and a full Year One execution plan.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%9A%9C%3C/text%3E%3C/svg%3E">
"""

SWITCH_TAB_OLD = """function switchTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}"""

SWITCH_TAB_NEW = """function switchTab(id, btn) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
  if (history.replaceState) history.replaceState(null, '', location.pathname + location.search + '#' + id);
}"""


def build() -> str:
    content = SOURCE.read_text(encoding="utf-8")

    idx = content.index(FRAME_RUNTIME_END) + len(FRAME_RUNTIME_END)
    after_frame = content[idx:]

    bidx = after_frame.index(BODY_START_MARKER)
    head_meta = after_frame[:bidx].strip()
    body_content = after_frame[bidx:]

    assert head_meta.startswith("<title>Heavy Iron Year One</title>"), "head split point moved"
    assert head_meta.rstrip().endswith("</style>"), "head split point moved"
    assert body_content.rstrip().endswith(CLOSING), "body does not end with closing tags"

    if SWITCH_TAB_OLD not in body_content:
        sys.exit("switchTab() function not found verbatim — source file changed shape, update this script")
    body_content = body_content.replace(SWITCH_TAB_OLD, SWITCH_TAB_NEW)

    body_main = body_content.rstrip()[: -len(CLOSING)]

    output = (
        "<!doctype html>\n"
        '<html lang="en">\n'
        "<head>\n"
        f"{HEAD_EXTRAS}{head_meta}\n"
        "</head>\n"
        "<body>\n"
        f"{body_main}\n"
        f"{HASH_ROUTING_SCRIPT}\n"
        f"{CLOSING}\n"
    )
    return output


if __name__ == "__main__":
    OUTPUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
