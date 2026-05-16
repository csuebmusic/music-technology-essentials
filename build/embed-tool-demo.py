"""
Re-embed the tool's demo audio as base64 inside the tool HTML.

When to run this:
  After regenerating assets/audio/module-02-week-05/dynamic-tool-demo.wav
  (typically by running build/generate-audio-demos-week-05.py), if you
  want the tool's embedded copy to reflect the new audio.

What it does:
  Reads the canonical WAV, base64-encodes it, and replaces the contents
  of the <script type="application/octet-stream" id="demo-audio-b64">
  block inside the tool HTML with the fresh data. No other parts of the
  tool are touched.

Why the tool has an embedded copy:
  Browsers block fetch() across origins under the file:// protocol, so
  fetching a sibling WAV from the tool's HTML fails when the page is
  opened by double-clicking. Embedding the WAV inside the HTML sidesteps
  that entirely. The trade-off is the HTML file grows from ~30 KB to
  ~1.4 MB, which is fine for a teaching tool loaded once per session.

Re-run with: python3 build/embed-tool-demo.py
"""

import base64
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WAV_PATH = os.path.join(REPO_ROOT, "assets", "audio", "module-02-week-05",
                        "dynamic-tool-demo.wav")
TOOL_PATH = os.path.join(REPO_ROOT, "module-02-audio-editing-mixing",
                         "lessons", "08-tool-mixing-dynamics.html")


def main():
    if not os.path.isfile(WAV_PATH):
        raise FileNotFoundError(
            f"Demo WAV not found at {WAV_PATH}. "
            "Run build/generate-audio-demos-week-05.py first."
        )
    if not os.path.isfile(TOOL_PATH):
        raise FileNotFoundError(f"Tool HTML not found at {TOOL_PATH}.")

    # Read WAV, base64-encode, wrap at 100 chars per line
    with open(WAV_PATH, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    wrapped = "\n".join(b64[i:i + 100] for i in range(0, len(b64), 100))

    # Splice the new b64 content into the existing block. The block opens
    # with <script type="application/octet-stream" id="demo-audio-b64"> on
    # its own line, contains base64 lines, and closes with </script>.
    src = open(TOOL_PATH).read()
    pattern = re.compile(
        r'(<script type="application/octet-stream" id="demo-audio-b64">\n)'
        r'.*?'
        r'(\n</script>)',
        re.DOTALL,
    )
    new_src, n_subs = pattern.subn(
        lambda m: m.group(1) + wrapped + m.group(2),
        src,
        count=1,
    )

    if n_subs != 1:
        raise RuntimeError(
            "Could not find the demo-audio-b64 <script> block in the tool. "
            "Has the block's id changed?"
        )

    if new_src == src:
        print("Embedded audio is already up to date. No changes written.")
        return

    open(TOOL_PATH, "w").write(new_src)
    wav_kb = os.path.getsize(WAV_PATH) / 1024
    tool_kb = os.path.getsize(TOOL_PATH) / 1024
    print(f"Re-embedded {wav_kb:.0f} KB WAV -> tool is now {tool_kb:.0f} KB")


if __name__ == "__main__":
    main()
