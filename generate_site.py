import json
import re
import html
import os

with open('/tmp/parsed_pages.json', 'r', encoding='utf-8') as f:
    site_data = json.load(f)

def get_nav(active_page, relative_prefix=''):
    p = relative_prefix
    
    is_home = ' active' if active_page == 'home' else ''
    is_cv = ' active' if active_page == 'cv' else ''
    is_pubs = ' active' if active_page == 'publications' else ''
    is_teaching = ' active' if active_page in ['teaching', 'info_theory', 'multimedia'] else ''
    
    return f"""
    <header class="site-header">
      <div class="container">
        <nav class="navbar">
          <a href="{p}index.html" class="brand" title="Leonardo Araujo - UFSJ">
            <img src="{p}images/logo.png" alt="Leonardo Araujo" class="brand-logo">
            <span class="brand-role">UFSJ</span>
          </a>
          
          <ul class="nav-links" id="nav-links">
            <li><a href="{p}index.html" class="nav-link{is_home}">Home</a></li>
            <li><a href="{p}cv.html" class="nav-link{is_cv}">CV</a></li>
            <li><a href="{p}publications.html" class="nav-link{is_pubs}">Publications</a></li>
            
            <li class="nav-item-dropdown">
              <a href="{p}teaching.html" class="nav-link{is_teaching}">
                Teaching
                <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
              </a>
              <ul class="dropdown-menu">
                <li><a href="{p}teaching.html" class="dropdown-item">Teaching Overview &amp; History</a></li>
                <li><a href="{p}information-theory.html" class="dropdown-item">Information Theory</a></li>
                <li><a href="{p}multimedia-signal-processing.html" class="dropdown-item">Multimedia Signal Processing</a></li>
              </ul>
            </li>

            <li><a href="https://github.com/leolca" target="_blank" rel="noopener" class="nav-link" title="GitHub Profile">GitHub ↗</a></li>
            <li><a href="http://lattes.cnpq.br/6946118605547297" target="_blank" rel="noopener" class="nav-link" title="CNPq Lattes CV" style="color:var(--primary);font-weight:600;">Lattes ↗</a></li>
          </ul>
          
          <div class="nav-actions">
            <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark/light theme" title="Toggle theme">
              <span id="theme-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
              </span>
            </button>
            <button class="menu-toggle" id="menu-toggle" aria-label="Toggle menu">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            </button>
          </div>
        </nav>
      </div>
    </header>
    """

def get_footer(relative_prefix=''):
    p = relative_prefix
    return f"""
    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div>
            <p><strong>Prof. Dr. Leonardo Carneiro de Araújo</strong> &bull; <a href="https://www.ufsj.edu.br" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Universidade Federal de São João del-Rei (UFSJ)</a></p>
            <p style="margin-top:0.25rem;font-size:0.85rem;">Departamento de Tecnologia em Engenharia Civil, Computação, Automação, Telemática e Humanidades (DTECH)</p>
            <p style="margin-top:0.25rem;font-size:0.85rem;">Campus Alto Paraopeba (CAP), Sala 109.2 &bull; Ouro Branco - MG, Brazil</p>
            <p style="margin-top:0.6rem;font-size:0.8rem;">
              PGP Fingerprint: <a href="https://keys.openpgp.org/vks/v1/by-fingerprint/A78AC85C00A084F6849A2E2C07B6698B47C96DBF" target="_blank" rel="noopener" class="key-code" style="font-size:0.75rem;">A78A C85C 00A0 84F6 849A 2E2C 07B6 698B 47C9 6DBF</a> 🔑
            </p>
          </div>
          <ul class="footer-links">
            <li><a href="{p}index.html" class="footer-link">Home</a></li>
            <li><a href="{p}cv.html" class="footer-link">Curriculum Vitae</a></li>
            <li><a href="{p}publications.html" class="footer-link">Publications</a></li>
            <li><a href="{p}teaching.html" class="footer-link">Teaching</a></li>
            <li><a href="http://lattes.cnpq.br/6946118605547297" target="_blank" rel="noopener" class="footer-link">Lattes CV</a></li>
            <li><a href="https://github.com/leolca" target="_blank" rel="noopener" class="footer-link">GitHub</a></li>
          </ul>
        </div>
      </div>
    </footer>
    <script src="{p}js/main.js"></script>
    """

def get_html_doc(title, active_page, body_content, relative_prefix=''):
    p = relative_prefix
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | Leonardo Araujo - UFSJ</title>
  <meta name="description" content="Academic homepage of Prof. Leonardo Araujo (UFSJ) - Publications, CV, Teaching in Information Theory and Multimedia Signal Processing">
  <link rel="stylesheet" href="{p}css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>👨‍🏫</text></svg>">
