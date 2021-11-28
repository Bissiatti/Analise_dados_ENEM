const quiz = document.querySelector("#ENEMquests");

const fgv = document.querySelector("#fgv")

const data = []

const init = document.querySelector("#init")

function toggleDisabled(elem){
  elem.disabled = !elem.disabled;
}

init.addEventListener("click",(e)=>{
  e.path[1].classList.add("null")
  e.path[2].children[1].classList.remove("null")
})


fgv.addEventListener("click",()=>{
  window.location.href = "https://emap.fgv.br/"
})


var calculateModel = function () {
  console.log(data)
  fetch('/'+ data)
  .then(response => {
    return response.json();
  })
  .then(data => {
    let result = document.querySelector('.result')

    let sp1 = document.createElement("span")
    sp1.classList.add("special")
    sp1.appendChild(document.createTextNode((1000*data[0]).toFixed(2)))

    let sp2 = document.createElement("span")
    sp2.classList.add("special")
    sp2.appendChild(document.createTextNode((1000*data[1]).toFixed(2)))
    result.innerHTML = ""

    result.appendChild(document.createTextNode("O seu desempenho médio no ENEM nas provas objetivas será de: "))
    result.appendChild(sp1)
    result.appendChild(document.createTextNode( ". O seu desempenho na nota de redação será: "))
    result.appendChild(sp2)
    result.appendChild(document.createElement("br"))
    result.appendChild(document.createTextNode( "Aviso: este resultado não corresponde a 100% da realidade, o modelo apenas mensura a influência das suas características socias e econômicas de acordo com a nota do ENEM."))
    result.appendChild(document.createElement("br"))
    result.appendChild(document.createTextNode("O modelo utilizado possuiu coeficiente de determinação de cerca de 40% para a nota média das provas objetivas e de 20% para a nota da redação."))
  });
}


var none = function(e) {
  toggleDisabled(e)
  e.path[3].classList.add("null");
  e.path[3].nextSibling.classList.remove("null");
  data.push(parseFloat(e.path[0].value)); 

  if (e.path[3].nextSibling.classList.contains("result")){
    calculateModel()
  }
}


var addQuestsJson = function(json){
  let count = 1
  let t = false
  for(let i in json){
    if (count ==  14 || count == 22 || count == 24 || count == 25 || count ==27){
      count++;
    } 
    else{
      var quest = document.createElement("div")
      quest.classList.add("quest")
      let p = document.createElement('p')
      p.appendChild(document.createTextNode(i))
      quest.appendChild(p)
      for(let j in json[i]){
        let answer = document.createElement('span')
        answer.classList.add("answer")
        let d = document.createElement('div')
        let input = document.createElement("input")
        input.setAttribute("type","radio")
        input.setAttribute("value",json[i][j][1])
        input.addEventListener('mousedown', function(e){ e.preventDefault(); }, false);

        input.addEventListener("click",(e)=>{
          e.disabled = true;
          setTimeout(() => {none(e)}, 300);
        })

        d.appendChild(input)
        d.appendChild(document.createTextNode(json[i][j][0]))
        answer.appendChild(d)
        quest.appendChild(answer)
      }
      if (t){
        let returnButton = document.createElement('BUTTON');
        let lbl = document.createTextNode("Retornar para a última pergunta");  
        returnButton.classList.add("return")      
        returnButton.appendChild(lbl);   
        returnButton.addEventListener("click",(e)=>{
          e.disabled = true;
          
          setTimeout(function(){
            toggleDisabled(e)
          },300);

          let x = e.path[1]
          x.classList.add("null")
          x.previousElementSibling.classList.remove("null");
          backElement = x.previousElementSibling
          data.splice(-1,1);
          for(let i =1; i < backElement.children.length-1;i++){
            backElement.children[i].firstElementChild.firstElementChild.checked = ""
          } 
        })
        quest.appendChild(returnButton)
      }
      quest.classList.add("null")
      quiz.appendChild(quest)
      t = true
      count++;
    }
  }
  let result = document.createElement("div")
  result.classList.add("null")
  result.classList.add("result")
  result.appendChild(document.createTextNode("Aguarde"))

  quiz.appendChild(result)
}

fetch("./quests.json")
  .then(response => {
    return response.json();
  })
  .then(data => addQuestsJson(data));

  
