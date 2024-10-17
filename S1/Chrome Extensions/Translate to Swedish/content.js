let lastClickedWord = '';

document.addEventListener('mousedown', function(event) {
  if (event.button === 2) { // Right click
    lastClickedWord = getWordAtPoint(event.clientX, event.clientY);
  }
});

function getWordAtPoint(x, y) {
  const element = document.elementFromPoint(x, y);
  if (element && element.textContent) {
    const range = document.caretRangeFromPoint(x, y);
    if (range) {
      range.expand('word');
      return range.toString().trim();
    }
  }
  return '';
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getClickedWord") {
    sendResponse({ word: lastClickedWord });
  } else if (request.action === "showTranslation") {
    showTranslationPopup(request.data);
  }
});

function showTranslationPopup(data) {
  // Remove any existing popup
  const existingPopup = document.getElementById('swedish-translator-popup');
  if (existingPopup) {
    existingPopup.remove();
  }

  // Create and style the popup
  const popup = document.createElement('div');
  popup.id = 'swedish-translator-popup';
  popup.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    z-index: 10000;
    max-width: 300px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  `;

  // Populate the popup with translation data
  popup.innerHTML = `
    <h3 style="margin-top: 0;">${data.word}</h3>
    <p><strong>Swedish:</strong> ${data.translation}</p>
    ${data.definition ? `<p><strong>Definition:</strong> ${data.definition}</p>` : ''}
    <button id="close-popup" style="margin-top: 10px;">Close</button>
  `;

  // Add the popup to the page
  document.body.appendChild(popup);

  // Add event listener to close button
  document.getElementById('close-popup').addEventListener('click', () => {
    popup.remove();
  });
}
