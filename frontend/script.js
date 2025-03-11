document
  .getElementById("contact-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let message = document.getElementById("message").value.trim();

    if (!name || !email || !message) {
      alert("All fields are required!");
      return;
    }

    if (!validateEmail(email)) {
      alert("Invalid email address!");
      return;
    }

    alert("Message sent successfully!");
  });

function validateEmail(email) {
  let re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}
