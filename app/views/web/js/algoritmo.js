document.getElementById("btnIniciar").addEventListener("click", () => {
  conver = document.getElementById("convergencia").value;
  indi = document.getElementById("individuos").value;
  rang = document.getElementById("rango").value;
  document.getElementById("loading").style.display = "flex";
  fetch(
    "/datos2?" +
      new URLSearchParams({
        convergencia: conver === "" ? 0.9 : conver,
        target: 5,
        nVacunas: 2,
        nContagios: 1,
        nIndividuos: indi === "" ? 8 : indi,
        rango: rang === "" ? 8 : rang,
        max: 6,
        min: 0,
      }),
    {
      method: "GET",
    }
  )
    .then((res) => res.json())
    .then((data) => {
      console.log("data recibida");
      document.getElementById("generaciones").style.display = "grid";
      document.getElementById("poblacion1").style.display = "grid";
      document.getElementById("pFinal").style.display = "grid";
      generaciones(data);

      pob_inicial(data);

      pob_final(data);
    })
    .finally(() => {
      document.getElementById("loading").style.display = "none";
    });
});
