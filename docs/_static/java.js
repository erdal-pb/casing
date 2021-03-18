let version =0;
let id_pic;

function clickv1() {
  //document.getElementById('v1').setAttribute('class', 'iframe-button-case-v1');
  //document.getElementById('v2').setAttribute('class', 'button');
  version = 1;
  picture(version);
}

function clickv2() {
  document.getElementById('v2').setAttribute('class', 'iframe-button-case-v1');
  document.getElementById('v1').setAttribute('class', 'button');
  version = 2;
  picture(version);
}

function picture(v){ 
  elements = document.getElementsByClassName("pic_mounting");
  for (var i = 0; i < elements.length; i++) {
      id_pic = elements[i].id;
      let pic = `../../_static/${v}_${id_pic}`;
      elements[i].src =pic;
      elements[i].style.display='block';
  }
}