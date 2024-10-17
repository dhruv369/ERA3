let contextMenuId = null;

function createContextMenu() {
  if (contextMenuId === null) {
    contextMenuId = chrome.contextMenus.create({
      id: "translateToSwedish",
      title: "Translate to Swedish",
      contexts: ["all"]
    });
  }
}

function removeContextMenu() {
  if (contextMenuId !== null) {
    chrome.contextMenus.remove(contextMenuId);
    contextMenuId = null;
  }
}

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.get('enabled', function(data) {
    const isEnabled = data.enabled !== false;
    chrome.storage.sync.set({enabled: isEnabled});
    if (isEnabled) {
      createContextMenu();
    }
  });
});

chrome.storage.onChanged.addListener((changes, namespace) => {
  if (namespace === 'sync' && 'enabled' in changes) {
    if (changes.enabled.newValue) {
      createContextMenu();
    } else {
      removeContextMenu();
    }
  }
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "translateToSwedish") {
    chrome.tabs.sendMessage(tab.id, { action: "getClickedWord" }, (response) => {
      if (response && response.word) {
        translateToSwedish(response.word)
          .then(result => {
            chrome.tabs.sendMessage(tab.id, {
              action: "showTranslation",
              data: result
            });
          })
          .catch(error => {
            console.error('Translation failed:', error);
          });
      }
    });
  }
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "getDefinition") {
    getDefinition(request.word)
      .then(definition => sendResponse({definition: definition}))
      .catch(error => sendResponse({error: error.message}));
    return true; // Indicates that the response is sent asynchronously
  }
  if (request.action === "translateToSwedish") {
    translateToSwedish(request.word)
      .then(result => sendResponse(result))
      .catch(error => sendResponse({error: error.message}));
    return true; // Indicates that the response is sent asynchronously
  }
});

async function getDefinition(word) {
  const url = `https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`;
  
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error('Definition request failed');
  }

  const data = await response.json();
  if (data.length > 0 && data[0].meanings.length > 0) {
    const definition = data[0].meanings[0].definitions[0].definition;
    return definition;
  } else {
    throw new Error('No definition found');
  }
}

async function translateToSwedish(word) {
  const translationUrl = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(word)}&langpair=en|sv`;
  const definitionUrl = `https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`;
  
  try {
    // Translate to Swedish
    const translationResponse = await fetch(translationUrl);

    if (!translationResponse.ok) {
      throw new Error('Translation request failed');
    }

    const translationData = await translationResponse.json();
    const translation = translationData.responseData.translatedText;

    // Get English definition
    const definitionResponse = await fetch(definitionUrl);
    let definition = "";

    if (definitionResponse.ok) {
      const definitionData = await definitionResponse.json();
      if (definitionData.length > 0 && definitionData[0].meanings.length > 0) {
        definition = definitionData[0].meanings[0].definitions[0].definition;
      }
    }

    return { word, translation, definition };
  } catch (error) {
    throw new Error('Request failed: ' + error.message);
  }
}
