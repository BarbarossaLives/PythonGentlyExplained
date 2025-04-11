
const button = document.querySelector('button');

button.addEventListener('click', function() {
  document.getElementsByClassName("with_name").innerHTML = "Hello person";
  console.log('Button clicked!');
});