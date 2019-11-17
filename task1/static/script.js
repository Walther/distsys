function load_data() {
  // Latest measurement of self
  $.ajax({
    url: "/api/currentTemp",
    success: function(data) {
      display_self_current(data);
    }
  });
  // History of self
  $.ajax({
    url: "/api/selfWeatherHistory",
    success: function(data) {
      display_self_history(data);
    }
  });
  // History of others
  $.ajax({
    url: "/api/othersWeatherHistory",
    success: function(data) {
      display_other_history(data);
    }
  });

  return true;
}

function display_self_current(data) {
  $("#city").html(data.city);
  $("#currentTemp").html(data.celsius);
}

function display_self_history(data) {
  // TODO: prettier display somehow?
  $("#selfWeatherHistory").text(JSON.stringify(data, null, 2));
}

function display_other_history(data) {
  // TODO: prettier display somehow?
  $("#othersWeatherHistory").text(JSON.stringify(data, null, 2));
}

$(document).ready(function() {
  // Refresh page info once a second
  setInterval(function() {
    load_data();
  }, 1000);
});
