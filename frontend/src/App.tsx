import heroImg from './assets/hero.png'
import { glyphs } from './glyphs'
import './App.css'

function App() {
  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
        </div>

        <div>
          <p>Download the ttf file to use the secret font</p>
        </div>

        <a href="/kasse.ttf" download>
          <button className="font">
            Download font
          </button>
        </a>
      </section>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(10, 1fr)",
        }}
      >
        {glyphs.map((code) => (
          <div key={code} style={{ textAlign: "center" }}>
            <img src={`/glyphs/${code}.png`} alt={code} />
          </div>
        ))}
      </div>

      <div className="ticks"></div>
    </>
  )
}

export default App