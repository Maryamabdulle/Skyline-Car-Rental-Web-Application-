document.getElementById("btn").addEventListener(
    "Book Now",
    function(event) {
      if (event.target.value === "Submit") {
        event.target.value = "Saved";
      } else {
        event.target.value = "Save";
      }
    },
    false
  );
  


