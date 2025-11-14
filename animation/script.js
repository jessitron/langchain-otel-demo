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

      // Get the left edge of the div
      const divRect = question.getBoundingClientRect();
      const divLeft = divRect.left;

      // Calculate offset for each span and trigger animation
      spans.forEach((span, index) => {
        // Get the left edge of this span
        const spanRect = span.getBoundingClientRect();
        const spanLeft = spanRect.left;

        // Calculate how far this span is from the left edge of the div
        const offset = spanLeft - divLeft;

        // Store the offset as a CSS custom property on this span
        span.style.setProperty('--offset', `${offset}px`);

        console.log(`Span ${index} ("${span.textContent}"): offset = ${offset}px`);

        // Add the fall-down class to trigger the animation
        span.classList.add('fall-down');
      });
    }
  });
});
