// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const question = document.querySelector('.question');

  // Listen for animation end on the question div
  question.addEventListener('animationend', (event) => {
    // Check if it's the moveInFromLeft animation that just ended
    if (event.animationName === 'moveInFromLeft') {
      console.log('moveInFromLeft completed! Starting fallDown on each span...');

      // Get all spans inside the question div
      const spans = question.querySelectorAll('span');

      // Add the fall-down class to each span to trigger the animation
      spans.forEach((span, index) => {
        span.classList.add('fall-down');
        console.log(`Added fall-down to span ${index}: ${span.textContent}`);
      });
    }
  });
});
