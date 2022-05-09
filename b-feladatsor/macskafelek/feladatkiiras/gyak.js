"use strict";

let sebesseg = [];

let gepardSebesseg = +document.getElementById("gepardSebesseg").innerText;
sebesseg.push(gepardSebesseg);
let jaguarSebesseg = +document.getElementById("jaguarSebesseg").innerText;
sebesseg.push(jaguarSebesseg);
let tigrisSebesseg = +document.getElementById("tigrisSebesseg").innerText;
sebesseg.push(tigrisSebesseg);
let oroszlanSebesseg = +document.getElementById("oroszlanSebesseg").innerText;
sebesseg.push(oroszlanSebesseg);

let tomeg = [];
let gepardTomeg = +document.getElementById("gepardTomeg").innerText;
tomeg.push(gepardTomeg);
let jaguarTomeg = +document.getElementById("jaguarTomeg").innerText;
tomeg.push(jaguarTomeg);
let tigrisTomeg = +document.getElementById("tigrisTomeg").innerText;
tomeg.push(tigrisTomeg);
let oroszlanTomeg = +document.getElementById("oroszlanTomeg").innerText;
tomeg.push(oroszlanTomeg);

let magassag = [];
let gepardMagassag = +document.getElementById("gepardMagassag").innerText;
magassag.push(gepardMagassag);
let jaguarMagassag = +document.getElementById("jaguarMagassag").innerText;
magassag.push(jaguarMagassag);
let tigrisMagassag = +document.getElementById("tigrisMagassag").innerText;
magassag.push(tigrisMagassag);
let oroszlanMagassag = +document.getElementById("oroszlanMagassag").innerText;
magassag.push(oroszlanMagassag);
console.log(magassag);

function kiertekel() {
  let info = document.getElementById("info");
  let ertekel = document.getElementById("szamitas").options.selectedIndex;

  if (ertekel == 1) {
    let leggyorsabb = "";
    let maxSebesseg = 0;

    for (let i = 0; i < sebesseg.length; i++) {
      if (maxSebesseg <= sebesseg[i]) {
        maxSebesseg = sebesseg[i];
        leggyorsabb = allat[i];
      }
    }

    info.innerText = "A leggyorsabb állat: " + leggyorsabb;
  } else if (ertekel == 4) {
    let legmagasabb = "";
    let maxMagassag = 0;

    for (let i = 0; i < magassag.length; i++) {
      if (maxMagassag <= magassag[i]) {
        maxMagassag = magassag[i];
        legmagasabb = allat[i];
      }
    }

    info.innerText = "A legmagasabb állat: " + legmagasabb;
  }
}
