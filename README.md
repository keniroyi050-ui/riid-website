# RIID portfolio website

Premium static multi-page portfolio website for RIID.

## Pages
- `/` Home
- `/work/` Portfolio
- `/services/`
- `/about/`
- `/contact/`
- `/start/`
- 12 individual concept-project case studies under `/work/<project>/`

The portfolio intentionally uses concept mockups only. It does **not** pretend the fictional businesses are paid client work or live websites.

## WhatsApp
All project forms and primary WhatsApp calls-to-action use:
`+234 803 394 9943` / `2348033949943`.

## Run locally
From this folder:

```bash
python -m http.server 8080
```

Open `http://localhost:8080`.

Do not open the HTML files directly with `file://` because the site uses root-relative clean routes.

## Deploy
The folder can be deployed directly to Vercel, Netlify, Cloudflare Pages, GitHub Pages (with route adjustments if needed), or any static host.

For Vercel, import the folder as a project with no build command and use the repository root as the output directory.

## Branding
- RIID main palette: near-black, off-white, electric blue.
- Favicon: `/favicon.svg`.
- Project concept business names are fictional English-language names created for portfolio demonstration.

## Assets
Mockup images in `/assets/mockups/` are concept visuals generated for the RIID portfolio and use Nigerian visual context.
