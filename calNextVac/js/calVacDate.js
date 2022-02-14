function submitDetails() {
  // get date of last vax & store it in last
  const lastVaxDate = document.querySelector("#lastVaxDate").value;
  // console.log(lastVaxDate); // e.g. 2022-02-10

  function checkDate() {
    let lastJab = new Date(lastVaxDate);
    console.log(`lastJab= ${lastJab}`); // Tue Feb 01 2022 08:00:00

    let nextJab = new Date(lastJab.setMonth(lastJab.getMonth() + 3));
    console.log(`nextJab= ${nextJab}`);

    alert(`Get your next jab by ${nextJab}`);
  }

  checkDate();
}

// var newDate = new Date(date.setMonth(date.getMonth() + 8));
