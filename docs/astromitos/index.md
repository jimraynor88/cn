<!-- index-astromitos.md -->
# 🌙✨ AstroMitos — El gran compendio de asteroides mitológicos en tu carta natal

<style>
/* ============================================
   Tema personalizado (Azul + Rosa + Lila)
   Se adapta al modo claro/oscuro del navegador
   ============================================ */
:root {
    --md-primary-fg-color: #1E3A8A;
    --md-primary-fg-color--light: #3B82F6;
    --md-accent-fg-color: #BE185D;
    --md-accent-fg-color--light: #EC4899;
    --md-default-fg-color--light: #4C1D95;
    --bg-gradient-start: #dbeafe;
    --bg-gradient-end: #ede9fe;
    --text-color: #1f2937;
    --card-bg: #ffffffcc;
    --border-light: #a21caf20;
}
@media (prefers-color-scheme: dark) {
    :root {
        --md-primary-fg-color: #60A5FA;
        --md-primary-fg-color--light: #93C5FD;
        --md-accent-fg-color: #F472B6;
        --md-accent-fg-color--light: #F9A8D4;
        --md-default-fg-color--light: #C084FC;
        --bg-gradient-start: #1e1b4b;
        --bg-gradient-end: #0f172a;
        --text-color: #e2e8f0;
        --card-bg: #1e293bcc;
        --border-light: #c084fc30;
    }
}
body { font-family: 'Segoe UI', Roboto, sans-serif; background: linear-gradient(135deg, var(--bg-gradient-start), var(--bg-gradient-end)); color: var(--text-color); padding: 2rem 1rem; }
.container { max-width: 1200px; margin: 0 auto; }
.hero { text-align: center; padding: 2rem 1rem 3rem; border-bottom: 2px solid var(--md-accent-fg-color); margin-bottom: 2rem; }
.hero h1 { font-size: 3.5rem; background: linear-gradient(135deg, var(--md-primary-fg-color--light), var(--md-accent-fg-color)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.themes { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin: 3rem 0; }
.card { background: var(--card-bg); backdrop-filter: blur(4px); border-radius: 28px; padding: 1.5rem; border: 1px solid var(--border-light); transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
.card:hover { transform: translateY(-5px); border-color: var(--md-accent-fg-color); }
.card-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.card h3 { color: var(--md-primary-fg-color--light); margin-bottom: 0.5rem; }
.badge { display: inline-block; background: var(--md-accent-fg-color); color: white; border-radius: 40px; padding: 0.2rem 0.8rem; font-size: 0.7rem; margin-right: 0.5rem; }
.highlight-myth { background: linear-gradient(120deg, #172554, #831843); border-radius: 32px; padding: 2rem; margin: 3rem 0; color: white; text-align: center; }
.btn-carta { display: inline-block; background: var(--md-accent-fg-color); color: white; font-size: 1.3rem; font-weight: bold; padding: 1rem 2.5rem; border-radius: 60px; text-decoration: none; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
.btn-carta:hover { background: var(--md-primary-fg-color); transform: scale(1.02); color: var(--md-accent-fg-color--light); }
.footer-note { text-align: center; margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border-light); }
@media (max-width: 640px) { .hero h1 { font-size: 2.2rem; } }
</style>

<div class="container">
<div class="hero">
<div class="deco">🌙 ✨ 🏛️</div>
<h1>AstroMitos</h1>
<div class="hero-sub">Cada asteroide, cada ninfa, cada monstruo olímpico es una llave que abre una puerta de tu psique.</div>
<p><strong>AstroMitos</strong> reúne más de 70 cuerpos celestes con sus historias, vínculos y mensajes ocultos para que descifres tu destino.</p>
</div>

<!-- 8 tarjetas temáticas: las 5 originales + 3 nuevas -->
<div class="themes">
    <!-- Amor y deseo -->
    <div class="card"><div class="card-icon">💘</div><h3>Amor y deseo</h3><p>Eros, Psique, Juno, Amors... ¿Cómo te enamoras? Los asteroides del corazón revelan el hilo invisible del afecto.</p><ul><li><span class="badge">Eros 433</span> Pasión pura</li><li><span class="badge">Psique 16</span> Amor del alma</li><li><span class="badge">Juno 3</span> Pacto matrimonial</li></ul></div>
    <!-- Dinero y abundancia -->
    <div class="card"><div class="card-icon">💰</div><h3>Dinero y abundancia</h3><p>Abundantia, Fortuna, Hermes, Plutus... ¿Dónde está tu vellocino de oro?</p><ul><li><span class="badge">Abundantia 151</span> Riqueza natural</li><li><span class="badge">Fortuna 19</span> Golpes de suerte</li><li><span class="badge">Jasón 8192</span> Búsqueda del tesoro</li></ul></div>
    <!-- Trabajo y vocación -->
    <div class="card"><div class="card-icon">⚒️</div><h3>Trabajo y vocación</h3><p>Prometeo, Dédalo, Talos, Telquines... ¿Eres un artesano del fuego o un arquitecto de laberintos?</p><ul><li><span class="badge">Prometeo 1809</span> Innovador rebelde</li><li><span class="badge">Dédalo 1864</span> Genio atrapado</li><li><span class="badge">Talos 5786</span> Rutina automática</li></ul></div>
    <!-- Familia y raíces -->
    <div class="card"><div class="card-icon">🏠</div><h3>Familia y raíces</h3><p>Ceres, Tetis, Mnemósine, Níobe... El árbol genealógico también tiene sus asteroides.</p><ul><li><span class="badge">Ceres 1</span> Matriarca nutricia</li><li><span class="badge">Tetis 17</span> Madre transformadora</li><li><span class="badge">Níobe 71</span> Orgullo y pérdida</li></ul></div>
    <!-- Sexo y transformación -->
    <div class="card"><div class="card-icon">🔥</div><h3>Sexo y transformación</h3><p>Medusa, Quimera, Circe, las Erinias... La energía cruda que todo lo quema y regenera.</p><ul><li><span class="badge">Medusa 149</span> Mirada que petrifica</li><li><span class="badge">Quimera 623</span> Deseo monstruoso</li><li><span class="badge">Erynnia 889</span> Karma sexual</li></ul></div>
    <!-- 👉 NUEVA: Salud y bienestar -->
    <div class="card"><div class="card-icon">🩺</div><h3>Salud y bienestar</h3><p>Higia, Asclepio, Quirón, Hygeia... Tu cuerpo, tus rutinas y tu sanación escrita en el cielo.</p><ul><li><span class="badge">Higia 10</span> Salud preventiva</li><li><span class="badge">Asclepio 1027</span> Medicina regeneradora</li><li><span class="badge">Quirón 2060</span> Herida que enseña</li></ul></div>
    <!-- 👉 NUEVA: Espiritualidad y magia -->
    <div class="card"><div class="card-icon">🔮</div><h3>Espiritualidad y magia</h3><p>Hécate, Morfeo, Pasítea, Hermes Psicopompo... Conexión con lo invisible, sueños y tránsitos del alma.</p><ul><li><span class="badge">Hécate 100</span> Magia y encrucijadas</li><li><span class="badge">Morfeo 4197</span> Sueños proféticos</li><li><span class="badge">Pasítea 1188</span> Descanso reparador</li></ul></div>
    <!-- 👉 NUEVA: Amistad y grupos -->
    <div class="card"><div class="card-icon">👥</div><h3>Amistad y grupos</h3><p>Cástor y Pólux, Argos, Parténope... La tribu, los compañeros de viaje y las redes de apoyo.</p><ul><li><span class="badge">Argos 3738</span> Colaboración anónima</li><li><span class="badge">Parténope 11</span> Amistad sincera</li><li><span class="badge">Dióscuros</span> Hermandad inquebrantable</li></ul></div>
</div>

<!-- Mitos destacados -->
<div class="highlight-myth">
<h2>🌌 Mitos que actúan en tu vida cotidiana</h2>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1.2rem; margin-top: 1rem;">
<div class="myth-item">🧩 Ariadna: el hilo que siempre encuentras</div>
<div class="myth-item">🔱 Quirón: la herida que sana</div>
<div class="myth-item">🌊 Tetis: la madre escurridiza</div>
<div class="myth-item">🏺 Pandora: la esperanza en el caos</div>
<div class="myth-item">🦁 Quimera: monstruo interior que domeñar</div>
<div class="myth-item">🗝️ Hermes: mensajero del destino</div>
<div class="myth-item">🩸 Medusa: la mirada que libera</div>
<div class="myth-item">🍎 Eris: la manzana de la discordia</div>
</div>
<p style="margin-top: 1.5rem;">Cada uno de estos personajes celestes está influyendo en tu carácter, tus relaciones y tu camino profesional.</p>
</div>

<!-- Catálogo rápido -->
<h2 style="text-align: center;">📜 Catálogo incluido en AstroMitos</h2>
<ul style="columns: 2; list-style: none; text-align: center;">
<li>✦ Eros (433)</li><li>✦ Psique (16)</li><li>✦ Ceres (1)</li><li>✦ Palas (2)</li>
<li>✦ Juno (3)</li><li>✦ Vesta (4)</li><li>✦ Quirón (2060)</li><li>✦ Medusa (149)</li>
<li>✦ Dejanira (157)</li><li>✦ Nessus (7066)</li><li>✦ Prometeo (1809)</li><li>✦ Dédalo (1864)</li>
<li>✦ Fides (37)</li><li>✦ Talos (5786)</li><li>✦ Hécate (100)</li><li>✦ Odiseo (1143)</li>
<li>✦ Atalanta (36)</li><li>✦ Pandora (55)</li><li>✦ Moiras (97,120,273)</li><li>✦ Cerbero (1865)</li>
<li>✦ Esfinge (896)</li><li>✦ Apofis (99942)</li><li>✦ Higia (10)</li><li>✦ Asclepio (1027)</li>
<li>✦ +70 cuerpos más</li>
</ul>

<!-- Botón final -->
<div style="text-align: center; margin: 3rem 0 2rem;">
    <a href="../servicios/carta-natal-personalizada.md" class="btn-carta">
        ✨ Obtén tu Carta Natal Personalizada ✨
    </a>
</div>
<div class="footer-note">
    🌠 ¿Quieres saber dónde se ubican <strong>Eros, Ceres, Quirón, Medusa</strong> y todos los demás en tu cielo natal? <br>
    Pide tu carta personalizada y descubre qué mitos te acompañan desde tu nacimiento.
</div>
</div>
