javascript:(function(){if(window.sq){window.sq.closed&&window.document.dispatchEvent(new Event('squirt.again'));}else{window.sq={};window.sq.userId='e9a38398-0bd1-482d-a2b7-09378cf58bb5';s=document.createElement('script');s.src='http://www.squirt.io/bm/squirt.js';s.s=window.location.search;s.idx=s.s.indexOf('sq-dev');if(s.idx!=-1){s.ampIdx=s.s.indexOf('&');s.host=s.s.substring(s.idx+7,s.ampIdx==-1?s.s.length:s.ampIdx);s.src='http://'+(s.host?s.host:'localhost')+':4000/bm/squirt.js';}document.body.appendChild(s);}})();
