const inicial = document.getElementById("ContPob_inicial");
const final = document.getElementById("ContPob_final");
const geners = document.getElementById("geners");

const pob_inicial = (data) => {
  inicial.innerHTML = "";
  data.generaciones["generacion 0"].forEach((element) => {
    element.forEach((item) => {
      if (item === 0) {
        inicial.innerHTML += `<img src="../web/res/2.png"/>`;
      } else if (item <= 3) {
        inicial.innerHTML += `<img src="../web/res/3.png"/>`;
      } else if (item <= 5) {
        inicial.innerHTML += `<img src="../web/res/1.png"/>`;
      }
    });
  });
};

const pob_final = (data) => {
  gen = Object.keys(data.generaciones).length - 1;
  final.innerHTML = "";
  data.generaciones["generacion " + gen].forEach((element) => {
    element.forEach((item) => {
      if (item === 0) {
        final.innerHTML += `<img src="../web/res/2.png"/>`;
      } else if (item <= 3) {
        final.innerHTML += `<img src="../web/res/3.png"/>`;
      } else if (item <= 5) {
        final.innerHTML += `<img src="../web/res/1.png"/>`;
      }
    });
  });
};

const generaciones = (data) => {
  gen = Object.keys(data.generaciones).length;
  geners.innerHTML = "";
  for (var i = 0; i < gen; i++) {
    var html = "";
    data.generaciones["generacion " + i].forEach((item) => {
      item.forEach((value) => {
        if (value === 0) {
          html += `<img src="../web/res/2.png"/>`;
        } else if (value <= 3) {
          html += `<img src="../web/res/3.png"/>`;
        } else if (value <= 5) {
          html += `<img src="../web/res/1.png"/>`;
        }
      });
    });
    geners.innerHTML += `<p>Generacion ${i}</p>
        <div class="contenido2">${html}
        </div>`;
  }
};
