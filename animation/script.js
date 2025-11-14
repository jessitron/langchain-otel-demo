// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  const question = document.querySelector(".question");
  const tokenCountElement = document.querySelector("#input-token-count");
  let tokenCount = 0;
  function incrementTokenCount() {
    tokenCount++;
    tokenCountElement.textContent = "" + tokenCount;
  }

  function makeASpan(content) {
    // there's a way to construct an element but I don't have internet to look it up
    return "<span>" + content + "</span>";
  }

  const questionParts = ["W", "hat ", "is ", "you", "r f", "av", "orite", " program", "ming ", "language", "?"];
  function nestTheRest(strings) {
    console.log("length of strings: ", strings.length);
    if (strings.length === 1) {
      return makeASpan(strings[0]);
    }
    const first = strings.shift().replaceAll(" ", "&nbsp");
    const rest = nestTheRest(strings);
    return makeASpan(first) + makeASpan(rest);
  }

  question.setHTMLUnsafe(nestTheRest(questionParts));
  question.classList.add("original-move-in");

  function dropToken(elem) {
    incrementTokenCount();
    elem.classList.add("fall-down");
  }

  const theInnerSpanFollows = (event) => {
    const animationName = event.animationName;
    if (animationName === "moveInFromLeft" || animationName === "continueLeft") {
      console.log(animationName + " completed!");

      // Get all spans inside this element
      const spans = event.target.querySelectorAll(":scope > span");

      if (spans.length === 1) {
        // this is the last one
        console.log("last span yo");
        dropToken(spans[0]);
        return;
      }

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
      dropToken(spans[0]);
    }
  };

  // Listen for animation end on the question div
  question.addEventListener("animationend", theInnerSpanFollows);
});
