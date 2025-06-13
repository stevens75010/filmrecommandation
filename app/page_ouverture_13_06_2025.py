import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cinément Vôtre - WMDb", layout="centered")

if "app_started" not in st.session_state:
    st.session_state.app_started = False

# Page d'accueil avec bouton pour entrer
if not st.session_state.app_started:

    # 🎬 Styles + intro
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to top, #000000, #1a1a1a);
            overflow-x: hidden;
        }
        .centered {
            text-align: center;
            color: gold;
            font-family: 'Georgia', serif;
            margin-top: 50px;
        }
        .title-fade {
            font-size: 52px;
            animation: fadeIn 3s ease-in-out;
            text-shadow: 0px 0px 10px rgba(255,215,0,0.9);
        }
        .subtitle-fade {
            font-size: 28px;
            animation: fadeIn 5s ease-in-out;
            font-style: italic;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        .fade-screen {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: black;
            animation: fadeOut 4s ease-in-out forwards;
            z-index: 9999;
        }
        @keyframes fadeOut {
            0% {opacity: 1;}
            100% {opacity: 0;}
        }
        </style>

        <div class="fade-screen"></div>

        <div class="centered">
            <div class="title-fade">🎥 <span style="color: crimson;">WMDb</span> présente</div>
            <div class="subtitle-fade">✨ Cinément Vôtre ✨</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🎼 Musique d'ambiance
    st.markdown(
        """
        <audio autoplay loop>
          <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # 📽️ Image clap de cinéma + 🎟️ Tapis rouge animé
    st.markdown(
        """
        <div style='text-align:center; margin-top:40px;'>
            <img src='https://media.giphy.com/media/l0MYB8Ory7Hqefo9a/giphy.gif' width='300'/>
            <br/>
            <img src='https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif' width='400' style='margin-top:20px;'/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 🎆 Feux d'artifice
    fireworks_html = """
    <canvas id="canvas"></canvas>
    <script>
    var canvas = document.getElementById("canvas");
    if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'canvas';
        document.body.appendChild(canvas);
    }
    var ctx = canvas.getContext("2d");
    canvas.style.position = 'fixed';
    canvas.style.top = 0;
    canvas.style.left = 0;
    canvas.style.zIndex = -1;
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    function Firework(x, y, r, g, b) {
      this.x = x;
      this.y = y;
      this.r = r;
      this.g = g;
      this.b = b;
      this.radius = 1;
      this.life = 0;
    }
    Firework.prototype.draw = function() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
      ctx.fillStyle = "rgba(" + this.r + "," + this.g + "," + this.b + "," + (1 - this.life / 100) + ")";
      ctx.fill();
    };
    Firework.prototype.update = function() {
      this.radius += 2;
      this.life += 2;
    };

    let fireworks = [];
    setInterval(() => {
      let x = Math.random() * canvas.width;
      let y = Math.random() * canvas.height / 2;
      let r = Math.floor(Math.random() * 255);
      let g = Math.floor(Math.random() * 255);
      let b = Math.floor(Math.random() * 255);
      for (let i = 0; i < 30; i++) {
        fireworks.push(new Firework(x, y, r, g, b));
      }
    }, 900);

    function animate() {
      ctx.fillStyle = "rgba(0,0,0,0.2)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      for (let i = 0; i < fireworks.length; i++) {
        fireworks[i].update();
        fireworks[i].draw();
        if (fireworks[i].life > 100) {
          fireworks.splice(i, 1);
          i--;
        }
      }
      requestAnimationFrame(animate);
    }
    animate();
    </script>
    """
    components.html(fireworks_html, height=0)

    # 🎟️ Bouton pour entrer
    if st.button("🎟️ Entrer dans WMDb", use_container_width=True):
        st.session_state.app_started = True

# 🌟 Application principale
else:
    st.title("🎬 WMDb - Cinément Vôtre")
    st.markdown("Bienvenue dans l’univers du cinéma. 🎞️ Explorez, analysez et vibrez comme sur la Croisette  !")
    # ➕ Ton contenu principal ici
