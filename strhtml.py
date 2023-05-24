import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <!DOCTYPE html>
<html lang="en">
<head>
<title>SIGJ MLS2T Page</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">

<script>
// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}
</script>

<style>

body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif}
body {font-size:16px;}
.w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}
.w3-half img:hover{opacity:1}

</style>
</head>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-orange w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Close Menu</a>
  <div class="w3-container">
    <h3 class="w3-padding-64" style = "color:black"><b><br>Machine Learning</b></h3>
    <h3 class="w3-padding-64" style="text-decoration: underline"><b><br>Speech to Text</b></h3>
  </div>
  <div class="w3-bar-block"> 
    <a href="https://drkamthorn-whisperai-transcribe-eywl3q.streamlit.app/" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white" target="_blank">ถอดเสียงบันทึก</a> 
    <a href="passw.php" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white" target="_blank">แก้ไขไฟล์ถอดเสียง</a> 
    <a href="" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white" target="_blank">ปรับไฟล์บันทึกให้ชัดขึ้น</a>  
    <a href="" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white" target="_blank">ตัดไฟล์บันทึกให้เล็กลง</a>
  </div>
</nav>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

  <!-- Header -->
  <div class="w3-container" style="margin-top:80px" id="showcase">
    <h1 class = "w3-jumbo" style="color: green;text-shadow: 2px 2px 4px #000000;"><b>ศูนย์การแพทย์กาญจนาภิเษก</b></h1>
    <h1 class="w3-xxxlarge w3-text-orange"><b>งานสารบรรณ</b></h1>
    <hr style="width:1000px;border:5px;color:blue;text-shadow: 2px 2px 4px #000000;" class="w3-round">
  </div>
  

  <div id="modal01" class="w3-modal w3-black" style="padding-top:0" onclick="this.style.display='none'">
    <span class="w3-button w3-black w3-xxlarge w3-display-topright">×</span>
    <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
      <img id="img01" class="w3-image">
      <p id="caption"></p>
    </div>
  </div>
<br><br>

<form action="" method="post">


<br><br>
<center>
<input type="button" class="button_active" onclick="location.href='https://drkamthorn-whisperai.streamlit.app/';">

<br><br>
<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" style="margin-top:75px;padding-right:58px"><p class="w3-right">By: Kamthorn Tantivitayatan, M.D.</p></div>
</center>
</form>



    """,
    height=600,
)
