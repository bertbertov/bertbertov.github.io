"""Generate 10 per-app privacy policy HTML pages from the shared template."""
from pathlib import Path

ROOT = Path(__file__).parent
TPL = (ROOT / 'privacy' / '_template.html').read_text(encoding='utf-8')

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
    'manga': {
        'name': 'Manga Offline',
        'accent': '#B985E0',
        'data': (
            '<ul>'
            '<li>The list of comic-book archives (.cbz / .zip files) you choose to open, plus your reading progress per book, is stored locally.</li>'
            '<li>The app reads <b>only the files you explicitly pick</b> via the Android Storage Access Framework. It never browses your storage on its own.</li>'
            '<li>No file content is uploaded.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Manga Offline requests no runtime permissions. File access uses the Storage Access Framework: Android shows you a system file-picker dialog, and the app receives access only to the specific file you tap.</p>'
        ),
    },
    'lensbox': {
        'name': 'Lensbox',
        'accent': '#F5F5F0',
        'data': (
            '<ul>'
            '<li>Lensbox is a calculator. Every input you type (focal length, aperture, focus distance, latitude / longitude for sun &amp; moon times, ND-filter stops, etc.) is held only in memory and used only to compute the result you see on screen.</li>'
            '<li>Nothing is saved between sessions in v1, nothing is uploaded, nothing is shared with any third party.</li>'
            '</ul>'
        ),
        'perms': (
            '<p>Lensbox requests no runtime permissions. Latitude and longitude for sun / moon calculations are entered manually.</p>'
        ),
    },
    'stutter': {
        'name': 'Stutter',
        'accent': '#FF8552',
        'data': (
            '<ul>'
            '<li>While a focus session is active, Stutter holds the task name and timer settings you entered in memory and in a persistent on-device notification so you can end the session at any time.</li>'
            '<li>When you end the session (or the timer reaches zero), this state is discarded.</li>'
            '<li>No session history is recorded. No data leaves your device.</li>'
            '</ul>'
        ),
        'perms': (
            '<ul>'
            '<li><b>POST_NOTIFICATIONS</b> &mdash; required to show the persistent &ldquo;focus session in progress&rdquo; notification with an End-session action.</li>'
            '<li><b>FOREGROUND_SERVICE</b> &amp; <b>FOREGROUND_SERVICE_SPECIAL_USE</b> &mdash; required to keep the timer and periodic voice check-ins running while the screen is off. The foreground service is terminated automatically when the session ends or you tap End in the notification.</li>'
            '<li><b>TextToSpeech</b> &mdash; Stutter uses Android&rsquo;s built-in TextToSpeech engine to speak the check-in phrase aloud. The text is generated on-device; no audio is uploaded.</li>'
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
    'stagecue': {
        'name': 'Stage Cue',
        'accent': '#FF3FA0',
        'data': (
            '<ul>'
            '<li>The set lists you create and the songs in each set list (title, key, BPM, duration, free-text notes) are stored locally.</li>'
            '<li>No part of this data leaves your device. There is no account, no sync, no upload.</li>'
            '</ul>'
        ),
        'perms': (
            '<ul>'
            '<li><b>WAKE_LOCK</b> &mdash; used to keep the screen on while a show is actively running so the phone does not lock between songs. The wake lock is released the moment you exit show mode.</li>'
            '</ul>'
        ),
    },
}


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
