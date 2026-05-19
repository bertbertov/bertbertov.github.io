"""Generate per-app privacy policy HTML pages from the shared template.

History:
- 2026-05-19 v1: 10 apps shipped.
- 2026-05-19 v2: Killed 4 apps after on-device QA failed product-fit (manga had no
  content path, lensbox couldn't beat PhotoPills, stutter was commodity vs phone's
  stock timer, stagecue was a toy without BLE multi-device sync). 6 apps remain
  active (3 of which are deferred until v2 features land — pawpath/bivouac/hanzi).
"""
from pathlib import Path

ROOT = Path(__file__).parent

TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Privacy Policy &mdash; {{APP_NAME}}</title>
<style>
  :root { color-scheme: dark; }
  html, body { background:#000; color:#E8E2D8; margin:0; padding:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; line-height:1.55; }
  main { max-width: 720px; margin: 0 auto; padding: 48px 24px 96px; }
  h1 { font-size: 28px; font-weight: 800; letter-spacing: -0.5px; margin: 0 0 8px; }
  h2 { font-size: 16px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: {{ACCENT}}; margin: 32px 0 8px; }
  p, li { font-size: 16px; }
  ul { padding-left: 22px; }
  .meta { color:#8B8378; font-size: 13px; letter-spacing: 0.4px; margin-bottom: 32px; }
  a { color: {{ACCENT}}; text-decoration: none; }
  a:hover { text-decoration: underline; }
  hr { border: 0; border-top: 1px solid #1F1F1F; margin: 40px 0; }
  .pill { display:inline-block; padding:3px 10px; border:1px solid #2A2A2A; border-radius:999px; color:#8B8378; font-size:11px; letter-spacing:1.2px; text-transform:uppercase; }
</style>
</head>
<body>
<main>
  <span class="pill">{{APP_NAME}}</span>
  <h1>Privacy Policy</h1>
  <p class="meta">Last updated: 19 May 2026 &middot; Developer: Albert Kamalov &middot; Contact: <a href="mailto:bertbertov@gmail.com">bertbertov@gmail.com</a></p>
  <h2>Summary</h2>
  <p>{{APP_NAME}} collects no personal data. Everything stays on your device. No accounts, no cloud sync, no ads, no analytics, no telemetry.</p>
  <h2>What data {{APP_NAME}} handles</h2>
  {{DATA_BLOCK}}
  <h2>Permissions used</h2>
  {{PERMS_BLOCK}}
  <h2>What we never collect</h2>
  <ul>
    <li>Your name, email, phone number, or any other identifier.</li>
    <li>Your location (unless explicitly noted in &ldquo;Permissions used&rdquo; above).</li>
    <li>Device identifiers, advertising IDs, or anything that could uniquely identify you.</li>
    <li>Crash reports, usage analytics, behavioral telemetry &mdash; none of it.</li>
  </ul>
  <h2>Third parties</h2>
  <p>{{APP_NAME}} contains no third-party SDKs that transmit data. There are no analytics providers, no ad networks, no crash reporters, no remote configuration services.</p>
  <h2>Children</h2>
  <p>{{APP_NAME}} is not directed at children under 13. Since the app collects no personal data, no special protections under COPPA / GDPR-K are required, but you should still use your own judgment about whether this app is appropriate for the child in your care.</p>
  <h2>Your data, your control</h2>
  <p>All data {{APP_NAME}} stores lives in a local database on your device. To delete everything: uninstall the app. Android removes the local database when the app is uninstalled.</p>
  <p>If you have Google Drive automatic backup enabled in Android Settings, an encrypted copy of the app&rsquo;s local data may be included in your system-level Google backup. That backup is controlled by Google&rsquo;s privacy policy, not by {{APP_NAME}}, and is restored only if you reinstall on a new device while signed in to the same Google account.</p>
  <h2>Changes to this policy</h2>
  <p>If this policy changes, the &ldquo;Last updated&rdquo; date above will change. Material changes (e.g. if a future version adds optional cloud sync) will be disclosed in the app&rsquo;s release notes on Google Play before the changed version ships.</p>
  <hr />
  <p class="meta">Questions? Email <a href="mailto:bertbertov@gmail.com">bertbertov@gmail.com</a>.</p>
</main>
</body>
</html>
"""

APPS = {
    'nightwake': {
        'name': 'Nightwake',
        'accent': '#FF6B35',
        'data': (
            '<ul>'
            '<li><b>Feeds, diapers, and sleep entries</b> you log are stored in a local SQLite database on your device.</li>'
            '<li>Entries include the time of day, duration, side (for feeds), outcome (for diapers), and any optional notes you type.</li>'
            '<li>No part of this data leaves your device. There is no account, no sync, no upload, no transmission.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Nightwake requests no runtime permissions in v1. The app works fully offline.</p>'
        ),
    },
    'tideglass': {
        'name': 'Tideglass',
        'accent': '#3FBAC2',
        'data': (
            '<ul>'
            '<li>The list of <b>spots</b> you save (each with a name, latitude, longitude, and tide-station reference) is stored locally.</li>'
            '<li>Tide predictions are computed entirely on-device using harmonic constituents bundled with the app for 12 reference stations (NOAA / UKHO public data).</li>'
            '<li>No network request is ever made.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Tideglass requests no runtime permissions. Coordinates are entered manually by you when adding a spot.</p>'
        ),
    },
    'kalimba': {
        'name': 'Kalimba Tuner',
        'accent': '#D4A24A',
        'data': (
            '<ul>'
            '<li>Kalimba Tuner records audio in real time only while you have the tuner screen open.</li>'
            '<li>The audio buffer is processed in memory by an on-device pitch-detection algorithm (YIN). Frequency, note, and cents-off-pitch are derived and shown on screen.</li>'
            '<li>The raw audio is <b>never written to disk</b>, <b>never uploaded</b>, and <b>never shared with any third party</b>. When you leave the tuner screen, the audio buffer is discarded.</li>'
            '</ul>'
        ),
        'perms': (
            '<ul>'
            '<li><b>RECORD_AUDIO</b> &mdash; required to detect the pitch of the tine you pluck. The microphone stream is processed entirely on-device, never recorded to a file, and never transmitted. You may revoke this permission at any time in Android Settings; the app will simply stop displaying pitch.</li>'
            '</ul>'
        ),
    },
    'pawpath': {
        'name': 'Pawpath',
        'accent': '#3FB47A',
        'data': (
            '<ul>'
            '<li>The dogs you add (name, optional notes) and the walks you log (start time, duration, count of pee / poop / play taps) are stored locally on your device.</li>'
            '<li>No part of this data leaves your device. There is no account, no sync, no upload.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Pawpath requests no runtime permissions in v1. GPS-route recording is planned for v2 and will be a clearly opt-in feature with a separate runtime permission prompt; until then the app does not access your location.</p>'
        ),
    },
    'hanzi': {
        'name': 'Hanzi Drill',
        'accent': '#C84B3F',
        'data': (
            '<ul>'
            '<li>The 30-character HSK 1 deck is bundled inside the app.</li>'
            '<li>Your finger-trace strokes are held only in memory while you are on the drill screen and are discarded when you tap &ldquo;Next character&rdquo;.</li>'
            '<li>Nothing is saved between sessions, nothing is uploaded.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Hanzi Drill requests no runtime permissions.</p>'
        ),
    },
    'bivouac': {
        'name': 'Bivouac',
        'accent': '#6BB6FF',
        'data': (
            '<ul>'
            '<li>The waypoints you save (name, latitude, longitude, optional elevation and notes) are stored locally.</li>'
            '<li>When you tap &ldquo;Export GPX&rdquo;, the app writes a standard GPX 1.1 file to the app&rsquo;s private cache and opens Android&rsquo;s system share-sheet so <i>you</i> choose where to send it (email, cloud drive, mapping app, etc.). Bivouac does not transmit the file itself.</li>'
            '<li>When you tap &ldquo;Share waypoint&rdquo;, only the text you see on the detail screen is handed to the system share-sheet.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Bivouac requests no runtime permissions in v1. Coordinates are entered manually. GPS-track recording is planned for v2 and will be a clearly opt-in feature with a separate runtime permission prompt; until then the app does not access your location.</p>'
        ),
    },
}

# 4 apps killed 2026-05-19 after on-device QA: Manga Offline (no content path),
# Lensbox (PhotoPills wins), Stutter (commodity), Stage Cue (toy without BLE sync).
# Their privacy pages were removed; old code archived at App/_killed_2026_05_19/.


def main():
    out_dir = ROOT / 'privacy'
    for slug, app in APPS.items():
        html = (TPL
                .replace('{{APP_NAME}}', app['name'])
                .replace('{{ACCENT}}', app['accent'])
                .replace('{{DATA_BLOCK}}', app['data'])
                .replace('{{PERMS_BLOCK}}', app['perms']))
        p = out_dir / f'{slug}.html'
        p.write_text(html, encoding='utf-8')
        print(f'wrote {p.name}  {p.stat().st_size}b')

    # Index page so the domain root doesn't 404
    idx = ROOT / 'index.html'
    idx.write_text(_index_html(), encoding='utf-8')
    print(f'wrote index.html  {idx.stat().st_size}b')

    # Index page for /privacy/ folder
    pidx = ROOT / 'privacy' / 'index.html'
    pidx.write_text(_privacy_index_html(), encoding='utf-8')
    print(f'wrote privacy/index.html  {pidx.stat().st_size}b')


def _index_html():
    rows = '\n'.join(
        f'<li><a href="privacy/{slug}.html">{a["name"]}</a></li>'
        for slug, a in APPS.items()
    )
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Albert Kamalov &mdash; Apps</title>
<style>
  html,body{{background:#000;color:#E8E2D8;margin:0;font-family:-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.55}}
  main{{max-width:640px;margin:0 auto;padding:48px 24px 96px}}
  h1{{font-size:24px;font-weight:800;letter-spacing:-0.4px;margin:0 0 8px}}
  p{{color:#A89D8E;font-size:14px}}
  ul{{list-style:none;padding:0;margin:32px 0 0}}
  li{{padding:14px 0;border-top:1px solid #1F1F1F;font-size:16px}}
  a{{color:#E8E2D8;text-decoration:none}}
  a:hover{{color:#FF6B35}}
</style></head><body><main>
<h1>Albert Kamalov &mdash; Android apps</h1>
<p>Privacy policies for apps published on Google Play.</p>
<ul>
{rows}
</ul>
</main></body></html>
"""


def _privacy_index_html():
    rows = '\n'.join(
        f'<li><a href="{slug}.html">{a["name"]}</a></li>'
        for slug, a in APPS.items()
    )
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Privacy Policies</title>
<style>
  html,body{{background:#000;color:#E8E2D8;margin:0;font-family:-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.55}}
  main{{max-width:640px;margin:0 auto;padding:48px 24px 96px}}
  h1{{font-size:24px;font-weight:800;letter-spacing:-0.4px;margin:0 0 8px}}
  p{{color:#A89D8E;font-size:14px}}
  ul{{list-style:none;padding:0;margin:32px 0 0}}
  li{{padding:14px 0;border-top:1px solid #1F1F1F;font-size:16px}}
  a{{color:#E8E2D8;text-decoration:none}}
  a:hover{{color:#FF6B35}}
</style></head><body><main>
<h1>Privacy policies</h1>
<p>Per-app privacy policies for apps published by Albert Kamalov.</p>
<ul>
{rows}
</ul>
</main></body></html>
"""


if __name__ == '__main__':
    main()