</head>
<body>
{get_nav(active_page, p)}
{body_content}
{get_footer(p)}
</body>
</html>
"""

# ==================== 1. GENERATE INDEX.HTML ====================
def generate_index():
    body = """
    <div class="hero-section">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-avatar-wrap">
            <img src="images/avatar.jpg" alt="Leonardo Araujo" class="hero-avatar" onerror="this.src='images/blacktocat.png'">
          </div>
          <div>
            <h1 class="hero-name">Leonardo Araujo</h1>
            <div class="hero-title">Professor at Universidade Federal de São João del-Rei (UFSJ)</div>
            <div class="hero-affiliation">
              Departamento de Tecnologia em Engenharia Civil, Computação, Automação, Telemática e Humanidades (DTECH)<br>
              Campus Alto Paraopeba (CAP) &bull; Sala 109.2 &bull; Ouro Branco, MG, Brazil
            </div>
            
            <blockquote class="hero-quote">
              "Est modus in rebus, sunt certi denique fines<br>
              Quos ultra citraque nequit consistere rectum."
              <span class="hero-quote-author">&mdash; Horace, Satires 1.1.106</span>
            </blockquote>
            
            <div class="hero-cta">
              <a href="cv.html" class="btn btn-primary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                Curriculum Vitae
              </a>
              <a href="publications.html" class="btn btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                Publications
              </a>
              <a href="http://lattes.cnpq.br/6946118605547297" target="_blank" rel="noopener" class="btn btn-secondary" style="border-color:var(--primary);color:var(--primary);">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                Official CNPq Lattes CV ↗
              </a>
              <a href="https://github.com/leolca" target="_blank" rel="noopener" class="btn btn-secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
                GitHub Profile ↗
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <main class="main-content">
      <div class="container">
        
        <!-- About / Profile Overview -->
        <section class="section">
          <h2 class="section-title">About & Research Focus</h2>
          <p style="font-size:1.05rem;line-height:1.75;margin-bottom:1rem;color:var(--text-secondary);">
            I am a Professor in the Department of Technology in Civil Engineering, Computing, Automation, Telematics, and Humanities (<strong>DTECH</strong>) at the <strong>Universidade Federal de São João del-Rei (UFSJ)</strong>, Campus Alto Paraopeba (CAP).
          </p>
          <p style="font-size:1rem;line-height:1.7;margin-bottom:1rem;color:var(--text-secondary);">
            I hold a Ph.D. in Electrical Engineering from the <em>Universidade Federal de Minas Gerais (UFMG)</em> with research conducted in collaboration with <em>Technische Universität Dresden (TU Dresden)</em>, focusing on Information Theory applied to spoken communication. My research and teaching span <strong>Information Theory</strong>, <strong>Digital Signal and Speech Processing</strong>, <strong>Multiresolution Wavelet Filter Banks</strong>, <strong>Data & Multimedia Compression</strong>, and the development of <strong>Open Source Tools and Scientific Educational Resources</strong>.
          </p>
          <p style="font-size:1rem;line-height:1.7;margin-bottom:1rem;color:var(--text-secondary);">
            I also serve as Section Editor and Layout Editor for <a href="https://periodicos.ufmg.br/index.php/textolivre/about/editorialTeam" target="_blank" rel="noopener" style="color:var(--primary);font-weight:600;">Texto Livre</a> (UFMG, Qualis CAPES A1), an open-access journal focused on language, technology, and free culture.
          </p>
        </section>

        <!-- Highlights Grid -->
        <section class="section">
          <h2 class="section-title">Academic & Creative Highlights</h2>
          <div class="cards-grid">
            
            <div class="card">
              <span class="badge badge-book" style="margin-bottom:0.75rem;">Books & Literature</span>
              <h3 class="card-title">Published Books</h3>
              <p class="card-text">
                Author of <em>Teoria da Informação e da Codificação</em>, <em>The Grand Hotel Infinita</em>, the bilingual illustrated mathematics series <em>Heróis Primos / Prime Heroes</em>, and the children's educational series <em>Pipoca / Popcorn</em>.
              </p>
              <a href="publications.html" class="btn btn-secondary btn-sm">Explore Books &rarr;</a>
            </div>

            <div class="card">
              <span class="badge badge-code" style="margin-bottom:0.75rem;">Open Source</span>
              <h3 class="card-title">Scientific Software & Tools</h3>
              <p class="card-text">
                Core and package contributor to <strong>GNU Octave</strong> (signal & statistics packages), official TeX/LaTeX hyphenation rules for Portuguese (<code>tex-hyphen</code>), and <code>biblatex-abnt</code>.
              </p>
              <a href="https://github.com/leolca" target="_blank" rel="noopener" class="btn btn-secondary btn-sm">GitHub Repositories &rarr;</a>
            </div>

            <div class="card">
              <span class="badge badge-paper" style="margin-bottom:0.75rem;">Teaching Portals</span>
              <h3 class="card-title">Interactive Courses</h3>
              <p class="card-text">
                Explore course syllabi, lecture video series, recommended bibliographies, and open interactive Jupyter Notebooks / Google Colabs for <em>Information Theory</em> and <em>Multimedia Signal Processing</em>.
              </p>
              <a href="teaching.html" class="btn btn-secondary btn-sm">View Courses &rarr;</a>
            </div>

            <div class="card">
              <span class="badge badge-media" style="margin-bottom:0.75rem;">Podcasts & Outreach</span>
              <h3 class="card-title">Science Communication</h3>
              <p class="card-text">
                Producer and host of the science podcasts <em>Ciência em Modulação</em> and <em>Contos em Bits</em>, exploring information concepts, technology, and mathematics for broad audiences.
              </p>
              <a href="publications.html" class="btn btn-secondary btn-sm">Listen & Read &rarr;</a>
            </div>

          </div>
        </section>

        <!-- Contact & Verification Section -->
        <section class="section">
          <h2 class="section-title">Contact & Location</h2>
          <table class="info-table">
            <tbody>
              <tr>
                <th>Institution</th>
                <td>Universidade Federal de São João del-Rei (UFSJ) &bull; Campus Alto Paraopeba (CAP)</td>
              </tr>
              <tr>
                <th>Department</th>
                <td>Departamento de Tecnologia em Engenharia Civil, Computação, Automação, Telemática e Humanidades (DTECH)</td>
              </tr>
              <tr>
                <th>Office</th>
                <td>Sala 109.2</td>
              </tr>
              <tr>
                <th>Address</th>
                <td>Rodovia MG 443, KM 7, Ouro Branco - MG, CEP 36420-000, Brazil</td>
              </tr>
              <tr>
                <th>Email</th>
                <td>
                  <code>leolca (at) ufsj.edu.br</code>
                  <button class="btn btn-secondary btn-sm" style="margin-left:0.5rem;padding:0.2rem 0.5rem;" data-copy="leolca@ufsj.edu.br">Copy Email</button>
                </td>
              </tr>
              <tr>
                <th>PGP Key</th>
                <td>
                  <span class="key-code">A78A C85C 00A0 84F6 849A  2E2C 07B6 698B 47C9 6DBF</span>
                  <a href="https://keys.openpgp.org/vks/v1/by-fingerprint/A78AC85C00A084F6849A2E2C07B6698B47C96DBF" target="_blank" rel="noopener" class="pub-link" style="margin-left:0.5rem;">Download Key 🔑</a>
                </td>
              </tr>
            </tbody>
          </table>
        </section>

      </div>
    </main>
    """
    return get_html_doc("Home", "home", body)


# ==================== 2. GENERATE CV.HTML ====================
def generate_cv():
    body = """
    <main class="main-content">
      <div class="container">
        
        <header class="page-header">
          <h1 class="page-title">Curriculum Vitae</h1>
          <p class="page-subtitle">Academic trajectory, research activities, professional background, and verified qualifications.</p>
        </header>

        <!-- Official Lattes Callout Banner -->
        <div class="cv-lattes-banner">
          <div class="cv-lattes-text">
            <h3>Plataforma Lattes &mdash; CNPq</h3>
            <p>For the complete, officially accredited academic curriculum vitae certified by the Brazilian National Council for Scientific and Technological Development (CNPq):</p>
          </div>
          <div>
            <a href="http://lattes.cnpq.br/6946118605547297" target="_blank" rel="noopener" class="btn btn-primary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              Open Official Lattes Profile (ID: 6946118605547297)
            </a>
          </div>
        </div>

        <!-- Academic Education -->
        <section class="section">
          <h2 class="section-title">Education & Degrees</h2>
          <div class="cv-timeline">
            
            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2008 &ndash; 2013</div>
              <div class="cv-timeline-title">Ph.D. (Doutorado) in Electrical Engineering</div>
              <div class="cv-timeline-place">Universidade Federal de Minas Gerais (UFMG), Brazil &amp; Technische Universität Dresden (TU Dresden), Germany</div>
              <div class="cv-timeline-desc">
                <strong>Thesis:</strong> <em>Teoria da Informação Aplicada à Comunicação Falada</em> (Information Theory Applied to Spoken Communication)<br>
                <strong>Advisor:</strong> Prof. Dr. Hani Camille Yehia
              </div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2004 &ndash; 2007</div>
              <div class="cv-timeline-title">M.Sc. (Mestrado) in Electrical Engineering</div>
              <div class="cv-timeline-place">Universidade Federal de Minas Gerais (UFMG), Brazil</div>
              <div class="cv-timeline-desc">
                <strong>Dissertation:</strong> <em>Banco de Filtros Wavelets com Fator de Escala Maior do que Dois</em> (Wavelet Filter Banks with Scale Factor Greater than Two)<br>
                <strong>Advisor:</strong> Prof. Dr. Hani Camille Yehia
              </div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">1999 &ndash; 2003</div>
              <div class="cv-timeline-title">B.Sc. (Bacharelado) in Electrical Engineering</div>
              <div class="cv-timeline-place">Universidade Federal de Minas Gerais (UFMG), Brazil</div>
              <div class="cv-timeline-desc">
                Undergraduate scientific initiation projects in multimodal speech reproduction, digital video coding using orthonormal spatiotemporal functions, and numerical methods for differential equations.
              </div>
            </div>

          </div>
        </section>

        <!-- Professional Appointments -->
        <section class="section">
          <h2 class="section-title">Academic & Professional Experience</h2>
          <div class="cv-timeline">
            
            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2011 &ndash; Present</div>
              <div class="cv-timeline-title">Professor</div>
              <div class="cv-timeline-place">Universidade Federal de São João del-Rei (UFSJ), DTECH &bull; Ouro Branco, MG</div>
              <div class="cv-timeline-desc">
                Teaching undergraduate and graduate courses in Information Theory, Multimedia Signal Processing, Signals and Systems, Digital Design, Digital Document Design, and Programming for Engineering.
              </div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">Editorial Position</div>
              <div class="cv-timeline-title">Section Editor &amp; Layout Editor (Diagramador)</div>
              <div class="cv-timeline-place"><a href="https://periodicos.ufmg.br/index.php/textolivre/about/editorialTeam" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">Revista Texto Livre</a> &bull; Faculdade de Letras, UFMG</div>
              <div class="cv-timeline-desc">
                Section Editor (Editor de Seção) and Technical Team Layout Editor (Diagramador) for <em>Texto Livre</em> (ISSN 1983-3652, Qualis CAPES A1), dedicated to language, literature, technology, and open science.
              </div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2010 &ndash; 2011</div>
              <div class="cv-timeline-title">Adjunct Professor</div>
              <div class="cv-timeline-place">Centro Universitário de Belo Horizonte (UNI-BH)</div>
              <div class="cv-timeline-desc">Taught Digital Signal Processing.</div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2000 &ndash; Present</div>
              <div class="cv-timeline-title">Researcher</div>
              <div class="cv-timeline-place">CEFALA &mdash; Centro de Estudos da Fala, Acústica, Linguagem e Música</div>
              <div class="cv-timeline-desc">Research in speech perception, acoustic models, signal processing, and psychoacoustics.</div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2007 &ndash; 2008</div>
              <div class="cv-timeline-title">Optimization & Artificial Intelligence Engineer</div>
              <div class="cv-timeline-place">Ottimah Soluções</div>
              <div class="cv-timeline-desc">Industrial optimization algorithms and artificial intelligence systems.</div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2007</div>
              <div class="cv-timeline-title">Professor of Artificial Intelligence</div>
              <div class="cv-timeline-place">Faculdade Metropolitana de Belo Horizonte</div>
              <div class="cv-timeline-desc">Course in Artificial Intelligence.</div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2005</div>
              <div class="cv-timeline-title">Professor of Artificial Intelligence</div>
              <div class="cv-timeline-place">Pontifícia Universidade Católica de Minas Gerais (PUC-MG)</div>
              <div class="cv-timeline-desc">Undergraduate lecture courses in Artificial Intelligence.</div>
            </div>

            <div class="cv-timeline-item">
              <div class="cv-timeline-date">2003 &ndash; 2005</div>
              <div class="cv-timeline-title">Software Developer</div>
              <div class="cv-timeline-place">ATAN Sistemas de Automação</div>
              <div class="cv-timeline-desc">Development of industrial automation software and web-based applications.</div>
            </div>

          </div>
        </section>

        <!-- Research Interests -->
        <section class="section">
          <h2 class="section-title">Research Areas & Interests</h2>
          <div class="cards-grid">
            <div class="card">
              <h3 class="card-title">Information & Communication Theory</h3>
              <p class="card-text">Entropy measures, channel capacity, rate-distortion theory, coding schemes, source entropy of natural language, Zipfian distribution models.</p>
            </div>
            <div class="card">
              <h3 class="card-title">Signal & Speech Processing</h3>
              <p class="card-text">Linear predictive coding (LPC), subband & wavelet filter banks, spectral analysis, psychoacoustics, speech synthesis, auditory perception.</p>
            </div>
            <div class="card">
              <h3 class="card-title">Multimedia & Compression</h3>
              <p class="card-text">Lossless and lossy compression algorithms, image processing, JPEG, DCT, quantization, dithering techniques, perceptual watermarking.</p>
            </div>
            <div class="card">
              <h3 class="card-title">Open Educational Resources</h3>
              <p class="card-text">Interactive Jupyter Notebooks for education, mathematical storytelling, scientific outreach, Portuguese typesetting algorithms.</p>
            </div>
          </div>
        </section>

        <!-- Languages & Technical Skills -->
        <section class="section">
          <h2 class="section-title">Languages & Technical Skills</h2>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:1.5rem;">
            
            <div class="card">
              <h3 class="card-title">Languages</h3>
              <ul style="padding-left:1.25rem;color:var(--text-secondary);font-size:0.95rem;line-height:1.75;">
                <li><strong>Portuguese:</strong> Native</li>
                <li><strong>English:</strong> Fluent (TOEFL Score: 102/120; Hearven & King's School of English, UK)</li>
                <li><strong>German:</strong> Advanced (10 months of study & research at TU Dresden, Germany)</li>
              </ul>
            </div>

            <div class="card">
              <h3 class="card-title">Scientific Computing & Programming</h3>
              <ul style="padding-left:1.25rem;color:var(--text-secondary);font-size:0.95rem;line-height:1.75;">
                <li><strong>Scientific Software:</strong> GNU Octave (core & package contributor), MATLAB, Python (NumPy, SciPy, Jupyter)</li>
                <li><strong>Languages:</strong> C/C++, Java, Shell Script, Perl, PHP, SQL</li>
                <li><strong>Typesetting & Publishing:</strong> LaTeX, BibLaTeX (ABNT), TeX Hyphenation</li>
                <li><strong>Environments:</strong> Linux / Unix, Git, Apache</li>
              </ul>
            </div>

          </div>
        </section>

        <!-- Scientific Events -->
        <section class="section">
          <h2 class="section-title">Scientific Events Organization & Editorial Work</h2>
          <ul class="syllabus-list">
            <li class="syllabus-item">
              <div>
                <strong>Revista Texto Livre (UFMG &bull; Qualis CAPES A1):</strong> Section Editor and Technical Team Layout Editor (Diagramador).
              </div>
              <div class="pub-links" style="margin-top:0.35rem;">
                <a href="https://periodicos.ufmg.br/index.php/textolivre/about/editorialTeam" target="_blank" rel="noopener" class="pub-link">Editorial Team Page ↗</a>
              </div>
            </li>
            <li class="syllabus-item"><strong>ISSP (International Seminar on Speech Production):</strong> Organization, editing, and proceedings publication.</li>
            <li class="syllabus-item"><strong>SemEA (Simpósio Brasileiro de Engenharia de Áudio):</strong> Organization, editorial board, and proceedings publication.</li>
            <li class="syllabus-item"><strong>SBRN (Brazilian Neural Networks Symposium):</strong> Editorial coordination and proceedings publication.</li>
            <li class="syllabus-item"><strong>ABRALIN (Associação Brasileira de Linguística):</strong> Editorial coordination and proceedings publication.</li>
            <li class="syllabus-item"><strong>Congresso Brasileiro de Hispanistas:</strong> Editorial coordination and proceedings publication.</li>
          </ul>
        </section>

      </div>
    </main>
    """
    return get_html_doc("Curriculum Vitae", "cv", body)


# ==================== 3. GENERATE PUBLICATIONS.HTML ====================
def generate_publications():
    pubs = site_data['publications']
    
    # Organize by year
    year_groups = {}
    current_year = 'Unknown'
    
    for it in pubs:
        txt = it['text'].strip()
        if re.match(r'^(19|20)\d{2}$', txt):
            current_year = txt
            if current_year not in year_groups:
                year_groups[current_year] = []
            continue
        if current_year != 'Unknown' and txt != 'Publications':
            year_groups[current_year].append(it)
            
    # Build HTML items
    items_html = []
    total_count = 0
    
    for year in sorted(year_groups.keys(), reverse=True):
        seen_texts = set()
        for it in year_groups[year]:
            raw_text = it['text'].strip()
            if raw_text in seen_texts:
                continue
            seen_texts.add(raw_text)
            total_count += 1
            
            low = raw_text.lower()
            category = 'article'
            badge_class = 'badge-paper'
            badge_label = 'Article'
            
            if any(k in low for k in ['livro:', 'book:', 'série', 'series', 'isbn']):
                category = 'book'
                badge_class = 'badge-book'
                badge_label = 'Book / Series'
            elif any(k in low for k in ['octave', 'github', 'tex', 'hyphen', 'biblatex', 'cjpeg', 'package']):
                category = 'software'
                badge_class = 'badge-code'
                badge_label = 'Open Source'
            elif any(k in low for k in ['podcast', 'spotify', 'ciência em modulação', 'contos em bits', 'substack', 'instagram']):
                category = 'media'
                badge_class = 'badge-media'
                badge_label = 'Media / Podcast'

            # Clean text for display: remove trailing "( link )" or "( download )"
            display_title = re.sub(r'\s*\(\s*(link|download|preprint|glottometrics|versão em português)\s*\)\s*', '', raw_text, flags=re.IGNORECASE)
            
            # Format link buttons
            links_markup = []
            for lk in it.get('links', []):
                t = lk['text'].strip()
                h = lk['href'].strip()
                if not h:
                    continue
                # Friendly link labels
                label = t
                if label.lower() in ['link', 'download']:
                    if 'amazon' in h: label = 'Amazon'
                    elif 'github' in h: label = 'GitHub'
                    elif 'arxiv' in h: label = 'arXiv'
                    elif 'spotify' in h: label = 'Spotify'
                    elif 'drive.google.com' in h: label = 'PDF / Drive'
                    elif 'poisson' in h: label = 'Poisson Book'
                    elif 'springer' in h: label = 'Springer'
                    elif 'tug.org' in h: label = 'TUGboat'
                    elif 'fliphtml5' in h: label = 'FlipBook'
                    elif 'substack' in h: label = 'Substack'
                    elif 'instagram' in h: label = 'Instagram'
                    else: label = 'View Document'
                elif label.lower() == 'preprint':
                    label = 'Preprint'
                elif label.lower() == 'glottometrics':
                    label = 'Glottometrics'
                elif label.lower() == 'versão em português':
                    label = 'Versão em Português'
                    
                links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link">{html.escape(label)} ↗</a>')
                
            links_div = f'<div class="pub-links">{"".join(links_markup)}</div>' if links_markup else ''
            
            items_html.append(f"""
            <div class="pub-item" data-category="{category}">
              <div class="pub-header">
                <span class="pub-year">{year}</span>
                <span class="badge {badge_class}">{badge_label}</span>
              </div>
              <div class="pub-title">{html.escape(display_title)}</div>
              {links_div}
            </div>
            """)

    body = f"""
    <main class="main-content">
      <div class="container">
        
        <header class="page-header">
          <h1 class="page-title">Publications & Contributions</h1>
          <p class="page-subtitle">Books, peer-reviewed articles, open-source software, preprints, and science communication (2003 &ndash; 2026).</p>
        </header>

        <!-- Filter & Search Toolbar -->
        <div class="filter-bar">
          <div class="filter-chips">
            <button class="filter-chip active" data-filter="all">All ({total_count})</button>
            <button class="filter-chip" data-filter="book">Books & Series</button>
            <button class="filter-chip" data-filter="software">Open Source & Tools</button>
            <button class="filter-chip" data-filter="article">Articles & Preprints</button>
            <button class="filter-chip" data-filter="media">Podcasts & Media</button>
          </div>
          <div class="search-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="pub-search" class="search-input" placeholder="Search by title, keyword, year...">
          </div>
        </div>

        <!-- Publication List -->
        <div id="pub-container">
          {"".join(items_html)}
        </div>
        
        <div id="pub-empty" style="display:none;text-align:center;padding:3rem 1rem;color:var(--text-muted);">
          <p>No publications found matching your search criteria.</p>
        </div>

      </div>
    </main>
    """
    return get_html_doc("Publications", "publications", body)


# ==================== 4. GENERATE TEACHING.HTML ====================
def generate_teaching():
    t_items = site_data['teaching']
    year_courses = {}
    current_year = None
    
    for it in t_items:
        txt = it['text'].strip()
        if re.match(r'^(19|20)\s*\d{2}$', txt):
            current_year = txt.replace(' ', '')
            year_courses[current_year] = []
            continue
        if current_year and txt.startswith('-'):
            c = txt.lstrip('- ').strip()
            if c not in year_courses[current_year]:
                year_courses[current_year].append(c)

    # Format teaching history
    history_rows = []
    for yr in sorted(year_courses.keys(), reverse=True):
        courses_str = "<br>".join([f"&bull; {html.escape(c)}" for c in year_courses[yr]])
        history_rows.append(f"""
        <tr>
          <td style="font-weight:700;font-family:var(--font-mono);color:var(--primary);vertical-align:top;width:90px;">{yr}</td>
          <td>{courses_str}</td>
        </tr>
        """)

    body = f"""
    <main class="main-content">
      <div class="container">
        
        <header class="page-header">
          <h1 class="page-title">Teaching & Courses</h1>
          <p class="page-subtitle">Undergraduate and graduate university instruction, lecture syllabi, and interactive learning environments.</p>
        </header>

        <!-- Flagship Course Cards -->
        <section class="section">
          <h2 class="section-title">Flagship Course Portals</h2>
          <div class="cards-grid">
            
            <div class="card" style="border-top:4px solid var(--primary);">
              <span class="badge badge-paper" style="margin-bottom:0.75rem;">Undergraduate / Graduate</span>
              <h3 class="card-title" style="font-size:1.3rem;">Information Theory</h3>
              <p class="card-text">
                Fundamental principles of communication, Shannon entropy, mutual information, channel capacity, rate-distortion, and asymptotic equipartition (AEP). Features complete lecture videos, syllabus, and interactive entropy notebooks.
              </p>
              <div style="margin-top:1rem;">
                <a href="information-theory.html" class="btn btn-primary btn-sm">Enter Course Hub &rarr;</a>
              </div>
            </div>

            <div class="card" style="border-top:4px solid var(--accent);">
              <span class="badge badge-code" style="margin-bottom:0.75rem;">Interactive Labs & Code</span>
              <h3 class="card-title" style="font-size:1.3rem;">Multimedia Signal Processing</h3>
              <p class="card-text">
                Comprehensive study of audio, speech, image, and video compression. Includes over 20 interactive Jupyter Notebooks and Google Colab environments covering LPC synthesis, JPEG DCT, wavelets, dithering, and polyphase filters.
              </p>
              <div style="margin-top:1rem;">
                <a href="multimedia-signal-processing.html" class="btn btn-primary btn-sm">Enter Course Hub &rarr;</a>
              </div>
            </div>

          </div>
        </section>

        <!-- Teaching Timeline History -->
        <section class="section">
          <h2 class="section-title">Teaching History (2007 &ndash; Present)</h2>
          <p style="color:var(--text-secondary);margin-bottom:1.25rem;">
            Chronological record of courses instructed at <strong>Universidade Federal de São João del-Rei (UFSJ)</strong>, <strong>Centro Universitário de Belo Horizonte (UNI-BH)</strong>, and <strong>Pontifícia Universidade Católica de Minas Gerais (PUC-MG)</strong>.
          </p>
          <table class="info-table" style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
            <thead>
              <tr style="background:var(--bg-secondary);">
                <th style="padding:0.75rem 1rem;">Academic Year</th>
                <th style="padding:0.75rem 1rem;">Courses Instructed</th>
              </tr>
            </thead>
            <tbody>
              {"".join(history_rows)}
            </tbody>
          </table>
        </section>

      </div>
    </main>
    """
    return get_html_doc("Teaching", "teaching", body)


# ==================== 5. GENERATE INFORMATION THEORY COURSE PAGE ====================
def generate_info_theory(relative_prefix=''):
    data = site_data['info_theory']
    
    # Process sections
    sections = {}
    current_h = 'Overview'
    sections[current_h] = []
    
    for it in data:
        if it['type'] == 'heading':
            current_h = it['text'].strip()
            sections[current_h] = []
        else:
            sections[current_h].append(it)

    # Format lists
    def format_section_items(items):
        out = []
        seen = set()
        for it in items:
            t = it['text'].strip()
            if t in seen:
                continue
            seen.add(t)
            
            # format links inside text
            links_markup = []
            for lk in it.get('links', []):
                h = lk['href']
                lbl = lk['text'] or 'link'
                if h:
                    links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link">{html.escape(lbl)} ↗</a>')
            
            # clean text of duplicate link names
            cleaned_text = t
            links_div = f'<div class="pub-links" style="margin-top:0.35rem;">{"".join(links_markup)}</div>' if links_markup else ''
            out.append(f'<li class="syllabus-item"><div>{html.escape(cleaned_text)}</div>{links_div}</li>')
        return "".join(out)

    body = f"""
    <main class="main-content">
      <div class="container">
        
        <header class="page-header">
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
            <a href="{relative_prefix}teaching.html" style="color:var(--primary);text-decoration:none;font-weight:600;font-size:0.9rem;">&larr; Back to Teaching</a>
          </div>
          <h1 class="page-title">Information Theory</h1>
          <p class="page-subtitle">Theory of communication, entropy measures, data compression, and channel coding.</p>
        </header>

        <blockquote class="hero-quote" style="margin-bottom:2.5rem;padding:1rem 1.25rem;">
          "The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have meaning; that is, they refer to or are correlated according to some system with certain physical or conceptual entities. These semantic aspects of communication are irrelevant to the engineering problem. The significant aspect is that the actual message is one selected from a set of possible messages."
          <span class="hero-quote-author">&mdash; Claude E. Shannon (1948), The Mathematical Theory of Communication</span>
        </blockquote>

        <section class="section">
          <h2 class="section-title">Course Introduction & Overview</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Introduction', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Asymptotic Equipartition Property (AEP)</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Asymptotic Equipartition Property (AEP)', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Video Lectures Series</h2>
          <p style="color:var(--text-secondary);margin-bottom:1rem;">Complete video lecture collections from leading researchers and courses:</p>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Video Lectures', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Course Schedule, Topics & Readings</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Course Schedule and Reading', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Recommended Bibliography</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Bibliography', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Suggested Readings & Media</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Suggested readings', []) + sections.get('On The Media', []))}
          </ul>
        </section>

        <section class="section">
          <h2 class="section-title">Scripts & Interactive Notebooks</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Scripts', []) + sections.get('Resource', []))}
          </ul>
        </section>

      </div>
    </main>
    """
    return get_html_doc("Information Theory", "info_theory", body, relative_prefix)


# ==================== 6. GENERATE MULTIMEDIA SIGNAL PROCESSING COURSE PAGE ====================
def generate_multimedia(relative_prefix=''):
    data = site_data['multimedia']
    
    sections = {}
    current_h = 'Overview'
    sections[current_h] = []
    
    for it in data:
        if it['type'] == 'heading':
            current_h = it['text'].strip()
            sections[current_h] = []
        else:
            sections[current_h].append(it)

    def format_section_items(items):
        out = []
        seen = set()
        for it in items:
            t = it['text'].strip()
            if t in seen:
                continue
            seen.add(t)
            
            links_markup = []
            for lk in it.get('links', []):
                h = lk['href']
                lbl = lk['text'] or 'link'
                if h:
                    if 'nbviewer' in lbl.lower():
                        links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link" style="background:#e0f2fe;color:#0369a1;">Jupyter nbviewer ↗</a>')
                    elif 'colab' in lbl.lower():
                        links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link" style="background:#fef3c7;color:#b45309;">Google Colab 🚀</a>')
                    elif 'pdf' in lbl.lower():
                        links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link">PDF Notes 📄</a>')
                    else:
                        links_markup.append(f'<a href="{html.escape(h)}" target="_blank" rel="noopener" class="pub-link">{html.escape(lbl)} ↗</a>')
            
            links_div = f'<div class="pub-links" style="margin-top:0.35rem;">{"".join(links_markup)}</div>' if links_markup else ''
            out.append(f'<li class="syllabus-item"><div>{html.escape(t)}</div>{links_div}</li>')
        return "".join(out)

    body = f"""
    <main class="main-content">
      <div class="container">
        
        <header class="page-header">
          <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">
            <a href="{relative_prefix}teaching.html" style="color:var(--primary);text-decoration:none;font-weight:600;font-size:0.9rem;">&larr; Back to Teaching</a>
          </div>
          <h1 class="page-title">Multimedia Signal Processing</h1>
          <p class="page-subtitle">Audio, voice, image, and video representation, compression algorithms, and perceptual modeling.</p>
        </header>

        <!-- Interactive Notebooks Spotlight -->
        <section class="section">
          <h2 class="section-title">Interactive Jupyter Notebooks &amp; Google Colab Labs</h2>
          <p style="color:var(--text-secondary);margin-bottom:1.25rem;">
            Hands-on interactive notebooks covering core signal processing and data compression techniques. Run them live in your browser via <strong>Google Colab</strong> or view them rendered on <strong>Jupyter nbviewer</strong>:
          </p>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Notebooks and examples', []))}
          </ul>
        </section>

        <!-- Course Schedule & Reading -->
        <section class="section">
          <h2 class="section-title">Course Schedule &amp; Reading Plan</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Course Schedule and Reading', []))}
          </ul>
        </section>

        <!-- Introductory Material -->
        <section class="section">
          <h2 class="section-title">Introduction &amp; Video Overviews</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Introduction', []))}
          </ul>
        </section>

        <!-- Recommended Bibliography -->
        <section class="section">
          <h2 class="section-title">Recommended Bibliography</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Bibliography', []))}
          </ul>
        </section>

        <!-- Suggested Readings & Standards -->
        <section class="section">
          <h2 class="section-title">Suggested Readings, Standards &amp; Resources</h2>
          <ul class="syllabus-list">
            {format_section_items(sections.get('Suggested Readings', []) + sections.get('Resource', []))}
          </ul>
        </section>

      </div>
    </main>
    """
    return get_html_doc("Multimedia Signal Processing", "multimedia", body, relative_prefix)


# Write all files
print("Generating pages...")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(generate_index())

with open("cv.html", "w", encoding="utf-8") as f:
    f.write(generate_cv())

with open("publications.html", "w", encoding="utf-8") as f:
    f.write(generate_publications())

with open("teaching.html", "w", encoding="utf-8") as f:
    f.write(generate_teaching())

with open("information-theory.html", "w", encoding="utf-8") as f:
    f.write(generate_info_theory())

with open("multimedia-signal-processing.html", "w", encoding="utf-8") as f:
    f.write(generate_multimedia())

# Also generate copies inside teaching/ so both URL paths work
os.makedirs("teaching", exist_ok=True)
with open("teaching/information-theory.html", "w", encoding="utf-8") as f:
    f.write(generate_info_theory(relative_prefix="../"))

with open("teaching/multimedia-signal-processing.html", "w", encoding="utf-8") as f:
    f.write(generate_multimedia(relative_prefix="../"))

print("All pages generated successfully!")
