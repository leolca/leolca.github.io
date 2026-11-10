# Leonardo Araujo - GitHub Pages Academic Homepage

Personal and academic homepage for **Prof. Dr. Leonardo Carneiro de Araújo** (Universidade Federal de São João del-Rei - UFSJ), hosted at [leolca.github.io](https://leolca.github.io).

## Site Structure

- **`index.html`**: Main homepage featuring bio, Horace quotation, affiliation (UFSJ / CAP / DTECH), contact details, PGP key, and quick highlights.
- **`cv.html`**: Academic Curriculum Vitae with full education timeline, professional experience, research areas, skills, languages, and a direct link to the verified [CNPq Lattes Profile (ID: 6946118605547297)](http://lattes.cnpq.br/6946118605547297).
- **`publications.html`**: Chronological catalogue (2003–2026) of books, peer-reviewed papers, open-source contributions (GNU Octave, TeX hyphenation, abntex), preprints, and podcasts with live search and category filtering.
- **`teaching.html`**: Overview of courses taught since 2007 and links to dedicated course hubs.
- **`information-theory.html`** (and `teaching/information-theory.html`): Syllabus, video lectures (including Portuguese lecture series), Shannon fundamentals, reading list, and interactive entropy tools.
- **`multimedia-signal-processing.html`** (and `teaching/multimedia-signal-processing.html`): Syllabus, video resources, recommended bibliography, and over 20 interactive Jupyter Notebooks & Google Colab environments (JPEG, DCT, Wavelets, LPC speech synthesis, dithering, polyphase filters, etc.).
- **`css/style.css`**: Responsive modern academic styling with light/dark theme support.
- **`js/main.js`**: Theme toggling, mobile navigation drawer, and live publication filtering.
- **`generate_site.py`**: Automated Python build script that parses the extracted content and regenerates the static pages.

## Local Preview

To preview the website locally on your machine:

```bash
python3 -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080) in your browser.

## Publishing to GitHub Pages

Once you are ready to update your live GitHub Pages site:

```bash
git add .
git commit -m "Update homepage with migrated content, courses, and CV"
git push -u origin main
```
