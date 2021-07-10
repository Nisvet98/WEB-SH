var elem = document.querySelectorAll('.first')

for(var i =0; i < elem.length; i++){
  elem[i].addEventListener('change',function(e){
    if(e.target.value == 'Set Author'){
       document.getElementById('set').style.display = 'inline-block'
       document.getElementById('star').style.display = 'none'
       document.getElementById('like').style.display = 'none'
    }
    if(e.target.value == 'Star'){
       document.getElementById('star').style.display = 'inline-block'
       document.getElementById('set').style.display = 'none'
       document.getElementById('like').style.display = 'none'
    }
    if(e.target.value == 'Like'){
       document.getElementById('like').style.display = 'inline-block'
       document.getElementById('star').style.display = 'none'
       document.getElementById('set').style.display = 'none'
    }
  })
}