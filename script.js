document.getElementById('verifyButton').onclick = async function() {
    await chrome.tabs.query({active: true, currentWindow: true}, async function(tabs) {
    const [{result}] = await chrome.scripting.executeScript({
      target: {tabId: tabs[0].id},
      function: searchInPage
    });
    // alert('http://team3.gdscupt.tech/download/' + result);
    let filename = "download_file.mp4"; // Fallback filename
    
    response = await fetch('https://team3.gdscupt.tech/download/filename/' + result);

    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        filename = json.filename;
        //transofm filename to utf-8 taking care of spaces
        filename = decodeHTMLEntities(filename);
    }

    chrome.downloads.download({
        url: 'https://team3.gdscupt.tech/download/' + result,  // Replace with your file URL
        filename: filename,
        saveAs: true
    });
});
};


function decodeHTMLEntities(text) {
  let doc = new DOMParser().parseFromString(text, 'text/html');
  return doc.documentElement.textContent;
}

function searchInPage() {
  const searchString = "https://www.mp4upload.com/embed-";  // Replace with your static string
  const bodyText = document.body.outerHTML;
  const searchRegExp = new RegExp(searchString, 'gi');
  const matches = bodyText.match(searchRegExp);

  if (matches) {
    // if found at least one match print it with a small offset after the match
    const match = matches[0];
    const matchIndex = bodyText.indexOf(match);
    const offset = 12;
    const matchEndIndex = matchIndex + match.length;
    const highlightedAfterMatch = bodyText.substring(matchEndIndex, matchEndIndex + offset);

    // alert(`Found ${highlightedAfterMatch}`);
    // alert("http://localhost:5000/download/" + highlightedAfterMatch);
    console.log(`Found ${highlightedAfterMatch}`);
    return highlightedAfterMatch;
    // return "str";
  } else {
    alert(`No matches found for "${searchString}"`);
  }
  return null;
}

