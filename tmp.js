$(document).ready(function() {
  "use strict";
  console.log('on ready');
  var _CACHE_COUNTRY_DATA = {};
  var _CACHE_CITY_DATA ={};
  var _SELECTED_CONTINENT_CODE = [];
  var _SELECTED_COUNTRY = "";

  $('.checkItem').change(function() {
    "use strict";
    console.log('on change');
    _SELECTED_CONTINENT_CODE = getSelectedChbox(this.form);
    resetDropbox('country-dropbox');
    for (var i = 0; i < _SELECTED_CONTINENT_CODE.length; i++) {
      loadCountryList(_SELECTED_CONTINENT_CODE[i]);
    }
  });

  function loadCountryList() {
    "use strict";
    console.log('on loadCountryList');
    console.log('_SELECTED_CONTINENT_CODE:'+_SELECTED_CONTINENT_CODE);
    for (var i = _SELECTED_CONTINENT_CODE.length - 1; i >= 0; i--) {
      console.log('check');
      if (! (_SELECTED_CONTINENT_CODE[i] in _CACHE_COUNTRY_DATA)){
        loadCountryInfo(_SELECTED_CONTINENT_CODE[i]);
      }
    }
    checkCountryData();
  }

  function loadCountryInfo(continentCode) {
    "use strict";
    console.log('on loadCountryList :'+continentCode);
    $.ajax({
      url: 'http://api.geonames.org/countryInfoJSON',
      type: "GET",
      data: {
        continentCode: continentCode,
        username: "jeok70"
      },
      datatype: "json",
      success: function(data) {
        console.log('on success');
        _CACHE_COUNTRY_DATA[continentCode] = data['geonames'];
        checkCountryData();

      },
      error: function(xhr, error) {
        alert('Ajax request error.');
      }
    });
  }

  function checkCountryData() {
    console.log('on checkCountryData');
    for (var i = _SELECTED_CONTINENT_CODE.length - 1; i >= 0; i--) {
      if (!(_SELECTED_CONTINENT_CODE[i] in _CACHE_COUNTRY_DATA)){
        console.log('found no data for '+_SELECTED_CONTINENT_CODE[i]);
        return;
      }
    }
    updateCountryDropbox();
  }

  function updateCountryDropbox() {
    console.log('on updateCountryDropbox');
    console.log(_CACHE_COUNTRY_DATA);
    resetDropbox("country-dropbox");
    var itemList=[];
    for (var i = _SELECTED_CONTINENT_CODE.length - 1; i >= 0; i--) {
      itemList = itemList.concat(getDataList(_CACHE_COUNTRY_DATA[_SELECTED_CONTINENT_CODE[i]], "countryName"));
    }
    setDropbox("country-dropbox", itemList);
  }

  $('#countryItem').change(function() {
    console.log('country selected');
    var selectCountryName = $("#countryItem option:selected").text();

    var findFlag = false;
    for (var i = _SELECTED_CONTINENT_CODE.length - 1; i >= 0; i--) {
      for (var j = _CACHE_COUNTRY_DATA[_SELECTED_CONTINENT_CODE[i]].length - 1; j >= 0; j--) {
        if (_CACHE_COUNTRY_DATA[_SELECTED_CONTINENT_CODE[i]][j].countryName == selectCountryName){
          console.log('found country data');
          _SELECTED_COUNTRY = _CACHE_COUNTRY_DATA[_SELECTED_CONTINENT_CODE[i]][j];
          findFlag = true;
        }
        if (findFlag) {break;}
      }
      if (findFlag) {break;}
    }

    // if (_CACHE_CITY_DATA[selectCountry]) {
    //   //找Country的資訊，填入City的input中
    //   var cachedata = _CACHE_COUNTRY_DATA;
    //   for (var i = 0; i < cachedata.length; i++) {
    //     if (cachedata[i]["countryName"] == selectCountry) {
    //       var east = cachedata[i]["east"];
    //       var west = cachedata[i]["west"];
    //       var north = cachedata[i]["north"];
    //       var south = cachedata[i]["south"];
    //       var lang = cachedata[i]["languages"];
    //       loadCityList(south, north, east, west);
    //     }
    //   }
    // }
    if (_CACHE_CITY_DATA[selectCountryName]) {
      checkCitiesData();
    }else{
      loadCities();
    }

  });

  function loadCities(){
    var langList = _SELECTED_COUNTRY.languages.split(',');
    for (var i = langList.length - 1; i >= 0; i--) {
      loadCityInfo(langList[i]);
    }
  }

  function checkCitiesData() {
    console.log('on checkCitiesData');
    var langList = _SELECTED_COUNTRY.languages.split(',');
    for (var i = langList.length - 1; i >= 0; i--) {
      if (!(langList[i] in _CACHE_CITY_DATA[_SELECTED_COUNTRY.countryName])){
        console.log('found no data for '+_SELECTED_COUNTRY.countryName+":"+langList);
        return;
      }
    }
    updateCityDropbox();
  }

  function updateCityDropbox() {
    console.log('on updateCityDropbox');
    // body...
  }

  function loadCityInfo(lang) {
    $.ajax({
      url: 'http://api.geonames.org/citiesJSON',
      type: "GET",
      data: {
        south: _SELECTED_COUNTRY.south,
        north: _SELECTED_COUNTRY.north,
        east: _SELECTED_COUNTRY.east,
        west: _SELECTED_COUNTRY.west,
        maxRows: 100,
        username: "jeok70",
        lang: lang
      },
      datatype: "json",
      success: function(data) {
        cityList = getDataList(data, 'name');
        console.log(cityList);
        _CACHE_CITY_DATA[_SELECTED_COUNTRY.countryName][lang] = cityList;

      },
      error: function(xhr, error) {
        alert('Ajax request error.');
      }
    });
  }

  function getSelectedChbox(frm) {
    var selchbox = [];
    $("input:checkbox[name=continent]:checked").each(function() {
      selchbox.push($(this).val());
    });
    return selchbox;
  }

  function getDataList(data, childNode) {
    console.log('on getDataList '+childNode);
    console.log(JSON.stringify(data));
    var result = [];
    for (var i = 0; i < data.length; i++) {
      result.push(data[i][childNode]);
    }
    console.log("result"+result);
    return result;
  }

  function resetDropbox(dropboxName) {
    var sel = document.getElementById(dropboxName);
    var count = $("#"+ dropboxName +" option").length;
    while (count>1) {
      sel.removeChild(sel.lastChild);
      count -= 1;
    }
  }

  function setDropbox(dropboxName, itemList) {
    console.log("on setDropbox dropboxName:" + dropboxName + " itemList:" +itemList)
    var sel = document.getElementById(dropboxName);

    for (var i = 0; i < itemList.length; i++) {
      var opt = document.createElement('option');
      opt.innerHTML = itemList[i];
      opt.value = itemList[i];
      sel.appendChild(opt);
    }
  }

});
