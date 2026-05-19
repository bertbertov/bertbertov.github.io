# bertbertov.github.io

Static site hosting per-app privacy policies for Android apps published by Albert Kamalov on Google Play.

Live: https://bertbertov.github.io

- Root index: app list
- `/privacy/<slug>.html` — per-app privacy policy (e.g. `/privacy/nightwake.html`)

Regenerate after editing `build.py` or the per-app spec:

```
python build.py
git commit -am "update policies" && git push
```
