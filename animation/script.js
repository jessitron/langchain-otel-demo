// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  const question = document.querySelector(".question");

  const theInnerSpanFollows = (event) => {
    const animationName = event.animationName;
    if (animationName === "moveInFromLeft" || animationName === "continueLeft") {
      console.log(animationName + " completed!");

      // Get all spans inside this element
      const spans = event.target.querySelectorAll(":scope > span");

      // I expect this to be 2 spans
      if (spans.length != 2) {
        console.log("waaaaaa, wanted 2 spans but there were ", spans.length, event.target);
        return;
      }

      // Get the left edge of the two spans
      const divLeft = spans[0].getBoundingClientRect().left;

      const span = spans[1];
      // Get the left edge of this span
      const spanRect = span.getBoundingClientRect();
      const spanLeft = spanRect.left;

      // Calculate how far this span is from the left edge of the div
      const offset = spanLeft - divLeft;

      // Store the offset as a CSS custom property on this span
      span.style.setProperty("--offset", `${offset}px`);

      console.log(`Span ("${span.textContent}"): offset = ${offset}px`);

      span.classList.add("keep-scooching");
      spans[0].classList.add("fall-down");
    }
  };

  // Listen for animation end on the question div
  question.addEventListener("animationend", theInnerSpanFollows);
});
