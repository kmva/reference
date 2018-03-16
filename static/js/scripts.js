$(document).ready(function() {
  let sidebar = $("#sidebar-nav");
  let content = $("#page-content-wrapper");
  let searchField = $("#search");
  let list = $("#sidebar-nav li ul");
  let oldURL;
  let newURL;
  

  let container = $('#page-content-wrapper');
  let whole = $(".whole")[0]

    //search function
  
  $(searchField).on('keyup', function searching(e){
      let term = e.target.value.toLowerCase();
      let funcs = $('#sidebar-nav li ul li');
      for(let k=0;k<funcs.length;k++){
      let name = funcs[k].firstElementChild.textContent;
        if(name.toLowerCase().indexOf(term) != -1){
          funcs[k].style.display = 'block';
        }else{
          funcs[k].style.display = 'none';
        }
      }
      
      let lowerli = $('.lowerli');
      let countOfHides = 0;
      
      $(lowerli).each(function(index, list){
        let litems = $(list).find('li');
          $(litems).each(function checkHidding(index, item){
            if($(item).css('display') != 'none'){
                countOfHides += 1; 
              }
          }).promise().done(function hideH1(){
            if(countOfHides >= 1){
              $(list).siblings('h1').eq(0).show();
            }else{
              $(list).siblings('h1').eq(0).hide()
            } 
              countOfHides = 0;
          })
      })
  })
    
  //manipulate number of blocks depended on current library 
    
  $(window).on('hashchange', (function view(func, syncResults, asyncResults)
  {
    event.preventDefault();
    //this.oldHash = ;
    let loc = window.location.hash.split("#")[1];
    let pathLib = loc.substring(0, loc.lastIndexOf('/'));
    let pathFunc = loc.substring(loc.lastIndexOf('/')+1);
    //history.pushState('', document.title, loc);
    
    
    let funcLen = eval(pathLib)['func_length'][pathFunc];
    
    let greyblock = $('.greyblock h2');
    let count = 0;
    
    if(greyblock.length < funcLen){
      count = funcLen - greyblock.length;
      for(let i=0;i < count;i++)
      {
        $(whole).clone().appendTo(container[0]);
      }  
    }else if(greyblock.length > funcLen){
      count = funcLen;
      for(let i=count;i < greyblock.length;i++)
      {
        $(greyblock[i]).parent().parent().remove();
      } 
    }
    
    let library = pathLib; 
    let funct = pathFunc;
      /*let parameters = {
        func: func
      };*/
    
    let url = "/" + library + "/" + funct;
      $.getJSON(url)
      .done(function(data, textStatus, jqXHR) {
        let lib = eval(library)
        let keys = Object.keys(lib);
        let amply = $('.amply');
        let greyblock = $('.greyblock h2');

        for(let i=0, j=0;i<keys.length-1;i++, j++){
           let key = keys[j];
            //let key = data[0][key] == undefined) ? keys[j+1] : key[i];
            console.log(data[0][key])
            while(data[0][key] === undefined || data[0][key] === '' || data[0][key] === null){
              if(j>keys.length-1){
                break;
              }
              j++;
              key = keys[j];
            }
           $(greyblock[i]).html(lib[key]);
           $(amply[i]).html(data[0][key]);
          }
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
          console.log(errorThrown.toString());
      });
    
  })
  )
  
})