function fetchBase (url, body) {
    return fetch(url, {
      method: 'post',
      credentials: 'same-origin',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(body)
    })
    .then((res) => res.json())
  };
function getCookie (cName) {
    if (document.cookie.length > 0) {
        let cStart = document.cookie.indexOf(cName + '=')
        if (cStart !== -1) {
        cStart = cStart + cName.length + 1
        let cEnd = document.cookie.indexOf(';', cStart)
        if (cEnd === -1) {
            cEnd = document.cookie.length
        }
        return unescape(document.cookie.substring(cStart, cEnd))
        }
    }
    return ''
};

export{
  fetchBase
}