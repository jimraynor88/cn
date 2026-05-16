---
title: CartaNatal.de – Tu carta natal personificada
description: Descubre tu Carta Natal como nunca antes. Habla en primera persona, con casas, aspectos, mitos y un enlace único para compartir. Conócete, reconócete.
hide:
  - navigation
  - toc
---

<style>
/* ------------------------------------------------------------
   ESTILOS EXCLUSIVOS PARA LA PORTADA PRINCIPAL
   (Basados en la estética de AstroMitos, pero ampliados)
   ------------------------------------------------------------ */

/* Hero principal */
.hero-main {
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem 1rem;
    background: radial-gradient(ellipse at 70% 30%, rgba(30,27,75,0.4), rgba(11,17,32,0.9));
    border-bottom: 2px solid var(--md-accent-fg-color);
    margin-bottom: 2rem;
}
.hero-main h1 {
    font-size: 3.5rem;
    background: linear-gradient(135deg, #F472B6, #C084FC, #8B5CF6);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 0.5rem;
}
.tagline {
    font-size: 1.4rem;
    font-weight: 300;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}
.hero-description {
    max-width: 700px;
    font-size: 1.1rem;
    color: var(--md-default-fg-color--light);
    margin-bottom: 2rem;
}
.btn-hero {
    display: inline-block;
    background: linear-gradient(90deg, #F472B6, #8B5CF6);
    color: white;
    font-weight: bold;
    padding: 0.9rem 2rem;
    border-radius: 60px;
    text-decoration: none;
    font-size: 1.1rem;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
.btn-hero:hover {
    transform: scale(1.02);
    box-shadow: 0 12px 30px rgba(244,114,182,0.4);
}

/* Sección de características (grid) */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}
.feature-card {
    background: rgba(30, 27, 75, 0.5);
    backdrop-filter: blur(4px);
    border-radius: 28px;
    padding: 1.8rem;
    text-align: center;
    border: 1px solid rgba(244, 114, 182, 0.3);
    transition: all 0.2s;
}
.feature-card:hover {
    border-color: var(--md-accent-fg-color);
    background: rgba(30, 27, 75, 0.7);
    transform: translateY(-5px);
}
.feature-icon {
    font-size: 2.8rem;
    margin-bottom: 1rem;
}
.feature-title {
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: var(--md-accent-fg-color--light);
}
.feature-text {
    font-size: 0.9rem;
    color: var(--md-default-fg-color--light);
}

/* Sección de la carta natal personificada (destacada) */
.personified {
    background: linear-gradient(120deg, #1e1b4e, #0f0a2a);
    border-radius: 48px;
    padding: 2.5rem;
    margin: 3rem 0;
    border: 1px solid var(--md-accent-fg-color);
    text-align: center;
}
.personified h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}
.personified blockquote {
    font-style: italic;
    font-size: 1.2rem;
    background: rgba(244,114,182,0.1);
    padding: 1rem;
    border-radius: 24px;
    max-width: 80%;
    margin: 1rem auto;
}
.unique-link {
    background: rgba(0,0,0,0.4);
    border-radius: 60px;
    padding: 0.8rem 1.5rem;
    display: inline-block;
    font-family: monospace;
    font-size: 1rem;
    margin: 1rem 0;
    border: 1px dashed var(--md-accent-fg-color);
}

/* Sección de servicios (botones tipo café) */
.services {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1.5rem;
    margin: 2rem 0;
}
.coffee-btn {
    background: rgba(30,27,75,0.6);
    border-radius: 60px;
    padding: 0.7rem 1.5rem;
    text-decoration: none;
    color: white;
    font-weight: bold;
    transition: all 0.2s;
    border: 1px solid var(--md-accent-fg-color);
}
.coffee-btn:hover {
    background: var(--md-accent-fg-color);
    color: #1e1b4b;
    transform: scale(1.03);
}
.footer-small {
    text-align: center;
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid var(--md-default-fg-color--lighter);
    font-size: 0.8rem;
}
@media (max-width: 600px) {
    .hero-main h1 { font-size: 2.2rem; }
    .tagline { font-size: 1rem; }
    .personified blockquote { max-width: 95%; font-size: 1rem; }
}
</style>

<div class="hero-main">
    <h1>CartaNatal.de</h1>
    <div class="tagline">✨ Tu carta natal personificada ✨</div>
    <div class="hero-description">
        Conócete a través de tu cielo natal. Una carta que <strong>habla en primera persona</strong>, tan humana como tú.<br>
        Sin nombres ni apellidos. Solo tú y tus estrellas. Con un enlace único para compartir.
    </div>
    <a href="#servicios" class="btn-hero">🌟 Descubre tu carta 🌟</a>
</div>

<!-- Sección de características -->
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">🗣️</div>
        <div class="feature-title">En primera persona</div>
        <div class="feature-text">Tu carta natal te habla como si fuera un ser vivo. Emociones, luces, sombras, dones y retos explicados desde el "yo".</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🏠</div>
        <div class="feature-title">Casa por casa</div>
        <div class="feature-text">Desglose completo de las 12 casas. Versión resumida y detallada. Incluye aspectos, perfiles personales y Conditio Vitae.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔗</div>
        <div class="feature-title">Enlace único y privado</div>
        <div class="feature-text">Recibirás un enlace del tipo <strong>la.cartanatal.de/XXXXXX</strong>. Compártelo solo con quien quieras. Sin nombres, solo fecha, hora y sexo.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">⭐</div>
        <div class="feature-title">Cartas de famosos</div>
        <div class="feature-text">Explora la misma estructura con personajes históricos. Aprende de su cielo y compáralo con el tuyo.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">AstroMitos</div>
        <div class="feature-text">Mitos asociados a planetas, asteroides y estrellas. Incluye su número para añadirlos a tu carta personalizada.</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🎓</div>
        <div class="feature-title">Cursos</div>
        <div class="feature-text">Próximamente: AstroTarot, Numerología y más. Aprende a interpretar tu carta y la de otros.</div>
    </div>
</div>

<!-- Sección destacada: Carta Natal Personificada -->
<div class="personified">
    <h2>🌙 Tu Carta Natal como nunca la habías visto 🌙</h2>
    <blockquote>
        “Yo soy tu carta natal. No nací contigo, pero te acompaño desde tu primer aliento. Conózcamos.”
    </blockquote>
    <p>Más allá de los datos técnicos: <strong>psicología, arquetipos y astrología</strong> fusionados en un texto único.</p>
    <div class="unique-link">
        🔒 Ejemplo de enlace privado: <em>la.cartanatal.de/lamejor</em> para Laura Menendez Jordán o el que tú quieras y esté disponible.
    </div>
    <p style="font-size:0.9rem;">Sin registro, sin cookies invasivas. Solo tu fecha, hora y sexo. El resto es magia.</p>
</div>

<!-- Sección Servicios -->
<h2 id="servicios" style="text-align:center;">🕯️ Servicios 🕯️</h2>
<div class="services">
    <a href="https://cartanatal.de/zona-servicios" class="coffee-btn">✨ Solicitar Carta Natal Personificada</a>
    <a href="https://cartanatal.de/zona-contacto" class="coffee-btn">📖 Preinscripción a Cursos (Formulario de Contacto)</a>
    <a href="https://cartanatal.de/zona-servicios" class="coffee-btn">☕ Invita a un café pequeño, mediano o grande como forma de apoyo para mantener la web.</a>
    </div>

<!-- Sección Contacto -->
<div style="text-align:center; margin: 3rem 0;">
    <h2>📬 Contacto seguro</h2>
    <p>Formulario cifrado con PGP. Tu privacidad es mi prioridad.</p>
    <a href="https://cartanatal.de/zona-contacto" class="btn-hero" style="background: linear-gradient(90deg, #8B5CF6, #F472B6);">✉️ Ir a contacto</a>
    <p style="font-size:0.8rem; margin-top:1rem;">🔐 Clave PGP disponible en la página de contacto.</p>
</div>

<div class="footer-small">
    🌠 CartaNatal.de – Un espacio para reconocerse a través de las estrellas. <br>
    Todos los derechos reservados. Hecho con 💙 y código estelar.
</div>
