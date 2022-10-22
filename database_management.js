function submit(){
    var destination = document.getElementById("destination").value;
    var time=document.getElementById('time').value;
    var num_seats=document.getElementById('num_seats').value;
    var duration_hr=document.getElementById('duration-hr').value;
    var duration_min=document.getElementById('duration-min').value;
    var comments=document.getElementById('comments').value;
    var params = "destination=" + destination + "&time=" + time + "&num_seats=" + num_seats+ "&duration_hr=" + duration_hr + "&duration-min=" + duration_min+ "&comments=" + comments;

    var req = new XMLHttpRequest();
    var url = "/";

    req.onreadystatechange = function()
    {
      if(this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
      } else {
        console.log("processing");
      }
    }

    req.open('POST', url, true);
    req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    req.send(params);
    console.log(params)
}
