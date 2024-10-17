document.addEventListener('DOMContentLoaded', function() {
  const translateBtn = document.getElementById('translateBtn');
  const wordInput = document.getElementById('wordInput');
  const result = document.getElementById('result');
  const enableToggle = document.getElementById('enableToggle');
  const statusText = document.getElementById('statusText');

  // Load the current state
  chrome.storage.sync.get('enabled', function(data) {
    enableToggle.checked = data.enabled !== false;
    updateStatus(enableToggle.checked);
  });

  enableToggle.addEventListener('change', function() {
    const isEnabled = enableToggle.checked;
    chrome.storage.sync.set({enabled: isEnabled}, function() {
      updateStatus(isEnabled);
    });
  });

  function updateStatus(isEnabled) {
    statusText.textContent = isEnabled ? 'Enabled' : 'Disabled';
    translateBtn.disabled = !isEnabled;
    wordInput.disabled = !isEnabled;
  }

  translateBtn.addEventListener('click', function() {
    const word = wordInput.value.trim();
    if (word) {
      chrome.runtime.sendMessage({action: "translateToSwedish", word: word}, function(response) {
        if (response.translation) {
          result.innerHTML = `<strong>${word}</strong> in Swedish:<br>${response.translation}`;
          if (response.definition) {
            result.innerHTML += `<br><br>Definition:<br>${response.definition}`;
          }
        } else {
          result.textContent = "Translation failed. Please try again.";
        }
      });
    } else {
      result.textContent = "Please enter a word to translate.";
    }
  });
});
