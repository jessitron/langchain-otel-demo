// Get references to elements
const button = document.getElementById('startAnimation');
const spans = document.querySelectorAll('.question span');
const whatSpan = spans[0]; // "What"
const isSpan = spans[1];   // "is"

button.addEventListener('click', () => {
  // Get the current positions of both spans before animation
  const whatRect = whatSpan.getBoundingClientRect();
  const isRect = isSpan.getBoundingClientRect();

  // Calculate how far "is" needs to move LEFT to reach "What"'s x-coordinate
  // Negative because "is" starts to the right of "What"
  const offset = whatRect.left - isRect.left;

  console.log('What position (left):', whatRect.left);
  console.log('Is position (left):', isRect.left);
  console.log('Calculated offset for "is":', offset);

  // Set the CSS variable on the "is" span
  isSpan.style.setProperty('--is-offset', `${offset}px`);

  // Trigger animations by adding classes
  whatSpan.classList.add('animate-what');
  isSpan.classList.add('animate-is');

  // Disable button to prevent multiple clicks
  button.disabled = true;
  button.textContent = 'Animating...';
});
