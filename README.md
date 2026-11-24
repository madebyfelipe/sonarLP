# Sonar — landing page

Landing page for **Sonar**, a 24/7 consultative AI agent for marketing teams (built on Agentplace).

- `index.html` — the built page (open it directly in a browser, no build step needed to view)
- `src/index.template.html` — editable source; the logo path is injected as `LOGO_D`
- `src/build.py` — `python3 src/build.py` regenerates `index.html` from the template + `assets/sonar-logo.svg`
- `assets/` — hero sky images and the vectorized Sonar wordmark

Palette: accent `#D6FF25`, blue `#36AEED`, off-white `#FAFAFA`. Type: Bricolage Grotesque, Geist, Geist Mono.
