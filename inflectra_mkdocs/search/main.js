var console={log:function(){}};  

function getSearchTermFromLocation() {
  var sPageURL = window.location.search.substring(1);
  var sURLVariables = sPageURL.split('&');
  for (var i = 0; i < sURLVariables.length; i++) {
    var sParameterName = sURLVariables[i].split('=');
    if (sParameterName[0] == 'q') {
      return decodeURIComponent(sParameterName[1].replace(/\+/g, '%20'));
    }
  }
}

function joinUrl (base, path, query) {
  if(query) path = path + "?kw="+encodeURI(query);
  
  if (path.substring(0, 1) === "/") {
    // path starts with `/`. Thus it is absolute.
    return path;
  }
  if (base.substring(base.length-1) === "/") {
    // base ends with `/`
    return base + path;
  }
  return base + "/" + path;
}

var filterTitles = ["/#property-summary", "/#action-summary", "/#property-detail", "/#action-detail", "/#see-also"];

function endsWith(str,suffix) {
    return str.indexOf(suffix, str.length - suffix.length) !== -1;
};

function formatResult (location, title, summary, query) {
  for(var i=0;i<filterTitles.length;i++)
  {
    if(endsWith(location, filterTitles[i]))
    {
      return undefined;
    }
  }
  return '<article><h3><a href="' + joinUrl(base_url, location, query) + '">'+ title + '</a></h3><strong>'+location+'</strong><p>' + summary +'</p></article>';
}

function displayResults (results, query) {
  var search_results = document.getElementById("mkdocs-search-results");
  while (search_results.firstChild) {
    search_results.removeChild(search_results.firstChild);
  }
  if (results.length > 0){
    for (var i=0; i < results.length; i++){
      var result = results[i];
      var html = formatResult(result.location, result.title, result.summary, query);
      if(html)
      {
        search_results.insertAdjacentHTML('beforeend', html);        
      }
    }
  } else {
    search_results.insertAdjacentHTML('beforeend', "<p>No results found</p>");
  }
}

function doSearch () {
  var query = document.getElementById('mkdocs-search-query').value;
  if (query.length > 2) {
    if (!window.Worker) {
      displayResults(search(query),query);
    } else {
      searchWorker.postMessage({query: query});
    }
  } else {
    // Clear results for short queries
    displayResults([]);
  }
}

function initSearch () {
  var search_input = document.getElementById('mkdocs-search-query');
  if (search_input) {
    search_input.addEventListener("keyup", doSearch);
  }
  var term = getSearchTermFromLocation();
  if (term) {
    search_input.value = term;
    doSearch();
  }
}

function onWorkerMessage (e) {
  if (e.data.allowSearch) {
    initSearch();
  } else if (e.data.results) {
    var results = e.data.results;
    displayResults(results, e.data.query);
  }
}

if (!window.Worker) {
  console.log('Web Worker API not supported');
  // load index in main thread
  $.getScript(joinUrl(base_url, "search/worker.js")).done(function () {
    console.log('Loaded worker');
    init();
    window.postMessage = function (msg) {
      onWorkerMessage({data: msg});
    };
  }).fail(function (jqxhr, settings, exception) {
    console.error('Could not load worker.js');
  });
} else {

  // Wrap search in a web worker
  var searchWorker = new Worker(joinUrl(base_url, "search/worker.js"));
  searchWorker.postMessage({init: true});
  searchWorker.onmessage = onWorkerMessage;
}
